# Plan controlado de transferencia al Excel — Fase 2C

**Estado:** preparado para revisión manual; el libro continúa provisional y conserva ejemplos didácticos.  
**Archivo de trabajo:** `06_excel/Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx`.  
**Original no modificado:** `06_excel/Plantilla Actividades de comprobación.xlsx`.

## Artefactos de transferencia

- `PLAN_FILAS_MATERIALES_FASE2C.csv`: correspondencia exacta entre filas previstas 2–18, componentes, fuentes, fórmulas, resultados y bloqueos.
- `PLAN_FILAS_HERRAMIENTAS_FASE2C.csv`: correspondencia prevista para la hoja `Herramientas`, sin cantidades ficticias.
- `05_materiales/MATRIZ_TECNICA_FASE2C.md`: clasificación entre producto, familia y componente sin referencia.
- `04_calculos/resultados_fase2b.csv`: resultados reproducibles y estados.

## Qué puede trasladarse tras revisión del estudiante

| Fila | Resultado | Fórmula propuesta | Condición previa |
|---:|---:|---|---|
| 3 | 51 paneles | `=4*4+5*7` | Aceptar 2 RJ45/área y regla de panel adicional cuando no queda reserva |
| 4 | 1 984 jacks | `=(4*5+7*6)*16*2` | Confirmar interpretación de área doble |
| 5 | 992 placas dobles | `=(4*5+7*6)*16` | Confirmar área doble y compatibilidad de placa/caja |
| 10 | 22 cassettes 12F | `=(4+7)*2` | Aprobar cassette pre-pigtailed y housing CCH |
| 11 | 6 cassettes 24F | `=3*2` | Aprobar cassette pre-pigtailed y housing CCH |

Las fórmulas son deliberadamente simples para poder explicarlas durante la defensa. No se insertaron automáticamente en el libro: el estudiante debe comprenderlas, introducirlas y probar el recálculo.

## Valores que no deben trasladarse aún

- Metros de cable Cat 6A, cables OS2 verticales o enlaces exteriores.
- Cantidad final de patch cords, racks, organizadores, housings ODF, bandejas, ductos o cajas.
- Los 94,5 m de desnivel vertical: son límite inferior geométrico, no metraje de compra.
- Las cinco y una posiciones teóricas de cajas: no son unidades comprables.
- Pigtails y adaptadores como compra separada si se usan cassettes pre-pigtailed.
- Cualquier precio, subtotal o costo.

## Estado del libro

El libro de trabajo sigue byte a byte igual al original hasta que el estudiante ejecute la transferencia manual. Esto preserva hojas, columnas, estilos y `J43=SUM(J2:J41)`, pero significa que **no es archivo final** porque conserva ejemplos didácticos.

Antes de entrega, el estudiante deberá:

1. Duplicar nuevamente la copia de trabajo como versión personal de edición.
2. Sustituir ejemplos solo en esa copia, siguiendo los CSV fila por fila.
3. Dejar I/J sin montos y consultar el tratamiento de `J43`.
4. Probar fórmulas, formato, apertura y recálculo en Excel.
5. Eliminar o completar renglones pendientes; nunca presentar `N/D` como cantidad de compra.
