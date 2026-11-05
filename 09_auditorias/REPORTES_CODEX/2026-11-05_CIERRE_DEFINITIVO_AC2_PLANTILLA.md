# Reporte Codex — cierre definitivo AC2 con plantilla publicada

**Fecha:** 2026-11-05. **Rama:** `desarrollo-proyecto`. **Objetivo:** integrar la plantilla original publicada con el cierre existente sin rehacer cálculos, matrices, Gantt ni planos.

## HECHO

- Se integró por fast-forward la plantilla original `insumos_entregable_2/Presupuesto FINAL.xlsx` desde `origin/desarrollo-proyecto`; el archivo fuente queda intacto.
- `08_entrega/generar_cierre_ac1_ac2.py` ahora abre esa plantilla, conserva sus siete hojas comerciales y sustituye sus contenidos de ejemplo. La salida añade solamente las hojas auxiliares ya necesarias: detalle de 223 partidas, fuentes, supuestos y parámetros.
- Se reutilizaron sin modificar U02, U03, U04C, el Gantt canónico y el reenvío AC1. La hoja de cronograma enlaza mediante ruta relativa a `gantt/GANTT_INA_CABLEADO_2026-2027.xlsx`.
- Se corrigió el IVA: un precio marcado **incluido** se desglosa a base neta; uno **excluido** conserva su base neta; uno **no confirmado** no recibe IVA adicional. El IVA de venta se calcula una vez sobre el precio antes de IVA. Los importes del PDF y del XLSX proceden de la misma lista `LINES` del generador.
- Se añadieron valoraciones académicas trazables para conduit 25 mm, fibra OS2 12F vertical, organizadores 1U y patch cords OS2, además de las referencias ya existentes de Cat6A, terminaciones, canasta, rack, equipos activos y ópticos.

## Cobertura y resultado

La tabla comercial tiene **15 grupos**: 12 valorados, de los cuales 4 son **PUBLICADO** y 8 **ESTIMADO** con base comercial identificada; 3 quedan **PENDIENTE**. La matriz técnica conserva sus 223 filas sin adjudicación automática; la cobertura económica se expresa por grupos comerciales, no como 223 compras ni como porcentaje de filas técnicas completamente cotizadas. Los grupos estimados no se presentan como cotizaciones firmes.

El total de proforma permanece **provisional: CRC 136.080.076,02**. Incluye base neta de materiales/equipos valorados, mano de obra interna existente del Gantt, 5 % imprevistos, 10 % administrativos, 15 % utilidad sobre costo y 13 % IVA de venta de referencia. No incluye fibra OS2 exterior 24F, cassettes/housings, herrajes/accesorios ni servicios especializados pendientes; por eso no es presupuesto completo ni oferta firme.

## VERIFICADO

- El XLSX abre con `openpyxl`: 11 hojas, siete funciones de la plantilla presentes y sin literales `#REF!`, `#DIV/0!`, `#VALUE!` ni `#NAME?`.
- XLSX y ZIP pasaron prueba de integridad ZIP.
- PDF de proforma: una página A4, texto extraíble, total `CRC 136,080,076.02` y estado `INCOMPLETA` visibles.
- Reenvío AC1: nueve planos PDF A3 y el Excel preservado en el paquete.
- `git diff --check`: sin errores antes de commit.

## PENDIENTE

- Cotizar OS2 24F exterior, cassettes/housings, herrajes/accesorios y fusión/OLTS/OTDR/certificación; confirmar stock, IVA y vigencia de precios web.
- Aprobar cantidades comerciales tras despiece físico. El conduit y otros grupos señalados ESTIMADO siguen siendo cómputo académico.
- Excel COM no estuvo disponible en sesión (`0x80070520`); no se declara recálculo visual en Microsoft Excel.

## Archivos

**Modificados:** `08_entrega/generar_cierre_ac1_ac2.py` y los archivos regenerados de `08_entrega/CIERRE_AC1_AC2_2026-11-05/`; este reporte y el índice Codex.

**No modificados:** plantilla original, Gantt, U02/U03/U04C, originales de AC1, planos y `main`.

**Siguiente acción mínima viable:** abrir el XLSX final en Excel y sustituir las filas pendientes con cotizaciones comparables antes de una emisión comercial definitiva.
