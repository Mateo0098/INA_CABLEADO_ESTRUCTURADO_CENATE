# Memoria complementaria de cantidades — Fase 3B

**Fecha:** 2026-10-25
**Alcance:** decisiones adicionales para completar el XLSX de Actividad 1. Conserva como base las entradas y resultados reproducibles de Fase 2D; no reabre esos cálculos.
**Clasificación:** los datos académicos adoptados se muestran como supuestos; los resultados son cálculos de escenario, no mediciones ni compras definitivas.

## 1. Entradas adoptadas

| Entrada | Valor | Clasificación/procedencia |
|---|---:|---|
| Áreas dobles por laboratorio | 16 | Mínimo indicado para ejercicio/docente |
| Puertos por área doble | 2 RJ45 | Supuesto adoptado expresamente para Fase 3B |
| TR | 1 por piso | Supuesto adoptado dentro del mínimo académico |
| Reserva cobre | 3 m/enlace | Supuesto Fase 2D adoptado |
| Desperdicio de cables | 5 % | Supuesto de compra Fase 2D adoptado |
| E1: ducto existente + tramo nuevo | 145 m + 50 m | 145 m reportados por estudiante, sin validación de campo; 50 m propuesta; se adopta E1→ER-A |
| Referencia de espaciamiento exterior | 25 m | Referencia aproximada reportada, no requisito ni medición confirmada |
| x para E2 | 75 m | Supuesto geométrico: 3 intervalos de referencia de 25 m para la extensión desde el corredor compartido supuesto |
| y para E3 | 50 m | Supuesto geométrico: 2 intervalos de referencia de 25 m para un trazado directo entre edificios A/B |
| Cable exterior OS2 24F | Corning `024EUK-T3601D2M` | Candidato verificado en matriz Fase 2D; disponibilidad local no comprobada |

Las plantas y el diagrama exterior son esquemáticos, no están a escala y no suministran separación entre edificios. Por ello, x=75 m e y=50 m son **supuestos académicos explícitos elegidos para cerrar un escenario**, no distancias obtenidas de escala, mediciones o evidencia de campo. El supuesto de 145 m compartidos hacia E2 también debe verificarse en sitio. El estudiante debe reemplazar estos valores si recibe mediciones aceptadas.

## 2. Fibra exterior adoptada para el libro

Con 3 m de recorrido interno y 5 m de reserva por extremo, más 5 % de desperdicio:

- E1: `(145 + 50 + 2×(3+5))×1,05 = 221,55 m` de cable 24F.
- E2: `(145 + 75 + 2×(3+5))×1,05 = 247,8 m` de cable 24F.
- E3: `(50 + 2×(3+5))×1,05 = 69,3 m` de cable 24F.
- Total exterior del escenario: `221,55 + 247,8 + 69,3 = 538,65 m` de cable 24F.

Los resultados utilizan un solo enlace dúplex activo por enlace de fibra: 11 verticales y 3 exteriores. Se computan dos patch cords ópticos por enlace —uno en cada extremo—: `(11+3)×2 = 28 unidades`. Las restantes posiciones del cassette quedan pasivas/no iluminadas; los transceptores no se seleccionan.

## 3. Cantidades trasladadas y canalización preliminar

Se conservan sin recalcular los resultados Fase 2D: 74 cajas Cat 6A de 305 m para A, 155 para B (229 total); 51 paneles; 1 984 jacks; 992 placas/cajas; 1 984 patch cords de usuario y 1 984 de rack; 89,25 m de OS2 12F para A y 194,775 m para B; 22 cassettes 12F; 6 cassettes 24F; 12 `CCH-01U`, uno `CCH-03U`, uno `CCH-04U`; 13 racks propuestos; 51 organizadores de cobre y 14 ópticos.

Para que el libro tenga cantidades expresables sin inventar fabricante:

- Bandeja perforada genérica de 100×50 mm, tramos de 3 m: `REDONDEAR.MAS(1 432,725/3;0)=478 tramos`. Sección preliminar; falta verificar ocupación, carga, soportes y accesorios.
- Bajantes de PVC genérico, diámetro nominal 25 mm, en tramos de 3 m, dos cables Cat 6A por área: `REDONDEAR.MAS(3 124,8/3;0)=1 042 tramos`. Verificar diámetro interior/ocupación contra ficha de producto y montaje final.
- Ducto exterior nuevo genérico, diámetro nominal 50 mm: 50 m propuestos. Verificar destino, ruta, capacidad y llenado con los cables seleccionados.
- Seis posiciones teóricas de registros son una variable de inspección, no una compra de seis cajas.
- Etiquetas genéricas: `1 984 enlaces × 2 extremos = 3 968 etiquetas`, supuesto de identificación; no hay fabricante/modelo seleccionado.
- Pigtails y adaptadores separados: cero unidades, dado que la configuración de cassettes adoptada integra la terminación indicada en la matriz técnica.

Los diámetros y secciones son una solución preliminar genérica solicitada para el escenario, sin marca ni referencia comercial verificada. No debe interpretarse como diseño constructivo, confirmación normativa, validación de llenado ni selección de compra.

## 4. Herramientas y celdas económicas

La hoja `Herramientas` contiene 11 equipos/juegos reutilizables según la cuadrilla académica. El lubricante aparece como consumible variable, no como herramienta, sin cantidad inventada; etiquetas se listan en materiales. No se incorporan modelos o proveedores a las herramientas porque la matriz no los respalda.

Las columnas I y J permanecen vacías. En la copia completada se borra `J43=SUM(J2:J41)` y se cambia su rótulo a **CANTIDADES DE MATERIALES — SIN COSTOS**: la fórmula era un total monetario sin datos económicos y no se agrega ningún monto. El original se mantiene intacto byte a byte.

## 5. Procedencia y limitaciones

El archivo se creó con asistencia de OpenAI Codex a partir de la plantilla original y los artefactos técnicos versionados. El estudiante debe revisar y comprender las hipótesis antes de su uso académico. Las especificaciones comerciales conservan la clasificación y fuentes de la matriz Fase 2D; no se verificaron disponibilidad local ni proveedores. Excel/LibreOffice no están instalados en el entorno de generación: las fórmulas fueron evaluadas contra sus valores en caché mediante el validador reproducible, pero no se observó el recálculo visual en Microsoft Excel.
