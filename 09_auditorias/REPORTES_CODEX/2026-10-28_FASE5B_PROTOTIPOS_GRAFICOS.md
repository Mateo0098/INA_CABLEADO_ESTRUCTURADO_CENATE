# Reporte Codex — Fase 5B: prototipos TR-A y planta A

**Fecha:** 2026-10-28. **Rama:** `desarrollo-proyecto`. **Commit de implementación:** `66459462a63125afc91dabcb3ff5f80e5038afca`. **Estado al redactar:** implementación confirmada localmente; publicación del reporte e índice pendiente del commit documental.

## Objetivo, alcance y estado

**HECHO.** Se crearon exclusivamente dos prototipos independientes: elevación frontal del rack TR-A y planta de canalizaciones del edificio A. Cada uno tiene SVG editable, PDF vectorial A3 horizontal y PNG de 4961 × 3508 píxeles (300 ppp). `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/COMPARATIVO_FASE5_VS_PROTOTIPOS.pdf` tiene dos páginas A3, cada una con la Fase 5 vigente, el prototipo y una ampliación de ambas.

**No modificados:** las nueve láminas vigentes de `08_entrega/ENTREGA_FINAL_INA_CENATE/06_PLANOS_TECNICOS/`, sus otras siete láminas, el Excel definitivo, la memoria, los originales y `main`. Los prototipos requieren evaluación antes de extender la técnica gráfica.

## Entradas y fuentes examinadas

- `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`, el índice y el reporte de Fase 5.
- `08_entrega/ENTREGA_FINAL_INA_CENATE/01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx`, `04_calculos/MEMORIA_CANTIDADES_FASE3B.md`, `04_calculos/MEMORIA_CALCULOS_FASE2D.md`, `05_materiales/MATRIZ_TECNICA_FASE2D.md` y `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/MEMORIA_TECNICA_RESUMIDA.md`.
- Láminas Fase 5 `02_pla_a` y `07_tr_a` en SVG, PDF y PNG, más `09_auditorias/generar_planos_fase5.py` y su validador.
- **Especificación de fabricante verificada; consulta 2026-10-28:** [Panduit NetKey 111369255](https://www.panduit.com/content/dam/panduit/en/website/about-us/thought-leadership/documents/111369255.pdf), candidato NK6XPPG48Y de 48 puertos Cat 6A y 2U; [Corning LAN-2564-AEN](https://www.corning.com/catalog/coc/documents/selection-guides/LAN-2564-AEN.pdf), CCH-01U de 1U con dos posiciones; [Corning ficha CCH](https://www.corning.com/catalog/coc/documents/product-family-specifications/pfss/c/en-US/cch-pigtailed-splice-cassette_CALA_AEN.pdf), cassette CCH-CS12-A9-P00RE de 12F OS2 y LC dúplex. Los símbolos no son una selección de compra.

## Cantidades, decisiones y supuestos

| Elemento | Valor con unidad | Clasificación y fundamento |
|---|---:|---|
| TR-A | 4 paneles pasivos × 48 = 192 posiciones | Diseño vigente y Excel. |
| Puertos TR-A | 160 asignados y 32 libres | Resultado: 5 laboratorios × 16 WA dobles × 2 RJ45 = 160; 192 − 160 = 32. Asignado no implica conexión activa. |
| PP04 | 01–16 asignados; 17–48 libres | Representación coherente con Fase 5; PP01–03 tienen 48 asignados cada uno. |
| Óptica TR-A | 1U CCH-01U; 1 cassette integrado OS2 12F; 6 adaptadores LC dúplex | Diseño vigente y especificación verificada. Sin accesorios duplicados. |
| Rack propuesto | U01 óptica, U02 organizador óptico, U03–U14 cuatro paneles de 2U y cuatro organizadores de 1U; U15–U42 libres | 14U ocupadas de 42U. Montaje final pendiente. |
| Laboratorios A | 5 laboratorios supuestos de 85 m²; 16 WA dobles y 32 Cat 6A por laboratorio | Geometría y cantidades académicas; no mediciones de campo. |
| Canalización | Bandeja preliminar 100 × 50 mm; tubo nominal Ø25 mm | Supuesto de diseño. Dos tubos independientes de ejemplo desde cada caja, uno por salida doble, con dos Cat 6A por tubo como ocupación preliminar. |

El rack representa rieles y perforaciones por U, 192 bocas frontales RJ45 con contacto y pestillo, organizadores con dedos, cassette de seis LC dúplex, segunda bahía libre, entrada posterior agrupada y un cordón frontal de ejemplo con extremo libre. La planta representa muros dobles, puertas, bandeja de dos bordes con travesaños, soportes, cinco derivaciones, pasamuros, cajas, tubos de doble trazo, salidas dobles y dos detalles ampliados.

**Supuesto no verificado:** ubicación de laboratorios, TR, puertas, salidas, cajas, soportes y recorridos. La planta declara “sin escala”; la elevación conserva paso vertical constante por U sin escala de ancho. No se inventaron cotas de obra ni equipos activos.

## Archivos exactos

**Creados en el commit de implementación:**

1. `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/README.md`
2. `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/SVG_EDITABLE/P1_TR_A.svg`
3. `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/SVG_EDITABLE/P2_PLANTA_A.svg`
4. `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/PDF_A3/P1_TR_A.pdf`
5. `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/PDF_A3/P2_PLANTA_A.pdf`
6. `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/PNG/P1_TR_A.png`
7. `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/PNG/P2_PLANTA_A.png`
8. `08_entrega/PROTOTIPOS_GRAFICOS_FASE5B/COMPARATIVO_FASE5_VS_PROTOTIPOS.pdf`
9. `09_auditorias/generar_prototipos_fase5b.py`
10. `09_auditorias/validar_prototipos_fase5b.py`

**Modificados en el commit de implementación:** `DECISIONES.md`, `PENDIENTES.md`. **Creados/modificados en el cierre documental:** este reporte y `09_auditorias/ULTIMO_REPORTE_CODEX.md`. **Examinados y no modificados:** los archivos de entrada indicados arriba, las nueve láminas Fase 5 y el PDF combinado vigente.

## Pruebas, revisión gráfica y límites

- `python 09_auditorias/generar_prototipos_fase5b.py`: creó 2 SVG, 2 PDF A3, 2 PNG 300 ppp y un comparativo vectorial de 2 páginas A3.
- `python 09_auditorias/validar_prototipos_fase5b.py`: **29/29** controles. Comprobó 192 conectores dibujados, 48 por panel, 160 asignados y 32 libres, numeración 01–48, 42U, cinco laboratorios, celdas de cantidades del Excel, márgenes de texto, formato PDF/PNG y ausencia de raster incrustado en PDF.
- `git diff --cached --check`: sin errores de espacios. Commit de implementación `66459462a63125afc91dabcb3ff5f80e5038afca` en `desarrollo-proyecto`.
- **VERIFICADO visualmente:** se renderizaron e inspeccionaron ambas páginas completas y las ampliaciones del comparativo, más recorte de bandeja, tubos y cajas y la parte inferior del rack. Se corrigieron los bloques numerados del panel, el riel de 42U, una etiqueta sobrepuesta, el cajetín de revisión y la ruta que antes compartía tubo para dos salidas. La versión final presenta tubos independientes desde cada caja y ninguna superposición material observada en esas zonas.

**Limitaciones:** no hubo impresión física ni medición de campo. Las pruebas no certifican capacidad de bandeja/tubo, seguridad, montaje, compatibilidad del recinto ni aceptación académica. Los símbolos son ilustrativos, no dibujos de fabricación.

## Problemas abiertos priorizados y siguiente acción

1. **Alto para continuar:** estudiante y ChatGPT evalúan si el detalle gráfico de los dos prototipos cumple el objetivo. Hasta esa valoración no se rediseñan las otras siete láminas.
2. **Alto antes de obra/compra:** medir y validar trazados, pasamuros, ocupación, soportes y posición final de TR/WA.
3. **Medio para defensa:** el estudiante revisa y comprende el contenido asistido por IA y sus supuestos.

**Siguiente acción mínima viable:** abrir el PDF comparativo y los dos PDF A3, registrar aceptación o correcciones. **HECHO** = archivos producidos; **VERIFICADO** = formatos, cantidades y renders revisados; **PENDIENTE** = evaluación del estudiante/ChatGPT y datos de campo.
