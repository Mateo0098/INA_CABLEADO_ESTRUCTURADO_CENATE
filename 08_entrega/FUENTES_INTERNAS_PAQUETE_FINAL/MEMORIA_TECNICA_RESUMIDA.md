# Memoria técnica resumida — Actividad de Comprobación N.º 1

**Curso:** ELTT12000 — Presupuesto de la red  
**Institución:** INA CENATE  
**Fecha de entrega:** 2026-10-29  
**Versión:** paquete final Fase 4, 2026-10-25

## Alcance y arquitectura

La propuesta organiza la infraestructura pasiva de dos edificios académicos. El edificio A considera 4 pisos, 5 laboratorios por piso y 85 m² por laboratorio. El edificio B considera 7 pisos, 6 laboratorios por piso y 75 m² por laboratorio. Cada laboratorio se representa con 16 áreas de trabajo dobles. Se propone un TR por piso y un ER propio por edificio. Los dibujos son esquemáticos y no están a escala.

El cableado horizontal Cat 6A se plantea en estrella desde los paneles de cada TR hacia cada área. El backbone vertical OS2 de 12 fibras enlaza cada ER con los TR de su edificio. Para las tres interconexiones exteriores se representa cable OS2 de 24 fibras. La selección de un circuito dúplex activo por enlace es un supuesto de escenario; las fibras restantes no se consideran iluminadas.

## Cantidades del escenario incluidas en el Excel

| Concepto | Cantidad | Base y clasificación |
|---|---:|---|
| Cable Cat 6A | 229 cajas de 305 m | Resultado calculado: 74 para A y 155 para B; incluye el 5 % de desperdicio supuesto. |
| Enlaces horizontales / jacks | 1 984 | Resultado calculado suponiendo 2 RJ45 por cada una de las 992 áreas dobles. |
| Placas y cajas de salida | 992 de cada una | Resultado calculado bajo el mismo supuesto de 16 áreas dobles por laboratorio. |
| Patch cords de cobre | 1 984 en usuario y 1 984 en rack | Cantidad de escenario, uno por extremo de cada enlace. |
| Paneles Cat 6A de 48 puertos | 51 | Resultado calculado: 4 por cada uno de los 4 TR de A y 5 por cada uno de los 7 TR de B. |
| Fibra OS2 24F exterior | E1 221,55 m; E2 247,8 m; E3 69,3 m | Resultados calculados con los recorridos supuestos detallados abajo. Total: 538,65 m. |
| Fibra OS2 12F vertical | A 89,25 m; B 194,775 m | Resultados calculados del escenario geométrico Fase 2D, no mediciones. |
| Cassettes de fibra | 22 de 12F y 6 de 24F | Resultado calculado a razón de dos cassettes por cable/enlace considerado. |
| Patch cords ópticos | 28 | Supuesto de 1 circuito LC dúplex activo en cada uno de 14 enlaces, dos cords por enlace. |
| Racks propuestos | 13 | Escenario de 1 rack por ER/TR; tamaño y capacidad final pendientes. |
| Bandeja genérica 100 × 50 mm, tramos de 3 m | 478 tramos | Resultado calculado de escenario; ocupación, cargas, soportes y accesorios pendientes. |
| Bajante PVC genérica, Ø nominal 25 mm, tramos de 3 m | 1 042 tramos | Resultado calculado bajo dos cables por área y 5 %; diámetro interior y llenado pendientes. |
| Ducto exterior genérico, Ø nominal 50 mm | 50 m | Propuesta reportada, ruta, destino y capacidad sin validación de campo. |
| Etiquetas | 3 968 | Supuesto de dos por cada uno de 1 984 enlaces. |
| Pigtails y adaptadores separados | 0 | La arquitectura adoptada considera cassette integrado; no duplicar terminaciones. |

## Fórmulas y supuestos principales

- Enlaces: `(4 × 5 + 7 × 6) × 16 × 2 = 1 984`; requiere confirmar la interpretación de dos salidas RJ45 por área doble.
- Cajas de cobre: `REDONDEAR.MAS(22 428 / 305; 0) + REDONDEAR.MAS(47 028,24 / 305; 0) = 229`. Los metrajes base provienen del escenario geométrico previo; 3 m de reserva por enlace y 5 % de desperdicio son supuestos.
- Fibra exterior OS2 24F: E1 `(145 + 50 + 2 × (3 + 5)) × 1,05 = 221,55 m`; E2 `(145 + 75 + 16) × 1,05 = 247,8 m`; E3 `(50 + 16) × 1,05 = 69,3 m`. Los 145 m fueron reportados por el estudiante, 50 m propuestos, x = 75 m e y = 50 m son supuestos; ninguno está confirmado por medición de campo.
- Fibra vertical: A `(16 + 19,5 + 23 + 26,5) × 1,05 = 89,25 m`; B `(16 + 19,5 + 23 + 26,5 + 30 + 33,5 + 37) × 1,05 = 194,775 m`.
- Canalizaciones: bandeja `REDONDEAR.MAS((472 + 892,5) × 1,05 / 3; 0) = 478`; bajantes `REDONDEAR.MAS(992 × 3 × 1,05 / 3; 0) = 1 042`. Son cantidades preliminares genéricas, no selección constructiva.

## Clasificación, limitaciones y procedencia

Los datos de pisos, laboratorios, áreas y mínimo de áreas de trabajo corresponden al escenario académico documentado en los archivos fuente del proyecto. Geometrías, recorridos, reservas, desperdicio, dos RJ45 por área, canalizaciones y activación dúplex son supuestos de diseño. Las cantidades son resultados calculados y no mediciones ni autorización de compra. No se incorporan precios.

No hay mediciones de campo en este paquete. Deben comprobarse en sitio las rutas, ductos, cajas, distancias y destino de E1; también deben validarse las dimensiones, ocupación/capacidad de canalizaciones y configuración final de racks. Las canalizaciones genéricas no constituyen una especificación verificada de fabricante. No se seleccionan equipos activos ni transceptores.

El libro y los esquemas fueron preparados con asistencia de OpenAI Codex. El estudiante debe revisar las reglas académicas aplicables, comprobar las fuentes oficiales, entender fórmulas y supuestos, y aprobar personalmente el contenido antes de presentarlo.
