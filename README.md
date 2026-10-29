# INA_CABLEADO_ESTRUCTURADO_CENATE

Repositorio del proyecto académico del INA para el módulo **ELTT12000 — Presupuesto de la red**, Actividad de Comprobación N.º 1. La fecha de entrega indicada por el docente es el **29 de octubre de 2026**.

## Objetivo

Preparar, diseñar y documentar de forma reproducible y auditable la infraestructura física de telecomunicaciones para dos edificios nuevos del complejo CENATE del INA. El alcance previsto comprende cableado horizontal, cuartos de telecomunicaciones (TR), cuartos de equipos (ER), canalizaciones y backbone de fibra óptica.

El repositorio contiene un escenario académico con cantidades calculadas y diseños esquemáticos. No son un dimensionamiento constructivo definitivo ni mediciones de campo. Las dimensiones arquitectónicas disponibles son preliminares y requieren validación; la primera actividad no incluye precios ni costos.

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

**Etapa:** Fase 5 - nueve laminas tecnicas A3 (PDF, PNG y SVG) incorporadas al paquete final. Revision academica humana y supuestos de campo siguen pendientes.

- Estructura base creada.
- Enunciado oficial y actualización docente preservados y auditados.
- Matriz con 76 requisitos oficiales `INA-*` y trazabilidad de los 38 registros contextuales `CTX-*`.
- No existe una rúbrica independiente; se controlan los criterios de evaluación incluidos en el enunciado.
- Plantilla Excel oficial operativa preservada sin modificación, auditada y compatible con las instrucciones.
- Entregables gráficos preliminares: nueve SVG editables y nueve PNG de 1600×1000 en `07_imagenes/fase2b/`, sujetos a revisión humana y a las mediciones pendientes.
- Modelo reproducible de capacidad y matriz de materiales candidatos disponibles; los metrajes, la selección integral de productos y las cantidades dependientes de campo permanecen pendientes.
- El original INA y la copia de trabajo Fase 2B se conservan intactos. `06_excel/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx` es un libro adicional asistido por IA, preparado bajo el escenario Fase 3B y no sustituye la revisión/comprensión del estudiante.
- Paquete de revisión Fase 2C disponible en `08_entrega/PAQUETE_REVISION_FASE2C/`, con imágenes, soporte técnico, planes de transferencia al Excel, fuentes reproducibles e inventario SHA-256.
- Guía de exposición individual de al menos ocho minutos disponible en `08_entrega/GUIA_EXPOSICION_8_MIN_FASE2C.md`.
- Escenario Fase 2D reproducible: recorridos de cobre verificados contra 90 m, fibra vertical por piso, sistema CCH por cuarto y plan de Excel para filas 2–27.
- El paquete histórico Fase 2D se conserva sin cambios. El escenario Fase 3B adopta x=75 m y y=50 m para E2/E3 y un circuito dúplex activo por enlace; son supuestos académicos, no mediciones.
- Paquete Fase 3B disponible en `08_entrega/PAQUETE_REVISION_FASE3B/`, con libro completado, memoria complementaria y nueve pares de imágenes actualizados.
- Paquete final en `08_entrega/ENTREGA_FINAL_INA_CENATE/`, con Excel, memoria tecnica, guia individual y planos Fase 5: nueve PDF A3, nueve PNG, nueve SVG y un PDF combinado de nueve paginas; incluye inventario SHA-256. Las imagenes y fuentes de `02_DISENOS_PNG/` y `03_DISENOS_EDITABLES_SVG/` son historicas.
- Las fuentes Markdown de los tres PDF y el README histórico del paquete se conservan fuera de la entrega en `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/`. Los PDF se generan con `09_auditorias/generar_pdf_entrega.py` y se comprueban con `09_auditorias/validar_pdf_entrega.py`.
- Revisión visual de los nueve PNG realizada el 2026-10-25: textos, identificación ER/TR y conexiones comprensibles; sin correcciones necesarias. No se hizo inspección visual en pantalla del XLSX ni los SVG; Excel sí abrió el XLSX por COM.
- Corrección crítica Fase 4: `06_excel/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx` se regeneró desde la plantilla usando Excel 16 COM; Excel abrió y guardó una copia de prueba y abrió también la ruta final empaquetada. Causa anterior: pérdida de declaraciones de prefijos OOXML por serialización manual con ElementTree.
- La primera actividad no debe incluir precios ni costos.
- La entrega y defensa individual son el 29 de octubre de 2026; la exposición debe durar al menos ocho minutos efectivos.

## Trazabilidad y uso de IA

La estructura y la organización documental inicial fueron preparadas el 18 de octubre de 2026 con asistencia de OpenAI Codex. El enunciado permite IA solo como apoyo conceptual, organizativo, lingüístico, de fórmulas comprendidas y visual. Prohíbe usarla como fuente técnica, para resolver directamente cálculos, generar automáticamente el Excel, sustituir el criterio del estudiante o aportar especificaciones sin verificación. El libro Fase 3B se generó por solicitud expresa del usuario, pero esta intervención no modifica el requisito académico: el estudiante debe revisar si puede entregar un artefacto asistido, comprender, corregir y defender personalmente todo contenido técnico.

Antes de trabajar, leer `README.md`, `DECISIONES.md`, `PENDIENTES.md` y `AGENTS.md`.
