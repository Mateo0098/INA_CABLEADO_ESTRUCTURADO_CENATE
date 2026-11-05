"""Genera la entrega definitiva AC1/AC2 desde las 37 partidas publicadas."""
from __future__ import annotations

import csv
import shutil
import zipfile
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05"
CSV = DEST / "DATOS_PRESUPUESTO_CHATGPT_37_PARTIDAS.csv"
TEMPLATE = ROOT / "insumos_entregable_2/Presupuesto FINAL.xlsx"
GANTT = ROOT / "gantt/GANTT_INA_CABLEADO_2026-2027.xlsx"
AC1 = ROOT / "08_entrega/ENTREGA_FINAL_INA_CENATE"
USD_CRC = Decimal("454.65")
IVA = Decimal("0.13")
LABOR = Decimal("13935679.31514")
IMPREV = Decimal("0.05")
ADMIN = Decimal("0.10")
UTILITY = Decimal("0.15")


def read_rows():
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 37
    for r in rows:
        q, p = Decimal(r["Cantidad"]), Decimal(r["Precio_unitario"])
        gross = q * p * (USD_CRC if r["Moneda"] == "USD" else 1)
        r["Base_neta_CRC"] = gross / (1 + IVA) if r["IVA_origen"] == "Incluido" else gross
        r["IVA_compra_CRC"] = (r["Base_neta_CRC"] * IVA if r["IVA_origen"] in ("Incluido", "Excluido") else None)
    return rows


def total(rows):
    material = sum((r["Base_neta_CRC"] for r in rows), Decimal())
    direct = material + LABOR
    before_utility = direct * (1 + IMPREV) * (1 + ADMIN)
    before_iva = before_utility * (1 + UTILITY)
    return material, before_iva * (1 + IVA)


def clear(ws):
    for rng in list(ws.merged_cells.ranges): ws.unmerge_cells(str(rng))
    ws.delete_rows(1, ws.max_row)


def title(ws, value, cols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=cols)
    c = ws.cell(1, 1, value); c.font = Font(bold=True, color="FFFFFF", size=15)
    c.fill = PatternFill("solid", fgColor="1F4E78"); c.alignment = Alignment(horizontal="center")


def finish(ws):
    ws.freeze_panes = "A3"; ws.sheet_view.showGridLines = False
    for row in ws.iter_rows():
        for c in row: c.alignment = Alignment(vertical="top", wrap_text=True)
    for col in ws.columns:
        ws.column_dimensions[get_column_letter(col[0].column)].width = min(50, max(12, max(len(str(c.value or "")) for c in col) + 2))


def build(rows):
    wb = load_workbook(TEMPLATE)
    cot, labor, sale, profit, gantt, holidays, proforma = [wb[n] for n in ["Cotización", "Mano de obra", "Precio de venta", "Ganancias", "Cronograma Gantt", "Feriados CR", "Factura proforma"]]
    for ws in (cot, labor, sale, profit, gantt, holidays, proforma): clear(ws)
    src = wb.create_sheet("Fuentes y supuestos")
    params = wb.create_sheet("Parámetros")
    title(params, "PARÁMETROS EDITABLES", 3)
    params.append(["Parámetro", "Valor", "Fundamento"])
    for row in [("Tipo de cambio USD/CRC", float(USD_CRC), "Referencia académica publicada"), ("IVA venta", float(IVA), "Referencia"), ("Imprevistos", float(IMPREV), "5 % costo directo"), ("Administración", float(ADMIN), "10 % directo más imprevistos"), ("Utilidad", float(UTILITY), "15 % costo ajustado"), ("Mano de obra Gantt", float(LABOR), "Gantt canónico; 26 actividades, 74 días")]: params.append(row)
    title(cot, "COTIZACIÓN — 37 PARTIDAS ACADÉMICAS", 11)
    cot.append(["ID", "Grupo", "Descripción", "Cantidad", "Unidad", "Precio unitario", "Moneda", "IVA origen", "Base neta CRC", "Clasificación", "Base y fuente"])
    for r in rows:
        cot.append([r[k] for k in ["ID", "Grupo", "Descripción", "Cantidad", "Unidad", "Precio_unitario", "Moneda", "IVA_origen"]] + [float(r["Base_neta_CRC"]), r["Clasificación"], r["Base_y_fuente"]])
    subtotal_row = cot.max_row + 1
    cot.append(["", "", "MATERIALES/EQUIPOS BASE NETA", "", "", "", "", "", f"=SUM(I3:I{subtotal_row-1})", "PARCIAL", "37 partidas académicas"])
    title(labor, "MANO DE OBRA — GANTT CANÓNICO", 5)
    labor.append(["Fuente", "Actividades", "Días hábiles", "Costo interno CRC", "Estado"])
    labor.append(["GANTT_INA_CABLEADO_2026-2027.xlsx", 26, 74, float(LABOR), "Reutilizado sin recálculo"])
    title(sale, "PRECIO DE VENTA — PROPUESTA ACADÉMICA", 4)
    sale.append(["Concepto", "Importe CRC", "Estado", "Nota"])
    sale.append(["Materiales y equipos", f"='Cotización'!I{subtotal_row}", "Parcial", "37 partidas"])
    sale.append(["Mano de obra interna", "='Mano de obra'!D3", "Provisional", "Gantt canónico"])
    sale.append(["Costo directo", "=SUM(B3:B4)", "Parcial", ""])
    sale.append(["Imprevistos", "=B5*'Parámetros'!B4", "Editable", "5 %"])
    sale.append(["Administración", "=(B5+B6)*'Parámetros'!B5", "Editable", "10 %"])
    sale.append(["Costo ajustado", "=SUM(B5:B7)", "Parcial", ""])
    sale.append(["Utilidad", "=B8*'Parámetros'!B6", "Editable", "15 %"])
    sale.append(["Precio antes IVA", "=B8+B9", "Parcial", ""])
    sale.append(["IVA venta", "=B10*'Parámetros'!B3", "Referencia", "13 %"])
    sale.append(["TOTAL ACADÉMICO", "=B10+B11", "ACADÉMICO", "No cotización firme"])
    title(profit, "GANANCIAS — USO INTERNO", 4)
    profit.append(["Indicador", "CRC", "Porcentaje", "Nota"])
    profit.append(["Costo ajustado", "='Precio de venta'!B8", None, ""])
    profit.append(["Utilidad", "='Precio de venta'!B9", "='Parámetros'!B6", "Supuesto comercial"])
    profit.append(["Precio antes IVA", "='Precio de venta'!B10", None, ""])
    title(gantt, "CRONOGRAMA GANTT — REFERENCIA", 5)
    gantt.append(["Archivo incluido", "Inicio", "Final", "Días", "Costo laboral CRC"])
    gantt.append(["../GANTT/GANTT_INA_CABLEADO_2026-2027.xlsx", date(2026,11,2), date(2027,2,16), 74, float(LABOR)])
    gantt["A3"].hyperlink = "../GANTT/GANTT_INA_CABLEADO_2026-2027.xlsx"; gantt["A3"].style = "Hyperlink"
    title(holidays, "FERIADOS CR — REFERENCIA GANTT", 3)
    holidays.append(["Fecha", "Feriado", "Fuente"])
    for d, n in [(date(2026,12,1), "Abolición del Ejército"), (date(2026,12,25), "Navidad"), (date(2027,1,1), "Año Nuevo")]: holidays.append([d,n,"Gantt canónico"])
    title(proforma, "FACTURA PROFORMA — PROPUESTA ACADÉMICA", 6)
    proforma.append(["Proforma", "PRO-CENATE-2026-1105", "Fecha", date(2026,11,5), "Vigencia", "15 días"])
    proforma.append(["Emisor", "[PENDIENTE: razón social, identificación, teléfono y correo]", None, None, None, None])
    proforma.append(["Cliente", "INA CENATE — [PENDIENTE: contacto y datos fiscales]", None, None, None, None])
    proforma.append(["Proyecto", "Suministro e instalación de infraestructura de cableado estructurado y fibra óptica para edificios A y B del INA CENATE.", None, None, None, None])
    proforma.append([]); proforma.append(["Concepto", "Alcance", "Antes IVA", "IVA", "Total", "Estado"])
    proforma.append(["Materiales/equipos", "37 partidas", "='Precio de venta'!B3", 0, "=C8", "Académico"])
    proforma.append(["Mano de obra", "Gantt canónico", "='Precio de venta'!B4", 0, "=C9", "Académico"])
    proforma.append(["Recargos y utilidad", "Parámetros editables", "='Precio de venta'!B6+'Precio de venta'!B7+'Precio de venta'!B9", 0, "=C10", "Académico"])
    proforma.append(["IVA de venta", "Referencia 13 %", 0, "='Precio de venta'!B11", "=D11", "Referencia"])
    proforma.append(["TOTAL PROPUESTA ACADÉMICA", "", "=C8+C9+C10", "=D8+D9+D10+D11", "=E8+E9+E10+E11", "No oferta firme"])
    proforma.append(["Condición", "Propuesta académica presupuestaria: siete precios publicados y treinta estimaciones identificadas; no es cotización comercial firme ni comprobante fiscal.", None, None, None, None])
    title(src, "FUENTES Y SUPUESTOS — 37 PARTIDAS", 11)
    src.append(["ID","Grupo","Descripción","Cantidad","Unidad","Precio","Moneda","IVA origen","Base neta CRC","Clasificación","Base/fuente"])
    for r in rows: src.append([r[k] for k in ["ID","Grupo","Descripción","Cantidad","Unidad","Precio_unitario","Moneda","IVA_origen"]]+[float(r["Base_neta_CRC"]),r["Clasificación"],r["Base_y_fuente"]])
    for ws in wb.worksheets:
        finish(ws)
        if ws.max_row >= 2:
            for c in ws[2]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="4F81BD")
    for ws in (cot, labor, sale, profit, proforma, src):
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value,(int,float)) and c.column >= 2: c.number_format = '₡#,##0.00;[Red](₡#,##0.00)'
    wb.calculation.fullCalcOnLoad = True; wb.calculation.forceFullCalc = True; wb.calculation.calcMode = "auto"
    return wb


def write_pdf(rows, grand):
    p=DEST/'ACTIVIDAD_2/FACTURA_PROFORMA_CENATE_AC2.pdf'; p.parent.mkdir(parents=True,exist_ok=True)
    doc=SimpleDocTemplate(str(p),pagesize=A4,rightMargin=1.4*cm,leftMargin=1.4*cm,topMargin=1.3*cm,bottomMargin=1.3*cm)
    s=getSampleStyleSheet(); story=[Paragraph("FACTURA PROFORMA — PROPUESTA ACADÉMICA",s['Title']),Spacer(1,.2*cm),Paragraph("Proforma PRO-CENATE-2026-1105 · Fecha 2026-11-05 · Vigencia 15 días",s['Normal']),Spacer(1,.15*cm),Paragraph("Emisor: [PENDIENTE: datos legales]. Cliente: INA CENATE — [PENDIENTE: datos fiscales].",s['Normal']),Spacer(1,.25*cm)]
    material, _=total(rows); direct=material+LABOR; recargos=(direct*(1+IMPREV)*(1+ADMIN)*(1+UTILITY))-direct
    data=[["Concepto","CRC","Estado"],["Materiales y equipos",f"CRC {material:,.2f}","37 partidas"],["Mano de obra",f"CRC {LABOR:,.2f}","Gantt canónico"],["Recargos y utilidad",f"CRC {recargos:,.2f}","Académico"],["IVA venta",f"CRC {(grand/(1+IVA)*IVA):,.2f}","Referencia"],["TOTAL",f"CRC {grand:,.2f}","Académico"]]
    t=Table(data,colWidths=[8*cm,5*cm,4*cm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1F4E78')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.3,colors.grey),('BACKGROUND',(0,-1),(-1,-1),colors.HexColor('#D9EAD3')),('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold'),('PADDING',(0,0),(-1,-1),6)])); story += [t,Spacer(1,.35*cm),Paragraph("Propuesta académica presupuestaria basada en siete precios publicados y treinta estimaciones identificadas. No es cotización comercial firme ni comprobante fiscal electrónico.",s['BodyText'])]; doc.build(story)


def copy_files(rows, grand):
    a1=DEST/'ACTIVIDAD_1'; a2=DEST/'ACTIVIDAD_2'; a1.mkdir(parents=True,exist_ok=True); a2.mkdir(parents=True,exist_ok=True)
    plans=a1/'PLANOS_TECNICOS_PDF_A3'; plans.mkdir(exist_ok=True)
    for p in (AC1/'06_PLANOS_TECNICOS/PDF_A3').glob('*.pdf'): shutil.copy2(p,plans/p.name)
    shutil.copy2(AC1/'01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx',a1/'INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx')
    (DEST/'GANTT').mkdir(exist_ok=True); shutil.copy2(GANTT,DEST/'GANTT'/GANTT.name)
    shutil.copy2(CSV,a2/'FUENTES_Y_SUPUESTOS_AC2.csv')
    (a2/'CORREO_ENTREGA_AC2.txt').write_text("Asunto: ACTIVIDAD DE COMPROBACIÓN 2\n\nEstimado cliente:\n\nAdjuntamos la propuesta académica presupuestaria para el suministro e instalación de infraestructura de cableado estructurado y fibra óptica en los edificios A y B del INA CENATE. Se incluyen el presupuesto editable, la proforma y sus fuentes y supuestos.\n\nLa propuesta distingue siete precios publicados de treinta estimaciones académicas identificadas; no constituye una cotización comercial firme ni comprobante fiscal. Se adjunta también la documentación final de la Actividad 1.\n\nAtentamente,\n[PENDIENTE: datos del emisor]\n",encoding='utf-8')
    write_pdf(rows,grand)


def main():
    rows=read_rows(); material, grand=total(rows)
    assert grand.quantize(Decimal('.01'),rounding=ROUND_HALF_UP)==Decimal('216518234.86')
    copy_files(rows,grand)
    wb=build(rows); out=DEST/'ACTIVIDAD_2/PRESUPUESTO_FINAL_CENATE_AC2.xlsx'; wb.save(out)
    with zipfile.ZipFile(out) as z: assert z.testzip() is None
    zip_path=DEST/'ENTREGA_DEFINITIVA_AC1_AC2.zip'
    with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
        for p in DEST.rglob('*'):
            if p.is_file() and p.name not in {zip_path.name,'README.md','DATOS_PRESUPUESTO_CHATGPT_37_PARTIDAS.csv'}: z.write(p,p.relative_to(DEST))
    print(f'material={material:.2f} total={grand:.2f}')

if __name__ == '__main__': main()
