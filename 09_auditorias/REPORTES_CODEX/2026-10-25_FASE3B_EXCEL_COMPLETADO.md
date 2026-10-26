# Fase 3B — Excel INA completado

**Fecha:** 2026-10-25
**Rama:** `desarrollo-proyecto`
**Commit de implementación:** `2ef7816056dbb579e00cdc7021cd8487988d36b7`
**Archivo:** `06_excel/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx`
**Paquete:** `08_entrega/PAQUETE_REVISION_FASE3B/`

## Resultado

Se creó el libro de escenario desde la plantilla INA original. Sustituye los ejemplos didácticos en `Cotización técnica` y completa `Herramientas`, conserva las dos hojas, encabezados, columnas A–K, estilos y colores, y no incorpora precios/costos. `J43=SUM(J2:J41)` se eliminó únicamente en la copia y su rótulo pasó a «CANTIDADES DE MATERIALES — SIN COSTOS». El original mantiene SHA-256 `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`.

El XLSX tiene SHA-256 `1A1CC4B4A825C21BF7C421B106235D9C921BCA4A42C384209E4F9408A7B7D530`; la copia en `08_entrega/` es idéntica.

## Cantidades principales

- Cobre: 229 cajas Cat 6A de 305 m (74 A + 155 B); 51 paneles de 48 puertos; 1 984 jacks; 992 placas y cajas; 1 984 patch cords de usuario y 1 984 de rack.
- Cuartos y organización: 11 TR; 13 racks propuestos; 51 organizadores de cobre y 14 ópticos.
- Fibra: 221,55 m E1; 247,8 m E2; 69,3 m E3 de cable 24F. Backbone vertical: 89,25 m en A y 194,775 m en B de cable 12F. Terminación: 22 cassettes 12F, 6 cassettes 24F, 12 `CCH-01U`, 1 `CCH-03U` y 1 `CCH-04U`.
- Patch cords ópticos: 28 unidades, suponiendo un circuito LC dúplex activo en cada uno de 14 enlaces y dos cords por enlace (uno en cada extremo); las fibras restantes no se dan por iluminadas.
- Terminación integrada: cero pigtails y cero adaptadores comprados por separado.
- Canalización de escenario: 478 tramos de bandeja genérica 100×50 mm/3 m; 1 042 tramos de bajante PVC genérica Ø nominal 25 mm/3 m; 50 m de ducto exterior genérico Ø nominal 50 mm. Seis posiciones de registro son teóricas y no una cantidad de compra.

## Supuestos y clasificación

Se adoptaron 16 áreas dobles/laboratorio, dos RJ45 por área, un TR por piso, 3 m de reserva de cobre por enlace, 5 % de desperdicio y geometría Fase 2D. Son supuestos académicos, no mediciones. E1 mantiene la hipótesis de 145 m de canalización reportada + 50 m propuestos hacia A. E2 usa x=75 m (tres intervalos teóricos de 25 m) y E3 usa y=50 m (dos intervalos); los planos son esquemáticos sin escala y 25 m no es norma. E2/E3 tampoco son mediciones.

Las canalizaciones son especificaciones genéricas preliminares sin fabricante/modelo verificado. Diámetro interior, llenado, cargas/soportes, accesorios y trazados requieren verificación con la ficha final y el sitio. La matriz Fase 2D conserva las referencias candidatas verificadas de cobre, fibra, racks y organizadores; no se reabrió su investigación ni se comprobó disponibilidad local.

El lubricante de tiro se identifica como consumible variable, no como herramienta, y queda sin cantidad inventada. Se incluyen 3 968 etiquetas como supuesto de dos por enlace. El libro y los nueve esquemas fueron preparados con asistencia de OpenAI Codex por solicitud expresa del usuario; deben someterse a revisión académica humana y a las reglas oficiales del curso.

## Verificaciones

| Control | Resultado |
|---|---|
| `python -m py_compile 09_auditorias/crear_excel_fase3b.py 09_auditorias/validar_excel_fase3b.py 03_diseno/generar_diagramas_fase2b.py` | Sin errores de sintaxis |
| `python 09_auditorias/validar_excel_fase3b.py` | 135/135 controles aprobados |
| `git diff --cached --check` | Sin errores tras normalizar espacios finales de memoria |
| OOXML/relaciones/XML | ZIP sin errores; todas las partes XML y relaciones parseables |
| Fórmulas y unidades | 29 fórmulas de cantidad y 11 fórmulas de herramientas evaluadas contra cachés numéricas esperadas; fórmulas admitidas por AST aritmético/`ROUNDUP`; sin errores de celda |
| Estilo/estructura | Hojas y encabezados A–K verificados; `styles.xml` y estilos de celdas originales coinciden con la plantilla; costos vacíos; ejemplos eliminados |
| Materiales/diseños | Revisión de los 9 SVG/PNG y coherencia de E2/E3, canalización y patch cords ópticos; nueve PNG 1600×1000; inspección visual del esquema exterior y TR-A |
| Original y paquete | Hash original intacto; XLSX empaquetado con hash idéntico; paquete incluye memoria y nueve pares de imágenes |

**Limitación concreta:** el entorno no dispone de Microsoft Excel ni LibreOffice. Se activó recálculo automático al abrir y se verificaron las fórmulas con valores almacenados y cálculo independiente; no se afirma haber observado apertura o recálculo visual en Excel.

## Archivos

**Modificados:** `README.md`, `DECISIONES.md`, `PENDIENTES.md`, `03_diseno/generar_diagramas_fase2b.py`, los nueve SVG y nueve PNG de `07_imagenes/fase2b/`.

**Creados:** `04_calculos/MEMORIA_CANTIDADES_FASE3B.md`; `06_excel/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx`; `08_entrega/PAQUETE_REVISION_FASE3B/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx`, `MEMORIA_CANTIDADES_FASE3B.md` y `IMAGENES_REVISION/` con los nueve SVG/PNG; `09_auditorias/crear_excel_fase3b.py`, `validar_excel_fase3b.py` y este reporte.

**No modificados:** `06_excel/Plantilla Actividades de comprobación.xlsx`, copia provisional Fase 2B, entradas/resultados y memoria de cálculos Fase 2D, paquete Fase 2D, rama `main`.

## HECHO / VERIFICADO / PENDIENTE

- **HECHO:** libro completado y empaquetado; ejemplos reemplazados en ambas hojas; cantidades, fórmulas, canalizaciones de escenario y herramientas incorporadas; gráficos alineados.
- **VERIFICADO:** 135/135 controles y hashes indicados; original preservado.
- **PENDIENTE:** revisión técnica/académica del estudiante; reemplazo de E1/E2/E3, cajas y rutas por mediciones aceptadas; verificación física de canalizaciones; apertura/recalculo en la aplicación de entrega.

## Git y siguiente acción

El commit de implementación es `2ef7816056dbb579e00cdc7021cd8487988d36b7` en `desarrollo-proyecto`. El reporte y el índice de transferencia se agregan en el commit documental asociado y se publicarán juntos únicamente en `origin/desarrollo-proyecto`; `main` no se modifica. Siguiente acción mínima: comprobar el push y la coincidencia del SHA remoto.
