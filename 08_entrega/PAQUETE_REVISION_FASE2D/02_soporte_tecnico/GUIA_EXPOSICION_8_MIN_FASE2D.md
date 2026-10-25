# Guía de exposición individual — Fase 2D

**Estado:** apoyo para ensayo; el estudiante debe comprender, verificar y expresar con sus propias palabras.

| Tiempo | Apoyo | Contenido mínimo |
|---|---|---|
| 0:00–0:45 | Backbone exterior | Tres enlaces E1/E2/E3; 145 m existentes y 50 m propuestos son referencias, no medición de cable. |
| 0:45–1:40 | Plantas A/B | Cinco y seis laboratorios, TR al extremo del pasillo como escenario y rutas en estrella. |
| 1:40–2:35 | Laboratorios | 16 áreas dobles, 32 enlaces por laboratorio y dos cables independientes por área. |
| 2:35–3:40 | Memoria Fase 2D | Fórmula de ruta: TR + medio pasillo + progresiva + distribución interior. Máximos 45,7 m A y 42,7 m B con reserva, ambos menores que 90 m. |
| 3:40–4:30 | Resultados de cobre | 69 456,24 m calculados; 229 cajas de 305 m = 69 845 m comerciales. Patch cords separados. |
| 4:30–5:25 | ER/TR | 12F vertical, 24F exterior, housings CCH por cuarto, racks de 42U como escenario; activos separados. |
| 5:25–6:15 | Fibra | Vertical 284,025 m de 12F. E1 221,55 m; E2/E3 permanecen fórmulas con `x/y`. |
| 6:15–7:10 | Matriz Fase 2D | Productos verificados, cantidades, canalizaciones pendientes y eliminación de pigtails/adaptadores duplicados. |
| 7:10–8:10 | Plan Excel | Filas listas, filas bloqueadas, fórmulas simples, precios vacíos y copia todavía provisional. |
| 8:10–8:35 | Cierre | Qué es dato, supuesto, resultado y pendiente indispensable. |

## Cálculos que deben poder reproducirse

- `62 × 16 × 2 = 1 984` enlaces de cobre.
- A: `22 428/305 → 74` cajas; B: `47 028,24/305 → 155`; total 229.
- A desfavorable: `3 + 1,2 + 21,25 + (10 + 4,25 + 3) + 3 = 45,7 m`.
- B desfavorable: `3 + 1,2 + 18,75 + (10 + 3,75 + 3) + 3 = 42,7 m`.
- Fibra vertical: `284,025 m` de escenario incluyendo reservas y 5 %.
- Cassettes: `11 × 2 = 22` de 12F y `3 × 2 = 6` de 24F.
- Housings: 12 `CCH-01U`, 1 `CCH-03U`, 1 `CCH-04U`.

## Respuestas breves

1. **¿Son definitivos los 69,8 km de cobre?** No. Son resultado del escenario geométrico completo, útil para la actividad y sujeto a revisión de planta/campo.
2. **¿Por qué el enlace cumple 90 m?** La ruta más desfavorable calculada, incluso con 3 m de reserva, es 45,7 m; el 5 % de desperdicio solo sirve para compra.
3. **¿Por qué E2/E3 no tienen cantidad?** Sus tramos `x/y` no tienen evidencia y no deben inventarse.
4. **¿Por qué no se compran pigtails/adaptadores?** Los cassettes seleccionados ya los integran.
5. **¿Dónde están los switches?** Fuera de este cierre pasivo; su número requiere arquitectura lógica, energía y puertos activos.
6. **¿Está listo el Excel?** Está lista la correspondencia. El estudiante debe transferir, revisar y probar la copia sin precios.
