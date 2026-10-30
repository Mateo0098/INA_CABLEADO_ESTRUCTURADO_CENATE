"""Controles técnicos y de integridad de las nueve láminas A3 de Fase 5C.

La inspección visual humana se registra por separado en el reporte de cierre.
"""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import argparse
import re
import zipfile
import xml.etree.ElementTree as ET
import fitz
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
DEFAULT=ROOT/"08_entrega/PLANOS_FASE5C_TRABAJO"
BOOK=ROOT/"08_entrega/ENTREGA_FINAL_INA_CENATE/01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx"
S="{http://www.w3.org/2000/svg}"
STEMS=["01_ext_01","02_pla_a","03_pla_b","04_wa_a","05_wa_b","06_er_a","07_tr_a","08_er_b","09_tr_b"]

def cached_excel():
    ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
    with zipfile.ZipFile(BOOK) as z:
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        rels={e.attrib['Id']:e.attrib['Target'] for e in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        sheet=wb.find('m:sheets/m:sheet',ns)
        target=rels[sheet.attrib['{'+ns['r']+'}id']]
        if not target.startswith('xl/'): target='xl/'+target
        root=ET.fromstring(z.read(target))
        return {e.attrib['r']:e.findtext('m:v',default='',namespaces=ns) for e in root.findall('.//m:sheetData/m:row/m:c',ns)}

def validate(base):
    checks=[]
    def check(ok,label): checks.append((bool(ok),label))
    svgdir,pdfdir,pngdir=(base/d for d in ('SVG_EDITABLE','PDF_A3','PNG'))
    for d,ext in ((svgdir,'.svg'),(pdfdir,'.pdf'),(pngdir,'.png')):
        check(sorted(x.stem for x in d.glob('*'+ext))==STEMS,f"Nueve {ext} vigentes y ordenados")
    roots={stem:ET.parse(svgdir/(stem+'.svg')).getroot() for stem in STEMS}
    text={stem:' '.join(x.text or '' for x in root.iter(S+'text')) for stem,root in roots.items()}
    for stem,root in roots.items():
        check(root.attrib.get('viewBox')=='0 0 1680 1188',f"SVG A3: {stem}")
        check('PROTOTIPO' not in text[stem] and '2026-10-29' in text[stem] and f'LÁMINA {int(stem[:2]):02d}/09' in text[stem],f"Cajetín definitivo: {stem}")
        geom=sum(len(root.findall('.//'+S+kind)) for kind in ('rect','line','circle','polyline'))
        check(geom>=100,f"Geometría vectorial: {stem}")
    for stem,count,assigned in (('07_tr_a',4,160),('09_tr_b',5,192)):
        groups=[g for g in roots[stem].iter(S+'g') if g.attrib.get('data-view')=='rack' and 'data-panel' in g.attrib]
        bypanel=Counter(g.attrib['data-panel'] for g in groups)
        check(bypanel=={f'PP{i:02d}':48 for i in range(1,count+1)},f"{stem}: {count} paneles de 48 RJ45 dibujados")
        check(sum(g.attrib.get('data-assigned')=='true' for g in groups)==assigned,f"{stem}: {assigned} asignados")
        check(len(groups)-assigned==(32 if count==4 else 48),f"{stem}: reserva física correcta")
        check(all({int(g.attrib['data-port']) for g in groups if g.attrib['data-panel']==f'PP{i:02d}'}==set(range(1,49)) for i in range(1,count+1)),f"{stem}: puertos 01–48 por panel")
        check(all(len(g.findall(S+'rect'))>=3 for g in groups),f"{stem}: cada RJ45 tiene geometría frontal")
        check(all(f'{u:02d}' in [t.text for t in roots[stem].iter(S+'text')] for u in range(1,43)),f"{stem}: numeración 01–42U")
    for stem in ('04_wa_a','05_wa_b'):
        labels=[x.text for x in roots[stem].iter(S+'text') if re.fullmatch(r'WA-\d{2}',x.text or '')]
        check(labels==[f'WA-{i:02d}' for i in range(1,17)],f"{stem}: 16 WA numeradas")
        check(len(roots[stem].findall('.//'+S+'rect'))>=100 and '32 puertos RJ45' in text[stem],f"{stem}: 32 RJ45 y mobiliario físico")
    for stem,n in (('02_pla_a',5),('03_pla_b',6)):
        labs=[x.text for x in roots[stem].iter(S+'text') if re.fullmatch(r'LAB [AB]-\d{2}',x.text or '')]
        check(len(labs)==n and len(set(labs))==n,f"{stem}: {n} laboratorios únicos")
        check('100 × 50 mm' in text[stem] and 'Ø25' in text[stem] and 'SUPUESTO' in text[stem],f"{stem}: bandeja/tubo/supuestos")
    for stem,a,b in (('06_er_a',4,2),('08_er_b',7,2)):
        c=Counter(g.attrib['data-cassette'] for g in roots[stem].iter(S+'g') if g.attrib.get('data-view')=='rack' and 'data-cassette' in g.attrib)
        check(c=={'12F':a,'24F':b},f"{stem}: cassettes del housing {a}×12F + {b}×24F")
        check('OS2 24F' in text[stem] and 'OS2 12F' in text[stem],f"{stem}: fibras exterior y vertical")
    check(all(k in text['01_ext_01'] for k in ('E1','E2','E3','221,55 m','247,80 m','69,30 m','no mediciones')),"Backbone exterior: enlaces y distancias de escenario")
    check('PP-B-Pxx-05' in text['09_tr_b'] and 'PP-A-Pxx-05' not in text['09_tr_b'],"Identificador correcto del detalle TR-B")
    combined=base/'PLANOS_TECNICOS_INA_CENATE_9_LAMINAS.pdf'
    with fitz.open(combined) as d:
        check(len(d)==9,"PDF combinado: nueve páginas")
        for i,stem in enumerate(STEMS):
            with fitz.open(pdfdir/(stem+'.pdf')) as single:
                pg=single[0]; cp=d[i]
                check(len(single)==1 and abs(pg.rect.width-1190.551)<.03 and abs(pg.rect.height-841.89)<.03,f"{stem}: PDF A3 horizontal")
                check(cp.get_text()==pg.get_text(),f"{stem}: combinado coincide con individual")
                spans=[sp for b in pg.get_text('dict')['blocks'] if 'lines' in b for ln in b['lines'] for sp in ln['spans']]
                check(all(sp['bbox'][0]>=10 and sp['bbox'][1]>=10 and sp['bbox'][2]<=pg.rect.width-10 and sp['bbox'][3]<=pg.rect.height-10 for sp in spans),f"{stem}: texto dentro de márgenes")
                check(len(pg.get_drawings())>100 and not pg.get_images() and '\ufffd' not in pg.get_text() and 'LÁMINA' in pg.get_text(),f"{stem}: vectorial y Unicode seleccionable")
                im=Image.open(pngdir/(stem+'.png'))
                check(im.size==(4961,3508),f"{stem}: PNG 300 ppp")
    cells=cached_excel()
    check((cells.get('G3'),cells.get('G4'),cells.get('G14'),cells.get('G15'))==('51','1984','22','6'),"Excel definitivo sin cambios: 51 paneles, 1984 RJ45, 22×12F, 6×24F")
    for ok,label in checks: print(('OK   ' if ok else 'FALLO ')+label)
    fails=[x for ok,x in checks if not ok]
    print(f"RESULTADO {len(checks)-len(fails)}/{len(checks)}")
    if fails: raise SystemExit(1)

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--base',type=Path,default=DEFAULT)
    validate(parser.parse_args().base)
