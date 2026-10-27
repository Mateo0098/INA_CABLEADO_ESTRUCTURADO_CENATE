# Cierre Fase 4 — formatos PDF del paquete final

**Fecha:** 2026-10-26. **Rama:** `desarrollo-proyecto`.
**Commit de implementación:** `726a161d6257cd1d30c27562d0be9f8a7ef79daa`.
**Estado Git al redactar:** árbol de implementación limpio en `desarrollo-proyecto`, `HEAD` adelantado un commit respecto de `origin/desarrollo-proyecto`; publicación del reporte y del índice de transferencia pendiente del commit documental.

## Objetivo, alcance y fuentes

**HECHO:** convertir la memoria y la guía del paquete `08_entrega/ENTREGA_FINAL_INA_CENATE/` a PDF de lectura, crear un índice PDF, conservar los Markdown fuera del paquete, actualizar el inventario y dejar un proceso reproducible de generación y validación. No se abrió ni modificó el XLSX ni se editaron los nueve pares PNG/SVG.

**Entradas examinadas:** `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`, `09_auditorias/ULTIMO_REPORTE_CODEX.md`, `09_auditorias/REPORTES_CODEX/2026-10-25_FASE4_CORRECCION_XLSX.md`, el README y el inventario anteriores del paquete, los dos Markdown originales y la lista de archivos del paquete. `origin` coincidía con `https://github.com/Mateo0098/INA_CABLEADO_ESTRUCTURADO_CENATE.git`; `git fetch origin desarrollo-proyecto` finalizó y la divergencia inicial era `0 0`. La rama `main` no se tocó.

## Decisiones de formato y supuestos

- **Decisión documental:** A4, márgenes de 49 puntos, tipografía Arial incrustada, encabezados jerárquicos, tablas con ancho controlado y encabezado repetido, pie con número de página. El índice PDF sustituye al README Markdown como puerta de entrada del paquete.
- **Fuentes intactas:** los Markdown de memoria y guía se trasladaron con coincidencia SHA-256; el README anterior del paquete se conservó como fuente histórica. El índice nuevo tiene fuente Markdown interna para permitir regeneración.
- **Supuestos técnicos no verificados:** no se revisaron ni cambiaron. Siguen provisionales, entre otros, dos RJ45 por área doble, rutas E1/E2/E3, reservas, desperdicio, canalizaciones y un circuito óptico dúplex activo por enlace.
- **Procedencia:** la conversión, el índice y las verificaciones fueron realizados con asistencia de OpenAI Codex. La revisión técnica y académica personal del estudiante sigue pendiente.

## Archivos exactos

**Modificados:**

- `README.md`
- `DECISIONES.md`
- `PENDIENTES.md`
- `08_entrega/ENTREGA_FINAL_INA_CENATE/INVENTARIO_SHA256.txt`
- `09_auditorias/ULTIMO_REPORTE_CODEX.md` (índice de transferencia de este cierre)

**Trasladados sin cambiar contenido:**

- `08_entrega/ENTREGA_FINAL_INA_CENATE/04_MEMORIA_TECNICA/MEMORIA_TECNICA_RESUMIDA.md` → `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/MEMORIA_TECNICA_RESUMIDA.md`
- `08_entrega/ENTREGA_FINAL_INA_CENATE/05_DEFENSA/GUIA_DEFENSA_INDIVIDUAL_8_MIN.md` → `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/GUIA_DEFENSA_INDIVIDUAL_8_MIN.md`
- `08_entrega/ENTREGA_FINAL_INA_CENATE/README.md` → `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/README_PAQUETE_FASE4.md`

**Creados:**

- `08_entrega/ENTREGA_FINAL_INA_CENATE/04_MEMORIA_TECNICA/MEMORIA_TECNICA_RESUMIDA.pdf`
- `08_entrega/ENTREGA_FINAL_INA_CENATE/05_DEFENSA/GUIA_DEFENSA_INDIVIDUAL_8_MIN.pdf`
- `08_entrega/ENTREGA_FINAL_INA_CENATE/INDICE_ENTREGABLES.pdf`
- `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/INDICE_ENTREGABLES.md`
- `09_auditorias/generar_pdf_entrega.py`
- `09_auditorias/validar_pdf_entrega.py`
- Este reporte.

**No modificados:**

- `08_entrega/ENTREGA_FINAL_INA_CENATE/01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx`
- `08_entrega/ENTREGA_FINAL_INA_CENATE/02_DISENOS_PNG/01_backbone_exterior.png`, `02_planta_tipica_edificio_A.png`, `03_planta_tipica_edificio_B.png`, `04_laboratorio_tipico_A.png`, `05_laboratorio_tipico_B.png`, `06_ER_A.png`, `07_TR_A.png`, `08_ER_B.png`, `09_TR_B.png`
- `08_entrega/ENTREGA_FINAL_INA_CENATE/03_DISENOS_EDITABLES_SVG/01_backbone_exterior.svg`, `02_planta_tipica_edificio_A.svg`, `03_planta_tipica_edificio_B.svg`, `04_laboratorio_tipico_A.svg`, `05_laboratorio_tipico_B.svg`, `06_ER_A.svg`, `07_TR_A.svg`, `08_ER_B.svg`, `09_TR_B.svg`
- Las fuentes `06_excel/`, `07_imagenes/`, los cálculos técnicos y `main`.

## Resultado implementado y cantidades

**HECHO:** el paquete contiene un XLSX, nueve PNG, nueve SVG y tres PDF de lectura; el inventario SHA-256 registra **22 archivos** (unidad: archivo; conteo de rutas del paquete, definitivo para este commit), sin incluirse a sí mismo. No hay Markdown versionado dentro del paquete. Los tres PDF tienen **2, 3 y 1 páginas A4**, respectivamente (unidad: página; resultado definitivo de la representación actual). Las fuentes Markdown permanecen en `08_entrega/FUENTES_INTERNAS_PAQUETE_FINAL/`.

**Cantidades técnicas conservadas, no recalculadas:** por ejemplo, 229 cajas de cable Cat 6A de 305 m, 1 984 enlaces y 538,65 m de fibra exterior OS2 24F figuran en la memoria como resultados del escenario provisional. Su fundamento y condiciones constan en la memoria; no son mediciones de campo ni cantidades definitivas de compra. No se añadieron precios.

**Resultados meramente propuestos:** ninguna modificación técnica. La aprobación del contenido y de los supuestos por el estudiante sigue pendiente.

## Pruebas y límites

- `python 09_auditorias/generar_pdf_entrega.py`: generó los tres PDF desde las fuentes internas. Entorno: ReportLab 5.1.0 y Markdown 3.11.2.
- `python 09_auditorias/validar_pdf_entrega.py --render-dir "$env:TEMP\INA_PDF_QA_2026-10-26"`: PyMuPDF 2.0 cotejó **64/64 fragmentos** de memoria, **44/44** de guía y **25/25** de índice; comprobó A4, numeración, límites de texto, ausencia de páginas vacías y el inventario. Renderizó las **seis páginas** a PNG.
- Inspección visual de los seis PNG renderizados: encabezados y caracteres legibles, tablas sin recortes ni solapamientos visibles, ninguna página vacía. El encabezado de la tabla de memoria se repite en la segunda página.
- Comparación del inventario anterior con los archivos actuales: **19/19 SHA-256 iguales** para el XLSX y los nueve PNG/nueve SVG. Los Markdown originales conservaron sus hashes anteriores: memoria `0A94F4716F64002D198BE09FCB195EC09D95F786F33336A060B1CE4E4A7A59CA`; guía `25A27BFA45E89548C9D8A3FDBA408417F9EDAD5D9B2ED346DC45E452CB794573`.
- `git diff --cached --check`: sin errores antes del commit de implementación. Los avisos de fin de línea de Git no afectaron los PDF ni el inventario.
- **Límite:** no se hizo prueba de impresión física ni de apertura en un lector PDF distinto de PyMuPDF. La comprobación fue de formato, texto e imagen renderizada; no valida la exactitud técnica o académica del escenario.

## Problemas abiertos y siguiente acción

1. **P1 — entrega académica:** el estudiante debe revisar el contenido técnico asistido por IA, contrastarlo con el enunciado y ensayar la defensa.
2. **P1 — ingeniería de campo:** rutas, dimensiones, canalizaciones, capacidad de racks y otras entradas provisionales requieren validación antes de obra o compra.
3. **P3 — entorno local:** una sesión de Excel abierta creó un archivo temporal `~$` en la carpeta del XLSX. Está ignorado por Git, no se incluyó en el inventario ni se versionó; cerrar esa sesión retirará el bloqueo temporal.

**Siguiente acción mínima viable:** abrir los tres PDF, el XLSX y los PNG en las aplicaciones que usará el estudiante, completar su revisión académica y ensayar la exposición. El commit documental que incluye este reporte y `09_auditorias/ULTIMO_REPORTE_CODEX.md` se publicará en `origin/desarrollo-proyecto`; su SHA final se comunicará en la respuesta terminal.

## Estado de cierre

- **HECHO:** conversión y organización implementadas en `726a161d6257cd1d30c27562d0be9f8a7ef79daa`.
- **VERIFICADO:** integridad del contenido fuente, representación A4 de todas las páginas y conservación binaria de los 19 artefactos protegidos.
- **PENDIENTE:** revisión humana y confirmación de publicación del commit documental.
