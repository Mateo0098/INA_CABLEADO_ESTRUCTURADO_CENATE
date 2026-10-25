# Fase 2D — cierre de cantidades y preparación del Excel INA

**Fecha:** 2026-10-25

**Rama:** `desarrollo-proyecto`

**Commit de implementación:** `470112ef46731e5cc301a7f37a2cd913b82f367e`

**Estado:** base técnica explicable y transferible al Excel; no es entrega final.

## 1. Objetivo y alcance

Se cerraron cantidades mediante un escenario académico explícito, sin convertir distancias supuestas en mediciones. Se calcularon rutas de cobre y fibra vertical, se mantuvieron E2/E3 como variables, se consolidó un sistema pasivo comercial compatible, se preparó la correspondencia Excel y se actualizaron únicamente cuatro figuras ER/TR afectadas.

No se repitió la auditoría de requisitos, no se seleccionaron equipos activos, no se incorporaron precios y no se editó ningún libro Excel.

## 2. Entradas y fuentes examinadas

- `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`.
- Índice e informe Fase 2C.
- `04_calculos/REVISION_VARIABLES_FASE2C.md`.
- `05_materiales/MATRIZ_TECNICA_FASE2C.md`.
- `06_excel/PLAN_TRANSFERENCIA_EXCEL_FASE2C.md`.
- `08_entrega/PAQUETE_REVISION_FASE2C/README.md`.
- Geometrías y figuras existentes en `03_diseno/` y `07_imagenes/fase2b/`.
- Documentación primaria de Panduit, Corning y Schneider Electric/APC enlazada en `05_materiales/MATRIZ_TECNICA_FASE2D.md`, consultada 2026-10-25.

## 3. Resultados implementados

### 3.1 Cobre

**Supuestos, no mediciones:** TR al extremo del pasillo; 3 m internos en TR; cruce de 1,2 m; profundidad de laboratorio 10 m; distribución lateral según fachada; bajante de 3 m; reserva de 3 m por enlace; desperdicio de compra de 5 %.

| Resultado | A | B | Total |
|---|---:|---:|---:|
| Ruta media | 30,375 m/enlace | 30,325 m/enlace | — |
| Ruta desfavorable sin reserva | 42,7 m | 39,7 m | — |
| Ruta desfavorable con reserva | 45,7 m | 42,7 m | — |
| Control docente de 90 m | Cumple | Cumple | Cumple en el escenario |
| Cable base | 19 440 m | 40 756,8 m | 60 196,8 m |
| Reserva | 1 920 m | 4 032 m | 5 952 m |
| Desperdicio | 1 068 m | 2 239,44 m | 3 307,44 m |
| Requerido | 22 428 m | 47 028,24 m | 69 456,24 m |
| Cajas de 305 m | 74 | 155 | 229 |
| Metros comerciales | 22 570 m | 47 275 m | 69 845 m |

Los patch cords son renglones separados: 1 984 de usuario y 1 984 de rack, referencia candidata de 7 ft. El conteo de rack expresa capacidad pasiva completa, no selección de switches.

### 3.2 Fibra

**Supuestos:** 3,5 m entre pisos; 3 m internos y 5 m de reserva en cada extremo; 5 % de desperdicio.

- A vertical: 89,25 m de cable OS2 12F.
- B vertical: 194,775 m de cable OS2 12F.
- Total vertical: 284,025 m.
- E1: 221,55 m de cable 24F si los 145 + 50 m corresponden a esa ruta.
- E2: `169,05 + 1,05x m`; `x` sigue pendiente.
- E3: `16,8 + 1,05y m`; `y` sigue pendiente.
- Total exterior: `407,4 + 1,05x + 1,05y m`.

Los 145 m y 50 m siguen clasificados como referencia aportada/propuesta. No se declararon mediciones nuevas.

### 3.3 Sistema pasivo compatible

- 229 cajas Panduit `PUP6AHD04BU-G` como escenario.
- 51 paneles `NK6XPPG48Y`, 1 984 jacks `CJ6X88TGBU`, 992 placas `CFPL2WHY`.
- 22 cassettes Corning `CCH-CS12-A9-P00RE` y 6 `CCH-CS24-A9-P00RE`.
- 12 housings `CCH-01U`, 1 `CCH-03U`, 1 `CCH-04U`.
- 13 racks nuevos APC/Schneider `AR3100B2`: once TR y dos ER; no se duplica ER-P.
- 51 organizadores de cobre y 14 ópticos `AR8425A`.
- Patch cord óptico `040402R5120003M`: variable de 0 a 204 según pares activos.
- Pigtails separados = 0; adaptadores separados = 0, porque los cassettes los integran.

Canalizaciones conservan cantidades de ruta y variables de producto: bandeja 1 432,725 m de escenario, 992 bajantes/3 124,8 m, 50 m de ducto propuesto y seis posiciones teóricas de registro. Sección, diámetro, accesorios y cajas reales siguen pendientes.

### 3.4 Excel

- Materiales mapeados a filas 2–27.
- Herramientas mapeadas a filas 2–13 para una cuadrilla académica.
- Cada fila indica fórmula, resultado, estado, fuente y acción del estudiante.
- E2, E3, patch cords ópticos, puesta a tierra y canalizaciones quedan bloqueados o condicionados explícitamente.
- Original y copia conservan SHA-256 `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`.
- La copia aún contiene ejemplos didácticos; no es final.

### 3.5 Imágenes y paquete

Se conservaron los nueve diseños. Solo cambiaron `06_ER_A`, `07_TR_A`, `08_ER_B` y `09_TR_B` para mostrar housings CCH, cassettes integrados, longitudes verticales de escenario y máximos de cobre frente a 90 m.

`08_entrega/PAQUETE_REVISION_FASE2D/` contiene 33 archivos: 32 artefactos registrados en `SHA256SUMS.csv` y el propio inventario.

## 4. Archivos modificados, creados y preservados

### Modificados

- `03_diseno/generar_diagramas_fase2b.py`.
- `07_imagenes/fase2b/06_ER_A.svg` y `.png`.
- `07_imagenes/fase2b/07_TR_A.svg` y `.png`.
- `07_imagenes/fase2b/08_ER_B.svg` y `.png`.
- `07_imagenes/fase2b/09_TR_B.svg` y `.png`.
- `README.md`, `DECISIONES.md`, `PENDIENTES.md`.

### Creados

- `04_calculos/entradas_fase2d.csv`.
- `04_calculos/modelo_calculos_fase2d.py`.
- `04_calculos/resultados_fase2d.csv`.
- `04_calculos/MEMORIA_CALCULOS_FASE2D.md`.
- `05_materiales/MATRIZ_TECNICA_FASE2D.md`.
- `06_excel/PLAN_FILAS_MATERIALES_FASE2D.csv`.
- `06_excel/PLAN_FILAS_HERRAMIENTAS_FASE2D.csv`.
- `06_excel/PLAN_TRANSFERENCIA_EXCEL_FASE2D.md`.
- `08_entrega/GUIA_EXPOSICION_8_MIN_FASE2D.md`.
- `08_entrega/preparar_paquete_revision_fase2d.ps1`.
- `09_auditorias/validar_fase2d.py`.
- `08_entrega/PAQUETE_REVISION_FASE2D/README.md`, `ESTADO_ENTREGABLES.csv`, `SHA256SUMS.csv`.
- `08_entrega/PAQUETE_REVISION_FASE2D/01_imagenes_revision/`: nueve SVG y nueve PNG.
- `08_entrega/PAQUETE_REVISION_FASE2D/02_soporte_tecnico/`: guía, matriz, memoria y resultados.
- `08_entrega/PAQUETE_REVISION_FASE2D/03_excel_provisional/`: copia Excel intacta y tres planes de transferencia.
- `08_entrega/PAQUETE_REVISION_FASE2D/04_fuentes_reproducibles/`: entradas, modelo, generador y exportador.

### No modificados

- `06_excel/Plantilla Actividades de comprobación.xlsx`.
- `06_excel/Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx`.
- Los cinco pares de imágenes exterior/plantas/laboratorios.
- Rama `main`.

## 5. Verificaciones ejecutadas

| Prueba | Resultado |
|---|---|
| `python 09_auditorias/validar_fase2d.py` | 129/129 controles aprobados |
| `python 09_auditorias/validar_fase2b.py` | 63/63 controles aprobados |
| `python -m py_compile ...` | Generador, modelo y validador sin errores de sintaxis |
| Analizador PowerShell | Exportador y preparador de paquete sin errores |
| Inspección visual | Cuatro PNG afectados legibles; ER-A/TR-A revisados a detalle y B conserva la misma geometría parametrizada |
| XML/PNG | 9/9 SVG válidos y 9/9 PNG 1600×1000 |
| Excel OOXML/hash | Original, copia y copia empaquetada íntegros e idénticos |
| Paquete SHA-256 | 32/32 artefactos coincidentes |
| `git diff --check` | Sin errores después de corregir saltos Markdown |

El validador histórico Fase 2C devuelve 116/124 después de Fase 2D porque compara las imágenes fuente actuales con la instantánea inmutable del paquete 2C. No indica corrupción: el validador Fase 2D compara las imágenes actuales con el paquete 2D y aprueba 18/18. El reporte histórico y su paquete no se reescribieron.

## 6. HECHO / VERIFICADO / PENDIENTE

- **HECHO:** existe un escenario completo de cobre, fibra vertical, E1, materiales y transferencia Excel.
- **VERIFICADO:** rutas desfavorables bajo 90 m, 58 resultados, sistema CCH sin duplicación, integridad de imágenes/Excel/paquete.
- **PROPUESTO:** 229 cajas de cobre, reservas, desperdicios, 13 racks y longitudes de canalización; requieren aceptación humana.
- **PENDIENTE:** `x/y`, confirmación de E1, sección/diámetro de canalizaciones, inspección de registros, pares activos, dos RJ45/área, `J43` y transferencia manual del Excel.

## 7. Problemas abiertos por impacto

1. **Crítico para cantidades completas:** faltan `x/y` de E2/E3 y confirmar el destino real del recorrido 145 + 50 m.
2. **Crítico para Excel:** el estudiante debe aprobar los supuestos, retirar ejemplos, introducir fórmulas y probar recálculo; el archivo sigue provisional.
3. **Alto:** seleccionar sección/diámetro y accesorios de canalizaciones; las longitudes por sí solas no definen producto.
4. **Alto:** confirmar dos RJ45 por área doble y `J43` con el docente.
5. **Medio:** definir pares activos, energía/carga/ventilación y puesta a tierra antes de cerrar patch cords ópticos y racks.
6. **Bajo/documental:** el validador histórico 2C no es aplicable a fuentes gráficas versionadas posteriores.

## 8. Siguiente acción mínima viable

El estudiante debe revisar `06_excel/PLAN_TRANSFERENCIA_EXCEL_FASE2D.md`, aceptar o corregir las entradas del escenario y trasladar manualmente únicamente las filas aprobadas a una copia personal. En paralelo debe resolver `x/y` o dejar E2/E3 explícitamente fuera de una cantidad cerrada. No debe declarar el Excel final mientras conserve ejemplos o filas pendientes.
