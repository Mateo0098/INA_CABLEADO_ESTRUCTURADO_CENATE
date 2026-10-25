# Paquete de revisión — Fase 2D

**Fecha:** 2026-10-25

**Estado:** base técnicamente explicable para completar el Excel; no es entrega final.

## Contenido

- `01_imagenes_revision/`: nueve SVG y nueve PNG; solo ER/TR cambiaron para reflejar housings CCH y longitudes de escenario.
- `02_soporte_tecnico/`: memoria de recorridos, resultados, matriz de materiales y guía de exposición.
- `03_excel_provisional/`: plan definitivo de correspondencia, CSV de materiales/herramientas y copia intacta con ejemplos.
- `04_fuentes_reproducibles/`: entradas y scripts de cálculos/diagramas.
- `ESTADO_ENTREGABLES.csv`: estado por bloque.
- `SHA256SUMS.csv`: integridad del paquete.

## Avances que reducen pendientes

- Cobre con rutas representativas, reserva, desperdicio y 229 cajas de 305 m como escenario.
- Verificación desfavorable de 45,7 m en A y 42,7 m en B frente a 90 m.
- Fibra vertical con cortes por piso y total de 284,025 m como escenario.
- E1 calculado en 221,55 m; E2/E3 conservados como fórmulas con variables.
- Housings CCH compatibles dimensionados por cuarto, sin duplicar accesorios.
- Plan Excel fila por fila y herramientas para una cuadrilla académica.

## Impedimentos reales para cerrar

1. Confirmación docente de dos RJ45 por área doble y tratamiento de `J43`.
2. Aceptación humana de la geometría/reservas/desperdicio usados en el escenario.
3. Valores `x/y`, capacidad de ductos y cajas exteriores.
4. Sección/diámetro y producto de canalizaciones interiores.
5. Puertos activos para fijar patch cords ópticos y validar racks/energía.
6. Transferencia y prueba manual del Excel por el estudiante.
