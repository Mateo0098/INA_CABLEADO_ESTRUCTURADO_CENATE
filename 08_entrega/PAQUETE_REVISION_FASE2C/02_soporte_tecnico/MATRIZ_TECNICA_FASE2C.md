# Matriz técnica consolidada y trazabilidad — Fase 2C

**Fecha de verificación:** 2026-10-25  
**Alcance:** cierre de coherencia entre `MATRIZ_TECNICA_FASE2B.md`, diseños y cálculos; sin precios ni selección comercial definitiva.  
**Responsable de aprobación:** estudiante.  
**Procedencia:** consolidación asistida por OpenAI Codex; especificaciones contrastadas contra documentación oficial del fabricante en la fecha indicada.

## Estados utilizados

- **Producto identificado:** número de parte y parámetros usados aparecen en documentación oficial. No implica disponibilidad local ni aprobación final.
- **Familia identificada:** existe documentación oficial de la familia, pero falta seleccionar housing, capacidad, longitud o variante.
- **Sin referencia verificada:** solo se conserva la función/especificación mínima; no debe copiarse marca o modelo al Excel.
- **Infraestructura por verificar:** dato de campo o elemento civil que no corresponde seleccionar como producto sin levantamiento.

## Trazabilidad diseño–cálculo–material

| ID Fase 2B | Componente y uso en diseño | Figuras que lo usan | Cálculo/cantidad vinculada | Producto/familia | Estado Fase 2C y tratamiento Excel |
|---|---|---|---|---|---|
| MAT-CU-01 | Cable horizontal Cat 6A desde TR a cada RJ45 | PLA-A, PLA-B, LAB-A, LAB-B, TR-A, TR-B | `A_CABLE_COBRE`, `B_CABLE_COBRE` = `N/D` | Panduit `PUP6AHD04BU-G`, Cat 6A U/UTP, CMP, 305 m, Ø nominal 5,8 mm | **Producto identificado.** No trasladar cantidad hasta medir rutas y aprobar desperdicio; clasificación CMP es candidata, no requisito local confirmado. |
| MAT-CU-02 | Terminación de cobre en TR | PLA-A, PLA-B, TR-A, TR-B | 4/TR A; 5/TR B; `TOTAL_PANELES=51` | Panduit NetKey `NK6XPPG48Y`, punchdown Cat 6A, 48 puertos, 2RU | **Producto identificado.** Cantidad provisional por interpretación de área doble y reserva. |
| MAT-CU-03 | Jack RJ45 de salida | LAB-A, LAB-B | `JACKS_CAT6A=1 984` | Panduit Mini-Com TX6A `CJ6X88TGBU`, UTP, 8P8C | **Producto identificado.** Cantidad provisional; compatible con placa Mini-Com, no se usa en el panel punchdown. |
| MAT-CU-04 | Placa de dos módulos en cada área doble | LAB-A, LAB-B | `PLACAS_DOBLES=992` | Panduit `CFPL2WHY`, dos módulos Mini-Com, aparece en guía oficial | **Producto identificado como candidato.** Verificar montaje/caja y disponibilidad antes de adoptar. |
| MAT-CU-05 | Patch cord en puesto de usuario | LAB-A, LAB-B | base funcional `1 984`; longitud pendiente | Panduit UTP28X, modelo oficial `UTP28X7BU` solo como ejemplo de 7 ft | **Familia identificada.** No adoptar modelo/cantidad comercial hasta validar longitud por mobiliario. |
| MAT-CU-06 | Patch cord en rack | TR-A, TR-B | base funcional `1 984`; depende de activos | Panduit UTP28X, longitud/variante pendiente | **Familia identificada.** No trasladar cantidad de compra sin switches y distribución final. |
| MAT-FO-01 | Cable de los tres enlaces exteriores | EXT-01, ER-A, ER-B | 3 cables; `E1_RUTA_BASE=195 m`; E2/E3 y reserva `N/D` | Corning `024EUK-T3601D2M`, 24F OS2, indoor/outdoor, uso oficial en ducto | **Producto identificado.** Solo cantidad de enlaces; no cerrar metros de compra. |
| MAT-FO-02 | Cable independiente de cada ER a TR | ER-A, ER-B, TR-A, TR-B | `CABLES_VERTICAL=11`; desnivel mínimo 94,5 m acumulado, no longitud comprable | Corning `012E81-33131-24`, 12F OS2, OFNR, Ø nominal 6,1 mm | **Producto identificado.** Longitudes por enlace pendientes. |
| MAT-FO-03 | Pigtail LC/UPC simplex como función de terminación | ER-A, ER-B, TR-A, TR-B | 408 pigtails funcionales | Corning `000201G2131002M`, OS2 LC/UPC, 2 m | **Producto alternativo identificado. Compra separada = 0** en la arquitectura provisional de cassette pre-pigtailed. |
| MAT-FO-04 | Adaptador LC dúplex como función de terminación | ER-A, ER-B, TR-A, TR-B | 204 adaptadores funcionales | Corning `ADP-DLCS-CCNRC-CLS`, LC dúplex UPC OS2 | **Producto alternativo identificado. Compra separada = 0** con cassettes pre-pigtailed. |
| MAT-FO-05 | Cassette que integra pigtails, adaptadores y protectores | ER-A, ER-B, TR-A, TR-B | `CASSETTES_CCH_12F=22`; `CASSETTES_CCH_24F=6` | Corning `CCH-CS12-A9-P00RE` y `CCH-CS24-A9-P00RE`, LC dúplex UPC OS2 | **Productos identificados; arquitectura provisional preferida.** Evita duplicar pigtails/adaptadores. Housing CCH aún pendiente. |
| MAT-FO-06 | Housing/ODF que recibe cassettes | ER-A, ER-B, TR-A, TR-B | ER-A 96F; ER-B 132F; ER-P 48F adicionales; cada TR 12F | Familia Corning CCH | **Familia identificada.** No hay número de parte ni cantidad final hasta comprobar slots, RU, entradas y combinación por cuarto. |
| MAT-FO-07 | Patch cord óptico desde cassette/ODF a activo | ER-A, ER-B, TR-A, TR-B | variable por pares activos | OS2 LC/UPC; segundo extremo y longitud pendientes | **Sin referencia verificada para la configuración final.** No trasladar cantidad. |
| MAT-RK-01 | Rack de piso para cada ER/TR | ER-A, ER-B, TR-A, TR-B | escenario máximo 13 unidades | 19 pulgadas, 42U propuesto | **Sin referencia verificada.** Capacidad, fondo, carga y un rack por cuarto no demostrados. |
| MAT-RK-02 | Organización horizontal/vertical | ER-A, ER-B, TR-A, TR-B | ligada a 51 paneles y housings | pendiente | **Sin referencia verificada.** RU ilustrativas, no cantidad de compra. |
| MAT-CA-01 | Ducto exterior existente | EXT-01 | 145 m reportados | no aplica | **Infraestructura por verificar.** No es renglón de compra. |
| MAT-CA-02 | Ducto exterior nuevo | EXT-01 | 50 m propuestos hacia A | diámetro/material pendientes | **Infraestructura por verificar.** No cerrar producto ni diámetro. |
| MAT-CA-03 | Cajas/registros | EXT-01 | 5 + 1 posiciones intermedias teóricas | pendiente | **Infraestructura por verificar.** No son seis unidades comprables sin inspección. |
| MAT-CA-04 | Bandeja y bajantes interiores | PLA-A, PLA-B, LAB-A, LAB-B, TR-A, TR-B | metraje `N/D`; ocupación pendiente | pendiente | **Sin referencia verificada.** Requiere rutas y diámetros reales. |

## Fuentes oficiales verificadas

| Producto/familia | Parámetros utilizados | Fuente oficial |
|---|---|---|
| Panduit `PUP6AHD04BU-G` | Cat 6A U/UTP, CMP, 305 m, Ø 5,8 mm | [Catálogo Panduit Network Infrastructure 2026](https://www.panduit.com/content/dam/panduit/en/corporate-non-product/documents/cpcb331-sa-eng-ni-catalog-2026/web/NI-Sng-Catalog-web-2026-cpcb331.pdf) |
| Panduit `NK6XPPG48Y` | Cat 6A, 48 puertos, 2RU | [Catálogo oficial NetKey](https://www.panduit.com/content/dam/panduit/emea/en/download/NI_Catalog_2021_EMEA_web.pdf) |
| Panduit `CJ6X88TGBU`, `CFPL2WHY`, familia UTP28X | Jack Cat 6A; placa de dos módulos; patch cord Cat 6A | [Guía oficial Panduit Smart Building](https://www.panduit.com/content/dam/panduit/en/website/solutions/applications/documents/smart-building-ebook-web-cpeb12-ww-eng.pdf) |
| Corning `024EUK-T3601D2M` | 24F OS2, loose tube, indoor/outdoor, ducto | [Ficha oficial 24F](https://ecatalog.corning.com/optical-communications/US/en/generate-product-specsheet/024EUK-T3601D2M.pdf?modifiedTS=2026-03-09-04%3A24%3A26) |
| Corning `012E81-33131-24` | 12F OS2, riser OFNR, Ø 6,1 mm | [Ficha oficial 12F](https://ecatalog.corning.com/optical-communications/US/en/generate-product-specsheet/012E81-33131-24.pdf?modifiedTS=2026-02-09-02%3A18%3A56) |
| Corning `000201G2131002M` | Pigtail OS2 LC/UPC simplex, 2 m | [Página oficial del producto](https://ecatalog.corning.com/optical-communications/US/en/c/Standard-Pigtail-Standard-LCUPC-Simplex-SM%2C-SMF-Ultra%2C-1F%2C-Single-Fiber-Riser%2C-Standard-Yellow-Jacket-2-Meters/p/000201G2131002M) |
| Corning `ADP-DLCS-CCNRC-CLS` | Adaptador LC dúplex UPC OS2 | [Ficha oficial del adaptador](https://ecatalog.corning.com/optical-communications/US/en/generate-product-specsheet/ADP-DLCS-CCNRC-CLS.pdf?modifiedTS=2026-03-09-03%3A01%3A05) |
| Corning `CCH-CS12-A9-P00RE` | Cassette 12F LC dúplex UPC OS2, pigtails y protectores incluidos | [Familia oficial CCH](https://www.corning.com/catalog/coc/documents/product-family-specifications/pfss/c/en-US/cch-pigtailed-splice-cassette_NAFTA_AEN.pdf) |
| Corning `CCH-CS24-A9-P00RE` | Cassette 24F, 12 adaptadores LC dúplex, UPC OS2, 24 protectores | [Página oficial del producto](https://ecatalog.corning.com/optical-communications/EMEA/en/Fiber-Optic-Hardware/Panels-Modules-and-Cassettes/CCH-Pigtailed-Splice-Cassette/p/CCH-CS24-A9-P00RE) |

## Decisión provisional de terminación óptica

Para mantener una sola arquitectura material, el escenario Fase 2C usa cassettes CCH pre-pigtailed: 22 de 12 fibras para los once enlaces verticales y seis de 24 fibras para los tres enlaces exteriores, uno por extremo. Los 408 pigtails, 204 adaptadores y 408 protectores/empalmes son controles funcionales **incluidos en esos cassettes**, no renglones adicionales de compra.

Esta decisión sigue provisional hasta seleccionar y verificar housings CCH con capacidad suficiente por cuarto. Si se abandona el cassette pre-pigtailed, deberán reactivarse los renglones separados y recalcular bandejas, paneles y accesorios; nunca se sumarán ambas alternativas.
