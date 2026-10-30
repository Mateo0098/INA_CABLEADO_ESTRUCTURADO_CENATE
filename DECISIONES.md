# Registro de decisiones, supuestos y cuestiones pendientes

**Última actualización:** 2026-10-25
**Etapa:** Fase 2D — cantidades de escenario y preparación Excel; entrega final abierta

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

## D-018 — Escenario académico de recorridos

- **Clasificación:** supuesto de diseño explícito, no medición de campo.
- **Geometría:** TR al extremo del pasillo; progresivas por centros de laboratorio; 3 m internos en TR, medio pasillo, distribución interior según 10 m de profundidad, bajante de 3 m y desviación lateral por fachada.
- **Reserva y desperdicio:** 3 m por enlace de cobre y 5 % de desperdicio de compra, tratados por separado. Fibra: 3 m internos y 5 m de reserva en cada extremo, más 5 %.
- **Control:** máximo con reserva A = 45,7 m y B = 42,7 m, ambos inferiores al máximo docente de 90 m.
- **Resultado condicionado:** 229 cajas de Cat 6A de 305 m; 284,025 m de cable vertical OS2 12F; E1 = 221,55 m de 24F bajo la hipótesis 145 + 50 m.
- **Límite:** E2 = `169,05 + 1,05x` y E3 = `16,8 + 1,05y`; no se cierran sin `x/y`.

## D-019 — Sistema pasivo compatible de referencia

- **Cobre:** cable, panel, jack, placa y patch cord Panduit Cat 6A documentados en `05_materiales/MATRIZ_TECNICA_FASE2D.md`.
- **Fibra:** 22 cassettes CCH 12F y 6 cassettes CCH 24F; 12 housings `CCH-01U`, un `CCH-03U` y un `CCH-04U`.
- **No duplicación:** pigtails y adaptadores separados permanecen en cero porque están integrados en los cassettes.
- **Racks:** 13 gabinetes nuevos de 42U como escenario, sin duplicar ER-P; activos, energía, carga y ventilación continúan separados.
- **Organización:** 51 organizadores de cobre y 14 ópticos, uno por panel/housing.

## D-020 — Preparación del Excel Fase 2D

- **Decisión:** mantener original y copia controlada sin cambios y preparar la transferencia manual de filas 2–27 y herramientas 2–13.
- **Listas para revisión:** cantidades numéricas de cobre, fibra vertical, E1, cassettes, housings, racks y organizadores.
- **Bloqueadas justificadamente:** E2/E3, patch cords ópticos activos, producto de canalización, puesta a tierra y cajas exteriores reales.
- **Restricción:** no hay precios; `J43` permanece sin resolver por el docente; el libro conserva ejemplos y no es final.

## Historial de cambios de decisión — Fase 2D

| Fecha | ID | Cambio | Motivo / evidencia | Impacto |
|---|---|---|---|---|
| 2026-10-25 | D-018 a D-020 | Cierre académico de longitudes y sistema pasivo | Modelo Fase 2D, matriz compatible y plan Excel | Reduce pendientes a variables de campo/docente/activos y revisión humana |

## D-021 — Guía operativa para cierre manual del Excel

- **Clasificación:** decisión de gestión documental.
- **Fecha:** 2026-10-25.
- **Decisión:** consolidar en `06_excel/GUIA_CIERRE_ESTUDIANTE_FASE3A.md` la transferencia fila por fila de materiales y herramientas, fórmulas de comprobación, unidades, estados, acciones, criterios de OOXML/hojas/columnas/precios y tratamiento explícito de `J43`.
- **Evidencia:** revisión dirigida de entradas, modelo, resultados, memoria, matriz, planes CSV y estructura documentada del libro.
- **Límite:** no existe una copia completada por el estudiante. Original y copia provisional siguen intactos y contienen ejemplos didácticos; no se reporta un libro final ni se simula validación de contenido nuevo.
- **Cantidades:** 74 y 155 cajas Cat 6A de 305 m; 51 paneles; 1 984 jacks; 992 placas; 11 TR; 13 racks propuestos. Son resultados condicionados al escenario/documentación Fase 2D, no mediciones nuevas ni selección definitiva.
- **Fibra/canalización:** cassettes y housings conservan arquitectura sin pigtails/adaptadores duplicados; E2/E3 permanecen paramétricos; se separa longitud de canalización de sección/diámetro/producto.
- **Herramientas:** tabla de 12 filas (2–13), con cantidad de escenario para una cuadrilla y distinción de herramientas reutilizables frente a lubricante/consumibles variables; sin marcas/modelos inventados.
- **Historial:** no se sobrescribe la decisión docente pendiente sobre `J43`; fórmula original `SUM(J2:J41)` y columnas económicas sin montos deben tratarse según confirmación docente.

## D-022 — Libro de escenario completado y supuestos exteriores Fase 3B

- **Clasificación:** decisión de diseño académica solicitada por el usuario; distancias y dimensionamiento de canalización son supuestos, no mediciones ni especificaciones verificadas de fabricante.
- **Fecha:** 2026-10-25.
- **Decisión:** producir `06_excel/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx` y su copia en `08_entrega/PAQUETE_REVISION_FASE3B/`, partiendo del original sin modificar; mantener estructura/estilos de las dos hojas y celdas de costo vacías.
- **Supuestos adoptados:** 16 áreas dobles por laboratorio, dos RJ45 por área, un TR/piso, reserva de cobre de 3 m por enlace, 5 % de desperdicio y geometría Fase 2D.
- **Estimaciones de fibra exterior:** x=75 m para E2 (tres intervalos teóricos de 25 m) e y=50 m para E3 (dos intervalos); diagramas esquemáticos sin escala y 25 m no normativos. E1 se conserva como escenario 145+50 m hacia A. Ninguna es medición de campo.
- **Resultados derivados nuevos:** E1 221,55 m; E2 247,8 m; E3 69,3 m de cable 24F; total exterior 538,65 m. Fibra activa: un circuito dúplex por cada uno de 14 enlaces, 28 patch cords, dos por enlace (uno por extremo).
- **Canalización preliminar genérica:** bandeja 100×50 mm/3 m (478 tramos); bajantes PVC nominal 25 mm/3 m, dos Cat 6A (1 042 tramos); ducto exterior nominal 50 mm (50 m propuestos). Sección/diámetro interior, ocupación, carga, trazado y accesorios requieren verificación antes de construcción/compra. No se inventa fabricante.
- **Otros consumibles:** 3 968 etiquetas como supuesto de dos por enlace; lubricante de tiro queda variable y claramente clasificado como consumible, no herramienta.
- **Terminación y costos:** 0 pigtails y 0 adaptadores separados bajo arquitectura de cassette integrado. En la copia se limpia `J43` y se rotula la fila como cantidades sin costos; I/J no contienen importes. El original se mantiene byte a byte intacto.
- **Procedencia/revisión humana:** XLSX y gráficas preparados con asistencia de OpenAI Codex por petición del usuario; revisar restricciones académicas, hipótesis y fórmulas, y defender individualmente el contenido. Esta decisión no cambia las reglas oficiales del curso.
- **Verificación:** `09_auditorias/validar_excel_fase3b.py`, 135/135 controles; OOXML/XML parseable, fórmulas y cachés coincidentes, estilos y SHA del original preservados. No hubo Microsoft Excel/LibreOffice para observar recálculo visual.

## D-023 — Consolidación final Fase 4

- **Clasificación:** decisión de gestión documental; no altera datos, supuestos ni resultados técnicos de Fase 3B.
- **Fecha:** 2026-10-25.
- **Decisión:** organizar `08_entrega/ENTREGA_FINAL_INA_CENATE/` como paquete autocontenido con el Excel completado, nueve PNG, nueve SVG, memoria resumida, guía de defensa de al menos ocho minutos e inventario SHA-256.
- **Fuentes:** libro de `06_excel/`, diseños de `07_imagenes/fase2b/` y cantidades/supuestos de `04_calculos/MEMORIA_CANTIDADES_FASE3B.md`.
- **Revisión visual:** los nueve PNG se revisaron el 2026-10-25; no se observaron errores que requieran corrección. No se pudo abrir visualmente el XLSX en Excel/LibreOffice.
- **Procedencia IA:** memoria y guía preparadas con apoyo de OpenAI Codex; el estudiante debe revisar y comprender el contenido antes de presentarlo.

## D-024 — Reparacion de compatibilidad Microsoft Excel del libro Fase 4

- **Clasificacion:** correccion del formato del entregable; no cambia materiales, formulas, cantidades ni decisiones tecnicas Fase 3B.
- **Fecha:** 2026-10-25.
- **Causa confirmada:** `09_auditorias/crear_excel_fase3b.py` modificaba libro y hojas como XML con `xml.etree.ElementTree`. ElementTree descarto declaraciones de espacios de nombres referenciadas por `mc:Ignorable`/`mc:Requires`; el XML retuvo prefijos como `x15`, `xr`, `xr6`, `xr10`, `xr2` y `x14ac` pero perdio sus declaraciones `xmlns`. Microsoft Open XML SDK reporto seis errores `MC_InvalidIgnorableAttribute`/`MC_InvalidRequiresAttribute`; la plantilla original reporto cero. Excel 16 COM rechazo el libro defectuoso con HRESULT `0x800A03EC`.
- **Correccion:** regenerar desde la plantilla original mediante Microsoft Excel 16 COM. Datos y formulas se escribieron por la interfaz de hojas de calculo, sin alterar XML a mano. El autorrelleno de formulas de tabla se desactivo solo durante esa sesion COM y se restauro al valor previo; no se cambio configuracion global.
- **Verificacion real:** Excel abrio la plantilla, el archivo regenerado, una copia de prueba guardada y reabierta, y la ruta final del paquete. Se comprobaron las dos hojas, las 29 formulas/cantidades de materiales, herramientas y ausencia de precios. Open XML SDK reporta cero errores en los dos entregables finales. La plantilla conserva SHA-256 `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`.
- **Preservacion:** el libro defectuoso se respaldo fuera del paquete final en `09_auditorias/evidencias/Excel_COM/INA_CENATE_ACTIVIDAD_1_COMPLETADA_DEFECTUOSO_2026-10-25.xlsx`, SHA-256 `1A1CC4B4A825C21BF7C421B106235D9C921BCA4A42C384209E4F9408A7B7D530`.
- **Procedencia:** `09_auditorias/regenerar_excel_fase4.ps1` toma la matriz aprobada existente en `crear_excel_fase3b.py`; el libro fue regenerado con asistencia de OpenAI Codex y requiere revision academica del estudiante.

## D-025 — Documentos de lectura PDF del paquete final

- **Clasificación:** decisión de formato y gestión documental; no altera datos, supuestos, cálculos ni diseños técnicos.
- **Fecha:** 2026-10-26.
- **Decisión:** entregar la memoria técnica y la guía individual como PDF A4, junto con `INDICE_ENTREGABLES.pdf`; conservar sus Markdown íntegros y el README histórico fuera de `08_entrega/ENTREGA_FINAL_INA_CENATE/`, en `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/`.
- **Fundamento:** permitir la lectura del paquete con Excel, un lector PDF y un visor de imágenes. El índice PDF explica la finalidad de cada carpeta y archivo.
- **Verificación:** cotejar fragmentos textuales de cada fuente Markdown con texto extraído del PDF, renderizar todas las páginas y revisar visualmente las seis páginas; comparar SHA-256 del XLSX y los nueve PNG/nueve SVG antes y después.
- **Procedencia y límite:** conversión y validación preparadas con OpenAI Codex; el estudiante aún debe revisar y comprender el contenido técnico antes de presentarlo.



## D-026 - Planos tecnicos A3 Fase 5 (2026-10-28)

- Clasificacion: decision de presentacion y resultados calculados representados; geometria y recorridos continuan como supuestos.
- Decision: incorporar nueve laminas numeradas 01/09-09/09 en PDF A3 horizontal, PNG y SVG editable, y un PDF combinado vectorial.
- Coherencia: Edificio A 160 puertos por TR en cuatro paneles de 48 (32 libres); Edificio B 192 por TR en cinco paneles de 48 (48 libres). Cada laboratorio tiene 16 WA dobles y 32 puertos bajo el supuesto adoptado.
- Fibra: OS2 24F para E1/E2/E3 y OS2 12F para backbone vertical. Cassette integrado representado sin duplicar pigtails/adaptadores. CCH-03U: 4 x 12F + 2 x 24F = 96 fibras en ER-A; CCH-04U: 7 x 12F + 2 x 24F = 132 en ER-B.
- Racks: elevaciones referenciales de 42U; puertos libres identificados como pasivos, sin implicar puertos activos.
- Supuestos: geometria, longitudes y canalizaciones no verificadas se rotulan como esquematicas o supuestas; no se declara escala numerica para plantas.
- Historico: conservar sin alterar los nueve PNG/SVG anteriores e identificarlos como coleccion historica en el indice del paquete.
- Procedencia: composicion visual con asistencia de OpenAI Codex; revision tecnica y academica personal pendiente.

## D-027 — Prototipos de representación física para TR-A y planta A (2026-10-28)

- **Clasificación:** decisión de presentación; conserva cantidades aprobadas, especificaciones verificadas de fabricante y supuestos de geometría separados.
- **Decisión:** crear solamente dos prototipos A3 horizontales en `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/`, sin reemplazar las nueve láminas vigentes ni alterar el Excel. Los prototipos serán evaluados antes de extender la técnica gráfica a las otras siete láminas.
- **TR-A:** gabinete frontal de 42U con rieles y numeración U01–U42; cuatro paneles de 48 conectores RJ45 dibujados, 160 posiciones asignadas y 32 libres; un cassette integrado OS2 12F en CCH-01U; cuatro organizadores horizontales y uno óptico. El cordón frontal es representativo, con extremo libre; no se instala ni presupone switch.
- **Planta A:** cinco laboratorios académicos y un TR por piso; bandeja preliminar 100 × 50 mm, tubos nominales Ø25 mm, cajas y pasamuros ilustrativos. Dos salidas dobles por laboratorio ilustran rutas independientes; no se fijan las 16 posiciones WA completas. Muros, rutas y fijaciones siguen como supuestos sin escala de obra.
- **Evidencia de fabricante consultada el 2026-10-28:** Panduit, guía NetKey `111369255.pdf`, página de paneles NK6XPPG48Y (48 puertos Cat 6A, 2U); Corning, guía `LAN-2564-AEN`, CCH-01U (1U, dos posiciones); Corning, ficha familiar `cch-pigtailed-splice-cassette_CALA_AEN.pdf`, cassette CCH-CS12-A9-P00RE (12F OS2, LC dúplex). Estas referencias respaldan símbolos y capacidades, no compra definitiva. Enlaces completos en el README de prototipos.
- **Procedencia y revisión:** composición vectorial con asistencia de OpenAI Codex. El estudiante y ChatGPT deben evaluar la mejora gráfica y la coherencia académica antes de modificar las otras siete láminas.

## D-028 — Consolidación de las nueve láminas Fase 5C (2026-10-29)

- **Clasificación:** decisión de presentación técnica. Las cantidades proceden del Excel definitivo y del diseño académico vigente; geometrías, rutas y fijaciones siguen siendo supuestos de diseño, no mediciones de campo.
- **Autorización:** la instrucción del usuario identifica los prototipos P1 TR-A y P2 planta A como aprobados y solicita extender su lenguaje físico a las nueve láminas.
- **Decisión:** reemplazar la colección vigente en `08_entrega/ENTREGA_FINAL_INA_CENATE/06_PLANOS_TECNICOS/` por nueve SVG, nueve PDF A3, nueve PNG a 300 ppp y un PDF combinado de nueve páginas; conservar la colección previa, byte a byte, en `08_entrega/HISTORICO_PLANOS_FASE5/`.
- **Coherencia:** A = cinco laboratorios × 32 RJ45 = 160 posiciones asignadas en cuatro paneles de 48, con 32 libres; B = seis × 32 = 192 asignadas en cinco paneles, con 48 libres. Las bocas de panel son pasivas; cordones frontales representativos con extremo libre, sin switches instalados.
- **Óptica:** E1–E3 OS2 24F exterior, vertical OS2 12F; ER-A 4 × 12F + 2 × 24F = 96 fibras en CCH-03U; ER-B 7 × 12F + 2 × 24F = 132 fibras en CCH-04U. Cassettes con conectores integrados, sin duplicar accesorios.
- **Formato y límites:** cotas y recorridos supuestos, plantas sin escala de obra, paso vertical uniforme por U en racks de 42U. No se efectuó impresión física ni validación constructiva.
- **Procedencia:** composición y comprobación asistidas por OpenAI Codex; el estudiante debe revisar y comprender el contenido antes de la entrega académica.
