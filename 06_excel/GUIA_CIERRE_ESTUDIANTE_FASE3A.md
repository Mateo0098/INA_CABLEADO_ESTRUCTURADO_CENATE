# Guía de cierre del Excel INA — Fase 3A

**Fecha:** 2026-10-25
**Estado del libro:** no existe una copia completada por el estudiante en el repositorio. El original y `Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx` siguen intactos; ambos aún contienen ejemplos didácticos. Esta guía no es el libro final.

## 1. Archivos de referencia y regla de transferencia

- Original inmutable: `06_excel/Plantilla Actividades de comprobación.xlsx`.
- Copia provisional intacta: `06_excel/Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx`.
- Materiales, especificaciones, fórmulas y acciones por fila: `06_excel/PLAN_FILAS_MATERIALES_FASE2D.csv`.
- Herramientas y cantidades por fila: `06_excel/PLAN_FILAS_HERRAMIENTAS_FASE2D.csv`.
- Fundamento numérico: `04_calculos/MEMORIA_CALCULOS_FASE2D.md` y `04_calculos/resultados_fase2d.csv`.
- Estado de candidatos: `05_materiales/MATRIZ_TECNICA_FASE2D.md`.

Crear un archivo nuevo desde la plantilla controlada. Trasladar manualmente únicamente las filas que el estudiante acepte y pueda explicar. Mantener las hojas `Cotización técnica` y `Herramientas`, encabezados, columnas y colores existentes. No agregar precios ni costos. Las cantidades de escenario no son mediciones ni órdenes de compra.

## 2. Materiales — guía por fila

Las fórmulas de esta tabla son fórmulas de comprobación para introducir en la columna G solo cuando la condición de la fila esté resuelta. En Excel en español, usar `REDONDEAR.MAS(...;0)` donde corresponda. Las referencias candidatas provienen de la matriz técnica Fase 2D y sus fuentes de fabricante enlazadas; son candidatas, no selección de compra.

| Fila | Componente y especificación | Cantidad / fórmula comprobable / unidad | Estado | Acción para finalizar |
|---:|---|---|---|---|
| 2 | Cable horizontal Cat 6A U/UTP CMP, caja de 305 m; Panduit `PUP6AHD04BU-G` | A: `REDONDEAR.MAS(22428/305;0)=74`; B: `REDONDEAR.MAS(47028,24/305;0)=155`; total 229 cajas | Condicionado a geometría, 3 m de reserva/enlace y 5 % de desperdicio; verificar ambiente CMP | Aceptar/ajustar el escenario y justificar la cubierta para el ambiente. No redondear el total agregado en lugar de cada edificio. |
| 3 | Panel Cat 6A, 48 puertos, 2RU, 19 in; Panduit `NK6XPPG48Y` | `(4 pisos × 4 paneles/TR) + (7 × 5)=51 paneles` | Condicionado a 2 RJ45 por área doble y reserva adoptada | Confirmar interpretación docente y asignación de puertos por TR. |
| 4 | Jack Cat 6A Mini-Com 8P8C; Panduit `CJ6X88TGBU` | `(4×5 + 7×6) laboratorios/piso × 16 áreas/lab × 2 RJ45/área = 1 984 unidades` | Condicionado; 2 RJ45/área doble pendiente de docente | Obtener confirmación docente; si difiere, corregir modelo y cantidades relacionadas antes de copiar. |
| 5 | Placa de dos módulos Mini-Com; Panduit `CFPL2WHY` | `(4×5 + 7×6) × 16 = 992 unidades` | Condicionado a 16 áreas dobles mínimas y distribución asumida | Confirmar montaje/compatibilidad en sitio y trasladar solo con los jacks aceptados. |
| 6 | Caja de salida doble, compatible con placa/montaje; referencia no seleccionada | `992 áreas × 1 caja/área = 992 unidades` | Cantidad funcional condicionada; tipo pendiente | Determinar montaje de superficie/empotrado y seleccionar una caja compatible. No inventar marca/modelo. |
| 7 | Patch cord cobre de usuario Cat 6A UTP 28 AWG, 7 ft; Panduit `UTP28X7BU` | `1 984 enlaces × 1 = 1 984 unidades` | Capacidad pasiva de escenario | Revisar longitud contra mobiliario y ubicación de tomas. |
| 8 | Patch cord cobre de rack Cat 6A UTP 28 AWG, 7 ft; Panduit `UTP28X7BU` | `1 984 enlaces × 1 = 1 984 unidades` | Capacidad pasiva completa; no significa puertos activos instalados | Revisar longitud/organización de rack. Mantener separado de equipos activos. |
| 9 | Cable exterior OS2 24F para E1; Corning `024EUK-T3601D2M` | `(145 m + 50 m + 2×(3+5) m)×1,05=221,55 m de cable` | Escenario condicionado a que 145+50 m sean E1 | Confirmar destino y recorrido. Distinguir m de ducto de m de cable. |
| 10 | Cable exterior OS2 24F para E2; misma referencia candidata | `(145+x+16)×1,05 = 169,05+1,05x m` | Pendiente: `x` no medido/aceptado | Dejar G sin cantidad hasta registrar longitud aprobada de `x`; no estimar. |
| 11 | Cable exterior OS2 24F para E3; misma referencia candidata | `(y+16)×1,05 = 16,8+1,05y m` | Pendiente: `y` no medido/aceptado | Dejar G sin cantidad hasta registrar longitud aprobada de `y`; no estimar. |
| 12 | Cable vertical OS2 12F OFNR, Corning `012E81-33131-24` | `(16+19,5+23+26,5)×1,05=89,25 m` | Escenario geométrico condicionado a 3,5 m/piso y reservas | Aceptar altura, recorridos internos, reservas y desperdicio; no presentarlo como medición. |
| 13 | Mismo cable vertical OS2 12F para B | `(16+19,5+23+26,5+30+33,5+37)×1,05=194,775 m` | Escenario geométrico condicionado | Igual que fila 12. |
| 14 | Cassette CCH preterminado 12F LC dúplex UPC OS2; Corning `CCH-CS12-A9-P00RE` | `11 enlaces ER–TR × 2 extremos = 22 cassettes` | Arquitectura provisional coherente; compatible como escenario | Revisar conectividad/extremos y mantener pigtails/adaptadores integrados; no comprarlos aparte. |
| 15 | Cassette CCH preterminado 24F LC dúplex UPC OS2; Corning `CCH-CS24-A9-P00RE` | `3 enlaces exteriores × 2 extremos = 6 cassettes` | Arquitectura provisional; E2/E3 físicos pendientes | Revisar ruta/terminación de los tres enlaces; no duplicar componentes incluidos. |
| 16 | Housing CCH 1U, 2 posiciones; Corning `CCH-01U` | `11 TR + 1 ER-P = 12 unidades` | Condicionado; ER-P depende de espacio y compatibilidad existentes | Confirmar capacidad/espacio en ER-P; los once TR corresponden al escenario por piso. |
| 17 | Housing CCH 3U, 6 posiciones; Corning `CCH-03U` | `1 unidad`; ER-A ocupa 6 posiciones (4 cassettes 12F + 2 de 24F) | Propuesta compatible por capacidad | Confirmar montaje/espacio del ER-A. |
| 18 | Housing CCH 4U, 12 posiciones; Corning `CCH-04U` | `1 unidad`; ER-B ocupa 9 posiciones (7 cassettes 12F + 2 de 24F) | Propuesta compatible por capacidad | Confirmar montaje/espacio del ER-B. |
| 19 | Patch cord óptico OS2 LC/UPC dúplex, 3 m; Corning `040402R5120003M` | `PARES_OPTICOS_ACTIVOS_EXTREMOS`; rango `0–204 unidades` | Pendiente de transceptores/pares activos | No cerrar cantidad hasta definir pares activos; 204 es máximo teórico. |
| 20 | Gabinete 19 in, 42U, 600×1 070 mm; APC/Schneider `AR3100B2` | `11 TR + 2 ER nuevos = 13 unidades` | Propuesta; activos, carga, energía, ventilación y espacio pendientes | Comprobar dimensiones/carga/servicios con diseño de cuartos; ER-P no se duplica. |
| 21 | Organizador horizontal 1U; APC/Schneider `AR8425A` | `51 paneles × 1 = 51 unidades` | Derivado de un organizador por panel | Confirmar distribución física y RU por rack. |
| 22 | Organizador horizontal 1U; APC/Schneider `AR8425A` | `12+1+1 housings = 14 unidades` | Derivado de un organizador por housing | Confirmar acomodo por cuarto; el conteo incluye housing ER-P sujeto a revisión. |
| 23 | Conjunto de equipotencialidad/puesta a tierra de rack; sin referencia | `11 TR+2 ER nuevos = 13 conjuntos` | Función/cantidad de escenario; referencia y solución institucional pendientes | Consultar sistema eléctrico/institucional y especificar conjunto compatible; dejar sin modelo hasta entonces. |
| 24 | Bandeja interior compartida; sección/producto no seleccionado | `(472+892,5)×1,05=1 432,725 m` de longitud de escenario | Longitud calculada; sección, ocupación, soportes y producto pendientes | Mantener longitud en memoria; no cerrar fila como compra hasta dimensionar sección y accesorios. |
| 25 | Bajante/tubería protegida para dos cables Cat 6A; diámetro/producto no seleccionado | `992 áreas×3 m×1,05=3 124,8 m`; 992 bajantes | Longitud calculada; diámetro/accesorios pendientes | Dimensionar ocupación, recorrido y método de instalación; no convertir longitud en diámetro seleccionado. |
| 26 | Ducto exterior nuevo; material/diámetro no seleccionados | `50 m` propuestos | Propuesta sin medición ni ruta aceptada | Confirmar trazado/destino y dimensionar ocupación; no cargar como compra cerrada antes de eso. |
| 27 | Caja/registro exterior; especificación según sitio | `5+1=6 posiciones teóricas`, no 6 unidades de compra | Pendiente de inspección | Inspeccionar registros existentes, condición y ubicación; comprar solo unidades justificadas por faltantes/estado. |

### Coherencia de fibra y canalización

El escenario contempla 11 enlaces verticales de 12F (22 cassettes, uno por extremo) y 3 enlaces exteriores de 24F (6 cassettes, uno por extremo). La arquitectura documentada integra terminación; los renglones separados de pigtails y adaptadores quedan en cero para evitar duplicación. Los patch cords ópticos dependen de pares activos. Para E2/E3 se conservan variables `x/y`, sin cantidad numérica. Las longitudes de bandeja, bajantes y ducto no determinan por sí solas sección, diámetro ni producto.

## 3. Herramientas: fila, actividad, fórmula, unidad y clasificación

Las herramientas son reutilizables o equipos compartidos. El lubricante es material consumible y depende del ducto/cable y método; no debe registrarse como herramienta reutilizable ni inventarse su cantidad. Las cantidades de equipos suponen una cuadrilla académica; el CSV de herramientas no atribuye marca/modelo/fabricante.

| Fila | Herramienta / actividad | Cantidad comprobable y unidad | Tipo / estado | Acción del estudiante |
|---:|---|---|---|---|
| 2 | Guía pasacables/juego de tiro para tendido de cobre/fibra | `1 frente de tendido = 1 juego` | Reutilizable; escenario una cuadrilla | Confirmar método y organización de cuadrilla. |
| 3 | Lubricante compatible con cable y ducto | `variable según ruta/producto`; sin número/unidad de compra fijada | Consumible, no herramienta; pendiente del sistema de ductos | Seleccionar solo si el método/producto lo requiere y seguir instrucción del fabricante. |
| 4 | Soportes de bobina para tendido | `1 bobina en uso × 2 apoyos = 2 unidades` | Reutilizable; par funcional | Verificar carga máxima contra bobina real. |
| 5 | Herramienta de impacto/terminación Cat 6A | `2 técnicos de terminación × 1 = 2 unidades` | Reutilizable; escenario de cuadrilla, compatibilidad pendiente | Confirmar compatibilidad con jacks/panel seleccionados. |
| 6 | Juego cortador/pelador de cobre | `2 técnicos × 1 juego = 2 juegos` | Reutilizable; escenario de cuadrilla | Confirmar cantidad y herramientas necesarias para cable seleccionado. |
| 7 | Fusionadora OS2 para empalmes de cassette | `1 equipo compartido = 1 unidad` | Reutilizable/equipo especializado | Confirmar que el procedimiento académico requiere fusión y calibración/estado. |
| 8 | Cortadora de precisión y peladora de fibra | `1 puesto especializado = 1 juego` | Reutilizable | Verificar compatibilidad y estado del equipo. |
| 9 | Fuente y medidor óptico OS2 | `1 juego de prueba compartido` | Reutilizable/equipo de medición | Definir método, longitudes de onda y criterio de aceptación con el curso. |
| 10 | OTDR OS2 | `1 equipo compartido` | Reutilizable; sujeto a procedimiento académico | Confirmar alcance y procedimiento; no especificar modelo. |
| 11 | Certificador Cat 6A con adaptadores de enlace permanente | `1 equipo compartido` para campaña de enlaces | Reutilizable; calibración vigente requerida | Confirmar disponibilidad, adaptadores correctos y calibración. |
| 12 | Etiquetadora | `1 unidad compartida` | Reutilizable; etiquetas/cinta son consumibles aparte | Definir esquema de identificación y consumible; no inventar cantidades de etiquetas. |
| 13 | Juego de herramientas de rack y nivel | `1 cuadrilla × 1 juego` | Reutilizable; escenario | Validar herramientas requeridas con el rack finalmente aceptado. |

## 4. Procedimiento de edición y control

1. Crear una copia nueva identificada, sin sobrescribir el original ni la copia controlada.
2. Resolver las condiciones indicadas en cada fila con evidencia del estudiante/docente. Trasladar datos y fórmulas a la misma fila lógica; mantener las columnas A–K, hojas, encabezados, colores y formatos originales.
3. Dejar vacías las cantidades de E2/E3 hasta resolver `x/y`; mantener la expresión paramétrica en memoria o nota explicativa, no como cantidad inventada en G.
4. Dejar sin cantidad cerrada los patch cords ópticos hasta definir pares activos. No duplicar pigtails/adaptadores integrados.
5. Conservar separadas las longitudes calculadas de bandejas/bajantes/ductos y la selección aún pendiente de sección/diámetro/producto.
6. Mantener las columnas económicas I y J sin importes. `J43` contiene originalmente `=SUM(J2:J41)`: solicitar criterio docente antes de cambiarla. Hasta recibirlo, registrar que la ambigüedad sigue pendiente; no interpretar la fórmula como autorización de costo.
7. Completar `Herramientas` desde filas 2–13. Equipos de medición/instalación son reutilizables; lubricante y consumibles (cinta/etiquetas) deben clasificarse aparte y cuantificarse solo con método/consumo justificados.
8. Revisar cada fórmula contra la memoria y hacer que el estudiante explique entradas, operación, unidad, redondeo y categoría de evidencia.
9. Retirar todos los ejemplos didácticos de la copia personal conforme a la plantilla, revisar referencias residuales y guardar como `..._REVISION_ESTUDIANTE.xlsx`. No marcar como final si hay ejemplos, cantidades no justificadas o pendientes presentados como resueltos.

## 5. Validación reproducible y alcance disponible

Desde la raíz del repositorio, ejecutar:

```powershell
python 09_auditorias/validar_fase2d.py
python 09_auditorias/validar_fase2b.py
```

Estos validadores revisan la evidencia ya registrada, incluidos los resultados Fase 2D y la integridad/estructura básica de los libros controlados. Para la copia que complete el estudiante, aplicar además esta lista y guardar evidencia del resultado:

- [ ] El archivo abre como OOXML: comprobar que es ZIP válido, `ZipFile.testzip()` no encuentra errores y XML de relaciones/hojas puede analizarse.
- [ ] Permanecen exactamente las dos hojas originales visibles: `Cotización técnica` y `Herramientas`.
- [ ] En `Cotización técnica` continúan las columnas originales A–K, orden, encabezados, estilos, colores y formatos; no se han añadido columnas ni renombrado hojas.
- [ ] Las fórmulas introducidas se recalculan en la aplicación que se usará para entregar; los resultados se comparan con la tabla de materiales y la memoria.
- [ ] No hay valores monetarios/precios en I/J ni montos añadidos. Revisar explícitamente `J43`; hasta que el docente responda, documentar la fórmula original y dejar el punto pendiente.
- [ ] Cotejar referencias y cantidades: A 74 cajas de 305 m, B 155; 51 paneles; 1 984 RJ45; 992 placas dobles; 11 TR; 13 racks propuestos.
- [ ] Revisar 22 cassettes 12F, 6 cassettes 24F, 12+1+1 housings y cero compras separadas duplicadas de pigtails/adaptadores.
- [ ] No hay ejemplos didácticos residuales ni filas que los presenten como componentes elegidos.
- [ ] E2/E3 no contienen cantidad cerrada mientras falten `x/y`; canalización separa metraje de sección/diámetro/producto.
- [ ] Herramientas cubren las actividades previstas; se distingue equipo reutilizable de lubricante/etiquetas y otros consumibles.

**No se ejecutó la validación de un libro completado por el estudiante:** tal archivo no existe en el repositorio. No se afirma por tanto que se hayan comprobado fórmulas nuevas, recálculo en Excel/LibreOffice, retiro de ejemplos ni contenido final. La comprobación actual solo corresponde a libros controlados intactos y a los cálculos/documentos existentes.
