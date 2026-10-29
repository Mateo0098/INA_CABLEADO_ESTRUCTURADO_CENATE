# Cierre Fase 5 - nueve planos tecnicos A3

**Fecha:** 2026-10-28
**Fase:** 5 - planos tecnicos profesionales
**Rama:** `desarrollo-proyecto`
**Commit de implementacion:** `9d3deef1ff1aa876a764b9946b642f7b8808c2db` (`feat: agregar nueve planos tecnicos A3 Fase 5`)
**Paquete:** `08_entrega/ENTREGA_FINAL_INA_CENATE/06_PLANOS_TECNICOS/`

## Objetivo y alcance

Se reemplazo la coleccion grafica de referencia como version vigente por nueve laminas tecnicas editables y listas para salida A3 horizontal. Se generaron nueve SVG, nueve PDF individuales, nueve PNG de 2382 x 1684 px y un PDF vectorial combinado de nueve paginas. Se conservaron los graficos anteriores y se identificaron como historicos en el indice de entrega y el README de Fase 2B.

El trabajo cubrio backbone exterior; plantas de distribucion A/B; laboratorios tipicos A/B; elevaciones ER-A, TR-A, ER-B y TR-B. No es un diseno constructivo ni acredita mediciones o inspeccion de campo.

## Entradas y fuentes examinadas

- `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md` y `09_auditorias/ULTIMO_REPORTE_CODEX.md`.
- `03_diseno/DISENO_INTEGRADO_REFERENCIA_FASE2.md`, `05_materiales/MATRIZ_TECNICA_FASE2D.md`, `04_calculos/MEMORIA_CANTIDADES_FASE3B.md` y sus resultados Fase 2D.
- `01_requisitos/MATRIZ_REQUISITOS.md`, requisitos de imagen INA-030 a INA-037 e INA-072 a INA-076.
- Excel corregido `08_entrega/ENTREGA_FINAL_INA_CENATE/01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx`.
- Nueve SVG/PNG historicos de `07_imagenes/fase2b/` y los archivos fuente del indice, memoria y guia de defensa del paquete.

## Clasificacion de datos y decisiones graficas

| Dato representado | Valor | Clasificacion y tratamiento |
|---|---:|---|
| Pisos, laboratorios y area | A: 4 pisos, 5 laboratorios/piso, 85 m2; B: 7 pisos, 6 laboratorios/piso, 75 m2 | Dato academico establecido en los documentos del proyecto. |
| Areas dobles y salidas | 16 WA por laboratorio; 2 RJ45 por WA; 32 enlaces por laboratorio | El minimo de 16 WA es academico; la interpretacion de dos tomas y sus cantidades son supuesto adoptado en el Excel. |
| Salidas por piso | A: 160; B: 192 | Resultado calculado y contrastado con el Excel. |
| Paneles por TR | A: 4 x 48 = 192 posiciones; 160 asignadas y 32 libres. B: 5 x 48 = 240; 192 asignadas y 48 libres | Capacidad y reserva calculadas. Paneles pasivos; no representan puertos de switch activos. |
| Fibra exterior | E1 221,55 m; E2 247,80 m; E3 69,30 m de cable OS2 24F | Resultados del escenario Excel. E1 usa 145 m reportados + 50 m propuestos; x=75 m e y=50 m son supuestos. Ninguna longitud es medicion de campo. |
| Backbone vertical | OS2 12F; A 4 enlaces, B 7 enlaces | Se diferencia graficamente de los cables exteriores OS2 24F. Metrajes del escenario, no mediciones. |
| Terminacion optica ER | ER-A CCH-03U: 4 cassettes 12F + 2 cassettes 24F = 96 fibras; ER-B CCH-04U: 7 cassettes 12F + 2 cassettes 24F = 132 fibras | Capacidad funcional indicada en la matriz. Se representa cassette integrado; no se duplican pigtails o adaptadores. |
| Canalizacion | Bandeja 100 x 50 mm y tubo nominal 25 mm; ducto exterior existente/nuevo | Especificacion preliminar del escenario; secciones, ocupacion, rutas y estado requieren validacion. |
| Geometria | Laboratorios 10 x 8,5 m y 10 x 7,5 m; pasillo 2,4 m; TR 3 x 3 m | Supuestos esquematicos. Plantas sin escala numerica y dimensiones rotuladas como supuestas. |
| Racks | ER-A/B y TR-A/B de 42U | Hipotesis de espacio representada en elevacion. Distribucion de U no sustituye validacion de recinto, energia, carga y equipos. |

## Archivos modificados

- `.gitattributes` - evita conversion de finales de linea en PDF, PNG y XLSX; fija SVG en LF.
- `README.md`, `DECISIONES.md`, `PENDIENTES.md`.
- `07_imagenes/fase2b/README.md` - rotulo historico.
- `08_entrega/ENTREGA_FINAL_INA_CENATE/INDICE_ENTREGABLES.pdf`.
- `08_entrega/ENTREGA_FINAL_INA_CENATE/INVENTARIO_SHA256.txt`.
- `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/INDICE_ENTREGABLES.md`.
- `09_auditorias/ULTIMO_REPORTE_CODEX.md` - indice de transferencia actualizado.

## Archivos creados

Generador y validador: `09_auditorias/generar_planos_fase5.py` y `09_auditorias/validar_planos_fase5.py`.

Reporte de cierre: `09_auditorias/REPORTES_CODEX/2026-10-28_FASE5_PLANOS_TECNICOS.md`.

PDF combinado: `06_PLANOS_TECNICOS/PLANOS_TECNICOS_INA_CENATE_9_LAMINAS.pdf`.

PDF individuales en `06_PLANOS_TECNICOS/PDF_A3/`: `01_ext_01.pdf`, `02_pla_a.pdf`, `03_pla_b.pdf`, `04_wa_a.pdf`, `05_wa_b.pdf`, `06_er_a.pdf`, `07_tr_a.pdf`, `08_er_b.pdf`, `09_tr_b.pdf`.

PNG en `06_PLANOS_TECNICOS/PNG/`: `01_ext_01.png`, `02_pla_a.png`, `03_pla_b.png`, `04_wa_a.png`, `05_wa_b.png`, `06_er_a.png`, `07_tr_a.png`, `08_er_b.png`, `09_tr_b.png`.

SVG editables en `06_PLANOS_TECNICOS/SVG_EDITABLE/`: `01_ext_01.svg`, `02_pla_a.svg`, `03_pla_b.svg`, `04_wa_a.svg`, `05_wa_b.svg`, `06_er_a.svg`, `07_tr_a.svg`, `08_er_b.svg`, `09_tr_b.svg`.

## Archivos decisivos no modificados

- El Excel corregido en el paquete y su copia de trabajo en `06_excel/`.
- `04_MEMORIA_TECNICA/MEMORIA_TECNICA_RESUMIDA.pdf` y `05_DEFENSA/GUIA_DEFENSA_INDIVIDUAL_8_MIN.pdf`.
- Las nueve parejas PNG/SVG anteriores en `02_DISENOS_PNG/` y `03_DISENOS_EDITABLES_SVG/`, y sus fuentes de `07_imagenes/fase2b/`; se conservaron como historicas.
- Requisitos oficiales, matriz, calculos Fase 2D/3B y matriz tecnica de materiales.
- Rama `main` y archivos Excel originales.

## Verificaciones

| Comando/control | Resultado |
|---|---|
| `python 09_auditorias/generar_planos_fase5.py` | Genera 9/9 SVG, PDF individual y PNG, mas PDF combinado. |
| `python 09_auditorias/validar_planos_fase5.py` | 59/59 controles aprobados. |
| Render PyMuPDF de los nueve PNG; revision de mosaico y detalle A3 de TR-A | Nueve hojas revisadas; texto, limites, rutas, cajetines y puertos legibles; se ajustaron etiquetas U, cajetin y rango del panel antes del cierre. |
| Verificacion PDF | Nueve paginas exactas, A3 horizontal (420 x 297 mm), numeracion 01/09 a 09/09 y texto/trazos vectoriales seleccionables. |
| Verificacion PNG | 2382 x 1684 px por lamina. |
| Control de Excel y capacidades | 51 paneles totales; 1 984 conexiones del escenario; 160 por TR A; 192 por TR B; 32 por laboratorio; reservas 32/48. |
| Control de racks y fibra | Cuatro elevaciones de 42U; exterior 24F separado del vertical 12F; capacidad CCH A 96F y B 132F; sin conteo duplicado de accesorios. |
| Integridad | 21/21 archivos protegidos del paquete conservaron SHA-256; inventario actualizado a 50 archivos y todos sus hashes coinciden. Los 10 PDF del plano quedaron registrados como binarios y sus blobs Git coinciden con los bytes locales. |
| `git diff --cached --check` | Sin errores despues de marcar formatos binarios. |

No se realizo impresion fisica. La entrega academica indicada en los requisitos es digital. Los controles automatizados no certifican la exactitud constructiva ni sustituyen la revision personal del estudiante.

## Problemas abiertos por impacto

1. **P1 - aprobacion academica:** el estudiante debe revisar y poder explicar personalmente los planos y el uso de IA conforme al enunciado.
2. **P1 - datos de campo:** validar dimensiones, recorridos, 145 m existentes, destino de 50 m, x/y, registros, canalizaciones, ocupacion y capacidad real de racks antes de tratar el escenario como definitivo.
3. **P2 - materiales e instalaciones:** comprobar fichas, compatibilidad local, energia, ventilacion, carga y activos; los equipos activos no se presentan como instalados.

## HECHO / VERIFICADO / PENDIENTE

- **HECHO:** nueve laminas tecnicas vigentes con PDF A3 individual y combinado, PNG y SVG editables; fuentes y generacion reproducibles.
- **VERIFICADO:** coherencia contra las cantidades adoptadas en el Excel, 59/59 controles, visualizacion de las nueve paginas, integridad de 50 archivos y conservacion de la coleccion historica.
- **PENDIENTE:** revision academica humana, mediciones y validacion constructiva de las hipotesis. No se afirma impresion fisica.

## Estado Git y siguiente accion

Commit de implementacion: `9d3deef1ff1aa876a764b9946b642f7b8808c2db` en `desarrollo-proyecto`, descendiente de `501052e714479273ee791c41b94f463aa0adcd0c`. `origin` coincide con `https://github.com/Mateo0098/INA_CABLEADO_ESTRUCTURADO_CENATE.git`. `main` no fue modificado.

**Siguiente accion minima viable:** publicar este reporte y actualizar el indice de transferencia en `09_auditorias/ULTIMO_REPORTE_CODEX.md`; despues, el estudiante revisa las laminas y sus supuestos.
