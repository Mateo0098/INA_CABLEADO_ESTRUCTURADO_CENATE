# Reporte Codex — Unidad 04C, presupuesto integrado

**Fecha:** 2026-11-05. **Rama:** `desarrollo-proyecto`. **Objetivo:** presupuesto independiente, editable y reproducible para la ampliación operativa, con precios web documentados y estados de incompletitud. **Autoría:** Codex con asistencia de IA; revisión humana técnica/académica pendiente. **SHA de implementación:** se confirma en la respuesta terminal tras commit/publicación.

## Alcance, entradas y decisiones

**HECHO:** se leyeron `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`, índice y reporte vigentes, matrices U02/U03, memorias/conciliación/pendientes y arquitectura U01. Se examinó rama, remoto y árbol. `origin/desarrollo-proyecto` avanzó de `de36794` a `e55dd66`; se hizo `fetch` y fast-forward sin tocar `main`. Los dos archivos personales sin seguimiento de `gantt/` se preservaron.

**Entradas técnicas:** `05_materiales/unidad_02_ampliacion/UNIDAD_02_MATRIZ_MAESTRA_MATERIALES.csv` (115 filas); `05_materiales/unidad_02_ampliacion/UNIDAD_02_MEMORIA_DE_CANTIDADES.md`; `05_materiales/unidad_03_herramientas/UNIDAD_03_MATRIZ_MAESTRA_HERRAMIENTAS.csv` (108 filas); `UNIDAD_03_CONCILIACION.md`; `UNIDAD_03_PENDIENTES.md`; `03_diseno/UNIDAD_01_ARQUITECTURA_RED_ACTIVA.md`. **Fuentes comerciales:** URL y fecha por oferta en `05_materiales/unidad_04_presupuesto/UNIDAD_04C_OFERTAS.csv`; [IVA general Hacienda](https://www.hacienda.go.cr/docs/GeneralidadesIVA.pdf); [consulta arancelaria TICA](https://portaltica.hacienda.go.cr/TicaExterno/hdbaranc.aspx). No se contactaron proveedores.

**Decisión provisional:** asociar precios web de Ticomer a 44 CRS354, siete adicionales y dos CRS317 solo para mostrar una referencia parcial; no se aprueban modelos ni compras. Las ofertas CQNet/Capris quedan sin selección por IVA, disponibilidad o ingeniería pendientes. No se suma simultáneamente compra de instrumentos y servicios de igual alcance. Se conserva sin precio el tipo de cambio y sin tasa la importación. El factor comercial 1 se asigna únicamente a tres filas de switches por unidad; conversiones de cable, canasta y conduit quedan abiertas hasta despiece. Las cantidades U03 no se transforman automáticamente en compras.

## Resultados implementados

- **223 partidas** importadas por ID: 115 U02 y 108 U03, sin ID repetido. **Seis ofertas** con URL/fecha, cinco con precio publicado; tres vinculadas provisionalmente a filas. Una partida de canasta admite dos ofertas, ambas sin selección. No se acreditó disponibilidad de 44/51 switches.
- **24/223** partidas con cifra funcional de referencia; **3/223** con cantidad comercial y oferta vinculada. Las demás quedan como `PENDIENTE` en costo. Los porcentajes dinámicos de cobertura están en `01_RESUMEN` y dependen del escenario/recálculo.
- Subtotal **provisional** de switches, calculado independientemente de Excel con tarifas web y referencia general del 13 %: **₡16.537.131,90** para 44 de acceso más dos distribuidores; **₡19.073.892,63** para 51 más dos. Unidades: colones costarricenses. No son costos completos ni cotizaciones firmes.
- Ocho hojas: resumen, partidas, cotizaciones, escenarios A/B/C y 44/51, importaciones, parámetros, pendientes, control y fuentes. Fórmulas reales para conversión comercial, IVA, costo y exclusión de siete adicionales/kits/servicio. El total completo figura **NO DISPONIBLE**.

**Resultados propuestos, sin implementar como compra:** adjudicación de switches, ópticos, cable, instrumentos; comparación monetaria completa B/C; aranceles y costo final de importación. La lista priorizada consta en `05_materiales/unidad_04_presupuesto/UNIDAD_04C_PENDIENTES_COTIZACION.md`.

## Archivos

**Creados:** `05_materiales/unidad_04_presupuesto/UNIDAD_04C_OFERTAS.csv`; `generar_presupuesto.py`; `validar_presupuesto.py`; `PRESUPUESTO_INTEGRADO_RED_OPERATIVA.xlsx`; `UNIDAD_04C_MEMORIA_PRESUPUESTARIA.md`; `UNIDAD_04C_PENDIENTES_COTIZACION.md`; este reporte.

**Modificados:** `DECISIONES.md`; `PENDIENTES.md`; `09_auditorias/ULTIMO_REPORTE_CODEX.md`.

**No modificados:** matrices U02/U03, documentos canónicos U01/U02/U03, `06_excel/`, `07_imagenes/`, `08_entrega/`, `gantt/`, originales INA y `main`. Los dos archivos sin seguimiento previos de `gantt/` no se añadieron.

## Verificaciones y límites

- `python 05_materiales/unidad_04_presupuesto/generar_presupuesto.py`: 223 partidas, seis ofertas, ocho hojas.
- `python 05_materiales/unidad_04_presupuesto/validar_presupuesto.py`: IDs, relaciones, varias ofertas por ID, cantidades 44+7, importación abierta, fórmulas y ZIP íntegro: **OK**. `openpyxl.load_workbook` abrió ocho hojas y 223 filas sin error.
- `git diff --check`: se ejecuta antes del commit; resultado final se informa al publicar.
- **Límite:** `openpyxl` escribe fórmulas sin evaluarlas. Excel COM falló con `0x80070520` (sesión de inicio no disponible); no se declara apertura visual ni recálculo Excel. Los subtotales arriba se calcularon separadamente por aritmética y no son valores cacheados del XLSX.

## Problemas abiertos por impacto

1. **Alto:** despiece de rutas y secciones, cantidades comerciales, disponibilidad/IVA aplicable y ofertas firmes para materiales y switches. Sin ello no existe costo completo.
2. **Alto:** inventario y calibración institucional, contenido de kits y alcance comparable de compra, alquiler y servicio de cobre/fibra.
3. **Alto:** compatibilidad óptica/DAC, ER principal y aprobación de arquitectura 44/51; no se adjudican alternativas por precio.
4. **Medio:** tipo de cambio con fuente/fecha e impuestos de importación por clasificación arancelaria. Revisión visual y recálculo en Excel.

**VERIFICADO:** estructura del libro y trazabilidad de las ofertas iniciales accesibles. **PENDIENTE:** todo cierre comercial, fiscal, de ingeniería y revisión humana. **Siguiente acción mínima viable:** obtener ofertas firmes y disponibilidad de switches, junto con el despiece de canasta/cable, y recalcular en Excel tras aprobar los datos.
