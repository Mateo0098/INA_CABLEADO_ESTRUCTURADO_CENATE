# Reporte Codex — corrección AC2 al machote Albis

## Alcance

Se generaron únicamente los archivos solicitados en `08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05/CORRECCION_FORMATO_ALBIS_2026-11-06/`, a partir de una copia binaria de `insumos_entregable_2/Presupuesto FINAL.xlsx` y de las 37 partidas publicadas. No se modificaron el machote, Gantt fuente, matrices ni AC1.

## HECHO

- Se preservaron los siete nombres y orden de hojas, rangos de impresión, combinaciones, anchos y alturas del machote.
- Se consolidaron las 37 partidas en 27 renglones de `Cotización` y se restauraron las fórmulas dañadas de la plantilla de forma mínima.
- Se incorporaron las 26 tareas del Gantt en filas existentes; `I42` suma las horas y alimenta mediante fórmula `Mano de obra`, después `Precio de venta` y `Factura proforma`.
- Se copiaron las fuentes y se creó el XLSX, PDF, ZIP y verificación solicitados.

## VERIFICADO

- 26 tareas; fórmula de horas `=SUM(I15:I19,I21:I41)` y cadena de referencias Gantt → Mano de obra → Precio de venta → Factura proforma.
- XLSX sin literales `#REF!`, `#VALUE!`, `#DIV/0!` o `#NAME?`; siete hojas y estructura de formato coincidente con el machote en controles de hojas, combinaciones, anchos, alturas y área de impresión.
- PDF legible de dos páginas, con total `₡216.518.234,86`; ZIP íntegro.

## PENDIENTE / LIMITACIÓN

- Microsoft Excel COM no estuvo disponible (`0x80070520`). Por ello no se pudo recalcular, guardar ni exportar nativamente la hoja `Factura proforma` desde Excel.
- El PDF se generó como reproducción programática de la cuadrícula y datos de la hoja `Factura proforma`; conserva sus conceptos y total, pero no se declara una exportación visual nativa de Excel.
- Siete precios son publicados y treinta estimaciones académicas identificadas, no ofertas firmes.

## Archivos creados

- `PRESUPUESTO_AC2_MACHOTE_ALBIS.xlsx`
- `FACTURA_PROFORMA_AC2_MACHOTE_ALBIS.pdf`
- `FUENTES_Y_SUPUESTOS_AC2.csv`
- `CORRECCION_AC2_MACHOTE_ALBIS.zip`
- `VERIFICACION_FORMATO_Y_FORMULAS.md`

Siguiente acción mínima viable: abrir el XLSX en Excel de escritorio, recalcular y exportar la hoja `Factura proforma` a PDF para sustituir la reproducción programática si el profesor exige esa exportación nativa.
