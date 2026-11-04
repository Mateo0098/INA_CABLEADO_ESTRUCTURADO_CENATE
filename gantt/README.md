# Cronograma Gantt — ejercicio complementario INA CENATE

**Estado:** planificación académica hipotética, preparada con asistencia de ChatGPT el 2026-11-04. Revisión del estudiante pendiente.

## Archivo

- [GANTT_INA_CABLEADO_2026-2027.xlsx](GANTT_INA_CABLEADO_2026-2027.xlsx): libro Excel editable con hojas `Project Planner`, `Criterios y etapas` y `Feriados CR`.
- El Gantt no sustituye la plantilla oficial `06_excel/`, el presupuesto ni el paquete de entrega ya consolidado. Es un ejercicio independiente surgido en clase.

## Reglas y supuestos

| Variable | Criterio |
|---|---|
| Inicio | 2026-11-02 |
| Final | 2027-02-16 |
| Duración del intervalo | 74 días hábiles |
| Días laborables | lunes a viernes |
| Feriados excluidos | 2026-12-01 (Abolición del Ejército), 2026-12-25 (Navidad), 2027-01-01 (Año Nuevo) |
| Estructura | seis etapas y 26 actividades de la pizarra de clase |
| Paralelismo | tareas de ambos edificios pueden solaparse cuando sea técnicamente razonable |
| Fórmula de fin | `WORKDAY(inicio, duración - 1, feriados)` |
| Duraciones | estimaciones hipotéticas propuestas para aprender a elaborar un Gantt |

El usuario escribió inicialmente «16 de febrero de 2026» para el final, fecha anterior al inicio. Se utilizó **2027**, coherente con la pizarra y el cronograma. No se asumió un receso navideño adicional a los feriados oficiales.

## Origen, limitaciones y verificación

Las actividades proceden de una fotografía de pizarra aportada por el estudiante; la asignación de fechas y duraciones y el archivo fueron elaborados con asistencia de IA. No son datos de campo, contratos ni cronograma constructivo validado.

**Verificación realizada:** 26 actividades, 74 fechas diarias laborables, 26 fórmulas `WORKDAY`, tres hojas, archivo XLSX/ZIP estructuralmente legible y fechas extremas correctas. **Pendiente:** abrir y recalcular en Microsoft Excel, revisar visualmente las barras y validar con el docente.

No se modifican `main`, los nueve planos, los documentos de materiales, los libros oficiales ni el índice de transferencia `09_auditorias/ULTIMO_REPORTE_CODEX.md`, reservado para la última intervención de Codex.
