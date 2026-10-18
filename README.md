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
- El recorrido exterior preliminar documentado hasta uno de los ER nuevos es de 195 m: 145 m de canalización subterránea existente más 50 m de canalización subterránea nueva propuesta. Falta determinar qué edificio recibe ese tramo y definir los demás recorridos.
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

**Etapa:** inicialización documental y control de versiones.

- Estructura base creada.
- Datos proporcionados para la sesión registrados sin elevar supuestos a hechos.
- Decisiones técnicas definitivas, levantamiento de campo, cálculos, materiales, Excel e imágenes: pendientes.
- Plantilla Excel original: pendiente de incorporación; deberá conservarse sin alterar su estructura y formato. La primera actividad no debe incluir precios ni costos.

## Trazabilidad y uso de IA

La estructura y los documentos iniciales fueron preparados el 18 de octubre de 2026 con asistencia de OpenAI Codex a partir de las instrucciones suministradas por el usuario. Los cálculos, textos e imágenes futuros que utilicen asistencia de IA deberán declararlo y someterse a revisión humana. Ningún contenido asistido debe atribuirse como elaborado íntegramente sin esa asistencia.

Antes de trabajar, leer `README.md`, `DECISIONES.md`, `PENDIENTES.md` y `AGENTS.md`.
