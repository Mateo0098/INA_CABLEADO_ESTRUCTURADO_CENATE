# Transferencia de contexto desde ChatGPT a Codex

Fecha de preparación: 18 de octubre de 2026.
Proyecto: INA — ELTT12000 Presupuesto de la red — Actividad de Comprobación N.º 1 (entrega 29-10-2026).

## Estado documental reportado por Codex antes de esta transferencia

- Rama de trabajo: `desarrollo-proyecto`; `main` no debe modificarse.
- Inicialización en `8388caa242e427405a68f2b657527c3641266c2c`.
- Codex reportó trabajo local de Fase 1 aún sin commit (matriz contextual, control de fuentes, estructura del Excel, auditoría de requisitos, cambios en README/DECISIONES/PENDIENTES).
- Plantilla Excel ya existente en la carpeta local `06_excel/`; Codex reportó integridad byte a byte y hojas `Cotización técnica` y `Herramientas`.
- Se publicaron después desde ChatGPT en `desarrollo-proyecto` las fuentes `01_requisitos/Markdown pegado.md` y `01_requisitos/Actualizacion_docente_ER_TR.md`.
- Este documento y los de `02_datos_campo/` y `03_diseno/` transfieren información que estaba solo en el chat; **no son una rúbrica oficial**.

## Jerarquía de evidencia

1. Enunciado original del docente, archivo `01_requisitos/Markdown pegado.md`.
2. Aclaración del docente, archivo `01_requisitos/Actualizacion_docente_ER_TR.md` (transcripción/reorganización del mensaje recibido).
3. Datos de campo y aclaraciones comunicados por el estudiante, registro `02_datos_campo/REGISTRO_MEDICIONES_Y_SUPUESTOS_CHAT.md`.
4. Propuestas conceptuales de ChatGPT, registro `03_diseno/ARQUITECTURA_CONCEPTUAL_CHAT.md`.

La rúbrica separada NO ha sido aportada. No inventarla. No convertir el registro contextual en normativa.

## Control para Codex

1. `git status` y `git fetch origin`.
2. Revisar los cambios locales sin commit antes de sincronizar la rama; usar un procedimiento no destructivo que preserve íntegramente el trabajo.
3. Confirmar existencia y lectura completa de las dos fuentes oficiales y dos archivos de contexto nuevos.
4. Conciliar CTX-* con identificadores oficiales y mantener trazabilidad histórica.
5. Auditar los requisitos adicionales de ER/TR y las nueve imágenes.
6. Mantener el original Excel intacto y preservar su formato; la Actividad 1 no permite precios/costos.
7. No iniciar diseños definitivos ni cálculos hasta registrar supuestos de distancias/rutas y comprobar integridad de fuentes.
8. Emitir informe de diferencias entre documentación previa y fuentes oficiales; llevar a commit los cambios solo después de verificar.
9. Mantener `main` sin alteraciones.

## Restricción académica consignada en el enunciado

El docente permite IA para explicaciones, organización, revisión y apoyos visuales, pero restringe su uso para resolver cálculos evaluados y generar automáticamente el archivo Excel completo. Mantener esta condición documentada y distinguir cualquier apoyo técnico de la labor evaluada.

## Archivos disponibles en la conversación que no deben confundirse con el repositorio remoto

Las carpetas locales de Codex no son accesibles automáticamente desde ChatGPT. Los commits remotos añadidos aquí NO incluyen los cambios locales todavía no publicados por Codex. La sincronización debe preservar ambos conjuntos de cambios.
