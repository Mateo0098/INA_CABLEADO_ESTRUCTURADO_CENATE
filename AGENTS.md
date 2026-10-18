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
