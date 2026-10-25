# Registro de decisiones, supuestos y cuestiones pendientes

**Última actualización:** 2026-10-25
**Etapa:** Fase 2C — paquete técnico de revisión preparado; entrega final abierta

## D-001 — Identidad y alcance académico

- **Clasificación:** dato establecido por el docente.
- **Registro:** proyecto del módulo ELTT12000 — Presupuesto de la red, Actividad de Comprobación N.º 1.
- **Entrega:** 2026-10-29.
- **Alcance:** infraestructura física de telecomunicaciones de dos edificios nuevos del complejo CENATE del INA.
- **Exclusión:** contratación y prestación del servicio ISP.
- **Fuente:** F-005 §§1, 8 y 13; confirmado contra el enunciado oficial.

## D-002 — Programa funcional de los edificios

| Elemento | Edificio A | Edificio B | Clasificación |
|---|---:|---:|---|
| Pisos | 4 | 7 | Dato establecido por el docente |
| Laboratorios por piso | 5 | 6 | Dato establecido por el docente |
| Área por laboratorio | 85 m² | 75 m² | Dato establecido por el docente |
| Áreas de trabajo dobles por laboratorio | Mínimo 16 | Mínimo 16 | Dato establecido por el docente |
| TR | Al menos 1 por piso | Al menos 1 por piso | Dato establecido por el docente |
| ER | 1 propio | 1 propio | Dato establecido por el docente |

No se derivan en esta etapa cantidades de salidas, cables, racks, puertos ni equipos.

## D-003 — Configuración arquitectónica preliminar

| Parámetro | Valor preliminar | Clasificación |
|---|---:|---|
| Geometría de laboratorio A | 10 × 8,5 m | Supuesto de diseño |
| Geometría de laboratorio B | 10 × 7,5 m | Supuesto de diseño |
| Forma de planta | Rectangular | Supuesto de diseño |
| Circulación | Pasillo central | Supuesto de diseño |
| Repetición | Pisos típicos idénticos dentro de cada edificio | Supuesto de diseño |
| Ubicación de ER | Planta baja | Supuesto de diseño |
| Alineación de TR | Vertical | Supuesto de diseño |
| Dimensión de TR | 3 × 3 m | Supuesto de diseño |
| Dimensión de ER | 4 × 4 m | Supuesto de diseño |
| Altura entre pisos | 3,5 m | Supuesto de diseño |
| Ancho del pasillo central | 2,4 m | Supuesto de diseño |

Estos valores no son mediciones de campo ni soluciones normativamente validadas.

## D-004 — Criterios iniciales del cableado interno

- **Dato establecido por el docente:** enlace permanente de cobre con máximo de 90 m.
- **Criterio contextual pendiente de validación:** topología horizontal en estrella; no aparece textualmente en F-005/F-006 y deberá sustentarse con los criterios técnicos aplicables.
- **Dato establecido por el docente:** backbone vertical desde cada ER hasta los TR.
- **Supuesto de diseño:** bandejas y derivaciones protegidas como canalización interior preliminar.
- **Decisión pendiente:** validar recorridos, ocupación, capacidad, protección, segregación y criterios aplicables antes del diseño definitivo.

## D-005 — Backbone exterior

- **Dato establecido por el docente:** existe un ER principal en un edificio del INA.
- **Información proporcionada por el estudiante (F-007):** 145 m de canalización subterránea existente; no aparece en F-005/F-006 y requiere evidencia o validación de campo.
- **Información proporcionada por el estudiante (F-007):** separación de referencia de 25 m entre cajas; no se interpreta como requisito normativo.
- **Propuesta proporcionada por el estudiante (F-007):** 50 m de canalización subterránea nueva para alcanzar uno de los ER.
- **Resultado aritmético preliminar sobre F-007:** 145 m + 50 m = 195 m hasta ese ER; no sustituye recorrido de cable ni medición verificada.
- **Dato establecido por el docente:** se requieren los enlaces ER principal–ER A, ER principal–ER B y ER A–ER B.
- **Decisiones pendientes:** identificar cuál edificio recibe los 50 m nuevos; levantar y aprobar los otros recorridos; verificar trazados, longitudes, cajas, ductos y condiciones de la infraestructura existente.

## D-006 — Imágenes técnicas requeridas

Se registran nueve imágenes mínimas futuras, con procedencia diferenciada:

1. Infraestructura exterior de los tres edificios.
2. Planta típica del edificio A.
3. Planta típica del edificio B.
4. Laboratorio representativo del edificio A.
5. Laboratorio representativo del edificio B.
6. ER del edificio A — actualización F-006.
7. TR del edificio A — actualización F-006.
8. ER del edificio B — actualización F-006.
9. TR del edificio B — actualización F-006.

Las primeras cinco se derivan de F-005 §4: exterior, dos plantas típicas y dos laboratorios típicos, siempre que no existan variaciones que exijan más imágenes. Las imágenes ER/TR deberán representar los elementos indicados en F-006 y todas deberán corresponder con cálculos, materiales y Excel; por ello no se generan en esta etapa.

## D-007 — Control documental

- **Decisión de gestión:** conservar originales, fuentes y evidencia; realizar cambios mediante ramas y commits acotados.
- **Dato establecido por el docente:** la plantilla Excel original del INA debe conservar estructura y formato; la primera actividad no debe incluir precios ni costos.
- **Decisión de gestión:** registrar la asistencia de IA como política interna. Aplicar estrictamente F-005 §9: la IA no puede ser fuente técnica, resolver cálculos ni generar automáticamente el Excel.
- **Decisión de gestión:** no adoptar marcas, modelos, normas ni especificaciones sin una fuente verificable.

## Mediciones de campo

No se han incorporado mediciones de campo en esta etapa.

## Especificaciones verificadas de fabricante

No se han incorporado especificaciones de fabricante en esta etapa.

## D-008 — Estado de las fuentes oficiales

- **Conclusión provisional histórica:** inicialmente no estaban disponibles el enunciado ni la actualización.
- **Resolución:** F-005 y F-006 se incorporaron mediante los commits remotos `fae8cc5` y `e066c93`, se preservaron con SHA-256 y se leyeron íntegramente.
- **Limitación:** no existe rúbrica independiente; se utilizan F-005 §§11–13 sin inventar ponderaciones.

## D-009 — Preservación y uso de la plantilla candidata

- **Evidencia verificada:** se incorporó una copia byte a byte de `Plantilla Actividades de comprobación.xlsx`, SHA-256 `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`.
- **Evidencia verificada:** el libro trae ejemplos didácticos de materiales, marcas, referencias, cantidades y proveedores; los precios por renglón están vacíos y `J43` contiene `SUM(J2:J41)`.
- **Decisión de gestión:** el original controlado no se editará y sus ejemplos no se considerarán selección ni dimensionamiento del proyecto.
- **Resolución de procedencia:** F-005 §5 exige la plantilla adjunta y el estudiante confirmó que el archivo incorporado es esa plantilla; se acepta como original operativo.
- **Decisión pendiente:** confirmar con el docente si la fórmula económica preexistente `J43` debe conservarse en la copia final o quedar vacía; no se incorporarán montos en ningún caso.

## D-010 — Cierre de Fase 1

- **Resultado:** 76 requisitos oficiales identificados: INA-001 a INA-071 desde F-005 e INA-072 a INA-076 desde F-006.
- **Decisión:** cerrar la Fase 1 documental. Los puntos abiertos están identificados y no impiden comenzar posteriormente el diseño, pero deberán resolverse antes de afectar cálculos o entrega.
- **Restricción:** este cierre no valida supuestos arquitectónicos, mediciones, productos, cantidades ni planos.
- **Continuidad verificada:** los registros F-007, F-008 y F-009 se integraron desde `origin/desarrollo-proyecto` mediante avance rápido hasta `6e086ea`; no hubo conflictos ni pérdida de cambios locales.

## Historial de cambios de decisión

| Fecha | ID | Cambio | Motivo / evidencia | Impacto |
|---|---|---|---|---|
| 2026-10-18 | D-001 a D-007 | Registro inicial | Instrucciones de inicialización del usuario | Base documental; sin diseño definitivo |
| 2026-10-18 | D-008 y D-009 | Control de fuentes y plantilla | Inventario local, hashes y auditoría OOXML | Fase 1 parcial; fuentes oficiales pendientes |
| 2026-10-18 | D-005, D-006, D-008 a D-010 | Cotejo y cierre oficial | F-005, F-006, F-007 y plantilla auditada | Corrige procedencias, define 76 requisitos y cierra Fase 1 |
| 2026-10-18 | D-010 | Recuperación de sesión | Commits remotos 0a65211, 281bc09 y 6e086ea | Integra datos, arquitectura conceptual y transferencia sin conflictos |

## D-011 — Identificación y geometría de referencia de Fase 2B

- **Clasificación:** decisión de diseño provisional.
- **Identificadores adoptados:** `ER-P`, `ER-A`, `ER-B`, `TR-{edificio}-P{piso}`, `LAB-{edificio}-P{piso}-L{número}` y `AT-{01..16}`.
- **Representación:** nueve SVG editables y nueve PNG 1600×1000 en `07_imagenes/fase2b/`, generados por un script reproducible.
- **Condición:** los esquemas no están a escala. Las geometrías de laboratorios, pasillos, ER/TR, ubicación en planta baja y alineación vertical siguen clasificadas como supuestos de diseño.
- **Procedencia:** apoyo visual de OpenAI Codex; revisión humana obligatoria antes de entrega.

## D-012 — Capacidad pasiva provisional de cobre

- **Supuesto:** una “área de trabajo doble” se modela con dos puertos RJ45; continúa pendiente de confirmación docente.
- **Resultado condicionado:** A = 640 enlaces, B = 1 344, total = 1 984.
- **Paneles:** 48 puertos. Se adopta provisionalmente una regla reproducible: redondear hacia arriba y agregar un panel cuando la división exacta dejaría cero posiciones libres.
- **Resultado:** A = 4 paneles/TR y 16 totales; B = 5 paneles/TR y 35 totales; total = 51 paneles, con 464 posiciones libres.
- **Limitación:** los metros de cable permanecen `N/D` hasta medir rutas y aprobar desperdicio. Los 90 m son límite, no longitud asumida.

## D-013 — Capacidad pasiva provisional de fibra

- **Supuesto de diseño:** 12 fibras OS2 por cada uno de los 11 enlaces ER–TR y 24 fibras OS2 por cada uno de los tres enlaces exteriores.
- **Resultado condicionado:** 264 terminaciones individuales verticales + 144 exteriores = 408 terminaciones/pigtails/empalmes si se terminan todas las fibras; 204 adaptadores LC dúplex bajo esa misma condición.
- **Separación de magnitudes:** cantidad de fibras, cantidad de cables, metros de cable y metros de ducto se registran por separado.
- **Limitación:** `x`, `y`, reservas y recorridos internos continúan pendientes; 145 m y 50 m no se replican automáticamente entre los tres enlaces.

## D-014 — Materiales candidatos y Excel de trabajo

- **Especificaciones verificadas de fabricante:** se documentaron candidatos oficiales de Panduit y Corning para panel Cat 6A, jack Cat 6A, cable Cat 6A, cables OS2 de 12/24 fibras, pigtail LC/UPC y adaptador LC dúplex.
- **Estado comercial:** candidatos, no selección final; disponibilidad local, compatibilidad integral y cantidades dependientes de medición siguen pendientes.
- **Excel:** se creó `06_excel/Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx` como copia byte a byte del original. Ambos conservan SHA-256 `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6` y `J43=SUM(J2:J41)`.
- **Decisión académica:** la copia no fue llenada automáticamente con IA. La correspondencia para traslado manual revisado está en `06_excel/CORRESPONDENCIA_FASE2B.md`; no contiene precios.

## Historial de cambios de decisión — Fase 2B

| Fecha | ID | Cambio | Motivo / evidencia | Impacto |
|---|---|---|---|---|
| 2026-10-25 | D-011 a D-014 | Implementación documental de Fase 2B | Nueve diseños, modelo reproducible, matriz técnica, copia Excel y 63 controles automáticos | Avance verificable; metrajes, selección final y llenado manual del Excel continúan pendientes |

## D-015 — Arquitectura provisional de terminación de fibra

- **Clasificación:** supuesto de diseño verificable, sujeto a revisión humana y compatibilidad integral.
- **Decisión provisional:** representar la terminación completa mediante cassettes preconectorizados/precargados: 22 unidades de 12 fibras para los once enlaces verticales y 6 unidades de 24 fibras para los tres enlaces exteriores, una por extremo.
- **Resultado calculado:** las 408 terminaciones funcionales y 204 posiciones LC dúplex permanecen como magnitudes de capacidad, pero pigtails y adaptadores comprados por separado se fijan en cero mientras se mantenga esta arquitectura, para evitar doble conteo.
- **Evidencia comercial:** familias Corning CCH documentadas en `05_materiales/MATRIZ_TECNICA_FASE2C.md`; no constituye compra ni selección definitiva.

## D-016 — Cierre controlado del Excel

- **Dato establecido por el docente:** la IA no debe generar automáticamente el Excel de entrega y la primera actividad no incluye precios.
- **Decisión de gestión:** preservar sin cambios tanto el original como la copia provisional y entregar planes de correspondencia fila por fila para que el estudiante haga el traslado manual, comprenda las fórmulas y retire los ejemplos didácticos.
- **Evidencia verificada:** ambos libros mantienen SHA-256 `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`, las hojas originales y `J43=SUM(J2:J41)`.
- **Condición:** la copia continúa marcada como provisional y no debe presentarse como final.

## D-017 — Límites de cierre académico de variables

- **Supuestos razonables para escenario:** 2 RJ45 por área doble, un TR por piso, reserva de panel según D-012, 12 fibras por enlace vertical, 24 fibras por enlace exterior y arquitectura de cassette de D-015.
- **Resultados de referencia, no mediciones:** ruta base parcial E1 = 195 m; desnivel vertical mínimo geométrico A = 21,0 m y B = 73,5 m, sin reservas ni recorridos internos.
- **Variables que no se cierran sin evidencia:** longitudes horizontales de cobre, recorridos completos E1/E2/E3, longitudes reales verticales, reservas, ocupación de ductos/bandejas, ubicación/estado de cajas y compatibilidad final de racks, gabinetes y activos.
- **Control:** `04_calculos/REVISION_VARIABLES_FASE2C.md` mantiene cada variable en su categoría y evita presentar escenarios como mediciones.

## Historial de cambios de decisión — Fase 2C

| Fecha | ID | Cambio | Motivo / evidencia | Impacto |
|---|---|---|---|---|
| 2026-10-25 | D-015 a D-017 | Cierre técnico controlado | Matriz consolidada, revisión de variables, planes Excel y 124 controles automáticos | Paquete revisable disponible; entrega final aún depende de validación humana, campo y traslado manual |
