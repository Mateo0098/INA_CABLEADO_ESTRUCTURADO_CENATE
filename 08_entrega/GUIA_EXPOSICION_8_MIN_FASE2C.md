# Guía de exposición individual — mínimo 8 minutos

**Estado:** apoyo de revisión; el estudiante debe adaptarlo a su propia explicación y comprender cada fórmula.

## Secuencia sugerida

| Tiempo | Archivo/apoyo | Explicación clave |
|---|---|---|
| 0:00–0:45 | EXT-01 | Alcance: edificios A/B, ER principal y tres enlaces distintos. Distinguir datos oficiales, reportados y variables `x/y`. |
| 0:45–1:45 | EXT-01 | OS2, 24 fibras/enlace, método subterráneo propuesto. Explicar que 145+50=195 m es ruta base E1, no cable a comprar. |
| 1:45–2:45 | PLA-A / PLA-B | Cinco y seis laboratorios por piso, un TR mínimo, bandeja central y enlaces en estrella. Indicar que cada ruta debe comprobar ≤90 m. |
| 2:45–3:45 | LAB-A / LAB-B | 16 áreas dobles, dos RJ45 por área como supuesto, 32 enlaces independientes por laboratorio. Las líneas naranjas son canalización compartida, no conexión en cadena. |
| 3:45–4:45 | ER-A / ER-B | Dos llegadas exteriores por ER, backbone vertical, capacidades 96F/132F y diferencia entre fibra terminada y puerto activo. |
| 4:45–5:45 | TR-A / TR-B | 160/192 enlaces por TR; 4/5 paneles de 48 puertos. Justificar el panel adicional en B para no quedar sin reserva. |
| 5:45–6:45 | Memoria/resultados | Mostrar fórmulas: laboratorios, áreas, puertos, paneles, terminaciones y cassettes. Señalar `N/D` donde faltan mediciones. |
| 6:45–7:30 | Matriz Fase 2C | Distinguir producto identificado, familia y componente pendiente. Explicar cassettes pre-pigtailed y por qué pigtails/adaptadores no se duplican. |
| 7:30–8:20 | Plan Excel | Mostrar filas previstas, columnas económicas vacías, fórmulas simples y bloqueos. Declarar que la copia conserva ejemplos y no es final. |
| 8:20–8:40 | Cierre | Resumir qué está verificado y qué requiere docente/campo antes de entregar. |

## Fórmulas que deben poder explicarse

- Laboratorios: `4×5 + 7×6 = 62`.
- Áreas dobles: `62×16 = 992`.
- RJ45: `992×2 = 1 984` bajo el supuesto de dos puertos.
- Paneles: A `4 pisos×4 = 16`; B `7×5 = 35`; total `51`.
- Terminaciones verticales: `11×12×2 = 264`.
- Terminaciones exteriores: `3×24×2 = 144`.
- Cassettes: verticales `11×2 = 22` de 12F; exteriores `3×2 = 6` de 24F.

## Preguntas previsibles

1. **¿Por qué no se usa 90 m por cable?** Porque 90 m es el máximo del enlace permanente; el metraje debe seguir el recorrido real.
2. **¿Por qué cinco paneles en B?** Cuatro cubren exactamente 192 puertos sin reserva; el quinto es una decisión provisional de capacidad.
3. **¿Por qué OS2?** Es la propuesta uniforme para exterior y vertical; la selección comercial está documentada como candidata.
4. **¿Por qué no hay switches definidos?** La capacidad pasiva no determina puertos activos ni energía; faltan requisitos lógicos.
5. **¿Por qué pigtails/adaptadores figuran como cero de compra separada?** El cassette candidato ya los integra; sumarlos duplicaría materiales.
6. **¿Qué impide cerrar el Excel?** Mediciones, housings, racks, activos, longitudes, reservas y dos consultas docentes.

## Archivos a tener abiertos

1. Los nueve PNG en orden numérico.
2. `04_calculos/MEMORIA_CALCULOS_FASE2B.md` y `resultados_fase2b.csv`.
3. `05_materiales/MATRIZ_TECNICA_FASE2C.md`.
4. `06_excel/PLAN_TRANSFERENCIA_EXCEL_FASE2C.md` y la copia de trabajo Excel.

Ensayar con cronómetro: el tiempo de abrir archivos no cuenta como exposición efectiva.
