# Cronograma Gantt — ejercicio complementario INA CENATE

**Estado:** planificación académica hipotética con ampliación de costos laborales del 2026-11-05, preparada con asistencia de ChatGPT. Revisión del estudiante pendiente.

## Archivo

- [GANTT_INA_CABLEADO_2026-2027.xlsx](GANTT_INA_CABLEADO_2026-2027.xlsx): libro Excel editable con seis hojas: `Project Planner`, `Criterios y etapas`, `Feriados CR`, `Tarifas MTSS`, `Mano de obra` y `Dotación diaria`.
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


## Versión ampliada: dotación y mano de obra (2026-11-05)

El mismo libro `GANTT_INA_CABLEADO_2026-2027.xlsx` fue sustituido por una versión más completa, sin cambiar su ruta. **Tiene seis hojas**: `Project Planner`, `Criterios y etapas`, `Feriados CR`, `Tarifas MTSS`, `Mano de obra` y `Dotación diaria`. Conserva las 26 actividades, calendario hábil, fórmulas `WORKDAY` y agrega técnicos por actividad, separación de horas por año, costos salariales y proyección diaria de técnicos concurrentes.

La cotización corresponde a un **escenario académico provisional**, sin precios de materiales ni contratos, y no constituye una tarifa comercial de instalación ni cotización firme. La categoría `Técnico Medio en Educación Diversificada (TMED)` es una hipótesis que debe contrastarse con las funciones y requisitos reales del puesto. El salario mínimo mensual de 2026 se consigna como ₡496.838,17, con conversión orientativa a hora de 30 días × 8 horas. El aumento de 2027 se utiliza solo como parámetro de proyección, **no como salario mínimo oficial validado**, pendiente de verificar el decreto y monto definitivo. Los aportes patronales, provisiones de aguinaldo y vacaciones, y la tasa ilustrativa del INS también son editables y requieren comprobación según las condiciones del empleador.

**Fuentes consignadas en la hoja de tarifas:**
- MTSS, salarios mínimos 2026: https://www.mtss.go.cr/temas-laborales/salarios/lista_salarios_minimos_2026.pdf
- MTSS, comunicado de ajuste 2027: https://www.mtss.go.cr/prensa/comunicados/2026/octubre/cp_022_2026.html

**Verificación de publicación:** archivo XLSX de 27.079 bytes; SHA-256 local `604660f59992f3c9d3436350a27742aff744bfd7fd9938536f1daa09e824b2fb`; Git blob SHA `f12fc56cb36e5dbe97bb491f057d6c80215b1df1`. ZIP íntegro, 17 entradas OOXML, seis hojas y 26 fórmulas `WORKDAY`, verificados antes de publicar. **Pendiente:** ensayo de apertura, recálculo y revisión visual en Excel; confirmar tarifas/categorías y validar cuadrillas y simultaneidad con criterio humano.

El historial de Git conserva la versión anterior del archivo. Ni `main`, ni `06_excel/`, ni la entrega anterior se modifican.

## Origen, limitaciones y verificación

Las actividades proceden de una fotografía de pizarra aportada por el estudiante; la asignación de fechas y duraciones y el archivo fueron elaborados con asistencia de IA. No son datos de campo, contratos ni cronograma constructivo validado.

**Verificación realizada:** 26 actividades, 74 fechas diarias laborables, 26 fórmulas `WORKDAY`, seis hojas y archivo XLSX/ZIP estructuralmente legible; fecha extrema y fórmulas comprobadas estructuralmente. **Pendiente:** abrir y recalcular en Microsoft Excel, revisar visualmente las barras y validar con el docente.

No se modifican `main`, los nueve planos, los documentos de materiales, los libros oficiales ni el índice de transferencia `09_auditorias/ULTIMO_REPORTE_CODEX.md`, reservado para la última intervención de Codex.
