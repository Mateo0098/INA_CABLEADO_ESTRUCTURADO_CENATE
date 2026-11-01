# Reporte Codex — Unidad 01, arquitectura de red activa

**Fecha:** 2026-11-01. **Fase:** ampliación documental Unidad 01. **Rama:** `desarrollo-proyecto`. **SHA de implementación:** `78351d37c7518100a0fd03621ad7c3459bb73e7e`. **Autoría:** documentación y cálculos comparativos preparados con asistencia de Codex; revisión y decisión técnica humana pendientes.

## Objetivo y alcance

**HECHO:** se creó una propuesta autónoma de arquitectura activa y operativa como **diseño funcional de referencia**, separada de la Actividad 1 del INA. Se revisaron selectivamente conectividad, conteos ópticos, capacidad SFP+, lógica y carga preliminar. No se instaló ni certificó infraestructura y no se elaboró presupuesto. La entrega académica original permanece fuera del alcance de edición.

## Entradas y fuentes examinadas

- `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`, `09_auditorias/ULTIMO_REPORTE_CODEX.md` y `09_auditorias/REPORTES_CODEX/2026-10-29_FASE5C_PLANOS_DEFINITIVOS.md`.
- `03_diseno/DISENO_INTEGRADO_REFERENCIA_FASE2.md`, `05_materiales/MATRIZ_TECNICA_FASE2D.md`, requisitos pertinentes INA-003/004/005/008/011/014/015/019/044/045/056 en `01_requisitos/MATRIZ_REQUISITOS.md` y estado documental Fase 5C. No se repitió auditoría de los 76 requisitos.
- Fichas oficiales MikroTik de [CRS354](https://mikrotik.com/product/crs354_48g_4splus2qplusrm), [CRS317](https://mikrotik.com/product/crs317_1g_16s_rm), [ejemplo óptico S+31DLC10D](https://mikrotik.com/product/s_31dlc10d), [OSPF RouterOS](https://help.mikrotik.com/docs/spaces/ROS/pages/9863229/OSPF) y [L3 hardware offloading](https://help.mikrotik.com/docs/spaces/ROS/pages/62390319/L3%2BHardware%2BOffloading), consultadas 2026-11-01. Las fichas verifican especificaciones publicadas, no disponibilidad local ni interoperabilidad de la instalación.

## Decisiones, supuestos y resultados

**Propuesta:** 44 switches de acceso (16 A, 28 B), un candidato L3 por ER nuevo, tres DAC SFP+ locales por TR y un enlace óptico vertical por TR. El ER principal requiere dos interfaces ópticas compatibles cuya existencia se desconoce. Como comparación, 51 switches (16 A, 35 B) igualan capacidad activa a 51 paneles pasivos; cinco equipos por TR B requieren cuatro enlaces locales y dos saltos para uno de ellos con el candidato de cuatro SFP+.

**Resultados calculados, unidades y carácter provisional:** 20×16×2 = 640 y 42×16×2 = 1344 enlaces RJ45, 1984 total; 44×48 = 2112 o 51×48 = 2448 puertos RJ45 nominales. Topología recomendada: 11×3 = 33 conjuntos DAC locales; 11 enlaces ópticos verticales + 3 exteriores = 14 circuitos dúplex; 14×2 = 28 transceptores LR y 28 patch cords LC dúplex. Distribución: ER-A 4+2 = 6/16 SFP+; ER-B 7+2 = 9/16. Suma preliminar de máximos de ficha: 44×60 W + 2×44 W = 2728 W; para 51: 51×60 W + 88 W = 3148 W. Son escenarios, no mediciones, diseño eléctrico final ni unidades adjudicadas. Las expresiones detalladas y límites constan en `03_diseno/UNIDAD_01_ARQUITECTURA_RED_ACTIVA.md`.

**Supuestos no verificados:** interpretación de dos RJ45 por área doble, geometrías y distancias Fase 3B/5C, un switch concentrador y un uplink por TR, módulos LR compatibles, DAC compatibles, VLAN por laboratorio, gateways en ER, OSPF y 13 UPS (una por rack nuevo). PoE solo ante demanda demostrada. La alternativa de uplink individual exige como mínimo 18 puertos SFP+ en ER-A y 30/37 en ER-B, por lo que un CRS317 por ER no basta; sus 94/108 módulos y cordones ópticos son cotas inferiores sin interconexiones adicionales de distribución.

## Archivos exactos

**Creados:** `03_diseno/UNIDAD_01_ARQUITECTURA_RED_ACTIVA.md`; este reporte.

**Modificados:** `DECISIONES.md`, `PENDIENTES.md`, `09_auditorias/ULTIMO_REPORTE_CODEX.md`.

**Examinados y no modificados:** `AGENTS.md`, `README.md`, `03_diseno/DISENO_INTEGRADO_REFERENCIA_FASE2.md`, `05_materiales/MATRIZ_TECNICA_FASE2D.md`, `01_requisitos/MATRIZ_REQUISITOS.md`, reporte Fase 5C; todo `06_excel/`, `07_imagenes/` y `08_entrega/`, incluidos XLSX, nueve planos, PDF, PNG, SVG y paquete Fase 5C. `main` no se modificó.

## Verificaciones y límites

- `git fetch origin desarrollo-proyecto`: completado antes de editar; `git rev-list --left-right --count HEAD...origin/desarrollo-proyecto`: `0 0` al inicio. Se conservó el trabajo local previo y no se hizo merge ni reset.
- Control aritmético de escenarios y puertos con expresiones explícitas en el documento; `git diff --check` y `git diff --name-only` al cierre para comprobar formato y alcance. Estado Git y SHA final se confirman tras commit/push.
- Las fichas oficiales permiten verificar puertos, potencia y altura de candidatos. No se probaron equipos físicos, firmware, fibra, DAC, ACL/firewall, OSPF, energía ni climatización. La disponibilidad en Costa Rica y cotizaciones no se verificaron.

## Problemas abiertos por impacto y siguiente acción

1. **Alto:** inventario y protocolo del ER principal, rutas de retorno, compatibilidad óptica y pruebas de seguridad/offload. Sin esto no hay instalación operativa demostrada.
2. **Alto:** aceptación de activación 44/51, demanda y fallas; medir fibra, tráfico y energía antes de seleccionar equipos/UPS.
3. **Medio:** revisar con el estudiante/docente la interpretación RJ45, la procedencia asistida por IA y proveedores establecidos en Costa Rica.

**Siguiente acción mínima viable:** inventariar el ER principal y probar en laboratorio el camino TR→ER→ER principal con equipo y módulos reales, registrando versión, rutas, ACL y falla de enlace. **HECHO** = documento y registros; **VERIFICADO** = aritmética y especificaciones citadas; **PENDIENTE** = validación técnica humana y física, adquisición y puesta en servicio.
