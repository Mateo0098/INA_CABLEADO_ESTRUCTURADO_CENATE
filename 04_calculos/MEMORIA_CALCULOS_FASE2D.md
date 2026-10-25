# Memoria de recorridos y cantidades — Fase 2D

**Fecha:** 2026-10-25

**Carácter:** escenario académico reproducible. Las dimensiones de planta, reservas y desperdicios aquí adoptados no son mediciones de campo.

## 1. Entradas clasificadas

Los datos docentes son los pisos, laboratorios, áreas dobles mínimas y el máximo de 90 m del enlace permanente. Las geometrías 10 × 8,5 m (A), 10 × 7,5 m (B), pasillo de 2,4 m, altura de 3,5 m y ubicación del TR al extremo del pasillo son supuestos de diseño. Los 145 m existentes y 50 m nuevos son referencias aportadas/propuestas y siguen sujetos a validación.

Para poder explicar y recalcular el escenario se adoptan:

- 3 m dentro del TR por enlace de cobre.
- Cruce de medio pasillo: 1,2 m.
- Distribución interior media: profundidad de 10 m + un cuarto de la fachada + bajante de 3 m.
- Ruta interior desfavorable: profundidad + media fachada + bajante.
- Reserva de terminación de cobre: 3 m por enlace, separada de la ruta.
- Desperdicio de compra: 5 % después de sumar reservas.
- Fibra: 3 m de recorrido interno y 5 m de reserva en cada extremo; 5 % de desperdicio de compra.

## 2. Cobre horizontal

El TR se coloca en el extremo este del pasillo. Dos filas de laboratorios comparten las mismas progresivas longitudinales.

| Control | Edificio A | Edificio B |
|---|---:|---:|
| Distancias TR–acceso de laboratorio | 4,25; 4,25; 12,75; 12,75; 21,25 m | 3,75; 3,75; 11,25; 11,25; 18,75; 18,75 m |
| Ruta media representativa | 30,375 m/enlace | 30,325 m/enlace |
| Ruta física desfavorable | 42,7 m | 39,7 m |
| Con 3 m de reserva | 45,7 m | 42,7 m |
| Control contra 90 m | Cumple | Cumple |

La comprobación de 90 m corresponde únicamente a esta geometría supuesta. El desperdicio de compra no aumenta la longitud del enlace y no se usa para probar el límite.

### Fórmula por laboratorio y piso

Para cada laboratorio `i`:

`L_i = 32 × (TR_interno + pasillo/2 + distancia_i + interior_promedio)`

Por piso se suman todos los `L_i`. Para el edificio se multiplica por pisos. Luego:

`L_instalada = L_base + enlaces × 3 m`

`L_requerida = L_instalada × 1,05`

`cajas_305 = REDONDEAR.MAS(L_requerida / 305; 0)`

| Resultado | A | B | Total |
|---|---:|---:|---:|
| Base de rutas | 19 440 m | 40 756,8 m | 60 196,8 m |
| Reserva por enlace | 1 920 m | 4 032 m | 5 952 m |
| Desperdicio 5 % | 1 068 m | 2 239,44 m | 3 307,44 m |
| Requerido calculado | 22 428 m | 47 028,24 m | 69 456,24 m |
| Cajas de 305 m | 74 | 155 | 229 |
| Metros comerciales | 22 570 m | 47 275 m | 69 845 m |

Los 229 empaques son una cantidad de escenario, no una medición ni una orden de compra. Los patch cords no forman parte de estos metros: se contabilizan 1 984 de usuario y 1 984 de rack, de 7 ft como referencia candidata, para capacidad pasiva completa.

## 3. Fibra vertical

Por enlace al TR del piso `p`, comenzando en piso 1:

`L_p = (p-1) × 3,5 + 2 × (3 + 5)`

El primer término es desnivel; el segundo reúne recorridos internos y reservas de ambos extremos. Al total se agrega 5 % de desperdicio.

| Resultado | A | B | Total |
|---|---:|---:|---:|
| Enlaces individuales antes de desperdicio | 16; 19,5; 23; 26,5 m | 16; 19,5; 23; 26,5; 30; 33,5; 37 m | 11 cables |
| Suma base | 85 m | 185,5 m | 270,5 m |
| Requerido con 5 % | 89,25 m | 194,775 m | 284,025 m de cable OS2 12F |

## 4. Fibra exterior

Cada enlace agrega 3 m internos y 5 m de reserva en cada extremo, más 5 % de desperdicio. Se mantiene la separación entre metros de ducto y metros de cable.

- E1, bajo la hipótesis explícita de que 145 + 50 m conducen a A: `(145 + 50 + 16) × 1,05 = 221,55 m de cable 24F`.
- E2: `(145 + x + 16) × 1,05 = 169,05 + 1,05x m`.
- E3: `(y + 16) × 1,05 = 16,8 + 1,05y m`.
- Total exterior: `407,4 + 1,05x + 1,05y m de cable 24F`.

E1 es un resultado de escenario, no una medición de cable. E2 y E3 no producen cantidad cerrada hasta determinar `x` y `y`.

## 5. Canalización interior

La bandeja compartida se aproxima como longitud de pasillo más una espina de 10 m y una transversal de fachada por laboratorio:

- A: 472 m base.
- B: 892,5 m base.
- Total: 1 364,5 m base; 1 432,725 m con 5 % de reserva.
- Bajantes: 992 unidades compartidas por dos cables; 2 976 m base y 3 124,8 m con 5 %.

Estas cantidades permiten completar la variable de longitud, pero la sección, material, accesorios y diámetro permanecen pendientes de una decisión de ocupación. No deben copiarse como producto comercial completo sin esa decisión.

## 6. Sistema óptico y cuartos

- 22 cassettes `CCH-CS12-A9-P00RE` y 6 cassettes `CCH-CS24-A9-P00RE`.
- 12 housings `CCH-01U`: once TR y uno para ER-P, este último sujeto al espacio existente.
- 1 `CCH-03U` en ER-A para seis cassettes.
- 1 `CCH-04U` en ER-B para nueve cassettes.
- 0 pigtails y 0 adaptadores comprados por separado.
- Patch cords ópticos: variable `PARES_OPTICOS_ACTIVOS_EXTREMOS`, entre 0 y 204; 204 es el máximo si se activan todas las posiciones dúplex.
- 13 racks nuevos de 42U como escenario: once TR y dos ER nuevos. ER-P no se duplica.

## 7. Reproducción

Entradas: `04_calculos/entradas_fase2d.csv`.

Modelo: `python 04_calculos/modelo_calculos_fase2d.py`.

Resultados: `04_calculos/resultados_fase2d.csv`.

Toda cantidad rotulada como escenario debe ser revisada y defendida por el estudiante antes de transferirse a la plantilla INA.
