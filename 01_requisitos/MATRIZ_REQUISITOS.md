# Matriz de requisitos oficiales INA

- **Fecha de corte:** 2026-10-18
- **Estado:** auditada contra el enunciado original y la actualización docente
- **Fuentes primarias:** F-005 y F-006, definidas en `CONTROL_DE_FUENTES.md`
- **Rúbrica:** no existe una rúbrica independiente; se usan los criterios de revisión y valoración incluidos en F-005

## Convenciones

- `INA-*`: requisito respaldado por una fuente oficial incorporada.
- `CTX-*`: registro contextual histórico de la auditoría inicial.
- Estado **Vigente**: requisito confirmado y aplicable a fases posteriores.
- Estado **Controlado**: requisito ya satisfecho documentalmente en esta fase.
- La matriz registra requisitos; no implica que el diseño, los cálculos o los entregables técnicos ya estén ejecutados.

## Requisitos oficiales

| ID | Requisito fiel resumido | Fuente y sección | Tipo | Entregable | Criterio de comprobación | Estado | Trazabilidad CTX / observaciones |
|---|---|---|---|---|---|---|---|
| INA-001 | Diseñar la infraestructura física de telecomunicaciones de los edificios A y B del CENATE. | F-005, introducción y §1 | Obligatorio / alcance | Proyecto integral | Ambos edificios están cubiertos por diseños, cálculos y Excel | Vigente | CTX-001, CTX-002 |
| INA-002 | Cálculos, especificaciones, diseños y materiales deben mantener coherencia entre sí. | F-005, introducción | Restricción de consistencia | Todos | Auditoría cruzada sin discrepancias | Vigente | CTX-032, CTX-037 |
| INA-003 | Edificio A: 4 pisos, 5 laboratorios por piso, 85 m² por laboratorio. | F-005, §1.1 | Dato oficial | Diseño y cálculo A | Se modelan 4 pisos y 20 laboratorios de 85 m² | Vigente | CTX-004 a CTX-006 |
| INA-004 | Edificio B: 7 pisos, 6 laboratorios por piso, 75 m² por laboratorio. | F-005, §1.2 | Dato oficial | Diseño y cálculo B | Se modelan 7 pisos y 42 laboratorios de 75 m² | Vigente | CTX-009 a CTX-011 |
| INA-005 | Cada edificio nuevo tendrá ER conectado por fibra con el ER principal existente. | F-005, §1.3 | Obligatorio / topología | Backbone exterior y ER | ER A y ER B enlazan con ER principal | Vigente | CTX-008, CTX-013, CTX-019, CTX-025 |
| INA-006 | Los ER A y B deben interconectarse mediante fibra óptica. | F-005, §1.3 | Obligatorio / topología | Backbone exterior | Enlace ER A–ER B individualizado | Vigente | CTX-025 |
| INA-007 | Diseñar los tres enlaces considerando recorrido, distancia, método, tipo de fibra y materiales. | F-005, §1.3 | Obligatorio / diseño | Diseño exterior, cálculos y Excel | Cada enlace documenta los cinco aspectos | Vigente | CTX-025 |
| INA-008 | Cada piso tendrá como mínimo un TR. | F-005, §1.4 | Obligatorio / mínimo | Plantas y backbone vertical | Todos los pisos muestran ≥1 TR | Vigente | CTX-008, CTX-013 |
| INA-009 | Incorporar TR adicionales cuando distancias o distribución lo requieran. | F-005, §1.4 | Condicional / diseño | Plantas y cálculos | Evaluación de cobertura y justificación por piso | Vigente | Complementa CTX-008 y CTX-013 |
| INA-010 | El enlace permanente de cobre no superará 90 m. | F-005, §1.4 | Restricción técnica | Cálculos horizontales | Todos los enlaces permanentes son ≤90 m | Vigente | CTX-026 |
| INA-011 | Cada laboratorio tendrá al menos 16 áreas de trabajo dobles. | F-005, §1.4 y §4.3 | Obligatorio / mínimo | Laboratorios, cálculos y Excel | ≥16 áreas dobles por laboratorio en los tres medios | Vigente | CTX-007, CTX-012 |
| INA-012 | Más de 16 áreas dobles requiere justificación por necesidades del laboratorio. | F-005, §1.4 | Condicional / diseño | Memoria y cálculos | Exceso documentado y justificado | Vigente | Complementa CTX-007 y CTX-012 |
| INA-013 | Dimensionar canalizaciones, salidas, cuartos y componentes según infraestructura y criterios de clase. | F-005, §1.4 | Obligatorio / técnico | Diseño y cálculos | Dimensionamiento trazable y defendible | Vigente | CTX-035, CTX-037 |
| INA-014 | Proveer infraestructura para comunicar los TR de cada piso con el ER del edificio. | F-005, §1.4 | Obligatorio / backbone vertical | Backbone vertical | Cada TR tiene enlace trazado a su ER | Vigente | CTX-028 |
| INA-015 | No contratar, cotizar ni instalar servicio ISP; sí incluir infraestructura interna justificada. | F-005, §1.5 | Restricción de alcance | Excel y memoria | No aparecen servicios ISP | Vigente | CTX-003 |
| INA-016 | Calcular e identificar todos los materiales y equipos necesarios. | F-005, §2 | Obligatorio / cálculo | Excel | Lista completa respaldada por cálculos | Vigente | CTX-037 |
| INA-017 | Calcular A para 4 pisos y 20 laboratorios, incluyendo áreas, TR, ER, canalizaciones y cableado. | F-005, §2.1 | Obligatorio / cálculo | Cálculo y Excel A | Cobertura de todos los subsistemas | Vigente | CTX-003 a CTX-008 |
| INA-018 | Calcular B para 7 pisos y 42 laboratorios, incluyendo áreas, TR, ER, canalizaciones y cableado. | F-005, §2.2 | Obligatorio / cálculo | Cálculo y Excel B | Cobertura de todos los subsistemas | Vigente | CTX-009 a CTX-013 |
| INA-019 | Calcular materiales y equipos de los tres enlaces de fibra. | F-005, §2.3 | Obligatorio / cálculo | Cálculo y Excel backbone | Los tres enlaces tienen cantidades propias | Vigente | CTX-025 |
| INA-020 | Seleccionar y justificar tipo de fibra entre opciones multimodo o monomodo indicadas. | F-005, §2.3 | Decisión técnica | Memoria y Excel | Tipo y justificación documentados | Vigente | Decisión pendiente |
| INA-021 | Determinar fibras, longitud por enlace y reserva de fibra. | F-005, §2.3 | Obligatorio / cálculo | Cálculo backbone | Valores por enlace con fórmula y reserva | Vigente | CTX-024, CTX-025 |
| INA-022 | Incluir distribución, terminación, conectores, adaptadores, accesorios, canalización, soportes y protección óptica. | F-005, §2.3 | Obligatorio / materiales | Excel backbone | Lista cubre cada categoría necesaria | Vigente | CTX-031 |
| INA-023 | Definir instalación aérea, subterránea o mixta y justificarla. | F-005, §2.3 | Decisión técnica | Diseño exterior | Método seleccionado con justificación | Vigente | CTX-022 y CTX-029 son insumos, no decisión final |
| INA-024 | Calcular con unidades apropiadas, recorridos reales, dimensiones, conectores, canalizaciones y reserva/desperdicio. | F-005, §2.4 | Obligatorio / método | Cálculos | Entradas, unidades y porcentajes trazables | Vigente | CTX-037 |
| INA-025 | No aceptar cantidades sin justificación; cálculos y diseños deben coincidir. | F-005, §2.4 | Restricción de calidad | Cálculos, diseños y Excel | Cada cantidad tiene base verificable | Vigente | CTX-032, CTX-037 |
| INA-026 | Presentar herramientas para canalizaciones, cableado, fibra, comprobación/certificación y montaje. | F-005, §3 | Obligatorio / herramientas | Hoja `Herramientas` | Categorías aplicables cubiertas | Vigente | Nuevo respecto de la matriz inicial |
| INA-027 | Las herramientas deben corresponder al método de instalación. | F-005, §3 | Restricción de coherencia | Herramientas y diseño | Relación herramienta–tarea demostrable | Vigente | Nuevo respecto de la matriz inicial |
| INA-028 | Presentar diseño exterior con A, B, edificio existente y los tres enlaces de fibra. | F-005, §4.1 | Obligatorio / gráfico | Imagen exterior | Tres edificios y tres enlaces visibles | Vigente | Parte de CTX-030 |
| INA-029 | El exterior identificará ER, método, canalizaciones/postes/registros, distancias y ayudas gráficas. | F-005, §4.1 | Obligatorio / contenido gráfico | Imagen exterior | Lista visual completa | Vigente | CTX-030, CTX-032 |
| INA-030 | Presentar distribución por piso con laboratorios, TR, canalizaciones y cableado. | F-005, §4.2 | Obligatorio / gráfico | Plantas A y B | Elementos visibles y conectividad comprensible | Vigente | Parte de CTX-030 |
| INA-031 | Se admite una planta típica por edificio solo si sus pisos son idénticos; variaciones requieren imágenes adicionales. | F-005, §4.2 | Condicional / gráfico | Plantas | Declaración de repetición o cobertura de variaciones | Vigente | CTX-015 era supuesto; queda por confirmar |
| INA-032 | La planta debe identificar edificio/piso, 5 o 6 laboratorios, TR y canalizaciones. | F-005, §4.2 | Obligatorio / contenido gráfico | Plantas A y B | Lista visual completa | Vigente | CTX-005, CTX-010, CTX-030 |
| INA-033 | Presentar interior de laboratorios con áreas, salidas, canalizaciones, recorridos y distribución física. | F-005, §4.3 | Obligatorio / gráfico | Laboratorios A y B | Lista visual completa | Vigente | Parte de CTX-030 |
| INA-034 | Se admite un laboratorio típico por edificio si son idénticos; mostrará ≥16 áreas dobles y concordará con cálculos. | F-005, §4.3 | Condicional / gráfico | Laboratorios A y B | Repetición justificada y cantidad coincidente | Vigente | CTX-007, CTX-012, CTX-030 |
| INA-035 | Referencias o imágenes externas deben incluir enlace de fuente. | F-005, §4.3 | Obligatorio / fuente | Imágenes | URL verificable por recurso externo | Vigente | Amplía CTX-036 |
| INA-036 | Diseños en PNG/JPG/JPEG, claros, legibles, completos, sin recortes y no solo descripción escrita. | F-005, §4.4 | Obligatorio / formato | Imágenes | Formato y revisión visual aprobados | Vigente | CTX-030 |
| INA-037 | Imágenes deben coincidir con cantidades y características del Excel. | F-005, §4.4 | Restricción de consistencia | Imágenes y Excel | Auditoría cruzada aprobada | Vigente | CTX-032 |
| INA-038 | Usar obligatoriamente la plantilla Excel adjunta para materiales, equipos y herramientas. | F-005, §5 | Obligatorio / formato | Excel | Entrega parte de la plantilla controlada | Controlado para el original; ejecución pendiente | CTX-033 |
| INA-039 | El Excel final conserva estructura, columnas, orden, encabezados, colores y formatos originales. | F-005, §5 y §5.1 | Restricción documental | Excel | Comparación estructural con original | Vigente | CTX-033 |
| INA-040 | Solo agregar filas necesarias; auxiliares temporales deben eliminarse antes de entregar. | F-005, §5.1 | Restricción documental | Excel | Sin columnas auxiliares en versión final | Vigente | Complementa CTX-033 |
| INA-041 | Completar campos aplicables con especificaciones claras sobre características, capacidad, instalación y compatibilidad. | F-005, §5.2 | Obligatorio / información | Excel | Sin descripciones genéricas | Vigente | CTX-036 |
| INA-042 | Incorporar fórmulas necesarias, automáticas y funcionales; no reemplazar resultados calculables por valores manuales. | F-005, §5.3 | Obligatorio / cálculo | Excel | Pruebas de recálculo exitosas | Vigente | CTX-037 |
| INA-043 | Demostrar y explicar fórmulas y procedimientos durante la presentación. | F-005, §5.3 | Obligatorio / defensa | Exposición | Demostración en vivo comprensible | Vigente | Nuevo respecto de CTX |
| INA-044 | En Actividad 1 no incluir precios, subtotales, costos ni montos; columnas económicas vacías. | F-005, §5.4 | Prohibición | Excel | `I2:J[n]` sin montos económicos | Vigente | CTX-034 |
| INA-045 | Materiales y equipos requieren fuentes confiables, verificables y actualizadas. | F-005, §6 | Obligatorio / evidencia | Excel y fuentes | Fuente válida por producto | Vigente | CTX-036 |
| INA-046 | Se admiten fabricantes, datasheets, distribuidores/proveedores especializados, empresas formales y proformas sin precios. | F-005, §6.1 | Fuentes permitidas | Fuentes técnicas | Origen pertenece a categoría autorizada | Vigente | CTX-036 |
| INA-047 | Se prohíben marketplaces generalistas, redes sociales, clasificados, blogs/foros no verificables e IA como fuente técnica. | F-005, §6.2 | Fuentes prohibidas | Fuentes técnicas | Ninguna fuente cae en categorías prohibidas | Vigente | Corrige alcance de CTX-038 |
| INA-048 | Identificar marca/modelo, enlazar preferiblemente ficha oficial y comprobar especificación, disponibilidad y actualidad. | F-005, §6.3 | Obligatorio / evidencia | Excel y defensa | Verificación por producto documentada | Vigente | CTX-036 |
| INA-049 | Trabajo estrictamente individual: cálculos, selección, Excel, diseños, investigación y defensa propios. | F-005, §7 | Restricción académica | Todos | Autoría y dominio individual | Vigente | Nuevo respecto de CTX |
| INA-050 | No compartir archivos, diseños, cálculos ni listados; similitudes indebidas quedan sujetas a evaluación INA. | F-005, §7 | Prohibición académica | Todos | Sin intercambio de productos | Vigente | Nuevo respecto de CTX |
| INA-051 | Solo pueden coincidir características generales y mediciones/cálculos grupales del 2026-10-13. | F-005, §7.1 | Excepción académica | Datos de entrada | Coincidencias limitadas a categorías autorizadas | Vigente | Los 145/25/50/195 m se registran como datos del estudiante |
| INA-052 | Entrega y presentación el 2026-10-29; no se aceptan entregas anticipadas ni posteriores. | F-005, §8 | Obligatorio / calendario | Entrega | Fecha exacta cumplida | Vigente | CTX-001 |
| INA-053 | Excepciones de plazo requieren justificación respaldada por vía institucional y valoración normativa. | F-005, §8 | Condicional / académico | Gestión de entrega | Evidencia institucional válida | Vigente | Nuevo respecto de CTX |
| INA-054 | IA solo como apoyo conceptual, organizativo, lingüístico, de fórmulas comprendidas y visual. | F-005, §9 y §9.1 | Uso permitido de IA | Proceso | Uso dentro de categorías autorizadas | Vigente | CTX-038 se precisa |
| INA-055 | Imágenes con IA deben representar la propuesta, ser coherentes, claras y técnicamente explicables. | F-005, §9.2 | Condición de IA | Imágenes y defensa | Concordancia y explicación demostrables | Vigente | CTX-032, CTX-038 |
| INA-056 | IA no puede resolver cálculos, generar el Excel, sustituir criterio técnico ni aportar especificaciones no verificadas. | F-005, §9.3 | Uso prohibido de IA | Cálculos, Excel y selección | Evidencia de trabajo propio y fuentes externas válidas | Vigente | Limita futuras sesiones; CTX-038 no autorizaba esto |
| INA-057 | El estudiante responde por el uso de IA y debe comprender y defender todo el contenido. | F-005, §9.4 | Responsabilidad académica | Defensa | Respuestas técnicas propias | Vigente | CTX-038; declaración interna de asistencia sigue como política de trazabilidad |
| INA-058 | Entrega exclusivamente digital; no se aceptan materiales físicos o impresos. | F-005, §10 | Restricción de formato | Entrega | Todos los archivos son digitales | Vigente | Nuevo respecto de CTX |
| INA-059 | Entregar Excel `.xlsx` con fórmulas y estructura original. | F-005, §10.1 | Obligatorio / formato | Excel | Extensión, fórmulas y estructura verificadas | Vigente | CTX-033 |
| INA-060 | Entregar diseños como PNG, JPG o JPEG claramente visualizables. | F-005, §10.2 | Obligatorio / formato | Imágenes | Archivos abren y son legibles | Vigente | CTX-030 |
| INA-061 | Referencias y enlaces deben estar disponibles durante la presentación. | F-005, §10.3 | Obligatorio / defensa | Fuentes | Enlaces accesibles en exposición | Vigente | CTX-036 |
| INA-062 | Identificar claramente archivos; se recomiendan nombres con estudiante y tipo de archivo. | F-005, §10.4 | Obligatorio + recomendación | Entrega | Archivos reconocibles | Vigente | Nuevo respecto de CTX |
| INA-063 | Presentar y defender individualmente ante la clase durante mínimo 8 minutos efectivos. | F-005, §11 y §11.4 | Obligatorio / defensa | Exposición | Cronometraje ≥8 min, sin contar preparación técnica | Vigente | Nuevo respecto de CTX |
| INA-064 | Explicar y justificar usando directamente Excel e imágenes; no limitarse a mostrar o leer. | F-005, §11 | Obligatorio / defensa | Exposición | Relación técnica explicada | Vigente | Nuevo respecto de CTX |
| INA-065 | Mostrar organización, especificaciones, cantidades por edificio, fibra, fórmulas, reservas y fuentes. | F-005, §11.1 | Obligatorio / defensa | Exposición Excel | Lista completa cubierta | Vigente | Nuevo respecto de CTX |
| INA-066 | Mostrar y explicar exterior, plantas y laboratorios con elementos identificables. | F-005, §11.2 | Obligatorio / defensa | Exposición de imágenes | Todas las categorías explicadas | Vigente | CTX-030 |
| INA-067 | Poder justificar ER/TR, áreas, recorridos, canalizaciones, fibra, materiales, ANSI/TIA y fórmulas. | F-005, §11.3 | Obligatorio / defensa | Exposición | Respuestas técnicas fundamentadas | Vigente | No especifica ediciones normativas concretas |
| INA-068 | Evidenciar dominio; la exposición no puede ser lectura ni admitir desconocimiento del trabajo. | F-005, §11.3 | Criterio de evaluación | Exposición | Comprensión demostrada | Vigente | Nuevo respecto de CTX |
| INA-069 | Verificar que Excel, fórmulas, imágenes, textos y versión final funcionen; mantener respaldo. | F-005, §11.5 | Obligatorio + recomendación | Entrega y defensa | Prueba de apertura y legibilidad | Vigente | Nuevo respecto de CTX |
| INA-070 | Ejecutar revisión previa de completitud, cálculos, coherencia, límites, compatibilidad, duplicados, herramientas, fuentes, Excel, precios, imágenes y exposición. | F-005, §12 | Control obligatorio | Auditoría final | Lista de §12 aprobada | Vigente | Consolida controles CTX-026, CTX-032 a CTX-037 |
| INA-071 | La valoración considera calidad técnica, precisión, selección, fuentes, coherencia y defensa; aplicar conocimientos y ANSI/TIA estudiadas. | F-005, §13 | Criterio de evaluación | Proyecto y defensa | Evidencia integral en entrega | Vigente | Criterios del enunciado usados ante ausencia de rúbrica separada |
| INA-072 | Presentar imagen del ER A con llegadas ópticas, equipos, rack/accesorios, patch cords, pigtails y canalización vertical. | F-006, ER e imágenes adicionales | Obligatorio / gráfico | Imagen ER A | Lista visual completa y coherente | Vigente | Parte de CTX-030 y CTX-031 |
| INA-073 | Presentar imagen del TR A con backbone desde ER, rack/equipos, patch cords, pigtails y canalizaciones a áreas. | F-006, TR e imágenes adicionales | Obligatorio / gráfico | Imagen TR A | Lista visual completa y coherente | Vigente | Parte de CTX-030 y CTX-031 |
| INA-074 | Presentar imagen del ER B con llegadas ópticas, equipos, rack/accesorios, patch cords, pigtails y canalización vertical. | F-006, ER e imágenes adicionales | Obligatorio / gráfico | Imagen ER B | Lista visual completa y coherente | Vigente | Parte de CTX-030 y CTX-031 |
| INA-075 | Presentar imagen del TR B con backbone desde ER, rack/equipos, patch cords, pigtails y canalizaciones a áreas. | F-006, TR e imágenes adicionales | Obligatorio / gráfico | Imagen TR B | Lista visual completa y coherente | Vigente | Parte de CTX-030 y CTX-031 |
| INA-076 | Las cuatro imágenes ER/TR deben coincidir con materiales, equipos, cantidades, canalizaciones, diseño y Excel. | F-006, cierre | Restricción de consistencia | Imágenes ER/TR y Excel | Auditoría cruzada aprobada | Vigente | CTX-032 |

## Trazabilidad histórica de requisitos contextuales

| CTX | Resolución tras fuentes oficiales |
|---|---|
| CTX-001–CTX-003 | Confirmados por INA-001, INA-015 y INA-052. |
| CTX-004–CTX-013 | Confirmados por INA-003, INA-004, INA-008, INA-009 e INA-011; “área doble” no se define más allá del término oficial. |
| CTX-014–CTX-018 | Permanecen como supuestos del estudiante: geometrías, plantas rectangulares, pasillo, repetición, ubicaciones, dimensiones y alturas no aparecen en F-005/F-006. |
| CTX-019 | Confirmado por INA-005: existe un ER principal en edificio existente; su ubicación física sigue pendiente. |
| CTX-020–CTX-024 | Reclasificados como información del estudiante F-007; 145 m, 25 m, 50 m y 195 m no aparecen en F-005/F-006. |
| CTX-025–CTX-026 | Confirmados por INA-005 a INA-007 e INA-010. |
| CTX-027 | La estrella horizontal no se enuncia expresamente; permanece como criterio de diseño por validar/aplicar con las normas estudiadas. |
| CTX-028 | Confirmado por INA-014 y reforzado por F-006. |
| CTX-029 | Bandejas y derivaciones protegidas siguen como supuesto; INA-013 e INA-023 exigen dimensionar y justificar el método. |
| CTX-030–CTX-032 | Precisados: F-005 exige cinco imágenes mínimas base y F-006 agrega cuatro ER/TR; total mínimo operativo de nueve, sujeto a imágenes extra si existen variaciones. |
| CTX-033–CTX-034 | Confirmados por INA-038 a INA-044 e INA-059. |
| CTX-035 | Se mantiene como regla interna de trazabilidad; no es requisito textual del INA. |
| CTX-036–CTX-037 | Confirmados y ampliados por INA-002, INA-024, INA-025 e INA-041 a INA-048. |
| CTX-038 | Precisado por INA-054 a INA-057: IA puede apoyar, pero no calcular, generar Excel, sustituir criterio ni servir de fuente técnica. La declaración de asistencia es política interna del repositorio, no exigencia textual de F-005. |

## Información de campo separada de requisitos oficiales

Fuente F-007, proporcionada por el estudiante:

- 145 m de canalización subterránea existente.
- Separación de referencia de 25 m entre cajas.
- 50 m adicionales de canalización subterránea propuesta.
- 195 m de recorrido físico preliminar hasta uno de los ER nuevos (`145 + 50`).

Estos datos pueden alimentar INA-007, INA-021, INA-023, INA-024 e INA-029, pero no se atribuyen al enunciado ni a la actualización docente.
