# Memoria reproducible de cálculos — Fase 2B

**Fecha de corte:** 2026-10-25  
**Estado:** capacidad preliminar; revisión y defensa por el estudiante obligatorias.  
**Procedencia:** estructura y automatización preparadas con apoyo de OpenAI Codex. No sustituye las mediciones ni el cálculo individual exigido por el docente.

## Uso

1. Revisar `entradas_fase2b.csv` y completar únicamente mediciones o porcentajes con evidencia.
2. Ejecutar `python 04_calculos/modelo_calculos_fase2b.py`.
3. Revisar `resultados_fase2b.csv`; `N/D` significa que falta una entrada y no debe reemplazarse por una distancia inventada.
4. Trasladar al Excel solo cantidades comprendidas, revisadas y aprobadas por el estudiante.

## Fórmulas principales

| Magnitud | Fórmula | Unidad | Condición |
|---|---|---|---|
| Laboratorios | pisos × laboratorios/piso | laboratorio | Dato oficial |
| Áreas dobles | laboratorios × 16 | área doble | Mínimo oficial |
| Enlaces de cobre | áreas dobles × 2 RJ45/área | enlace | Supuesto pendiente de confirmar |
| Paneles por TR | redondeo superior(enlaces/TR ÷ 48) + 1 si la división es exacta | panel | Reserva provisional: evita dejar el TR sin posiciones libres |
| Cable de cobre | enlaces × longitud promedio medida × (1 + desperdicio/100) | m cable | Queda `N/D` sin medición y porcentaje aprobado |
| Terminaciones verticales | TR × 12 fibras × 2 extremos | terminación | Propuesta de 12 fibras |
| Terminaciones exteriores | 3 enlaces × 24 fibras × 2 extremos | terminación | Propuesta de 24 fibras |
| Adaptadores LC dúplex | redondeo superior(terminaciones individuales ÷ 2) | adaptador | Solo si se terminan todas las fibras con LC dúplex |
| Cassettes pre-pigtailed 12F | 11 enlaces verticales × 2 extremos | cassette | 22; arquitectura provisional CCH, incluye pigtails/adaptadores/protectores |
| Cassettes pre-pigtailed 24F | 3 enlaces exteriores × 2 extremos | cassette | 6; arquitectura provisional CCH, incluye pigtails/adaptadores/protectores |

## Resultados de capacidad comprobados

| Control | Edificio A | Edificio B | Total |
|---|---:|---:|---:|
| Laboratorios | 20 | 42 | 62 |
| Áreas dobles | 320 | 672 | 992 |
| Enlaces/puertos RJ45 | 640 | 1 344 | 1 984 |
| Enlaces por TR | 160 | 192 | — |
| Paneles de 48 puertos por TR | 4 | 5 | — |
| Paneles totales | 16 | 35 | 51 |
| Capacidad total | 768 | 1 680 | 2 448 |
| Posiciones libres | 128 | 336 | 464 |

## Separación de magnitudes

- **Ducto:** 145 m existentes reportados y 50 m nuevos propuestos; ambos requieren validación de ruta/capacidad.
- **Cable:** longitud física de cada cable más reserva aprobada; no equivale a metros de ducto.
- **Fibras:** cantidad de hilos dentro de cada cable (12 o 24); no es longitud ni número de cables.
- **Cajas:** seis posiciones intermedias teóricas en los tramos de 145 m y 50 m combinados (cinco y una respectivamente); no constituyen una cantidad de compra.
- **Terminación óptica:** 408 empalmes/pigtails funcionales y 204 adaptadores LC dúplex continúan siendo controles de capacidad. Si se adopta la arquitectura provisional de cassettes pre-pigtailed, esos elementos vienen incluidos y la compra separada es cero; no se deben duplicar.

## Límites inferiores calculables sin inventar recorridos

- Enlace E1: `145 + 50 = 195 m` de ruta base reportada/propuesta, antes de entradas, reserva y ajustes; no es metraje de cable a comprar.
- Desnivel vertical acumulado A: `(0+1+2+3) × 3,5 = 21 m`.
- Desnivel vertical acumulado B: `(0+1+2+3+4+5+6) × 3,5 = 73,5 m`.
- Total de desnivel: `94,5 m`. Es un límite inferior basado en altura de piso no medida; excluye recorridos horizontales, entrada a cuartos y reservas.

## Variables que impiden cerrar metrajes

- `LONG_PROM_COBRE_A`, `LONG_PROM_COBRE_B` y `DESPERDICIO_COBRE`.
- `X_RUTA_B`, `Y_RUTA_A_B` y `RESERVA_FIBRA`.
- Rutas verticales e ingresos a ER/TR, incluida la separación real del ER y el TR del primer piso.
- Diámetros exteriores de cables, diámetro interior útil y ocupación admisible de canalizaciones.

No se usa 90 m como longitud de cada enlace: es un límite máximo que debe comprobarse contra cada recorrido físico.
