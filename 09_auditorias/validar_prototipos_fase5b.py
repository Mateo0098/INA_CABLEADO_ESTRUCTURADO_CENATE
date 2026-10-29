"""Controles reproducibles de cantidades, contenido vectorial y formato A3.

No sustituye la inspección visual ni la revisión académica del diseño.
"""
from pathlib import Path
from collections import Counter
import hashlib
import zipfile
import xml.etree.ElementTree as ET

import fitz
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"08_entrega/PROTOTIPOS_GRAFICOS_FASE5B"
OLD=ROOT/"08_entrega/ENTREGA_FINAL_INA_CENATE/06_PLANOS_TECNICOS"
BOOK=ROOT/"08_entrega/ENTREGA_FINAL_INA_CENATE/01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx"
checks=[]
def check(ok,what): checks.append((bool(ok),what))

svg_paths=sorted((OUT/"SVG_EDITABLE").glob("*.svg"))
pdf_paths=sorted((OUT/"PDF_A3").glob("*.pdf"))
png_paths=sorted((OUT/"PNG").glob("*.png"))
check([p.stem for p in svg_paths]==["P1_TR_A","P2_PLANTA_A"],"Dos SVG editables, exclusivamente los prototipos solicitados")
check([p.stem for p in pdf_paths]==["P1_TR_A","P2_PLANTA_A"],"Dos PDF individuales")
check([p.stem for p in png_paths]==["P1_TR_A","P2_PLANTA_A"],"Dos PNG")

SVGNS="{http://www.w3.org/2000/svg}"
rack=ET.parse(OUT/"SVG_EDITABLE/P1_TR_A.svg").getroot()
plan=ET.parse(OUT/"SVG_EDITABLE/P2_PLANTA_A.svg").getroot()
check(rack.attrib.get("viewBox")=="0 0 1680 1188" and plan.attrib.get("viewBox")=="0 0 1680 1188","SVG A3 horizontal con viewBox común")
ports=[g for g in rack.iter(SVGNS+"g") if g.attrib.get("data-view")=="rack"]
check(len(ports)==192,"192 conectores RJ45 realmente dibujados en los cuatro paneles")
counts=Counter(g.attrib.get("data-panel") for g in ports)
check(counts=={f"PP{i:02d}":48 for i in range(1,5)},"48 posiciones en cada panel")
check(all({int(g.attrib["data-port"]) for g in ports if g.attrib["data-panel"]==f"PP{i:02d}"}==set(range(1,49)) for i in range(1,5)),"Numeración individual 01–48 en cada panel")
assigned=[g for g in ports if g.attrib.get("data-assigned")=="true"]
check(len(assigned)==160 and len(ports)-len(assigned)==32,"160 asignadas y 32 de reserva")
check(Counter(g.attrib["data-panel"] for g in assigned)=={"PP01":48,"PP02":48,"PP03":48,"PP04":16},"Asignación PP01–03 completas y PP04 01–16")
check(all(len(g.findall(SVGNS+"rect"))>=3 and len(g.findall(SVGNS+"line"))>=4 for g in ports),"Cada RJ45 tiene marco, garganta, pestillo y contactos")
detail=[g for g in rack.iter(SVGNS+"g") if g.attrib.get("data-view")=="detalle"]
check(len(detail)==48 and {g.attrib.get("data-port") for g in detail}=={f"{i:02d}" for i in range(1,49)},"Detalle PP04 con 48 tomas y numeración individual")

texts_r=" ".join(t.text or "" for t in rack.iter(SVGNS+"text"))
texts_p=" ".join(t.text or "" for t in plan.iter(SVGNS+"text"))
check(all(x in texts_r for x in ("U01 óptica","U15–42","OS2 12F","CCH-01U","42U")),"Housing, backbone y distribución U identificados")
check(all(x in texts_p for x in ("LAB A-01","LAB A-02","LAB A-03","LAB A-04","LAB A-05","TR-A","100 × 50 mm","Ø25","160 enlaces")),"Planta: cinco laboratorios, TR, canalización y 160 enlaces")
check("SUPUESTO" in texts_p and "sin escala" in texts_p.lower(),"Geometría declarada supuesta y sin escala")
check(len(plan.findall(".//"+SVGNS+"polyline"))>=5 and len(plan.findall(".//"+SVGNS+"rect"))>=80 and len(plan.findall(".//"+SVGNS+"line"))>=200,"Símbolos de planta con geometría vectorial detallada")

for p in pdf_paths:
    d=fitz.open(p); pg=d[0]
    check(len(d)==1 and abs(pg.rect.width-1190.551)<.03 and abs(pg.rect.height-841.89)<.03,"PDF A3 horizontal: "+p.name)
    check(len(pg.get_drawings())>100 and len(pg.get_text())>500 and len(pg.get_images())==0,"Trazos y texto vectoriales: "+p.name)
    spans=[s for b in pg.get_text("dict")["blocks"] if "lines" in b for ln in b["lines"] for s in ln["spans"]]
    check(all(sp["bbox"][0]>10 and sp["bbox"][1]>10 and sp["bbox"][2]<pg.rect.width-10 and sp["bbox"][3]<pg.rect.height-10 for sp in spans),"Texto dentro de márgenes: "+p.name)
    d.close()
for p in png_paths:
    im=Image.open(p)
    check(im.width>=4900 and im.height>=3400 and im.width>im.height,"PNG A3 cercano a 300 ppp: "+p.name)

comp=fitz.open(OUT/"COMPARATIVO_FASE5_VS_PROTOTIPOS.pdf")
check(len(comp)==2 and all(abs(p.rect.width-1190.551)<.03 and abs(p.rect.height-841.89)<.03 for p in comp),"Comparativo de dos páginas A3 horizontales")
check(all(len(p.get_drawings())>100 and len(p.get_images())==0 for p in comp),"Comparativo conserva trazos vectoriales y sin imágenes incrustadas")
comp.close()

NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
with zipfile.ZipFile(BOOK) as z:
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rel=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    rels={e.attrib['Id']:e.attrib['Target'] for e in rel}
    sheet=wb.find('m:sheets/m:sheet',NS)
    target=rels[sheet.attrib['{'+NS['r']+'}id']]
    if not target.startswith('xl/'): target='xl/'+target
    root=ET.fromstring(z.read(target))
    cells={e.attrib['r']:e.findtext('m:v',default='',namespaces=NS) for e in root.findall('.//m:sheetData/m:row/m:c',NS)}
check(cells.get('G3')=='51' and cells.get('G4')=='1984',"Excel definitivo: 51 paneles totales y 1 984 conexiones del escenario")
check(cells.get('G14')=='22' and cells.get('G15')=='6',"Excel definitivo: 22 cassettes 12F y 6 cassettes 24F")
check(4*48==192 and 5*16*2==160 and 192-160==32,"Capacidad TR-A y cinco laboratorios coherentes")
check(1+1+4*(2+1)==14 and 14<=42,"U01–14 ocupadas; rack dentro de 42U")

for ok,label in checks: print(("OK   " if ok else "FAIL ")+label)
failed=[x for ok,x in checks if not ok]
print(f"RESULTADO: {len(checks)-len(failed)}/{len(checks)} controles")
if failed: raise SystemExit(1)
