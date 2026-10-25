# Plan de transferencia manual al Excel — Fase 2D

**Estado:** correspondencia técnicamente preparada; el libro no se modificó y todavía no es final.

La guía consolidada de edición por fila, herramientas y controles de cierre está en `06_excel/GUIA_CIERRE_ESTUDIANTE_FASE3A.md`.

## Archivos controlados

- Original intacto: `06_excel/Plantilla Actividades de comprobación.xlsx`.
- Copia provisional intacta: `06_excel/Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx`.
- Materiales: `06_excel/PLAN_FILAS_MATERIALES_FASE2D.csv`.
- Herramientas: `06_excel/PLAN_FILAS_HERRAMIENTAS_FASE2D.csv`.
- Fórmulas y fundamento: `04_calculos/MEMORIA_CALCULOS_FASE2D.md`.

## Filas listas para traslado después de revisión

Las filas 2–8 y 12–22 tienen cantidad numérica reproducible. Las filas 2, 9, 12, 13 y 20 siguen siendo escenarios explícitos; el estudiante debe aceptar sus entradas antes de copiarlas. Las filas 3–8 dependen además de confirmar dos RJ45 por área doble.

| Grupo | Filas | Control antes de introducir en G |
|---|---|---|
| Cobre y salidas | 2–8 | Geometría, 2 RJ45/área, reserva 3 m, desperdicio 5 %, longitud de patch cord |
| Fibra exterior E1 | 9 | Confirmar que 145 + 50 m corresponde a E1 |
| Fibra vertical | 12–13 | Aceptar 3,5 m/piso, 3 m internos y 5 m de reserva por extremo |
| Cassettes/housings | 14–18 | Arquitectura CCH; espacio del ER-P |
| Rack/organización | 20–22 | Mantener activos fuera del conteo y revisar capacidad física |

## Filas que deben permanecer pendientes

- Fila 10: E2 depende de `x`; conservar la fórmula documental, no escribir una cantidad ficticia.
- Fila 11: E3 depende de `y`.
- Fila 19: patch cords ópticos dependen de `PARES_OPTICOS_ACTIVOS_EXTREMOS`, entre 0 y 204.
- Fila 23: puesta a tierra tiene cantidad funcional 13, pero falta referencia compatible/institucional.
- Filas 24–25: existe longitud de escenario, pero falta sección/diámetro del sistema de canalización.
- Fila 26: los 50 m son propuesta, no medición ni producto seleccionado.
- Fila 27: seis posiciones teóricas no equivalen a seis cajas comprables.

## Procedimiento concreto del estudiante

1. Crear una copia personal nueva desde el archivo de trabajo; nunca editar el original.
2. Revisar cada fila del CSV y marcar en una lista personal si acepta el supuesto y puede explicar la fórmula.
3. Sustituir los ejemplos didácticos únicamente en la copia personal, respetando columnas A–K, hojas, colores y estilos.
4. Copiar A–F, D/E y K solo donde la matriz Fase 2D aporta una referencia oficial. No inventar marca/modelo para filas pendientes.
5. En G introducir la fórmula propuesta de las filas aprobadas y comprobar que devuelve el resultado de referencia.
6. En las filas 10, 11 y 19 dejar G sin cantidad hasta resolver variables; no escribir `N/D` como compra.
7. Mantener I y J sin precios. Consultar al docente si `J43=SUM(J2:J41)` debe conservarse.
8. Completar `Herramientas` desde su CSV. Las cantidades suponen una sola cuadrilla académica; dejar vacía la del lubricante.
9. Comprobar apertura, fórmulas, recálculo, estilos y ausencia de ejemplos residuales.
10. Guardar con nombre nuevo que incluya `REVISION_ESTUDIANTE`; no reemplazar la copia controlada hasta aprobarla.

## Pruebas manuales mínimas

- Fórmula de cobre: 74 + 155 = 229 cajas.
- Fórmula de paneles: 4 × 4 + 5 × 7 = 51.
- Fórmula de salidas: (4 × 5 + 7 × 6) × 16 × 2 = 1 984.
- Cassettes: (4 + 7) × 2 = 22 y 3 × 2 = 6.
- Housings: 12 `CCH-01U`, 1 `CCH-03U`, 1 `CCH-04U`.
- Confirmar que no existan filas de compra separadas para 408 pigtails o 204 adaptadores.
- Confirmar que I/J no contengan montos.

## Condición para llamar al libro “final”

Todos los ejemplos deben haberse retirado, cada fila debe estar aprobada o eliminada justificadamente, las variables `x`, `y` y pares activos deben resolverse o excluirse de la compra, y el estudiante debe probar el archivo en la aplicación que usará para entregar. Hasta entonces es una base de transferencia, no el Excel final.
