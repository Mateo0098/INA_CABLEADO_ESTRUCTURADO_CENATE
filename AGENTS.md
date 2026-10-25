# Instrucciones permanentes para agentes

Estas reglas aplican a todo el repositorio `INA_CABLEADO_ESTRUCTURADO_CENATE`.

## Inicio obligatorio de cada sesión

1. Leer completamente `README.md`, `DECISIONES.md` y `PENDIENTES.md`.
2. Leer este archivo antes de actuar.
3. Inspeccionar `git status`, `git remote -v` y `git branch -a`.
4. Revisar los archivos relacionados antes de modificarlos.
5. Trabajar en una rama distinta de `main`. No modificar `main` directamente.
6. Si el repositorio o `origin` no coinciden con el proyecto esperado, detener las modificaciones, documentar el problema y pedir orientación.

## Ingeniería y evidencia

- Clasificar cada entrada como: dato establecido por el docente, medición de campo, supuesto de diseño, resultado calculado, especificación verificada de fabricante o decisión pendiente.
- No transformar un supuesto en dato confirmado ni una estimación en medición.
- No inventar marcas, modelos, referencias, normas, precios, fichas técnicas o fuentes.
- Registrar fuente, fecha de consulta, versión, unidad y responsable cuando correspondan.
- Mantener cálculos reproducibles: conservar entradas, fórmulas, unidades, redondeos y vínculo con sus resultados.
- Marcar las inconsistencias; no resolverlas silenciosamente.
- Someter a revisión humana todo contenido técnico generado o transformado con IA y registrar su procedencia.

## Coherencia entre entregables

- Mantener sincronizados requisitos, decisiones, diseños, cálculos, lista de materiales, Excel e imágenes.
- No crear una imagen técnica que contradiga los cálculos o los materiales aprobados.
- No seleccionar definitivamente productos antes de verificar información del fabricante.
- Conservar la estructura y el formato de la plantilla Excel original del INA.
- No introducir precios ni costos en la primera actividad.
- Guardar originales sin modificación y trabajar sobre copias claramente identificadas cuando aplique.

## Método de trabajo

- Realizar cambios acotados, revisables y verificables.
- No sobrescribir decisiones previas: registrar el cambio, motivo, evidencia, fecha e impacto.
- Actualizar `DECISIONES.md` y `PENDIENTES.md` al cerrar cada etapa.
- Registrar problemas, incertidumbres, dependencias y datos faltantes.
- Generar un reporte de cierre por etapa en `09_auditorias/`, incluyendo alcance, entradas, cambios, verificaciones, pendientes y referencia del commit.
- Revisar diferencias y ejecutar controles pertinentes antes de confirmar cambios.
- No ejecutar operaciones destructivas, eliminar información, reescribir el historial Git ni forzar publicaciones sin autorización expresa.

## Convenciones documentales

- Usar español claro, unidades explícitas y fechas ISO (`AAAA-MM-DD`).
- Separar hechos, supuestos y resultados en tablas o secciones identificables.
- Referenciar archivos mediante rutas relativas al repositorio.
- Evitar archivos temporales, bloqueos de Office, cachés, credenciales y artefactos locales.
- Usar `.gitkeep` solo para conservar directorios todavía vacíos.

## Protocolo permanente de comunicación Codex → GitHub → ChatGPT

**Objetivo:** el usuario no debe tener que copiar la salida de la terminal de Codex para que ChatGPT evalúe los resultados. GitHub es el canal de transferencia documental y la fuente de evidencia; ChatGPT revisará los archivos publicados mediante su conector GitHub cuando el usuario indique continuar o revisar. **No hay envío automático ni notificación directa de Codex a una conversación activa de ChatGPT.**

1. Antes de intervenir, sincronizar con `origin/desarrollo-proyecto` de manera segura, respetando cualquier modificación local y sin tocar `main`.
2. Cada intervención tendrá un alcance preciso, verificaciones y criterios de aceptación; evitar auditorías generales repetidas.
3. Al finalizar un bloque, guardar un **reporte autocontenido** Markdown en `09_auditorias/REPORTES_CODEX/` con nombre `AAAA-MM-DD_<fase>_<tema>.md`. Incluir obligatoriamente:
   - objetivo y alcance; entradas/fuentes examinadas;
   - decisiones de diseño y supuestos no verificados;
   - lista exacta de archivos modificados, creados y no modificados;
   - resultados implementados y resultados meramente propuestos;
   - pruebas: comandos, resultados obtenidos y limitaciones de verificación;
   - cantidades con unidad, fundamento y carácter provisional/definitivo;
   - problemas abiertos priorizados por impacto real en la entrega;
   - estado Git, rama y SHA de implementación si está disponible;
   - siguiente acción mínima viable; distinción entre **HECHO / VERIFICADO / PENDIENTE**.
4. Actualizar `09_auditorias/ULTIMO_REPORTE_CODEX.md` como **índice de transferencia**. Debe contener ruta relativa al último reporte, fecha, fase, commit implementado cuando exista, estado, bloqueos y hasta tres prioridades siguientes. Este es el primer archivo que ChatGPT leerá.
5. Publicar el reporte y el índice junto con los cambios en `origin/desarrollo-proyecto`; si el SHA final no se conoce al redactar el reporte, referenciar el commit de implementación y confirmar posteriormente el SHA final en la respuesta terminal. Evitar ciclos interminables de commits solo para actualizar el hash.
6. Si la publicación falla, **no afirmar que ChatGPT puede leer el reporte**. Mantener archivos locales, diagnosticar el error y comunicar solamente ruta, SHA local y motivo de no publicación. No asumir que la conversación de ChatGPT puede acceder a archivos del disco local.
7. La salida final de Codex al usuario debe ser breve: estado de publicación, rama, SHA final, ruta del reporte e índice. No pegar informes extensos en terminal, salvo que falle la transferencia.
8. ChatGPT debe revisar primero `09_auditorias/ULTIMO_REPORTE_CODEX.md`, después el reporte indicado y solo los archivos decisivos para comprobar hallazgos. No dar por validado el proyecto completo por el mero hecho de que pasen controles automatizados.
9. Documentar la autoría asistida por IA y conservar los requisitos académicos oficiales y la trazabilidad; evitar alterar silenciosamente reglas del profesor, originales o cálculos de autoría individual.
10. En cada nueva sesión de Codex, retomar el último checkpoint verificable; no ejecutar otra auditoría de 76 requisitos ya cerrada sin una inconsistencia nueva y concreta.

**Indicador de trabajo:** el progreso se mide por artefactos utilizables para la entrega del INA y controles relevantes, no por la cantidad de reportes, unidades o commits.
