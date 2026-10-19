# INA_CABLEADO_ESTRUCTURADO_CENATE

Repositorio del proyecto académico del INA para el módulo **ELTT12000 — Presupuesto de la red**, Actividad de Comprobación N.º 1. La fecha de entrega indicada por el docente es el **29 de octubre de 2026**.

## Objetivo

Preparar, diseñar y documentar de forma reproducible y auditable la infraestructura física de telecomunicaciones para dos edificios nuevos del complejo CENATE del INA. El alcance previsto comprende cableado horizontal, cuartos de telecomunicaciones (TR), cuartos de equipos (ER), canalizaciones y backbone de fibra óptica.

Esta inicialización no contiene dimensionamiento definitivo, cantidades, selección final de productos, precios, costos ni planos. Las dimensiones arquitectónicas disponibles son preliminares y requieren validación.

## Alcance conocido

- Edificio A: 4 pisos, 5 laboratorios por piso y 85 m² por laboratorio.
- Edificio B: 7 pisos, 6 laboratorios por piso y 75 m² por laboratorio.
- Cada laboratorio requiere como mínimo 16 áreas de trabajo dobles.
- Se requiere al menos un TR por piso y un ER propio en cada edificio.
- El cableado horizontal seguirá una topología en estrella y el enlace permanente de cobre no excederá 90 m.
- El backbone vertical conectará cada ER con sus TR.
- Se requieren tres interconexiones: ER principal–ER A, ER principal–ER B y ER A–ER B.
- Como información proporcionada por el estudiante, el recorrido exterior preliminar hasta uno de los ER nuevos es de 195 m: 145 m de canalización subterránea existente más 50 m de canalización subterránea nueva propuesta. Estos valores no aparecen en el enunciado oficial; falta validarlos, determinar qué edificio recibe el tramo y definir los demás recorridos.
- La contratación o prestación del servicio ISP está fuera del alcance.

## Clasificación obligatoria de la información

Todo dato o conclusión debe identificarse como una de estas categorías:

1. **Dato establecido por el docente**.
2. **Medición realizada en campo**.
3. **Supuesto de diseño**.
4. **Resultado calculado**.
5. **Especificación verificada de fabricante**.
6. **Decisión pendiente**.

Un supuesto no debe presentarse como medición o dato confirmado. Las fuentes, fórmulas, unidades, versiones de archivos y responsables de cambios deben conservarse para permitir la auditoría.

## Estructura del repositorio

| Ruta | Finalidad |
|---|---|
| `01_requisitos/` | Enunciados, rúbricas, criterios del docente y requisitos controlados. |
| `02_datos_campo/` | Mediciones, fotografías y registros de campo con procedencia. |
| `03_diseno/` | Criterios, esquemas y planos de diseño en desarrollo. |
| `04_calculos/` | Cálculos reproducibles, entradas, fórmulas y resultados. |
| `05_materiales/` | Materiales candidatos y fichas de fabricante verificadas. |
| `06_excel/` | Plantilla original del INA y copias de trabajo controladas. |
| `07_imagenes/` | Imágenes técnicas, fuentes y versiones exportadas. |
| `08_entrega/` | Entregables consolidados y reportes de cierre. |
| `09_auditorias/` | Revisiones de calidad, trazabilidad y controles de cambios. |
| `DECISIONES.md` | Registro de datos, supuestos, decisiones y cuestiones abiertas. |
| `PENDIENTES.md` | Trabajo priorizado y criterios de terminación. |
| `AGENTS.md` | Reglas permanentes para futuras sesiones de Codex. |

## Estado

**Etapa:** Fase 1 cerrada — requisitos oficiales auditados; diseño aún no iniciado.

- Estructura base creada.
- Enunciado oficial y actualización docente preservados y auditados.
- Matriz con 76 requisitos oficiales `INA-*` y trazabilidad de los 38 registros contextuales `CTX-*`.
- No existe una rúbrica independiente; se controlan los criterios de evaluación incluidos en el enunciado.
- Plantilla Excel oficial operativa preservada sin modificación, auditada y compatible con las instrucciones.
- Entregables gráficos mínimos: cinco imágenes base del enunciado más cuatro imágenes ER/TR de la actualización; total mínimo de nueve, ampliable si existen variaciones.
- Decisiones técnicas definitivas, levantamiento de campo, cálculos, selección de materiales e imágenes: pendientes.
- La primera actividad no debe incluir precios ni costos.
- La entrega y defensa individual son el 29 de octubre de 2026; la exposición debe durar al menos ocho minutos efectivos.

## Trazabilidad y uso de IA

La estructura y la organización documental inicial fueron preparadas el 18 de octubre de 2026 con asistencia de OpenAI Codex. El enunciado permite IA solo como apoyo conceptual, organizativo, lingüístico, de fórmulas comprendidas y visual. Prohíbe usarla como fuente técnica, para resolver directamente cálculos, generar automáticamente el Excel, sustituir el criterio del estudiante o aportar especificaciones sin verificación. El estudiante debe elaborar, comprender y defender personalmente todo contenido técnico.

Antes de trabajar, leer `README.md`, `DECISIONES.md`, `PENDIENTES.md` y `AGENTS.md`.
