# Registro de datos de campo y supuestos preliminares

Origen: información proporcionada por el estudiante en conversaciones de ChatGPT, octubre de 2026. Documento de transferencia de contexto; no sustituye levantamiento topográfico, planos existentes ni verificaciones del docente.

## A. Datos comunicados como observados o definidos en clase

| ID | Concepto | Dato | Estado |
|---|---|---|---|
| CAM-01 | Canalización subterránea de telecomunicaciones existente a partir del edificio con ER principal hacia el patio posterior | **145 m** | Dato reportado por el estudiante; verificar extremos, método de medición y disponibilidad |
| CAM-02 | Separación entre cajas de telecomunicaciones del trazado | **25 m** | Criterio de clase, no conteo verificado de cajas |
| CAM-03 | Desde el final de canalización existente hasta el ER de uno de los edificios nuevos | **50 m** | Tramo adicional propuesto, método de instalación elegido: subterráneo |
| CAM-04 | Existencia de un ER principal en un edificio ya construido, antes del tramo anterior | Ubicación conceptual | Informado por el estudiante; localización precisa pendiente |

**Corrección histórica importante:** inicialmente se mencionaron 120/125 m, después 45 m y finalmente el estudiante aclaró que el valor correcto es **145 m**. No volver a utilizar 45, 120 ni 125 m como longitud del tramo existente.

La suma geométrica **145 + 50 = 195 m** identifica un recorrido preliminar hasta **uno** de los ER nuevos; **no** representa automáticamente el metraje de cable a comprar, ni los tres enlaces completos. Falta identificar edificio receptor, rutas de enlaces restantes y reservas de fibra.

## B. Datos oficiales del enunciado, no mediciones

- Edificio A: 4 pisos, 5 laboratorios por piso, 85 m² por laboratorio.
- Edificio B: 7 pisos, 6 laboratorios por piso, 75 m² por laboratorio.
- Mínimo un TR por piso, con posibles TR adicionales cuando corresponda.
- Mínimo 16 áreas de trabajo dobles por laboratorio.
- Límite máximo de 90 m de enlace permanente de cobre.

Los valores oficiales deben cotejarse contra `01_requisitos/Markdown pegado.md`.

## C. Supuestos preliminares, sujetos a comprobación

| ID | Propuesta | Condición |
|---|---|---|
| SUP-01 | Edificio A: laboratorios de 10 x 8,5 m | Área matemática de 85 m²; no es medida de campo |
| SUP-02 | Edificio B: laboratorios de 10 x 7,5 m | Área matemática de 75 m²; no es medida de campo |
| SUP-03 | Planta rectangular y pasillo central | Preferencia expresada por el estudiante |
| SUP-04 | Pisos típicos idénticos en cada edificio | Preferencia expresada por el estudiante |
| SUP-05 | Pasillo de 2,4 m de ancho | Hipótesis no validada normativamente |
| SUP-06 | TR de 3 x 3 m | Dimensión de estudio, sujeta a capacidad y normas |
| SUP-07 | ER de 4 x 4 m | Dimensión de estudio, sujeta a capacidad y normas |
| SUP-08 | Altura entre pisos de 3,5 m | Hipótesis no medida |
| SUP-09 | Un ER en planta baja por edificio | Ubicación propuesta, no confirmada |
| SUP-10 | TR alineados verticalmente | Propuesta de simplificación del backbone |
| SUP-11 | Bandeja aérea interior con bajantes protegidas | Alternativa de estudio, no diseño aprobado |
| SUP-12 | Puestos de estudio con mobiliario aproximado de 1,20 x 0,60 m | Referencia tentativa, comprobar circulación y accesibilidad |

## D. Pendientes específicos de levantamiento

1. Ubicación del ER principal y extremos del tramo subterráneo existente.
2. Identidad del nuevo edificio cuyo ER se alcanza tras el tramo adicional de 50 m.
3. Distancia y trazado del ER principal al otro edificio; distancia ER A–ER B.
4. Número real, posición, dimensiones, estado y capacidad disponible de cajas y ductos existentes.
5. Alturas entre pisos, huecos técnicos, puertas, escaleras y acceso a ER/TR.
6. Definición de «área de trabajo doble» y disposición real de mobiliario.
7. Longitud real de rutas horizontales desde TR hasta las salidas.

Regla de uso: no convertir propuestas en mediciones, ni sumas de recorrido en lista de cantidades de material sin cálculo y justificación.
