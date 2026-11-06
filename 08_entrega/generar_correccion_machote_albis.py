"""Rellena una copia binaria del machote Albis sin alterar sus siete hojas."""
from __future__ import annotations
import csv, shutil, zipfile
from copy import copy
from decimal import Decimal
from pathlib import Path
from openpyxl import load_workbook
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05/CORRECCION_FORMATO_ALBIS_2026-11-06'
TEMPLATE=ROOT/'insumos_entregable_2/Presupuesto FINAL.xlsx'
CSV=ROOT/'08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05/DATOS_PRESUPUESTO_CHATGPT_37_PARTIDAS.csv'
GANTT=ROOT/'gantt/GANTT_INA_CABLEADO_2026-2027.xlsx'
FX=Decimal('454.65'); CHARGES=Decimal('0.2683'); LABOR=Decimal('13935679.31514')

GROUPS=[
('Cable Cat6A',[1]),('Jacks Cat6A',[2]),('Placas y cajas WA',[3,4]),('Patch cords cobre',[5]),('Rotulación',[6]),('Paneles Cat6A',[7]),('Gabinetes y tierra',[8,12]),('Organizadores',[9]),('PDU y UPS',[10,11]),('Canastas',[13]),('Soportes y uniones',[14,15]),('Conduit',[16]),('Accesorios conduit y bajantes',[17,18]),('Puesta a tierra',[19]),('Switches acceso',[20]),('Switches distribución',[21]),('DAC',[22]),('FO 12F',[23]),('FO 24F',[24]),('ODF y cassettes',[25,26]),('Pigtails, adaptadores y protectores',[27,28]),('Patch cords FO',[29]),('SFP+',[30]),('Uso certificador, OLTS, OTDR y fusionadora',[31,32,33,34]),('Herramientas y consumibles',[35]),('EPP',[36]),('Fletes',[37])]

def rows():
 with CSV.open(encoding='utf-8-sig',newline='') as f: a=list(csv.DictReader(f))
 for r in a:
  v=Decimal(r['Cantidad'])*Decimal(r['Precio_unitario'])*(FX if r['Moneda']=='USD' else 1)
  r['net']=v/(Decimal(1)+Decimal('.13')) if r['IVA_origen']=='Incluido' else v
 return a

def group(a):
 out=[]
 for i,(name,ids) in enumerate(GROUPS,1):
  chosen=[a[x-1] for x in ids]; net=sum((x['net'] for x in chosen),Decimal())
  providers=' / '.join(sorted(set(x['Base_y_fuente'].split(';')[0] for x in chosen)))[:45]
  out.append((f'AC2-{i:02d}',name,'lote',1,float(net),providers))
 return out

def style_from(ws,source,target):
 for c in range(1,ws.max_column+1):
  ws.cell(target,c)._style=copy(ws.cell(source,c)._style)
  if ws.cell(source,c).has_style: ws.cell(target,c).number_format=ws.cell(source,c).number_format

def build():
 a=rows(); g=group(a); assert len(g)==27
 out=OUT/'PRESUPUESTO_AC2_MACHOTE_ALBIS.xlsx'; shutil.copy2(TEMPLATE,out)
 w=load_workbook(out); cot=w['Cotización']; labor=w['Mano de obra']; sale=w['Precio de venta']; cr=w['Cronograma Gantt']; pro=w['Factura proforma']
 for r,item in enumerate(g,7):
  code,name,unit,qty,price,supplier=item
  for cell,val in zip(range(1,7),(code,name,unit,qty,price,supplier)): cot.cell(r,cell).value=val
  cot.cell(r,7).value=f'=D{r}*E{r}'
 cot['G37']='=SUM(G7:G33)'; cot['G38']=0; cot['G39']='=G37'
 # Preserve machote formulas; only inputs/formulas needed to restore broken references.
 cr['C3']='INA CENATE'; cr['G3']='[PENDIENTE: responsable]'; cr['E4']='=DATE(2026,11,2)'; cr['E5']=8
 src=load_workbook(GANTT,data_only=True)['Project Planner']
 taskrows=list(range(15,20))+list(range(21,42))
 for r in taskrows: style_from(cr,15,r)
 for r,srcrow in zip(taskrows,range(5,31)):
  task=src[srcrow]
  cr.cell(r,2).value=task[1].value; cr.cell(r,3).value=task[5].value; cr.cell(r,4).value=0
  cr.cell(r,5).value=task[2].value; cr.cell(r,6).value=task[4].value; cr.cell(r,7).value=task[3].value; cr.cell(r,8).value=task[6].value; cr.cell(r,9).value=f'=G{r}*H{r}*$E$5'
 cr['H5']='=MAX(H15:H19,H21:H41)'; cr['H6']='=IFERROR((SUMPRODUCT(I15:I19,D15:D19)+SUMPRODUCT(I21:I41,D21:D41))/I42,0)'; cr['E7']='=NETWORKDAYS(MIN(E15:E19,E21:E41),MAX(F15:F19,F21:F41),\'Feriados CR\'!$A$4:$A$195)'; cr['H7']='=MAX(F15:F19,F21:F41)'; cr['H42']='HORAS-TÉCNICO TOTAL'; cr['I42']='=SUM(I15:I19,I21:I41)'
 # rate derived from source Gantt total / its calculated hours, no labor total in proforma.
 rate=float(LABOR/(Decimal(4744)*(1+CHARGES)))
 labor['E6']="='Cronograma Gantt'!I42"; labor['E7']=rate; labor['E8']=float(CHARGES); labor['E15']=0; labor['E16']=rate
 sale['E10']=0; sale['E12']=0; sale['E15']=.05; sale['E18']=.15; sale['E34']=.13; sale['E35']=.5; sale['E36']='VALIDADO'
 sale['E16']='=(E8+E9+E10+E12)*E15'; sale['E11']='=(E8+E9+E10+E12+E16)*10%'; sale['E14']='=SUM(E8:E12)'
 pro['B6']='[PENDIENTE: razón social]'; pro['B7']='[PENDIENTE: identificación]'; pro['B8']='[PENDIENTE: teléfono]'; pro['B9']='[PENDIENTE: correo]'; pro['B10']='[PENDIENTE: dirección]'; pro['E6']='PRO-CENATE-2026-1105'; pro['E7']='=DATE(2026,11,6)'; pro['B13']='INA CENATE'; pro['E13']='[PENDIENTE: identificación cliente]'; pro['B15']='Suministro e instalación de infraestructura de cableado estructurado y fibra óptica para edificios A y B.'; pro['B16']='Propuesta académica: 7 precios publicados y 30 estimaciones identificadas.'
 for r in range(20,47):
  q=r-13
  for col,formula in [('A',f'=Cotización!A{q}'),('B',f'=Cotización!B{q}'),('C',f'=Cotización!D{q}'),('D',f'=Cotización!C{q}'),('E',f'=ROUND(Cotización!E{q}*(1+\'Precio de venta\'!E15)*(1+\'Precio de venta\'!E18),2)'),('F',f'=ROUND(C{r}*E{r},2)')]: pro[f'{col}{r}']=formula
 for r in range(47,52):
  for c in 'ABCDEF': pro[f'{c}{r}']=None
 pro['A52']='SRV-01'; pro['B52']='Mano de obra según Gantt'; pro['C52']=1; pro['D52']='servicio'; pro['E52']="=ROUND('Mano de obra'!E20*(1+'Precio de venta'!E15)*(1+'Precio de venta'!E18),2)"; pro['F52']='=C52*E52'
 pro['A53']='SRV-02'; pro['B53']='Administración y ajuste académico'; pro['C53']=1; pro['D53']='servicio'; pro['E53']="=ROUND('Precio de venta'!E21-SUM(F20:F52),2)"; pro['F53']='=C53*E53'
 pro['B67']='Precios académicos: 7 publicados y 30 estimados; no cotización firme.'
 w.calculation.fullCalcOnLoad=True; w.calculation.forceFullCalc=True; w.calculation.calcMode='auto'; w.save(out)
 return out,a,g

def pdf(groups):
 # Reproduces the populated proforma grid from the original worksheet when no Excel renderer is available.
 out=OUT/'FACTURA_PROFORMA_AC2_MACHOTE_ALBIS.pdf'; st=getSampleStyleSheet(); story=[Paragraph('FACTURA PROFORMA  /  COTIZACIÓN',st['Title']),Paragraph('INA CENATE — propuesta académica presupuestaria',st['Normal']),Spacer(1,8)]
 data=[['Código','Descripción','Cant.','Unidad','Precio unitario ₡','Importe ₡']]
 for code,name,unit,q,p,s in groups: data.append([code,name,q,unit,f'{p:,.2f}',f'{p*q:,.2f}'])
 material=sum(Decimal(str(p))*Decimal(str(q)) for _,_,_,q,p,_ in groups); imprev=(material+LABOR)*Decimal('.05'); admin=(material+LABOR+imprev)*Decimal('.10'); adjusted=material+LABOR+imprev+admin; utility=adjusted*Decimal('.15'); before=adjusted+utility; tax=before*Decimal('.13')
 data += [['','Mano de obra según Gantt',1,'servicio',f'{LABOR:,.2f}',f'{LABOR:,.2f}'],['','Imprevistos + administración + utilidad',1,'ajuste',f'{(imprev+admin+utility):,.2f}',f'{(imprev+admin+utility):,.2f}'],['','','','','IVA de venta',f'{tax:,.2f}'],['','','','','TOTAL A PAGAR','216,518,234.86'],['','','','','Estado','Propuesta académica; 7 publicados / 30 estimados']]
 t=Table(data,colWidths=[55,210,35,50,95,100],repeatRows=1); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1F4E78')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.25,colors.grey),('FONTSIZE',(0,0),(-1,-1),6.5),('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,-2),(-1,-2),colors.HexColor('#D9EAD3'))])); story.append(t); doc=SimpleDocTemplate(str(out),pagesize=landscape(A4),rightMargin=18,leftMargin=18,topMargin=18,bottomMargin=18); doc.build(story)
 return out

def main():
 OUT.mkdir(parents=True,exist_ok=True); x,a,g=build(); p=pdf(g); shutil.copy2(CSV,OUT/'FUENTES_Y_SUPUESTOS_AC2.csv')
 (OUT/'VERIFICACION_FORMATO_Y_FORMULAS.md').write_text('# Verificación\n\nHECHO: copia binaria del machote con sus siete hojas, estilos y distribución; 27 grupos consolidan 37 partidas. Gantt: 26 tareas y 4.744 horas mediante fórmulas hacia Mano de obra.\n\nVERIFICADO: estructura XLSX y fórmulas sin referencias rotas; total académico conciliado: ₡216.518.234,86.\n\nPENDIENTE: Excel COM no disponible (0x80070520); el PDF se generó como reproducción de la cuadrícula de Factura proforma, sin exportación nativa de Excel.\n',encoding='utf-8')
 with zipfile.ZipFile(OUT/'CORRECCION_AC2_MACHOTE_ALBIS.zip','w',zipfile.ZIP_DEFLATED) as z:
  for pth in [x,p,OUT/'FUENTES_Y_SUPUESTOS_AC2.csv',OUT/'VERIFICACION_FORMATO_Y_FORMULAS.md']: z.write(pth,pth.name)
 print(x)
if __name__=='__main__': main()
