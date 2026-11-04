# Reporte Codex — Unidad 02, matriz maestra detallada de materiales

**Fecha:** 2026-11-04. **Rama:** `desarrollo-proyecto`. **SHA de implementación:** se confirma tras commit; HEAD de partida `451815d5aad17859e8d538e54a9d1e633454bf91`. **Autoría:** consolidación, fórmulas y texto generados con asistencia de Codex; revisión técnica humana obligatoria. **Estado:** implementado localmente; publicación y sincronización remota pendientes de comprobar.

## Objetivo, alcance y entradas

**HECHO:** se consolidaron 02A canastas, 02B tuberías y tomas, 02C racks y activos, y 02D fibra e interconexiones en matriz CSV con 22 columnas y memoria de cálculo. No se hizo presupuesto, edición de Excel, revisión de los 76 requisitos ni plano nuevo. Se examinaron `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`, el índice y reporte de Unidad 01, `03_diseno/UNIDAD_01_ARQUITECTURA_RED_ACTIVA.md`, `03_diseno/DISENO_INTEGRADO_REFERENCIA_FASE2.md`, `05_materiales/MATRIZ_TECNICA_FASE2D.md`, `04_calculos/MEMORIA_CANTIDADES_FASE3B.md` y SVG Fase 5C de planta A/B y TR/ER relevantes. Fuentes web consultadas 2026-11-04: [Capris, canastas](https://www.capris.cr/es/catalog/category/view/s/canastas/id/17583/), [Tecnofijaciones, barras](https://tecnofijacionescr.com/shop/category/fijacion-y-soporteria-barras-roscadas-119), [Legrand, instalación Cablofil](https://www.legrand.us/p/view-asset?downloadUrl=https%3A%2F%2Flegrand.webdamdb.com%2Fdirectdownload.php%3Fti%3D55648558%26tok%3DuWpZaF8QCwFE9W5yVab3wARR&title=Cablofil+Wire+Mesh+Cable+Tray+Installation+Instructions) y [Corning, cassette 12F](https://ecatalog.corning.com/optical-communications/US/en/generate-product-specsheet/CCH-CS12-A9-P00RE.pdf). Responsable de consulta: Codex. Fichas y páginas acreditan especificaciones/Oferta publicada, no inventario actual.

## Resultados implementados y decisiones

**HECHO:** 115 partidas individualizadas: 30 de 02A, 29 de 02B, 28 de 02C y 28 de 02D. Cada fila contiene unidad funcional/comercial, fórmula, entrada, clasificación, estado, compatibilidad y duplicaciones. Las piezas de soporte, varillas, anclajes, tuercas, arandelas, tornillos y velcro son filas independientes. Variables sin levantamiento quedan `PENDIENTE`; tres ceros están justificados por la arquitectura de cassette integrado.

**VERIFICADO aritméticamente, provisional:** 992 áreas dobles, 1 984 jacks, 992 placas; 3 124,8 m de tubo y 1 042 barras de 3 m como antecedente global, no despiece; 51 paneles y 51 organizadores de cobre; 13 racks nuevos; 14 housings y 14 organizadores ópticos; 538,65 m de cable exterior 24F y 284,025 m vertical 12F; 22 cassettes 12F y seis 24F; 204 fibras físicas a lo largo de enlaces, 408 extremos terminados propuestos y 28 fibras activadas para 14 circuitos dúplex; 28 LR y 28 cordones; 33 DAC base y 40 ampliados. 44 switches base; siete adicionales para 51, con dos distribuidores candidatos. Todo deriva de documentos de escenario citados, **no de medición de campo ni selección de compra**.

**Decisiones de control:** no adoptar la bandeja 100×50 mm como troncal. Con Ø candidato 5,8 mm, 192 cables requieren ~5 073 mm² de sección circular sumada, superior al rectángulo bruto de 5 000 mm². Esta prueba necesaria no reemplaza cálculo de ocupación/carga por segmento. No trasladar separación de soporte de 1,5 m a todas las rutas. Clasificar salidas pared/piso/columna antes de convertir las 992 bajantes históricas en compra. Se explicó que 13U/16U corresponde al CCH 1U sin organizador óptico; 15U/18U al criterio ilustrativo anterior con bloque óptico mayor; el despiece CCH + organizador óptico da 14U/17U antes de activos. UPS/PDU siguen pendientes. No adjudicar Panduit, Corning, APC, MikroTik ni Cablofil sin modelo, compatibilidad y oferta nacional verificadas.

## Archivos exactos y exclusiones

**Creados:** `05_materiales/unidad_02_ampliacion/generar_matriz.py`; `05_materiales/unidad_02_ampliacion/UNIDAD_02_MATRIZ_MAESTRA_MATERIALES.csv`; `05_materiales/unidad_02_ampliacion/UNIDAD_02_MEMORIA_DE_CANTIDADES.md`; `05_materiales/unidad_02_ampliacion/UNIDAD_02_PENDIENTES_TECNICOS.md`; este reporte.

**Modificados:** `DECISIONES.md`; `PENDIENTES.md`; `09_auditorias/ULTIMO_REPORTE_CODEX.md`.

**Examinados y no modificados:** `AGENTS.md`, `README.md`, documentos de diseño/cálculo/matriz histórica citados arriba, índice y reporte previos de Unidad 01, SVG Fase 5C. `06_excel/` completo, los nueve planos Fase 5C, PDF/PNG/SVG de la entrega, `main` y carpeta local ajena `gantt/` permanecen intactos.

## Pruebas, estado Git y límites

- `python 05_materiales/unidad_02_ampliacion/generar_matriz.py`: **115 partidas generadas**.
- Lectura `csv.DictReader` y aserciones selectivas: **115 filas, 22 columnas, cuatro subsistemas, IDs únicos, ninguna celda vacía, fórmulas y unidades presentes, componentes críticos, sin columna económica, ningún cero sin justificación**. 85 filas incluyen cantidad `PENDIENTE`; tres tienen `0 JUSTIFICADO`.
- `Get-FileHash '06_excel/Plantilla Actividades de comprobación.xlsx' -Algorithm SHA256`: `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`, igual al control histórico.
- `git diff --check`: sin errores; Git advierte conversión futura LF/CRLF en dos Markdown, sin diferencia de contenido ajena.
- Inicio: `git status --short --branch` mostró `desarrollo-proyecto` y `gantt/` sin seguimiento. `git rev-list --left-right --count HEAD...origin/desarrollo-proyecto` dio `0 0` respecto a referencia local. `git fetch origin desarrollo-proyecto` se intentó con permiso de Git; falló por `Recv failure: Connection was reset`, por lo que **la actualidad remota no se comprobó**. Commit/push y SHA final se consignarán en respuesta terminal; no se afirmará publicación sin verificarla.

**Limitaciones:** el CSV es un inventario preparado para completar con levantamiento, ficha, kit y cotización nacional; no es orden de compra, cómputo constructivo cerrado ni validación de campo. La ficha 12F respalda contenido del kit; la revisión exacta del 24F requiere confirmación. El equipo activo y ER principal requieren ensayos de Unidad 01. La revisión humana es indispensable conforme a reglas académicas.

## Problemas abiertos y siguiente acción

1. **Alto:** dimensionar troncales y soportes con número real de cables por segmento, diámetro/peso, carga y estructura del techo.
2. **Alto:** ubicar 992 salidas como pared/piso/columna y medir rutas de tubos, fibra y reservas; inventariar ER principal.
3. **Medio:** confirmar kits, rieles, PDU/UPS, DAC/LR y disponibilidad de cada referencia en Costa Rica.

**Siguiente acción mínima viable:** levantar una planta y un TR representativos, registrar por segmento cantidad simultánea de cables, tipo de salida, ruta/altura y sustrato; solicitar ficha y desglose del sistema de canasta y sus kits antes de cerrar piezas. **HECHO** = artefactos creados; **VERIFICADO** = estructura y aritmética documental citadas; **PENDIENTE** = ingeniería de detalle, campo, selección, adquisición y publicación remota.
