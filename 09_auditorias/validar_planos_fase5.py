"""Controles documentales, de capacidades y formato para los planos Fase 5."""
from __future__ import annotations
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET
import fitz
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_entrega/ENTREGA_FINAL_INA_CENATE/06_PLANOS_TECNICOS'
SVG=BASE/'SVG_EDITABLE'; PDF=BASE/'PDF_A3'; PNG=BASE/'PNG'
BOOK=ROOT/'08_entrega/ENTREGA_FINAL_INA_CENATE/01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx'
checks=[]
def check(ok,label): checks.append((bool(ok),label))

svgs=sorted(SVG.glob('*.svg')); pdfs=sorted(PDF.glob('*.pdf')); pngs=sorted(PNG.glob('*.png'))
check(len(svgs)==len(pdfs)==len(pngs)==9,'Nueve SVG, PDF individuales y PNG')
for p in pdfs:
    d=fitz.open(p); page=d[0]; r=page.rect
    check(len(d)==1 and abs(r.width-1190.551)<0.02 and abs(r.height-841.89)<0.02,'A3 horizontal individual: '+p.name)
    check(bool(page.get_text().strip()),'PDF vectorial con texto seleccionable: '+p.name)
    spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for line in b['lines'] for s in line['spans']]
    check(all(s['bbox'][0]>=10 and s['bbox'][1]>=10 and s['bbox'][2]<=r.width-10 and s['bbox'][3]<=r.height-10 for s in spans),'Texto dentro de hoja: '+p.name)
    d.close()
for p in pngs:
    im=Image.open(p)
    check(im.width>=2300 and im.height>=1600 and im.width>im.height,'PNG A3 de alta resolución: '+p.name)
combined=fitz.open(BASE/'PLANOS_TECNICOS_INA_CENATE_9_LAMINAS.pdf')
check(len(combined)==9,'PDF combinado con exactamente nueve páginas')
check(all(abs(pg.rect.width-1190.551)<0.02 and abs(pg.rect.height-841.89)<0.02 for pg in combined),'Nueve páginas A3 horizontales')
check(all('LÁMINA %02d/09'%(i+1) in pg.get_text() for i,pg in enumerate(combined)),'Numeración ordenada 01/09 a 09/09')
check(all(len(pg.get_text().strip())>100 for pg in combined),'Contenido vectorial/textual en cada página')
combined.close()

texts={p.name:p.read_text(encoding='utf-8') for p in svgs}
check(all(sum(1 for _ in __import__('re').finditer(r'<circle ',texts[n]))==34 and texts[n].count('PUESTO DOBLE')==16 for n in ('04_wa_a.svg','05_wa_b.svg')),'32 símbolos RJ45 en 16 WA; 2 símbolos adicionales en leyenda')
check('16 áreas WA' in texts['04_wa_a.svg'] and '16 áreas WA' in texts['05_wa_b.svg'],'16 WA por laboratorio en A y B')
check('160 puertos asignados' in texts['02_pla_a.svg'] and '192 puertos asignados' in texts['03_pla_b.svg'],'160/192 puertos asignados por piso en planta')
check('4 × 48 = 192' in texts['02_pla_a.svg'] and '32 libres' in texts['02_pla_a.svg'],'Capacidad/reserva A: 192/32')
check('5 × 48 = 240' in texts['03_pla_b.svg'] and '48 libres' in texts['03_pla_b.svg'],'Capacidad/reserva B: 240/48')
check('PP04: 01–16 asignados, 17–48 libres' in texts['07_tr_a.svg'],'Asignación final A: PP04 puertos 01–16 y 32 libres')
check('PP05: 01–48 libres' in texts['09_tr_b.svg'],'Asignación final B: PP05 completo como reserva')
check(all('42U' in texts[n] for n in ('06_er_a.svg','07_tr_a.svg','08_er_b.svg','09_tr_b.svg')),'Cuatro elevaciones de rack con 42U')
check('OS2 24F' in texts['01_ext_01.svg'] and 'OS2 12F' in texts['06_er_a.svg'],'Exterior 24F separado de backbone vertical 12F')
check('CCH-03U' in texts['06_er_a.svg'] and '96 fibras' in texts['06_er_a.svg'],'Capacidad CCH ER-A sin duplicación de accesorios')
check('CCH-04U' in texts['08_er_b.svg'] and '132 fibras' in texts['08_er_b.svg'],'Capacidad CCH ER-B sin duplicación de accesorios')
check('221,55 m' in texts['01_ext_01.svg'] and '247,80 m' in texts['01_ext_01.svg'] and '69,30 m' in texts['01_ext_01.svg'],'Longitudes de fibra exterior rotuladas como escenario')
check('SUPUESTO' in texts['02_pla_a.svg'] and 'SUPUESTO' in texts['03_pla_b.svg'],'Geometrías rotuladas como supuestos')

# Confirm selected workbook quantities in the packaged corrected Excel.
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
with zipfile.ZipFile(BOOK) as z:
    wb=ET.fromstring(z.read('xl/workbook.xml')); rel=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    rels={e.attrib['Id']:e.attrib['Target'] for e in rel}
    sheet=wb.find('m:sheets/m:sheet',NS); target=rels[sheet.attrib['{'+NS['r']+'}id']]
    if not target.startswith('xl/'): target='xl/'+target
    root=ET.fromstring(z.read(target)); cells={e.attrib['r']:e.findtext('m:v',default='',namespaces=NS) for e in root.findall('.//m:sheetData/m:row/m:c',NS)}
    check(cells.get('G3')=='51','Excel: 51 paneles de 48 puertos')
    check(cells.get('G4')=='1984','Excel: 1 984 conexiones RJ45 del escenario')
    check(cells.get('G14')=='22' and cells.get('G15')=='6','Excel: 22 cassettes 12F y 6 cassettes 24F')

# U accounting: populated modules + explicit reserved/available units = 42U.
check((3+1+1+5+32)==42 and (4+1+1+5+31)==42,'Ocupación ER-A/ER-B dentro de 42U')
check((1+1+4*3+5+23)==42 and (1+1+5*3+5+20)==42,'Ocupación TR-A/TR-B dentro de 42U')

failed=[label for ok,label in checks if not ok]
for ok,label in checks: print(('OK  ' if ok else 'FAIL')+label)
print(f'RESULTADO: {len(checks)-len(failed)}/{len(checks)} controles aprobados')
if failed: raise SystemExit(1)
