# Unidad 01 — arquitectura de red activa y operativa (referencia)

**Fecha:** 2026-11-01. **Estado:** propuesta documental asistida por IA, pendiente de revisión técnica humana. **Alcance:** ampliación separada de la Actividad 1 del INA; no modifica su Excel, planos ni prohibición de precios. No describe una instalación operativa, certificada o aprobada.

## 1. Entradas, procedencia y límites

| Entrada | Valor | Clasificación y procedencia |
|---|---:|---|
| Pisos y laboratorios A / B | 4 y 20 / 7 y 42 | Dato docente, `01_requisitos/MATRIZ_REQUISITOS.md` INA-003/004 |
| TR y ER nuevos | 4 y 1 / 7 y 1 | Mínimo docente INA-005/008; un TR por piso es escenario |
| Áreas dobles por laboratorio | 16 | Mínimo docente INA-011 |
| Dos RJ45 por área doble | 2 | Supuesto académico pendiente de confirmación docente, `03_diseno/DISENO_INTEGRADO_REFERENCIA_FASE2.md` |
| Enlaces horizontales A / B | 640 / 1344 | Resultado: 20×16×2 / 42×16×2; 1984 total Cat 6A de escenario |
| Enlaces ER–TR y exteriores | 11 OS2 12F; E1/E2/E3 OS2 24F | Propuesta pasiva histórica; INA-005/014/019 y diseño Fase 5C |
| Longitudes de E1/E2/E3 | 221,55 / 247,80 / 69,30 m de cable | Supuestos y resultados del escenario Fase 3B/5C; **no son mediciones** |
| ER principal existente | ubicación e interfaces desconocidas | Hecho docente: existe ER; inventario activo y compatibilidad pendientes |

La matriz `05_materiales/MATRIZ_TECNICA_FASE2D.md` solo cubre materiales pasivos. Los 51 paneles de 48 posiciones tienen 2448 posiciones, pero 1984 enlaces asignados; un panel no equivale a un switch. INA-015 excluye un ISP nuevo. INA-044 impide importes en la Actividad 1. La adquisición de la ampliación priorizará proveedores establecidos en Costa Rica; aquí no se afirma disponibilidad, proveedor, precio ni cotización. Toda importación futura exige justificar ausencia de alternativa nacional o ventaja verificable y contabilizar producto, transporte, seguro si aplica, tributos, nacionalización y entrega local.

## 2. Dos escalas de activación

| Magnitud | 44 switches: mínimo de puertos asignados | 51 switches: igualar posiciones de panel |
|---|---:|---:|
| A: switches/TR × 4 TR | 4×4 = 16 | 4×4 = 16 |
| B: switches/TR × 7 TR | 4×7 = 28 | 5×7 = 35 |
| Total de acceso | **44** | **51** |
| Puertos RJ45 1G nominales | 44×48 = **2112** | 51×48 = **2448** |
| Puertos asignados a enlaces horizontales | **1984** | **1984** |
| Puertos activos nominales libres | 128 (A:128; B:0) | 464 (A:128; B:336) |
| Equipo de distribución candidato | 1 en ER-A + 1 en ER-B | Igual, sujeto a topología |

El escenario de 44 deja sin activación simultánea las 48 posiciones pasivas de reserva por TR B, pero cubre sus 192 enlaces asignados. Los 51 permiten activar toda posición pasiva bajo este modelo de 48 puertos/switch; no se afirma que todas estén cableadas a puestos. Los puertos de administración separados no se cuentan como capacidad de usuario.

## 3. Candidatos y especificaciones verificadas

Consulta de fichas oficiales del fabricante el **2026-11-01**, responsable de registro: Codex; selección y compatibilidad final pendientes.

| Candidato | Confirmado en ficha oficial | Uso propuesto, no adjudicado |
|---|---|---|
| [MikroTik CRS354-48G-4S+2Q+RM](https://mikrotik.com/product/crs354_48g_4splus2qplusrm) | 48 RJ45 1G, 4 SFP+ 10G, 2 QSFP+ 40G, 44 mm ≈1U, consumo máximo 60 W con accesorios, 50 W sin ellos, dos entradas AC 100–240 V, tres ventiladores. Manual: [CRS354](https://help.mikrotik.com/docs/spaces/UM/pages/17956968/CRS354-48G-4S%202Q%20RM). | Acceso sin PoE de salida; cuatro SFP+ permiten tres enlaces locales y uno óptico en el concentrador de cada TR del escenario 44. |
| [MikroTik CRS317-1G-16S+RM](https://mikrotik.com/product/crs317_1g_16s_rm) | 16 SFP+ 10G, RJ45 1G de gestión, 44 mm ≈1U, máximo 44 W, dos entradas AC 100–240 V, dos ventiladores. [Manual](https://help.mikrotik.com/docs/spaces/UM/pages/17956940/CRS317-1G-16S%20RM). | Un candidato L3 por ER nuevo. Capacidad de rutas/ACL/rendimiento condicionada por RouterOS, configuración y prueba. |

10GBASE-LR dúplex LC sobre OS2 es la hipótesis óptica. El [S+31DLC10D oficial](https://mikrotik.com/product/s_31dlc10d) ejemplifica 10 Gb/s, 1310 nm, monomodo y LC dúplex hasta 10 km; **no queda seleccionado**. Deben verificarse módulos concretos en ambas plataformas, presupuesto óptico extremo a extremo, potencia, pérdidas de empalmes/conectores, codificación y versión de firmware. Un enlace dúplex usa dos fibras, dos transceptores (uno por equipo) y dos patch cords LC dúplex (uno por extremo). El tramo fijo no es un patch cord.

## 4. Arquitectura física: alternativas obligatorias

**Alternativa A — concentración local, recomendación provisional para 44.** En cada TR hay cuatro CRS354 candidatos: tres equipos de acceso subordinados conectan por un enlace SFP+ 10G local al cuarto, que concentra; este conecta por un enlace óptico 10G OS2 12F al CRS317 del ER. Cada equipo tiene camino explícito: puesto → switch → enlace local si corresponde → concentrador TR → fibra ER–TR → distribución. Los tres enlaces locales pueden usar conjuntos DAC SFP+ de longitud compatible con el rack, si la compatibilidad se confirma; al ser locales no consumen fibras del backbone ni módulos LR. Si se emplea AOC u óptica local, cambia el inventario; no se sustituyen silenciosamente los 33 DAC por LR.

Puertos SFP+ por TR: concentrador 3 locales + 1 uplink = **4/4**; cada subordinado 1/4. En ER-A: cuatro enlaces verticales + E1 + E3 = **6/16 SFP+**; ER-B: siete + E2 + E3 = **9/16 SFP+**. Quedan 10 y 7 puertos respectivamente, antes de gestión, redundancia u otros servicios. ER principal necesita **dos interfaces ópticas compatibles** para E1/E2, además de capacidad de encaminamiento y alimentación; se desconoce si existen. E3 ocupa una interfaz en cada ER nuevo. La capacidad de 16 puertos por CRS317 **no autoriza** uplinks individuales de todos los switches.

**Alternativa A ampliada — 51 switches.** En cada TR B se requieren cinco switches. Con solo cuatro SFP+ en el concentrador, una topología local determinable usa: concentrador → dos subordinados y un segundo concentrador local; el segundo → quinto equipo; más uplink del primero al ER. Son cuatro enlaces locales por TR B y **dos saltos locales** para el quinto. En los TR A permanecen tres enlaces locales. Ocupación máxima del primer equipo B: 4/4 SFP+; segundo: 2/4. Funciona topológicamente, pero aumenta dependencia del equipo central y del intermedio. Antes de aprobar 51, valorar un agregador TR adicional de ≥6 puertos SFP+ verificados, o una distribución con más puertos; ambos cambian cantidades, carga y costos. No se presentan como equipos elegidos.

**Alternativa B — uplink óptico individual de cada switch.** Cada switch de acceso tiene un enlace ER–TR propio, sin enlaces locales; elimina el concentrador TR como punto único, pero las 12 fibras por cable ER–TR solo ofrecen seis pares dúplex. Cuatro o cinco circuitos caben en fibras, sujetos a terminación y presupuesto óptico. Exige por lo menos 44/51 circuitos verticales, frente a 11 de A, y capacidad de distribución A **16+2=18** y B **28+2=30** para 44, o B **35+2=37** para 51. Un único CRS317 de 16 SFP+ por ER es insuficiente en ambos casos. Harían falta equipos/puertos adicionales y enlaces entre distribución todavía por diseñar; por ello los conteos ópticos siguientes son **cotas inferiores**, no lista final de adquisición.

| Recurso, fórmula | A recomendada 44 | A ampliada 51 | B individual 44 | B individual 51 |
|---|---:|---:|---:|---:|
| Enlaces locales SFP+ dentro de TR | 11×(4−1)=**33** | 4×3 + 7×4=**40** | 0 | 0 |
| Conjuntos DAC locales (uno/enlace) | **33** | **40** | 0 | 0 |
| Extremos SFP+ locales (2/enlace; integrados en DAC) | **66** | **80** | 0 | 0 |
| Circuitos ópticos verticales | **11** | **11** | **44** | **51** |
| Circuitos ópticos exteriores | **3** | **3** | **3** | **3** |
| Módulos LR, 2×(verticales+exteriores) | **28** | **28** | **≥94** | **≥108** |
| Patch cords LC dúplex, 2×(verticales+exteriores) | **28** | **28** | **≥94** | **≥108** |
| Pares de fibra ocupados: vertical/exterior | 11/3 | 11/3 | 44/3 | 51/3 |

Los **28 transceptores históricos** y 28 cordones representan solo 14 circuitos ópticos entre cuartos. A incorpora además 33 o 40 conjuntos DAC, cuyos extremos SFP+ no se suman a los módulos LR ni a los patch cords ópticos. B requiere cassettes/patching adecuados para 4 o 5 pares por TR y sus extremos ER, y puede requerir óptica adicional para interconectar la distribución. La diferencia de costo no puede cuantificarse sin oferta local, módulos compatibles, ingeniería de distribución y rutas; B aumenta módulos, cordones, puertos ER y complejidad, mientras A concentra fallas y tráfico.

**Sobresuscripción nominal, no pronóstico de tráfico:** A de 44, hasta 192 puertos de 1 Gb/s por TR comparten un uplink de 10 Gb/s: **19,2:1** frente a velocidad nominal simultánea. A con 51 en B, hasta 240:10 = **24:1**. El concentrador y la fibra son puntos únicos de falla; los DAC subordinados también aíslan su switch si fallan. Dos fuentes AC por equipo protegen contra una fuente fallida solo si hay dos alimentaciones útiles; no crean redundancia de camino. Para resiliencia real se requieren enlaces/rutas independientes, equipos de distribución adicionales y convergencia probada. E1/E2/E3 forman un triángulo lógico potencial, pero pueden compartir ducto y no prueban diversidad física.

## 5. Lógica, encaminamiento y condiciones de seguridad

Hipótesis: una VLAN por laboratorio (62 VLAN de usuario en total, identificadores y subredes pendientes), con puerto de usuario de acceso y transporte etiquetado por enlaces locales y verticales. Los gateways L3 residirían en el equipo de distribución del ER correspondiente; VLAN de gestión separada. Deben definirse también servicios DHCP/DNS, direccionamiento, ACL entre laboratorios, tratamiento de invitados/voz/AP si existieran, prioridad de tráfico, monitoreo y gestión. No se asignan rangos IP ficticios.

E1/E2/E3 se proponen como interfaces L3 enrutadas de 10 Gb/s, sin extender VLAN de usuario entre edificios. OSPF en RouterOS v7 es **candidato**, sujeto a autorización/configuración del ER principal, direccionamiento, área, autenticación, métricas, filtrado de anuncios y rutas de retorno. Si el principal no participa en OSPF, se deberá diseñar intercambio de rutas estáticas o protocolo aceptado por la institución; no basta instalar dos interfaces. Probar pérdida de E1/E2/E3, convergencia y ausencia de bucles. La [documentación oficial OSPF](https://help.mikrotik.com/docs/spaces/ROS/pages/9863229/OSPF) describe el protocolo, no confirma compatibilidad con el ER existente.

La [documentación oficial de L3 hardware offloading](https://help.mikrotik.com/docs/spaces/ROS/pages/62390319/L3%2BHardware%2BOffloading) incluye CRS317 y CRS354, pero advierte que rutas aceleradas pueden eludir CPU/firewall; ACL de switch son sin estado y el firewall con seguimiento de conexiones usa CPU o FastTrack bajo condiciones. Por ello se deben probar en laboratorio, con versión RouterOS registrada, VLAN, ACL, firewall, rutas OSPF, rendimiento y estado real de offload. No se promete aceleración y filtrado completo simultáneos ni rendimiento L3 a velocidad de línea bajo reglas aún indefinidas.

## 6. Energía, espacio y adquisición

| Carga activa máxima de ficha, sin óptica externa/otros equipos adicionales | Escenario 44 | Escenario 51 |
|---|---:|---:|
| Acceso A, 16×60 W | 960 W | 960 W |
| Acceso B, 28×60 W o 35×60 W | 1680 W | 2100 W |
| Distribución nueva, 2×44 W | 88 W | 88 W |
| **Suma aritmética de máximos de ficha** | **2728 W** | **3148 W** |

Son límites preliminares de equipos candidatos, no demanda medida ni potencia eléctrica de diseño final. Por TR A: 4×60 = 240 W; TR B: 240 W o 300 W. En ER nuevo: mínimo 44 W por distribución, antes de transceptores, administración, ventilación y otros equipos. No se atribuye carga al ER principal desconocido. Las fichas dan dos entradas AC; PDU A/B independientes serían propuesta donde existan circuitos separados. Si ambas entradas van a una sola PDU/UPS, no hay redundancia eléctrica real. **13 UPS** = 11 TR + 2 ER nuevos, hipótesis de una por rack nuevo, sin selección ni autonomía. Número/tipo de tomas PDU, VA/W reales, factor de potencia, baterías, tiempo de respaldo, puesta a tierra, circuitos, protecciones y climatización requieren levantamiento y cálculo eléctrico. No incluir UPS del ER principal sin inventario.

Ocupación frontal mínima: referencia pasiva de `03_diseno/DISENO_INTEGRADO_REFERENCIA_FASE2.md` = 15U por TR A y 18U por TR B; más 4×1U = **19U A / 22U B** en escenario 44, o 5×1U = **23U B** en 51. La distribución añade 1U activo por ER. No se concluye que el rack 42U sea suficiente: quedan UPS, PDU, espacios térmicos, profundidad, radio de curvatura, cableado y mantenimiento. Verificar ventilación con disipación térmica real, flujo de aire y ambiente del cuarto. PoE se dimensionará solo si aparece demanda probada de AP, telefonía, cámaras u otros equipos; las computadoras no justifican PoE. El CRS354 candidato sin sufijo P no ofrece PoE de salida documentado.

## 7. Matriz de decisiones y cierre

| Estado | Decisión o dato | Evidencia/acción |
|---|---|---|
| **Confirmado del escenario académico** | 62 laboratorios, 11 TR, 1984 enlaces condicionados a dos RJ45/área, tres enlaces exteriores | Requisitos INA y cálculos arriba; aclarar interpretación docente |
| **Especificación verificada de fabricante** | Puertos, dimensiones, entradas AC y máximos W de CRS354/CRS317 | Fichas oficiales consultadas 2026-11-01; no implica adjudicación |
| **Resultado calculado** | 44/51 switches; topologías y conteos de tabla; 2728/3148 W | Expresiones y unidades conservadas en este documento |
| **Propuesta provisional** | 44 switches, concentración local 3 DAC/TR, un LR por extremo ER–TR, CRS317 por ER, VLAN por laboratorio, gateways ER y enlaces exteriores enrutados | Validar tráfico, compatibilidad, seguridad y falla |
| **Pendiente** | ER principal, PoE, rutas, óptica, redundancia, UPS, PDU, proveedores nacionales, costos y aprobación | Inventario, ensayos, mediciones y ofertas futuras separados de Actividad 1 |

Para declarar completa la arquitectura: (1) confirmar con docente la interpretación RJ45; (2) inventariar ER principal y acordar enrutamiento/rutas de retorno; (3) medir rutas y certificar fibra/terminaciones, compatibilidad óptica y presupuesto de pérdidas; (4) medir demanda de tráfico, PoE y tolerancia a fallas; (5) probar RouterOS, VLAN, OSPF/alternativa, ACL/firewall y offload; (6) levantar energía, rack, climatización y UPS; (7) verificar proveedor establecido en Costa Rica y disponibilidad de **todos** los equipos, accesorios y herramientas; (8) revisión y aprobación técnica humana. Hasta entonces es un diseño funcional de referencia, sin certificación ni presupuesto.
