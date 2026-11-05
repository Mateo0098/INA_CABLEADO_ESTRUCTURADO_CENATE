# Integración de costos laborales al cronograma Gantt — ChatGPT

**Fecha:** 2026-11-05. **Rama:** `desarrollo-proyecto`. **Autoría:** intervención directa de ChatGPT sobre artefacto generado con asistencia de IA. **Estado:** integración documental y binaria verificable; revisión humana pendiente.

## Objetivo y alcance

Publicar la versión del Gantt con personal por actividad y costos laborales, manteniendo el archivo canónico y la documentación del ejercicio complementario. No modificar el Excel original INA, ni el entregable de octubre, ni la rama `main`.

## HECHO

- Actualizado `gantt/GANTT_INA_CABLEADO_2026-2027.xlsx`, con seis hojas (`Project Planner`, `Criterios y etapas`, `Feriados CR`, `Tarifas MTSS`, `Mano de obra`, `Dotación diaria`).
- Actualizado `gantt/README.md`, `README.md`, `AGENTS.md`, `DECISIONES.md` y `PENDIENTES.md`.
- Creado este reporte independiente. No se modificó `09_auditorias/ULTIMO_REPORTE_CODEX.md` al no ser una sesión de Codex.

## VERIFICADO

- Archivo local de entrada: `/mnt/data/Gantt_INA_Costa_Rica_Mano_de_Obra.xlsx`.
- Tamaño: 27.079 bytes; hash SHA-256: `604660f59992f3c9d3436350a27742aff744bfd7fd9938536f1daa09e824b2fb`.
- SHA Git blob calculado localmente y recuperado por GitHub: `f12fc56cb36e5dbe97bb491f057d6c80215b1df1`.
- Contenedor XLSX ZIP íntegro (`testzip() = None`), 17 entradas OOXML, seis hojas, 26 fórmulas `WORKDAY` y hojas de costos y dotación presentes.
- El repositorio mantiene `main` sin cambios y conserva el historial de la versión anterior del archivo.

## SUPUESTOS Y PENDIENTES

- La categoría TMED y la conversión mensual a horas son referencias de planificación, no tarifa comercial ni clasificación laboral confirmada.
- Ajuste 2027 y contribuciones patronales son parámetros presupuestarios provisionales; verificar decreto 2027, clasificación, modalidad laboral, póliza INS, cargas y provisiones aplicables.
- Validar el número de técnicos por actividad y la simultaneidad con un responsable de ejecución.
- No se efectuó apertura/cálculo visual de este XLSX en Microsoft Excel en esta intervención.
- El hash y la estructura son comprobaciones de archivo, **no** certificación de exactitud legal o constructiva.

**Siguiente acción mínima:** revisar en Excel las seis hojas y sustituir las tarifas supuestas por bases salariales verificadas aplicables al escenario docente.
