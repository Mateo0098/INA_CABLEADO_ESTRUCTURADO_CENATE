"""Controles dirigidos de alcance y coherencia U03; sin dependencias externas."""
import csv
import re
import subprocess
from pathlib import Path

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
rows=list(csv.DictReader((BASE/'UNIDAD_03_MATRIZ_MAESTRA_HERRAMIENTAS.csv').open(encoding='utf-8-sig',newline='')))
checks=[]
def check(label, condition):
    checks.append((label,bool(condition)))
    if not condition: raise AssertionError(label)
check('IDs únicos', len({r['ID único'] for r in rows})==len(rows))
check('Cuatro subunidades', {r['Subunidad de origen'] for r in rows}=={'03A','03B','03C','03D'})
check('Campos completos', all(all(v.strip() for v in r.values()) for r in rows))
check('Nombres funcionales únicos', len({r['Herramienta equipo o consumible'] for r in rows})==len(rows))
check('Sin columnas de precios', not any(re.search('precio|costo|importe',k,re.I) for k in rows[0]))
check('Sin importes monetarios', not re.search(r'₡|\bUSD\b|\bCRC\b|\$\s*\d', (BASE/'UNIDAD_03_MATRIZ_MAESTRA_HERRAMIENTAS.csv').read_text(encoding='utf-8-sig')))
byname={r['Herramienta equipo o consumible']:r for r in rows}
check('TG exacto', byname['Herramienta auxiliar TG']['Modelo o referencia candidata']=='EGJT-1' and 'CJ6X88TGBU' in byname['Herramienta auxiliar TG']['Función técnica'])
check('Panel exacto', byname['Herramienta de impacto de panel']['Modelo o referencia candidata']=='PDT110' and 'NK6XPPG48Y' in byname['Herramienta de impacto de panel']['Función técnica'])
check('Continuidad sin certificación', 'no certifica Cat 6A' in byname['Comprobador de continuidad']['Especificación requerida'])
check('OLTS y OTDR distintos', byname['OLTS monomodo']['Función técnica']!=byname['OTDR monomodo']['Función técnica'] and 'no sustituye OLTS' in byname['OTDR monomodo']['Especificación requerida'])
for n in ('Fusionadora monomodo','Certificador Cat 6A completo','OLTS monomodo','OTDR monomodo'):
    check('Modalidades '+n, all(m in byname[n]['Modalidades de adquisición posibles'] for m in ('Compra','Alquiler','Servicio especializado contratado')))
for n in ('Etiquetas de cable y toma','Limpieza óptica consumible','Protectores de fusión'):
    check('No duplicar U02 '+n, byname[n]['Cantidad de referencia']=='0 ADICIONAL U03' and 'U02-' in byname[n]['Referencia a Unidad 02'])
check('EPP sin cuantificación prematura', all(r['Cantidad de referencia']=='PENDIENTE' for r in rows if r['Categoría']=='EPP'))
check('Portátil común', '03B; 03C; 03D' in byname['Portátil compartida']['Recurso compartido o duplicación'])
check('Pérdidas y fusiones unidades distintas', byname['Servicio de fusión']['Unidad funcional']!=byname['Servicio de medición de pérdida']['Unidad funcional'])
check('Fuente no duplica OLTS', all('Función incluida en OLTS' in byname[n]['Recurso compartido o duplicación'] for n in ('Fuente óptica 1310/1550 nm','Medidor de potencia')))
u02=ROOT/'05_materiales/unidad_02_ampliacion/UNIDAD_02_MATRIZ_MAESTRA_MATERIALES.csv'
u02ids={r['ID único'] for r in csv.DictReader(u02.open(encoding='utf-8-sig',newline=''))}
check('Referencias U02 existentes', all(ref in u02ids for r in rows for ref in re.findall(r'U02-02[A-D]-\d{3}',r['Referencia a Unidad 02'])))
for f in ('UNIDAD_03_MEMORIA_TECNICA.md','UNIDAD_03_PENDIENTES.md','UNIDAD_03_CONCILIACION.md'):
    check('Documento '+f,(BASE/f).is_file())
allowed={'DECISIONES.md','PENDIENTES.md','09_auditorias/ULTIMO_REPORTE_CODEX.md','09_auditorias/REPORTES_CODEX/2026-11-04_UNIDAD03_MATRIZ_MAESTRA.md'}
changed=subprocess.check_output(['git','diff','--name-only','fe132770626d65b258261e45e719420544ffcfd8'],cwd=ROOT,text=True).splitlines()
check('Alcance tracked y archivos protegidos intactos',all(p in allowed or p.startswith('05_materiales/unidad_03_herramientas/') for p in changed))
check('Rama exclusiva',subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='desarrollo-proyecto')
print(f'{len(checks)}/{len(checks)} controles aprobados; {len(rows)} filas; revisión técnica humana pendiente')
