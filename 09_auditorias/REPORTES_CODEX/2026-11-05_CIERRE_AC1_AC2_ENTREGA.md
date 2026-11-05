# Reporte Codex — cierre AC1 y AC2

**Fecha:** 2026-11-05. **Rama:** `desarrollo-proyecto`. **Objetivo:** crear el paquete de entrega urgente de Actividad de Comprobación 2 y reenviar la versión final de Actividad 1. Autoría asistida por Codex; revisión humana académica y comercial pendiente.

## Alcance y fuentes

Se usaron las matrices U02 (115 registros) y U03 (108 filas), U04C y su CSV de ofertas, U01, memorias de cantidades, el Gantt canónico (`26` actividades, `74` días hábiles) y el paquete final AC1. Se leyó `gantt/README.md`. No se efectuó otra auditoría general.

La plantilla solicitada `insumos_entregable_2/Presupuesto FINAL.xlsx` no estaba presente en el repositorio ni se encontró otra copia con ese nombre. Se creó un libro de salida nuevo, con diseño comercial y once hojas, que cubre las siete funciones requeridas: Cotización, Mano de obra, Precio de venta, Ganancias, Cronograma Gantt, Feriados CR y Factura proforma; añade detalle, fuentes, supuestos y parámetros.

## HECHO

- Se creó `08_entrega/CIERRE_AC1_AC2_2026-11-05/PRESUPUESTO_FINAL_CENATE.xlsx` con fórmulas, parámetros editables y las 223 partidas fuente preservadas en detalle. La hoja de Ganancias queda separada de la proforma.
- Se generó `FACTURA_PROFORMA_CENATE.pdf`, de una página A4, con fecha 2026-11-05, emisor/cliente editables, alcance de ambos edificios, condiciones y total marcado como parcial/incompleto.
- Se crearon `FUENTES_Y_ESTIMACIONES_PRESUPUESTO.csv`, `NOTAS_DEL_PRESUPUESTO.md` y `CORREO_ENTREGA_AC2.md` con el asunto exacto solicitado.
- Se preparó `ACTIVIDAD_1_REENVIO/` con copia idéntica del Excel final de AC1 y las nueve láminas PDF A3. Hash SHA-256 del Excel de reenvío y del Excel final de origen: `0B27F59C51CD1C6CB51EC5AB3E93725BD96F3ADEC13A93807340DD282E69C0F4`.
- Se generó `CIERRE_AC1_AC2_2026-11-05.zip` sin sustituir los archivos individuales.

## Cantidades, precios y completitud

El presupuesto conserva 223 filas de fuentes técnicas sin convertirlas automáticamente en compras. Hay tres filas con precios U04C directamente vinculables (CRS354, siete adicionales y CRS317): **3/223 = 1,35 %** de las partidas maestras con precio comercial exacto. El cierre usa además cinco grupos comerciales publicados o comparables señalados como **ESTIMADO** (cable Cat6A, canasta, rack, panel y transceptor), sin presentarlos como oferta firme. Por ello el porcentaje de partidas maestras completamente valoradas sigue siendo 1,35 %; no se declara costo completo.

La proforma muestra **CRC 146.823.749,18** como total parcial: materiales/equipos valorados, mano de obra interna de Gantt, 5 % imprevistos, 10 % administrativos, 15 % utilidad e IVA de referencia 13 %. Los precios USD usan CRC 454,65 por USD como referencia BCCR/MONEX de venta del 2026-11-04, editable en el libro. Es un parámetro de presupuesto, no tipo de cambio de contratación.

## VERIFICADO

- `python 08_entrega/generar_cierre_ac1_ac2.py`: salida generada.
- `openpyxl.load_workbook`: 11 hojas; las siete funciones exigidas están presentes.
- Revisión de celdas: sin literales `#REF!`, `#DIV/0!`, `#VALUE!` ni `#NAME?`.
- ZIP interno de XLSX y ZIP del paquete: íntegros.
- PDF: una página A4, texto extraíble y rótulos `CRC` e `INCOMPLETA` visibles.
- Reenvío AC1: nueve PDF A3 presentes y Excel idéntico al archivo final fuente.

## PENDIENTE / limitaciones

- Fibra OS2, conduit, herrajes, accesorios y servicios de fusión/certificación no tienen cotización comparable: se excluyen del total y evitan declarar presupuesto completo.
- Disponibilidad, IVA y vigencia de precios publicados requieren confirmación. Las cantidades de cable/canasta son cómputos académicos y necesitan despiece físico.
- La mano de obra es costo interno del Gantt basado en TMED y proyección 2027; no equivale a tarifa comercial ni sustituye revisar categorías, cargas, INS y simultaneidad.
- Excel COM no estuvo disponible en esta sesión; no se declara apertura/recalculo visual con Microsoft Excel.

## Archivos modificados y no modificados

**Creados:** paquete `08_entrega/CIERRE_AC1_AC2_2026-11-05/`; generador `08_entrega/generar_cierre_ac1_ac2.py`; este reporte.

**No modificados:** originales INA, `06_excel/`, U02/U03/U04C, Gantt canónico, planos fuente, `main` y los dos archivos personales sin seguimiento de `gantt/`.

**Siguiente acción mínima viable:** abrir el XLSX final en Excel, recalcularlo y sustituir los grupos pendientes con cotizaciones comparables antes de usar esta proforma como documento comercial definitivo.
