# Guía de defensa individual — mínimo 8 minutos

**Actividad de Comprobación N.º 1 · Cableado Estructurado · INA CENATE**  
**Material para estudiar y ensayar:** explicar con palabras propias y reconocer qué datos son supuestos.

## Guion sugerido (8:30–9:00 minutos)

### 0:00–0:50 | Objetivo

“El objetivo es presentar una propuesta de infraestructura pasiva de telecomunicaciones para dos edificios nuevos. Incluye el cableado horizontal, cuartos ER y TR, backbone de fibra y cantidades de materiales. La hoja Excel no contiene precios. El diseño es académico y esquemático: las rutas y dimensiones que no provienen del enunciado están identificadas como supuestos y requieren confirmación antes de construir o comprar.”

### 0:50–1:45 | Edificios y arquitectura

“El edificio A tiene cuatro pisos y cinco laboratorios por piso, para veinte laboratorios. El edificio B tiene siete pisos y seis laboratorios por piso, para cuarenta y dos. El escenario asigna un TR a cada piso y un ER a cada edificio. El ER concentra la conexión exterior y el backbone del edificio; cada TR distribuye el cableado horizontal del piso. La ubicación exacta y las dimensiones representadas son supuestos, no un levantamiento arquitectónico.”

### 1:45–2:35 | ER, TR y áreas de trabajo

“ER significa cuarto de equipos y TR cuarto de telecomunicaciones. Se mantienen separados incluso cuando el ER está en el primer piso, para no contar dos veces el mismo recinto o equipo. Cada laboratorio se representa con dieciséis áreas de trabajo dobles. Para dimensionar, se asumieron dos conectores RJ45 por área doble: dieciséis por dos dan treinta y dos enlaces por laboratorio. Esa interpretación debe confirmarse con el docente.”

### 2:35–3:25 | Cableado horizontal Cat 6A

“Cada enlace horizontal Cat 6A va desde un puerto del panel en el TR hasta una salida del área de trabajo, en topología estrella. En el escenario, el recorrido más largo con reservas es 45,7 metros en A y 42,7 metros en B, ambos por debajo del máximo de 90 metros indicado para el enlace permanente. Esos resultados dependen de una geometría propuesta; el plano no demuestra la distancia real. El cable del enlace permanente se cuenta aparte de los patch cords de usuario y de rack.”

### 3:25–4:15 | Salidas y patch panels

“Hay sesenta y dos laboratorios entre los dos edificios. Con dieciséis áreas dobles y dos RJ45 por área, el cálculo es 62 por 16 por 2, igual a 1 984 enlaces. Eso requiere 1 984 jacks y, bajo una salida doble por área, 992 placas y cajas. Cada piso de A tiene 160 enlaces: cuatro paneles de 48 ofrecen 192 puertos. Cada piso de B tiene 192 enlaces: cinco paneles de 48 ofrecen 240. La diferencia es capacidad reservada, no puertos usados.”

### 4:15–5:10 | Cable y reservas

“La cantidad de cable se calcula con los metrajes del escenario geométrico que quedó documentado: 22 428 metros para A y 47 028,24 para B antes de reservas. Se divide cada total entre 305 metros por caja y se redondea hacia arriba: 74 cajas para A y 155 para B, 229 en total. Los cálculos incorporan 3 metros de reserva por enlace y 5 por ciento de desperdicio como supuestos. No son mediciones de campo ni una orden de compra; si cambian rutas o reservas, cambia la cantidad.”

### 5:10–6:10 | Backbone OS2

“El backbone vertical se modela con cable OS2 de 12 fibras entre cada ER y cada TR: cuatro enlaces en A y siete en B. Los resultados del escenario son 89,25 metros en A y 194,775 en B. Para el exterior se muestran tres enlaces de OS2 de 24 fibras: ER principal–ER A, ER principal–ER B y ER A–ER B. Las cantidades calculadas son 221,55, 247,8 y 69,3 metros. En estas fórmulas, 145 metros existentes fueron reportados pero no medidos por nosotros, 50 metros son una propuesta y x = 75 m e y = 50 m son supuestos. Deben sustituirse por rutas verificadas.”

### 6:10–7:05 | Racks, terminación y materiales

“El libro contabiliza paneles, jacks, placas, cajas, patch cords, cassettes, organizadores, racks propuestos y herramientas. Se consideran 22 cassettes de 12 fibras y seis de 24 fibras. La terminación se representa con cassettes integrados, por eso pigtails y adaptadores separados quedan en cero para evitar duplicarlos. Se estiman 28 patch cords ópticos suponiendo un circuito LC dúplex activo en cada uno de catorce enlaces: dos cords por enlace, uno por extremo. No significa que las fibras restantes estén activas ni que se hayan seleccionado transceptores.”

### 7:05–7:55 | Canalizaciones y límites

“Como escenario de cantidades, se muestran 478 tramos de bandeja genérica de 100 por 50 milímetros y 1 042 tramos de bajante PVC de diámetro nominal 25 milímetros, ambos de tres metros, además de 50 metros de ducto exterior nominal de 50 milímetros. No tienen marca ni modelo verificado. Falta revisar diámetro interior, llenado, carga, soportes, accesorios y las condiciones del sitio. Seis posiciones de registro son una referencia teórica de inspección, no una cantidad de compra.”

### 7:55–8:40 | Cierre

“En resumen, el Excel contiene resultados calculados para un escenario y conserva sus fórmulas. No contiene precios. Antes de comprar o construir hay que confirmar la interpretación de las áreas dobles, dimensiones y recorridos, las rutas de fibra, canalizaciones y capacidad de los racks. No presentamos esos valores como mediciones. El siguiente paso es que el estudiante compruebe el contenido con el enunciado y pueda explicar cada fórmula.”

## Preguntas técnicas probables

1. **¿Por qué eligió un TR por piso?**  
   Es la distribución asumida para el escenario, dentro del requisito mínimo de al menos uno por piso. La ubicación y suficiencia se deben validar con planos y distancias reales.

2. **¿Por qué hay dos RJ45 por área doble?**  
   Se adoptó como supuesto de dimensionamiento. Produce 32 enlaces por laboratorio. Debe confirmarse que “doble” significa dos salidas en el criterio del docente.

3. **¿Cómo explica los 1 984 enlaces?**  
   `(20 laboratorios A + 42 laboratorios B) × 16 áreas × 2 puertos = 1 984`.

4. **¿Por qué hay más puertos de panel que enlaces?**  
   Los paneles son unidades de 48 puertos y se redondea al siguiente panel completo por TR. La diferencia es capacidad disponible.

5. **¿El máximo de 45,7 m demuestra que todos los enlaces reales cumplen 90 m?**  
   No. Es el máximo del escenario geométrico. Solo un levantamiento y una medición de rutas reales podrían confirmarlo.

6. **¿Por qué hay 229 cajas de cable?**  
   Se dividen los metrajes calculados por 305 m por caja y se redondea hacia arriba por edificio: 74 para A y 155 para B. La reserva de 3 m por enlace y el desperdicio de 5 % son supuestos.

7. **¿Qué significan 145 m, 50 m, x e y?**  
   145 m es una longitud reportada de canalización existente, 50 m una extensión propuesta, x = 75 m e y = 50 m son supuestos geométricos. No son mediciones de cable y falta verificar el destino de E1.

8. **¿Por qué OS2 y cuántas fibras se usan?**  
   El escenario definido usa OS2: 12 fibras en los enlaces ER–TR y 24 fibras en los tres enlaces exteriores. Las longitudes son resultados condicionados por las entradas supuestas.

9. **¿Por qué hay 28 patch cords ópticos?**  
   Se supuso un circuito LC dúplex activo por cada uno de once enlaces verticales y tres exteriores. Son 14 enlaces por dos extremos. La cantidad activa real depende del diseño de equipos.

10. **¿Por qué pigtails y adaptadores aparecen en cero?**  
    La arquitectura de terminación adoptada usa cassettes integrados que incluyen esos componentes. Añadirlos por separado duplicaría la cantidad en este escenario.

11. **¿Las canalizaciones ya están listas para compra?**  
    No. Son genéricas y preliminares. Se requiere seleccionar producto y comprobar ficha, diámetro interior, llenado, cargas, soportes y accesorios.

12. **¿Por qué no hay precios ni switches?**  
    La actividad no debe incluir precios. Los switches, transceptores y demás elementos activos requieren una arquitectura y datos adicionales, por lo que no se deducen de los puertos pasivos.

13. **¿Qué información falta para convertirlo en diseño constructivo?**  
    Mediciones de campo, planos aprobados, rutas y registros inspeccionados, validación de canalizaciones, confirmación del docente sobre áreas dobles y revisión de capacidad de los racks, más especificaciones verificadas para las selecciones finales.

## Repaso antes de exponer

- Poder explicar cada multiplicación, división y redondeo del Excel sin leer el guion.
- Señalar qué valores son datos académicos, supuestos y resultados calculados.
- No llamar “medición” a ninguna distancia del escenario.
- Distinguir salida/área de trabajo, enlace permanente, patch cord, TR y ER.
- Abrir el libro y las imágenes, verificar que corresponden al escenario y ensayar con cronómetro.
- La guía y los artefactos tuvieron asistencia de IA; la explicación final debe reflejar comprensión y criterio propios del estudiante.
