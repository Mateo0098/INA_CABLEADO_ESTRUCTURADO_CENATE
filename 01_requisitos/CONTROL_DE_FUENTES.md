# Control de fuentes

**Fecha de corte:** 2026-10-18

## Inventario y jerarquía

| ID | Fuente | Ubicación | Clasificación | Integridad / estado | Uso |
|---|---|---|---|---|---|
| F-001 | Instrucciones del usuario para inicialización y auditoría | Conversación de trabajo | Contexto secundario | Sin hash de archivo | Historial, reglas de repositorio y contexto no contenido en fuentes oficiales |
| F-002 | `Plantilla Actividades de comprobación.xlsx` | `06_excel/Plantilla Actividades de comprobación.xlsx` | Plantilla oficial vinculada operacionalmente por F-005 y por confirmación del estudiante | SHA-256 `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`; 15 866 bytes; preservada | Original de solo lectura y patrón estructural del futuro Excel |
| F-003 | Segunda descarga de la plantilla | Fuera del repositorio | Duplicado exacto | Mismo SHA-256 que F-002 | No incorporar nuevamente |
| F-004 | `Actividad_Comprobación_instrucciones.docx` | Fuera del repositorio | Fuente descartada | SHA-256 `C08A5C8B95A5AE580726269F60DD27F235578E81374D1826A9E0C3FA106BCD76` | Ninguno; pertenece a TMGA19008, Gestión Ambiental |
| F-005 | `Markdown pegado.md` | `01_requisitos/Markdown pegado.md` | Fuente oficial principal: enunciado de Actividad de Comprobación N.º 1, ELTT12000 | SHA-256 `925207D46E68CB004C16E4EBA60C659053BB60C2B172D98505FCF45AE5C7FD55`; 32 245 bytes | Requisitos académicos, técnicos, de entrega y criterios de evaluación |
| F-006 | `Actualizacion_docente_ER_TR.md` | `01_requisitos/Actualizacion_docente_ER_TR.md` | Actualización posterior del docente sobre ER/TR | SHA-256 `990FD71CE44067E316B1F30E43255D3E07C9BC78B3AB4F60AC93D4A4C03CA426`; 1 466 bytes | Cuatro imágenes adicionales y contenido obligatorio de ER/TR |
| F-007 | `REGISTRO_MEDICIONES_Y_SUPUESTOS_CHAT.md` | `02_datos_campo/REGISTRO_MEDICIONES_Y_SUPUESTOS_CHAT.md` | Información y supuestos del estudiante; no requisito docente | SHA-256 `4D260B64E884936889A1FB3851D90248D6C6D025C5FF5E30EF81EA1093B03C7F`; 4 170 bytes | 145 m, 25 m, 50 m, 195 m y supuestos, separados de F-005/F-006 |
| F-008 | `ARQUITECTURA_CONCEPTUAL_CHAT.md` | `03_diseno/ARQUITECTURA_CONCEPTUAL_CHAT.md` | Propuesta conceptual secundaria; no diseño aprobado | SHA-256 `15B97679E24473E08CE00AAE882451EB24244AAF2025D03DFD9A7D4C1FB44C89`; 5 956 bytes | Transferencia de alternativas, riesgos y asuntos abiertos |
| F-009 | `TRANSFERENCIA_CONTEXTO_CHATGPT_CODEX.md` | `09_auditorias/TRANSFERENCIA_CONTEXTO_CHATGPT_CODEX.md` | Registro de transferencia y recuperación; no requisito ni rúbrica | SHA-256 `394E66A620135425AD4FAA4C0A82B43B8EB50CA723D0FD71C4EC6B3673861D7E`; 3 247 bytes | Cadena de contexto y controles de sincronización |

## Vinculación de la plantilla

F-005 §5 exige usar la plantilla Excel adjunta al correo. El estudiante identificó F-002 como la plantilla ya incorporada. Su estructura coincide con los dos entregables tabulares exigidos: materiales/equipos y herramientas. Se acepta como plantilla oficial operativa para el proyecto, conservando el hash como control.

Metadatos observados de F-002:

- `creator`: `Docente`.
- `lastModifiedBy`: `Albis Villalobos Villalobos`.
- creación/modificación interna: `2026-10-14T00:08:42Z`.
- aplicación: Microsoft Excel.

Los metadatos apoyan la cadena de custodia, pero no sustituyen el hash ni la confirmación del estudiante.

## Rúbrica y criterios de evaluación

No se suministró una rúbrica independiente. Esta ausencia se mantiene como limitación documental, no como bloqueo de cierre. Para control de calidad se usan:

- F-005 §11: presentación y defensa individual.
- F-005 §12: revisión previa a la entrega.
- F-005 §13: factores fundamentales de valoración.

No se inventan ponderaciones, escalas ni criterios adicionales.

## Precedencia y manejo de discrepancias

1. F-006 complementa a F-005 para imágenes ER/TR; no lo reemplaza.
2. F-005/F-006 prevalecen sobre resúmenes contextuales CTX cuando hay diferencia.
3. F-007 nunca se atribuye al docente; F-008 nunca se presenta como ingeniería aprobada.
4. Los originales F-002, F-005 y F-006 no se editan para adaptar conclusiones.
5. Nuevas versiones se incorporarán con ID y hash nuevos; no se sobrescribirán las anteriores.

## Limitaciones vigentes

- No hay rúbrica separada.
- F-006 indica remitente, pero no fecha de emisión.
- No se incorporaron planos oficiales ni evidencia primaria original de las mediciones grupales del 2026-10-13; F-007 es un registro de transferencia del estudiante.
- La frase “área de trabajo doble” no incluye una definición adicional en F-005.
- Las ediciones concretas de normas ANSI/TIA no se enumeran en F-005; deberán verificarse sin inventarlas.
