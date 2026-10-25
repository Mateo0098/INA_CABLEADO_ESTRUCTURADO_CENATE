# Revisión de variables y supuestos — Fase 2C

**Fecha:** 2026-10-25  
**Objetivo:** separar decisiones académicas defendibles de datos que no pueden cerrarse sin evidencia.

## Supuestos utilizables como escenario académico

Estos valores pueden sostener un escenario provisional si el estudiante los comprende, acepta y presenta como supuestos, nunca como mediciones:

| Variable/decisión | Valor de escenario | Efecto | Condición |
|---|---:|---|---|
| Puertos por área doble | 2 RJ45 | 1 984 enlaces | Interpretación provisional; consultar docente |
| Panel de cobre | 48 puertos | 51 paneles | Producto candidato identificado |
| Reserva de panel | Agregar uno si la división exacta deja cero posiciones | B usa 5 paneles/TR | Decisión de diseño, no requisito normativo |
| Fibra vertical | 12 fibras/enlace | 11 cables; 132 fibras por extremo de TR/ER | Decisión de capacidad |
| Fibra exterior | 24 fibras/enlace | 3 cables | Decisión de capacidad |
| Terminación completa | Terminar todas las fibras | 408 empalmes/pigtails funcionales | Permite disponibilidad total; revisar costo/alcance en Actividad 2 |
| Cassette pre-pigtailed | Activado (`1`) | 22 cassettes 12F + 6 cassettes 24F; compra separada de pigtails/adaptadores = 0 | Provisional hasta seleccionar housing CCH |
| Geometría de referencia | 10×8,5 m A; 10×7,5 m B; 3,5 m/piso | Diagramas y límite inferior de desnivel | No presentar como levantamiento |

## Resultados calculables pero no comprables

| Resultado | Valor | Por qué no es cantidad de compra |
|---|---:|---|
| Ruta base E1 | 195 m | Suma de ducto reportado y tramo propuesto; faltan entradas y reserva de cable |
| Desnivel vertical acumulado A | 21 m | Excluye recorridos horizontales, ingreso a cuartos y reserva |
| Desnivel vertical acumulado B | 73,5 m | Igual limitación; altura entre pisos no medida |
| Desnivel acumulado total | 94,5 m | Límite inferior geométrico de once cables, no bobina requerida |
| Posiciones intermedias en 145 m | 5 | Aplicación teórica de ~25 m, sin inspección |
| Posición intermedia en 50 m | 1 | Referencia teórica, no registro aprobado |

## Variables que no pueden resolverse responsablemente

| Variable | Evidencia faltante | Consecuencia |
|---|---|---|
| `LONG_PROM_COBRE_A/B` | Rutas físicas por puerto o muestreo representativo aprobado | Metros de Cat 6A quedan `N/D` |
| `X_RUTA_B`, `Y_RUTA_A_B` | Trazado y medición de los enlaces | Metros de cable exterior E2/E3 quedan `N/D` |
| Reserva de fibra | Criterio docente/proyecto y ubicaciones de reserva | No calcular bobinas finales |
| Desperdicio de cobre | Procedimiento de corte y criterio aprobado | No calcular total/rollos |
| Ductos y bandejas | Diámetros interiores, cables simultáneos, ruta y criterio de ocupación | No seleccionar dimensiones |
| Cajas/registros | Levantamiento, estado, accesibilidad y diseño civil | No convertir posiciones en unidades |
| Housing CCH | Número de slots, RU, entradas y combinación por cuarto | Cassettes no forman aún un sistema completo |
| Racks | Activos, housings, PDU/UPS, fondo, carga, ventilación y acceso | 42U y 13 unidades siguen como escenario |
| Patch cords | Mobiliario, disposición del rack y puertos activos | Longitud y compra pendientes |
| Equipos activos | Arquitectura lógica, demanda de puertos activos, energía y ópticos | No seleccionar switches/transceptores |

## Regla de cierre

Un supuesto académico puede aparecer en diagramas, memoria o fórmula si está rotulado y admite recalcularse. Una medición ausente no se sustituye por un supuesto cuando afecta metraje de compra, canalización, seguridad o compatibilidad del sistema.
