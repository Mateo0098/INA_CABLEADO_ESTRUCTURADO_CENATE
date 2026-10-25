# Matriz técnica de materiales candidatos — Fase 2B

**Fecha de consulta:** 2026-10-25  
**Responsable de revisión final:** estudiante  
**Alcance:** candidatos técnicos sin precios ni selección comercial definitiva. Las fuentes son páginas o fichas oficiales del fabricante; la disponibilidad local y la compatibilidad integral siguen pendientes.  
**Procedencia:** estructura y preselección asistidas por OpenAI Codex; toda adopción requiere revisión humana conforme a INA-045 a INA-048 e INA-056.

## Componentes pasivos

| ID | Componente / función | Especificación mínima de diseño | Marca y modelo candidato verificado | Fuente oficial | Cantidad o variable vinculada | Estado de validación |
|---|---|---|---|---|---|---|
| MAT-CU-01 | Cable horizontal de cobre | Cat 6A U/UTP, 4 pares, 23 AWG; cubierta y clasificación según ambiente real | Panduit TX6A, `PUP6AHD04BU-G` | [Panduit — Category 6A Copper Cable](https://www.panduit.com/en/products/featured-products/category-6a-copper-cable.html) | `A_CABLE_COBRE + B_CABLE_COBRE` en m cable; actualmente `N/D` | Especificación del candidato verificada; longitud, cubierta aplicable y presentación comercial pendientes |
| MAT-CU-02 | Terminación de cobre en TR | Panel Cat 6A, 48 puertos, 2RU, montaje 19 pulgadas | Panduit NetKey `NK6XPPG48Y` | [Panduit — NetKey Patch Panels, ficha oficial](https://www.panduit.com/content/dam/panduit/en/products/media/8/78/678/0678/61760678.pdf) | 51 paneles provisionales: A=16, B=35 | Modelo/capacidad verificados; compatibilidad con cable/jacks, puesta a tierra y disponibilidad pendientes |
| MAT-CU-03 | Jack de salida RJ45 | Cat 6A UTP, 8 posiciones/8 hilos, compatible con placa y sistema elegido | Panduit Mini-Com TX6A `CJ6X88TGBU` | [Panduit — catálogo oficial de infraestructura](https://distributorportal.panduit.com/content/dam/panduit/en/support/catalogs/Network-Infrastructure-Enterprise-Catalog-EMEA-NCCB94.pdf) | `JACKS_CAT6A` = 1 984 provisionales | Modelo y Cat 6A verificados; color, placa, herramienta y sistema completo pendientes |
| MAT-CU-04 | Placa/caja para área doble | Dos posiciones RJ45, identificación y montaje compatibles | Pendiente | — | `PLACAS_DOBLES` = 992 provisionales | No seleccionar hasta verificar placa, caja, jack y canalización como sistema |
| MAT-CU-05 | Patch cord de usuario | Cat 6A, longitud según mobiliario, compatible con canal | Pendiente | — | `PATCH_CORD_COBRE_USUARIO` = 1 984 provisionales | Longitud/modelo pendientes |
| MAT-CU-06 | Patch cord de rack | Cat 6A, longitud según orden del rack, compatible con canal | Pendiente | — | `PATCH_CORD_COBRE_RACK` = 1 984 provisionales | Depende de equipos activos y distribución final del rack |
| MAT-FO-01 | Cable exterior por ducto | OS2, 24 fibras, apto para ducto exterior y condiciones ambientales verificadas | Corning `024EUK-T3601D2M` | [Corning — ficha oficial 24F OS2](https://ecatalog.corning.com/optical-communications/US/en/generate-product-specsheet/024EUK-T3601D2M.pdf) | 3 cables; longitudes `L_E1`, `L_E2`, `L_E3` pendientes | Conteo/tipo/uso en ducto del candidato verificados; ruta, reserva, transición y disponibilidad pendientes |
| MAT-FO-02 | Cable vertical ER–TR | OS2, 12 fibras, clasificación riser interior | Corning MIC Riser `012E81-33131-24` | [Corning — ficha oficial 12F OS2](https://ecatalog.corning.com/optical-communications/CALA/es_CO/Cables-de-fibra-%C3%B3ptica/Interno/Cables-Riser-internos/Cable-tight-buffered-MIC%C2%AE%2C-Riser/p/012E81-33131-24) | 11 cables independientes; longitudes por piso pendientes | Conteo/OS2/riser verificados; recorrido, reserva y método de terminación pendientes |
| MAT-FO-03 | Pigtail para terminación por fusión | OS2, LC/UPC simplex, longitud y cubierta compatibles con ODF | Corning `000201G2131002M` | [Corning — pigtail LC/UPC OS2 oficial](https://ecatalog.corning.com/optical-communications/US/en/c/Standard-Pigtail-Standard-LCUPC-Simplex-SM%2C-SMF-Ultra%2C-1F%2C-Single-Fiber-Riser%2C-Standard-Yellow-Jacket-2-Meters/p/000201G2131002M) | 408 si se terminan todas las fibras de ambos extremos | Producto verificado; cantidad provisional y compatibilidad de cassette/ODF pendientes |
| MAT-FO-04 | Adaptador óptico | LC dúplex, UPC, OS2, interior | Corning `ADP-DLCS-CCNRC-CLS` | [Corning — adaptador LC dúplex OS2 oficial](https://ecatalog.corning.com/optical-communications/US/en/Fiber-Optic-Connectivity/Adapters/Fiber-Optic-Adapters/p/ADP-DLCS-CCNRC-CLS) | 204 adaptadores provisionales | Producto verificado; montaje en panel y cantidad final pendientes |
| MAT-FO-05 | Bandeja/cassette de empalme | Capacidad coherente con fibras, pigtails, protectores y panel | Pendiente; Corning CCH solo como familia a evaluar | [Corning — CCH Pigtailed Splice Cassette](https://ecatalog.corning.com/optical-communications/US/en/Fiber-Optic-Hardware/Panels-Modules-and-Cassettes/CCH-Pigtailed-Splice-Cassette/p/cch-pigtailed-splice-cassette?variant=adapter-type-lc-duplex&variant=fiber-category-sm-os2) | Vinculada a 408 empalmes provisionales | Familia verificada; no se fija modelo/cantidad hasta definir housings y agrupación |
| MAT-FO-06 | ODF/panel de distribución | ER A ≥96 posiciones; ER B ≥132; ER principal ≥48 adicionales; cada TR 12 | Pendiente | — | Capacidades por cuarto, no una compra única | Bloqueado por selección de familia, RU, entradas de cable y bandejas |
| MAT-FO-07 | Patch cord óptico | OS2 LC/UPC dúplex; longitud y segundo conector según activo | Pendiente | — | Variable por pares efectivamente activados | No equiparar fibras terminadas con transceptores o patch cords activos |
| MAT-RK-01 | Rack de piso | 19 pulgadas; 42U como alternativa inicial; fondo/carga/acceso compatibles | Pendiente | — | 13 provisionales: 2 ER + 11 TR, sujeto a capacidad | 42U es hipótesis; no se ha demostrado un rack por cuarto ni seleccionado modelo |
| MAT-RK-02 | Organizadores horizontales/verticales | Compatibles con Cat 6A, radios de curvatura y ocupación | Pendiente | — | En función de 51 paneles y diseño final de rack | Cantidad y RU pendientes |
| MAT-CA-01 | Ducto exterior existente | Capacidad útil, continuidad y estado verificados | No aplica | Evidencia de campo pendiente | 145 m de ducto reportado; no comprar | No verificado físicamente |
| MAT-CA-02 | Ducto exterior nuevo | Material/diámetro según cables, ocupación, protección y sitio | Pendiente | — | 50 m propuestos hacia A; destino/ruta por confirmar | No seleccionar diámetro sin datos de cables y criterio aplicable |
| MAT-CA-03 | Cajas/registros | Dimensiones, carga, drenaje, acceso y separación según ruta real | Pendiente | — | Posiciones teóricas: 5 en 145 m y 1 en 50 m | No son cantidades de compra; inspección y diseño civil pendientes |
| MAT-CA-04 | Bandeja interior y bajantes | Capacidad calculada por diámetros reales y cantidad simultánea de cables | Pendiente | — | Metros por medir; rutas visibles en SVG | Sin dimensión ni metraje definitivo |

## Equipos activos y energía

Los switches, transceptores, UPS, PDU, ventilación y puesta a tierra no se seleccionan en esta etapa. El número de posiciones pasivas (1 984 RJ45 y 408 terminaciones individuales de fibra) **no determina por sí solo** la cantidad de puertos activos. Los SVG reservan espacio y lo rotulan como pendiente.

## Herramientas por método propuesto

| Tarea | Herramienta funcional requerida | Cantidad de referencia | Estado |
|---|---|---:|---|
| Preparación de canalización | Guía pasacables, lubricante compatible, mandril/elemento de comprobación y elementos de tiro | 1 juego por cuadrilla | Modelo pendiente |
| Tendido de cobre | Soportes de bobina, guía y control de tensión/radio | 1 juego por cuadrilla | Modelo pendiente |
| Terminación Cat 6A | Herramienta compatible con el jack/panel seleccionado y cortador/pelador | 1 juego por técnico | Depende del sistema final |
| Fibra por fusión | Fusionadora, cortadora de precisión, peladora, alcohol y consumibles aprobados | 1 juego especializado | Modelo/calibración pendientes |
| Comprobación óptica | Fuente y medidor compatibles con OS2; OTDR cuando corresponda al procedimiento | 1 juego | Procedimiento/modelo pendientes |
| Certificación de cobre | Certificador de cableado con adaptadores de enlace permanente Cat 6A vigentes | 1 juego | Modelo/calibración pendientes |
| Montaje de rack | Herramientas manuales aisladas/apropiadas, nivel, etiquetadora y torquímetro cuando aplique | 1 juego | Detalle pendiente |

No se incorporan precios, proveedores comerciales ni cantidades cerradas de herramientas sin definir cuadrilla y procedimiento de instalación.
