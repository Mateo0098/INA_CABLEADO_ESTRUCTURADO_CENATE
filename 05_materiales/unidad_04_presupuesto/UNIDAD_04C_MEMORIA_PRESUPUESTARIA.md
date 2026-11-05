# Unidad 04C — memoria presupuestaria de la red operativa

**Fecha:** 2026-11-05. **Responsable de elaboración:** Codex con asistencia de IA; revisión técnica y académica humana pendiente. **Alcance:** ampliación operativa independiente de la Actividad 1. No se alteran el Excel INA, los documentos canónicos ni las matrices U02/U03.

## Entradas y clasificación

| Dato | Magnitud | Clase y fuente |
|---|---:|---|
| Materiales U02 | 115 registros | Inventario técnico académico, `../unidad_02_ampliacion/UNIDAD_02_MATRIZ_MAESTRA_MATERIALES.csv` |
| Herramientas/servicios U03 | 108 registros | Inventario funcional, `../unidad_03_herramientas/UNIDAD_03_MATRIZ_MAESTRA_HERRAMIENTAS.csv` |
| Acceso base/ampliado | 44 / 51 switches | Resultado propuesto de `../../03_diseno/UNIDAD_01_ARQUITECTURA_RED_ACTIVA.md`; siete adicionales, no 51 adicionales |
| Precios de seis ofertas | Cinco con cifra, tres vinculadas provisionalmente | Precio web publicado, no cotización firme; evidencia por URL y fecha en `UNIDAD_04C_OFERTAS.csv` |
| IVA general | 13 % | Tarifa general documentada por [Hacienda](https://www.hacienda.go.cr/docs/GeneralidadesIVA.pdf), consulta 2026-11-05; aplicación real y exenciones pendientes de factura y condición de comprador |
| Tipo de cambio | Pendiente | No se asigna valor sin fuente y fecha |

## Resultado provisional calculable

El libro vincula **tres ofertas web exactas** de Ticomer a las filas de 44 switches base, siete adicionales y dos distribuidores. El precio web observado el 2026-11-05 fue ₡320.703 por CRS354 y ₡261.849 por CRS317, ambos **sin IVA**. Una simulación con tarifa general del 13 % produce:

| Escenario | Fórmula | Subtotal de switches, CRC | Estado |
|---|---|---:|---|
| 44 acceso + 2 distribución | `(44×₡320.703 + 2×₡261.849)×1,13` | ₡16.537.131,90 | Provisional, sin disponibilidad suficiente demostrada |
| 51 acceso + 2 distribución | `(51×₡320.703 + 2×₡261.849)×1,13` | ₡19.073.892,63 | Provisional, siete adicionales una sola vez |

Estos importes **no son presupuesto total ni orden de compra**. La disponibilidad publicada como «últimas unidades» no demuestra 44/51 unidades. Solo **24/223** filas contienen cifra funcional (muchas de referencia académica); solo **3/223** tienen factor comercial y oferta seleccionada. La cobertura monetaria del escenario base es **3 partidas calculables entre las activas**, según recálculo de Excel; el porcentaje exacto se muestra en `01_RESUMEN`. La mayoría de materiales, equipos ópticos, herramientas, EPP, servicios y logística carecen de costo cerrado.

## Método de cálculo y controles

`02_PARTIDAS` conserva los 223 ID originales y la dependencia/duplicación de cada fila. La cantidad comercial es `REDONDEAR.MAS(cantidad funcional/factor de conversión;0)`; sin factor o cantidad, el costo muestra `PENDIENTE`, nunca ₡0. Los tres switches usan factor 1 porque la función y la venta son por unidad. Para cable por caja de 305 m, canasta por tramo de 3 m y conduit por barra, primero se debe aprobar el despiece y patrón de cortes; por eso los 229 rollos académicos, 478 tramos globales y 1.042 tubos históricos no se transfieren como compra definitiva.

Una oferta con IVA incluido se descompone en neto `bruto/(1+tasa)` e IVA `bruto−neto`; una sin IVA calcula `neto×tasa` y suma una vez. «IVA no confirmado» bloquea el importe. La tarifa de referencia es configurable. En moneda extranjera, falta de tipo de cambio bloquea el costo. `05_IMPORTACIONES` exige CIF, clasificación, arancel, base, IVA y logística antes de mostrar costo puesto en Costa Rica; no hay tasas arancelarias supuestas. [Consulta oficial TICA](https://portaltica.hacienda.go.cr/TicaExterno/hdbaranc.aspx) para clasificación futura.

En el escenario 51 solo se activan los siete switches y siete DAC adicionales de sus propias filas. La selección de oferta no ocurre por precio mínimo. La modalidad de servicio desactiva la compra de los instrumentos comparables en las fórmulas, pero las filas de servicio permanecen sin cantidades ni ofertas; por ello los escenarios B/C no tienen comparación monetaria integral. La alternativa Ubiquiti UF-SM-10G no se adjudica: compatibilidad, potencia, longitud, codificación y firmware siguen pendientes. Cable CMP y LSZH tampoco se equiparan sin aprobación de requisito de instalación.

## Actualización

1. Registrar ofertas nuevas en `UNIDAD_04C_OFERTAS.csv` con ID válido, URL, fecha, moneda, IVA, presentación, disponibilidad y compatibilidad. Un catálogo sin precio deja el precio vacío.
2. Aprobar cantidades funcionales, unidad de venta y factor en el generador o en una copia de trabajo del libro. Descontar kit, stock institucional y recurso compartido; documentar la decisión.
3. Ejecutar `python 05_materiales/unidad_04_presupuesto/generar_presupuesto.py` y `python 05_materiales/unidad_04_presupuesto/validar_presupuesto.py` con `openpyxl>=3.1`.
4. Abrir y recalcular en Excel; revisar visualmente totales y fórmulas. `openpyxl` no calcula resultados ni conserva como entradas del CSV los cambios editados solo en el XLSX.

**Limitación principal:** el libro es una estructura de presupuesto con un subtotal web provisional; falta aprobación de ingeniería, compras, cantidades, ofertas firmes y revisión humana de contenido asistido por IA.
