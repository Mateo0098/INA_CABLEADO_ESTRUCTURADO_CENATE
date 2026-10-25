# Matriz técnica consolidada — Fase 2D

**Fecha de consulta:** 2026-10-25

**Alcance:** sistema pasivo académico compatible y cantidades/variables vinculadas con `04_calculos/resultados_fase2d.csv`. No contiene precios, proveedores ni equipos activos.

**Aprobación:** todas las cantidades de escenario requieren comprensión y revisión del estudiante. La disponibilidad en Costa Rica no fue verificada.

## Sistema de cobre

| ID | Componente | Referencia candidata verificada | Cantidad o variable | Estado y uso |
|---|---|---|---:|---|
| 2D-CU-01 | Cable horizontal Cat 6A U/UTP CMP, caja 305 m, Ø nominal 5,8 mm | Panduit `PUP6AHD04BU-G` | 229 cajas = 69 845 m comerciales | Escenario geométrico: A 74, B 155. Cubierta CMP es candidata; confirmar ambiente. |
| 2D-CU-02 | Panel punchdown Cat 6A, 48 puertos, 2RU, 19 in | Panduit `NK6XPPG48Y` | 51 paneles | 4 por TR A y 5 por TR B. |
| 2D-CU-03 | Jack UTP Cat 6A Mini-Com, 8P8C | Panduit `CJ6X88TGBU` | 1 984 unidades | Dos por área doble; pendiente confirmación docente. |
| 2D-CU-04 | Placa de dos módulos Mini-Com | Panduit `CFPL2WHY` | 992 unidades | Una por área doble; caja de montaje pendiente. |
| 2D-CU-05 | Patch cord Cat 6A UTP, 28 AWG, 7 ft | Panduit `UTP28X7BU` | 1 984 usuario + 1 984 rack | Capacidad pasiva completa; no equivale a 1 984 puertos activos instalados. |
| 2D-CU-06 | Caja de salida para placa doble | Referencia pendiente | 992 unidades | Cantidad funcional cerrada; tipo y montaje dependen del sitio. |

## Sistema de fibra OS2

| ID | Componente | Referencia candidata verificada | Cantidad o variable | Estado y uso |
|---|---|---|---:|---|
| 2D-FO-01A | Cable OS2 24F indoor/outdoor para E1 | Corning `024EUK-T3601D2M` | 221,55 m | Escenario 145 + 50 m, entradas/reservas y 5 %; verificar ruta. |
| 2D-FO-01B | Mismo cable para E2 | Corning `024EUK-T3601D2M` | `169,05 + 1,05x` m | `x` pendiente; no trasladar cantidad cerrada. |
| 2D-FO-01C | Mismo cable para E3 | Corning `024EUK-T3601D2M` | `16,8 + 1,05y` m | `y` pendiente; no trasladar cantidad cerrada. |
| 2D-FO-02A | Cable vertical OS2 12F OFNR, Ø nominal 6,1 mm | Corning `012E81-33131-24` | 89,25 m en A | Cuatro cortes: 16; 19,5; 23; 26,5 m, más 5 % global. |
| 2D-FO-02B | Mismo cable vertical en B | Corning `012E81-33131-24` | 194,775 m en B | Siete cortes: 16 a 37 m, más 5 % global. |
| 2D-FO-03 | Cassette pre-pigtailed 12F LC dúplex UPC OS2 | Corning `CCH-CS12-A9-P00RE` | 22 unidades | Una por extremo de cada enlace ER–TR. Incluye pigtails/protectores. |
| 2D-FO-04 | Cassette pre-pigtailed 24F LC dúplex UPC OS2 | Corning `CCH-CS24-A9-P00RE` | 6 unidades | Una por extremo de E1/E2/E3. Incluye 12 adaptadores y 24 protectores. |
| 2D-FO-05 | Housing CCH 1U, 2 posiciones | Corning `CCH-01U` | 12 unidades | 11 TR + ER-P; el de ER-P depende de espacio existente. |
| 2D-FO-06 | Housing CCH 3U, 6 posiciones | Corning `CCH-03U` | 1 unidad | ER-A: 4 cassettes 12F + 2 cassettes 24F. |
| 2D-FO-07 | Housing CCH 4U, 12 posiciones | Corning `CCH-04U` | 1 unidad | ER-B: 7 cassettes 12F + 2 cassettes 24F. |
| 2D-FO-08 | Patch cord OS2 LC UPC dúplex–LC UPC dúplex, 3 m | Corning `040402R5120003M` | variable `0..204` | Cantidad igual a pares ópticos activos en ambos extremos; 204 es máximo, no compra cerrada. |
| 2D-FO-09 | Pigtail LC/UPC separado | No comprar en esta arquitectura | 0 | Incluido en cassettes; control contra duplicación. |
| 2D-FO-10 | Adaptador LC dúplex separado | No comprar en esta arquitectura | 0 | Incluido en cassettes; control contra duplicación. |

Los cassettes CCH usan una posición de panel/cassette del housing. El inventario por cuarto es: TR = 1/2 posiciones; ER-P = 2/2; ER-A = 6/6; ER-B = 9/12.

## Racks y organización

| ID | Componente | Referencia candidata verificada | Cantidad | Estado y fundamento |
|---|---|---|---:|---|
| 2D-RK-01 | Gabinete 19 in, 42U, 600 × 1 070 mm | APC/Schneider Electric `AR3100B2` | 13 unidades | 11 TR + ER-A + ER-B. Referencia candidata; capacidad activa, carga y energía siguen pendientes. |
| 2D-RK-02 | Organizador horizontal 1U | APC/Schneider Electric `AR8425A` | 51 unidades | Uno por panel de cobre. |
| 2D-RK-03 | Organizador horizontal 1U | APC/Schneider Electric `AR8425A` | 14 unidades | Uno por housing óptico, incluido ER-P. |
| 2D-RK-04 | Puesta a tierra/equipotencialidad de rack | Referencia pendiente | 13 conjuntos | Función necesaria; selección depende del sistema eléctrico/institucional. |

Control pasivo de RU en cada TR: A = 1U CCH + 8U paneles + 4U organizadores = 13U; B = 1U + 10U + 5U = 16U. El espacio restante no selecciona switches, PDU o UPS.

## Canalización y accesorios

| ID | Componente | Especificación mínima | Cantidad/variable | Estado |
|---|---|---|---:|---|
| 2D-CA-01 | Bandeja interior compartida | Sección por ocupación de cables y soporte del sitio | 1 432,725 m de ruta con 5 % | Longitud de escenario; sección y producto pendientes. |
| 2D-CA-02 | Bajante/tubería protegida | Una por área doble, apta para dos cables Cat 6A | 992 bajantes; 3 124,8 m con 5 % | Longitud de escenario; diámetro y accesorios pendientes. |
| 2D-CA-03 | Caja de salida | Compatible con placa doble y montaje | 992 unidades | Tipo pendiente; no duplicar con placa. |
| 2D-CA-04 | Ducto exterior existente | Capacidad/estado por inspeccionar | 145 m de referencia | Infraestructura, no compra. |
| 2D-CA-05 | Ducto exterior nuevo | Material/diámetro según ocupación y sitio | 50 m propuestos | No cerrar producto hasta confirmar ruta. |
| 2D-CA-06 | Cajas/registros exteriores | Carga, drenaje y dimensiones según sitio | 5 + 1 posiciones teóricas | No son seis unidades de compra sin inspección. |
| 2D-CA-07 | Accesorios de bandeja/tubería | Curvas, uniones, soportes y fijaciones compatibles | variable por trazado/producto | Cantidad no resoluble sin sistema de canalización. |

## Herramientas — escenario de una cuadrilla académica

| Herramienta funcional | Cantidad de referencia | Estado |
|---|---:|---|
| Guía pasacables/juego de tiro | 1 juego | Escenario de una cuadrilla |
| Soportes de bobina | 2 unidades | Par funcional |
| Herramienta de impacto/terminación compatible | 2 unidades | Una por técnico de cobre |
| Juego de corte y pelado de cobre | 2 juegos | Una por técnico de cobre |
| Fusionadora OS2 | 1 unidad | Equipo especializado compartido |
| Cortadora de precisión y peladora de fibra | 1 juego | Equipo especializado compartido |
| Fuente y medidor óptico OS2 | 1 juego | Prueba básica |
| OTDR OS2 | 1 unidad | Sujeto al procedimiento académico |
| Certificador con adaptadores Cat 6A | 1 juego | Calibración vigente requerida |
| Etiquetadora | 1 unidad | Consumibles variables |
| Herramientas de rack y nivel | 1 juego | Cuadrilla única |
| Lubricante de tiro compatible | variable por método | Producto/cantidad pendientes |

## Fuentes oficiales

- Panduit Cat 6A: [catálogo Network Infrastructure 2026](https://www.panduit.com/content/dam/panduit/en/corporate-non-product/documents/cpcb331-sa-eng-ni-catalog-2026/web/NI-Sng-Catalog-web-2026-cpcb331.pdf), [NetKey](https://www.panduit.com/content/dam/panduit/emea/en/download/NI_Catalog_2021_EMEA_web.pdf), [UTP28X7BU](https://www.panduit.com/content/dam/panduit/en/products/media/2/72/172/1172/111431172.pdf).
- Corning cables: [24F `024EUK-T3601D2M`](https://ecatalog.corning.com/optical-communications/US/en/generate-product-specsheet/024EUK-T3601D2M.pdf?modifiedTS=2026-03-09-04%3A24%3A26), [12F `012E81-33131-24`](https://ecatalog.corning.com/optical-communications/US/en/generate-product-specsheet/012E81-33131-24.pdf?modifiedTS=2026-02-09-02%3A18%3A56).
- Corning CCH: [cassettes pre-pigtailed](https://ecatalog.corning.com/optical-communications/US/en/Fiber-Optic-Hardware/Panels-Modules-and-Cassettes/CCH-Pigtailed-Splice-Cassette/p/cch-pigtailed-splice-cassette), [housings CCH](https://www.corning.com/catalog/coc/documents/product-family-specifications/0164_NAFTA_AEN.pdf), [patch cord OS2 LC-LC](https://ecatalog.corning.com/optical-communications/US/en/Fiber-Optic-Cable-Assemblies/Indoor-Cable-Assemblies/Two-Fiber-Indoor-Cable-Assemblies/Fiber-Optic-Jumper%2C-2-F%2C-LC-Duplex-to-LC-Duplex%2C-Zipcord-Cable%2C-Riser%2C-2-0-mm-legs/p/fiber-optic-jumper-2-f-zipcord-lc-duplex-to-lc-duplex-riser-2.0-mm?variant=fiber-category-sm-os2).
- Schneider Electric/APC: [rack `AR3100B2`](https://shop.se.com/pro/us/en/product/apc-netshelter-sx-server-rack-gen-2-42u-1991h-x-600w-x-1070d-mm-with-sides-black-taa/), [organizador `AR8425A`](https://www.se.com/us/en/product/AR8425A/horizontal-cable-organizer-1u/).

## Exclusiones controladas

No se seleccionan switches, transceptores, PDU, UPS ni otros activos. No se duplican pigtails, adaptadores o bandejas de empalme fuera de los cassettes. No se asignan referencias a canalizaciones, cajas o puesta a tierra sin los datos que determinan su compatibilidad.
