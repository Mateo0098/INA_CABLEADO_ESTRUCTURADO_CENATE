# Fase 3A — cierre operativo del Excel INA CENATE

**Fecha:** 2026-10-25
**Fase:** 3A — guía de transferencia y cierre operativo
**Rama observada:** `desarrollo-proyecto`
**HEAD previo:** `846900b0dda373813c0a9a8e52ec30056d1184c7`
**Sincronización/publicación:** tras la recuperación puntual de permisos se ejecutó `git fetch origin`; `HEAD...origin/desarrollo-proyecto` indicó `0 0` antes del commit. El SHA final queda registrado en este reporte y en el índice tras crear el commit.

## Objetivo y alcance

Preparar una guía inequívoca para que el estudiante complete manualmente su copia personal del libro INA; revisar de forma dirigida las cantidades solicitadas, la coherencia de fibra/canalizaciones y herramientas; documentar qué verificaciones del libro final no son posibles porque aún no existe. No se editó ningún archivo XLSX ni se repitieron investigaciones de producto o auditorías generales.

## Entradas examinadas

- `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md` e índice de transferencia vigente.
- `09_auditorias/REPORTES_CODEX/2026-10-25_FASE2D_CIERRE_CANTIDADES.md`.
- Modelo, entradas, resultados y memoria de Fase 2D en `04_calculos/`.
- `05_materiales/MATRIZ_TECNICA_FASE2D.md`.
- `06_excel/PLAN_TRANSFERENCIA_EXCEL_FASE2D.md`, planes CSV de materiales/herramientas y estructura documentada de plantilla.
- `09_auditorias/validar_fase2d.py`, `validar_fase2b.py` y referencias existentes a `J43`.

## Clasificación de evidencia y resultados

| Elemento | Clasificación | Resultado/control |
|---|---|---|
| Pisos A/B, laboratorios, mínimo de 16 áreas dobles y límite 90 m | Dato docente según archivos de entrada Fase 2D | No revalidado contra fuentes oficiales en esta fase acotada |
| Geometría, reservas y desperdicios usados en metraje | Supuesto de diseño | Escenario Fase 2D; requiere aceptación del estudiante |
| Cajas Cat 6A | Resultado calculado condicionado | A 74 cajas de 305 m; B 155 cajas de 305 m; total 229 |
| Paneles y salidas | Resultado condicionado | 51 paneles, 1 984 RJ45 y 992 placas; 2 RJ45 por área doble sigue sujeto a confirmación docente |
| Cuartos | Resultado derivado | 11 TR según un TR por piso en escenario; 13 racks propuestos (11 TR + 2 ER nuevos), no selección final |
| Fibra | Escenario/arquitectura candidata | 11 enlaces verticales 12F y 3 exteriores 24F; cassettes: 22×12F y 6×24F; housings 12×1U + 1×3U + 1×4U |
| Terminación óptica | Decisión de arquitectura provisional | Pigtails y adaptadores separados en cero para no duplicar integración de cassettes; patch cords ópticos 0–204 según pares activos |
| E2/E3 | Decisión pendiente | Se conservan `169,05+1,05x m` y `16,8+1,05y m`; no hay cantidades cerradas |
| Canalización | Resultado de longitud más decisión pendiente de producto | Bandeja 1 432,725 m y tubería/bajantes 3 124,8 m son longitudes de escenario; sección/diámetro/producto no seleccionados |
| Herramientas | Escenario de instalación | 12 filas (2–13) para una cuadrilla; equipos reutilizables separados de lubricante/etiquetas consumibles |
| Excel de estudiante | No disponible | No se simuló edición ni validación final |

Las referencias de fabricante registradas en la matriz se conservaron como candidatas verificadas según el checkpoint 2D. Esta fase no hizo nueva verificación de fichas ni disponibilidad comercial.

## Cambios de esta fase

### Modificado

- `06_excel/PLAN_TRANSFERENCIA_EXCEL_FASE2D.md`: referencia añadida a la guía operativa de Fase 3A.
- `DECISIONES.md`: D-021 registra la guía, clasificación y límites de esta fase.
- `PENDIENTES.md`: checkpoint Fase 3A con hechos, verificaciones y bloqueos.

### Creado

- `06_excel/GUIA_CIERRE_ESTUDIANTE_FASE3A.md`: instrucciones por cada fila de materiales/herramientas, cálculo/unidad, estado, acción, reglas de transferencia y lista reproducible de control.
- `09_auditorias/REPORTES_CODEX/2026-10-25_FASE3A_CIERRE_OPERATIVO_EXCEL.md`: este reporte.
- `09_auditorias/ULTIMO_REPORTE_CODEX.md`: índice actualizado para transferencia local.

### No modificado

- `06_excel/Plantilla Actividades de comprobación.xlsx` (original).
- `06_excel/Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx` (copia provisional).
- Los CSV de entrada/resultados Fase 2D y la memoria de cálculo.
- Rama `main`.

## Instrucciones mínimas de edición

1. Crear una copia personal nueva; no sobrescribir original ni copia controlada.
2. Revisar y aceptar cada supuesto. Trasladar manualmente solo filas que el estudiante pueda explicar.
3. Preservar las dos hojas, encabezados, columnas A–K, orden, colores y formatos; mantener I/J sin importes.
4. Dejar E2/E3 y patch cords ópticos sin cantidad cerrada hasta resolver variables/pares activos. No convertir metraje de canalización en diámetro o producto seleccionado.
5. No comprar pigtails/adaptadores por separado mientras se mantenga cassette integrado. Resolver `J43` con el docente antes de cambiar la fórmula original.
6. Retirar los ejemplos didácticos en la copia personal, probar recálculo en la aplicación de entrega y ejecutar la lista de control de `GUIA_CIERRE_ESTUDIANTE_FASE3A.md`.

## Pruebas y verificaciones

| Control | Resultado |
|---|---|
| Inspección `git status`, remoto, ramas | Rama local `desarrollo-proyecto`; remoto `https://github.com/Mateo0098/INA_CABLEADO_ESTRUCTURADO_CENATE.git`; remotes locales incluían `origin/desarrollo-proyecto` y `origin/main` |
| Diagnóstico de permisos | Usuario efectivo `mateo\codexsandboxoffline`; no se encontró `index.lock`; `Get-Process git,git-remote-https,ssh` no devolvió procesos; la escritura fue denegada desde el contexto sandbox |
| Sincronización | `git fetch origin` con elevación puntual terminó correctamente; divergencia local/remota antes de integrar: `0 0` |
| Modelo y CSV Fase 2D | Inspección dirigida confirma coherencia documental de cantidades indicadas; no se modificaron ni recalcularon resultados |
| Herramientas | El CSV cubre filas 2–13; solo lubricante sin cantidad numérica; no contiene modelos/proveedores inventados |
| Integridad del libro disponible | Checkpoint/validador Fase 2D documenta original y copia con SHA-256 `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`, hojas originales y `J43=SUM(J2:J41)`; esta fase no volvió a modificar/escribir libros |
| Contenido final del Excel | No ejecutable: no existe libro completado por el estudiante. Ejemplos, fórmulas nuevas, recálculo, ausencia de precios en copia editada y tratamiento final de J43 quedan sin comprobar |
| Push/commit | Se creó y publicó el commit descrito al final de este reporte en `origin/desarrollo-proyecto`; `main` no fue modificada. La elevación se limitó a operaciones Git del repositorio |

Comandos que el estudiante puede ejecutar al disponer de su copia: `python 09_auditorias/validar_fase2d.py` y `python 09_auditorias/validar_fase2b.py`, más la lista específica de libro estudiante documentada en la guía. Los validadores actuales no validan una futura copia editada de forma automática.

## Archivos y estado exacto del Excel

- Original: presente, intacto según SHA-256 registrado; contiene ejemplos didácticos; no es entregable final.
- Copia provisional: presente, idéntica según SHA-256 registrado; contiene ejemplos didácticos; no es entregable final.
- Copia personal completada: no existe en el repositorio; integridad OOXML posterior, fórmulas nuevas, estructura conservada tras edición, precios, ejemplos residuales y recálculo no pueden afirmarse.
- `J43`: fórmula original `SUM(J2:J41)`; tratamiento aún pendiente de criterio docente. Columnas económicas no autorizan introducir importes.

## Problemas abiertos, por impacto

1. **Cierre de Excel:** falta la copia manual del estudiante y su revisión; no marcar final mientras conserve ejemplos.
2. **Decisión docente:** confirmar dos RJ45 por área doble y tratamiento de `J43`.
3. **Campo/diseño:** resolver destino E1, `x/y`, recorridos, estado de ductos/registros y dimensiones de canalización.
4. **Activos:** definir pares ópticos activos y compatibilidad/capacidad de racks.

## HECHO / VERIFICADO / PENDIENTE

- **HECHO:** guía operativa por fila creada y enlazada desde el plan de transferencia; decisión y pendientes documentados.
- **VERIFICADO:** cifras objetivo cotejadas contra entradas/resultados/memoria Fase 2D; correspondencia de herramientas completa; no se editó ningún libro.
- **PENDIENTE:** transferencia manual, control de la futura copia, criterio docente y mediciones.

## Git y siguiente acción mínima viable

- **Rama:** `desarrollo-proyecto`.
- **HEAD previo:** `846900b0dda373813c0a9a8e52ec30056d1184c7`.
- **SHA de implementación/publicación:** se completará en este reporte luego de crear el commit; el índice de transferencia lo reflejará.
- **Publicación:** `origin/desarrollo-proyecto`; `main` sin cambios.
- **Siguiente acción:** el estudiante completa y valida su copia personal.
