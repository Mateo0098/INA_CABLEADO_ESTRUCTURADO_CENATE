# Correspondencia para la copia de trabajo Excel — Fase 2B

## Estado de archivos

| Archivo | Estado | SHA-256 al 2026-10-25 |
|---|---|---|
| `06_excel/Plantilla Actividades de comprobación.xlsx` | Original controlado, no modificado | `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6` |
| `06_excel/Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx` | Copia de trabajo identificada; aún byte a byte igual al original | `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6` |

La copia se deja deliberadamente sin sustitución automática del contenido didáctico. El enunciado prohíbe que la IA genere el Excel con cantidades, fórmulas y resultados; el estudiante debe revisar, comprender y trasladar manualmente los renglones aprobados. Esta sesión sí deja la fuente reproducible de cálculo y la correspondencia exacta para hacerlo.

## Correspondencia de columnas

| Columna original | Contenido a trasladar | Fuente controlada |
|---|---|---|
| A — Material o equipo | Nombre de componente | `05_materiales/MATRIZ_TECNICA_FASE2B.md`, columna componente |
| B — Categoría o tipo | Cobre, fibra, rack, canalización, accesorio o equipo | Matriz técnica |
| C — Especificaciones técnicas | Especificación mínima y condición de instalación | Matriz técnica; revisar compatibilidad antes de adoptar |
| D — Marca | Solo marca con fuente oficial | Matriz técnica; dejar pendiente donde no hay verificación |
| E — Modelo o referencia | Número exacto verificado | Matriz técnica; no copiar una familia como si fuera modelo final |
| F — Unidad de medida | `unidad`, `panel`, `m cable`, `m ducto`, etc. | `04_calculos/resultados_fase2b.csv` |
| G — Cantidad | Resultado revisado o fórmula comprendida | `resultados_fase2b.csv`, campos fórmula/resultado/estado |
| H — Proveedor | Proveedor especializado verificado, si aplica | Pendiente; no confundir fabricante con proveedor |
| I — Precio unitario | Vacío | INA-044 |
| J — Precio total | Vacío en renglones | INA-044 |
| K — Fuente | Enlace oficial directo | Matriz técnica |

## Correspondencia de cantidades

| Renglón técnico futuro | Resultado/variable | Estado para traslado |
|---|---|---|
| Panel Cat 6A de 48 puertos | `TOTAL_PANELES = 51` | Provisional: depende de 2 RJ45/área y regla de reserva documentada |
| Jack Cat 6A | `JACKS_CAT6A = 1 984` | Provisional: depende de interpretación de área doble |
| Placa/caja doble | `PLACAS_DOBLES = 992` | Provisional |
| Patch cord Cat 6A, usuario | `PATCH_CORD_COBRE_USUARIO = 1 984` | Provisional; longitud pendiente |
| Patch cord Cat 6A, rack | `PATCH_CORD_COBRE_RACK = 1 984` | Provisional; equipos activos/longitud pendientes |
| Cable Cat 6A | `A_CABLE_COBRE + B_CABLE_COBRE` | **No trasladar cantidad:** ambos están `N/D` hasta medir rutas y aprobar desperdicio |
| Cable OS2 12 fibras | `CABLES_VERTICAL = 11` | Cantidad de cables provisional; metrajes pendientes por enlace |
| Cable OS2 24 fibras | `ENLACES_EXTERIORES = 3` | Cantidad de cables provisional; metrajes E2/E3 y reservas pendientes |
| Pigtail LC/UPC OS2 | `PIGTAILS_Y_EMPALMES = 408` | Máximo provisional si se terminan todas las fibras |
| Adaptador LC dúplex OS2 | `ADAPTADORES_LC_DUPLEX = 204` | Provisional; sujeto a panel/cassette final |
| Ducto existente | 145 m reportados | Referencia/inspección, **no compra** |
| Ducto nuevo | 50 m propuestos | No cerrar hasta confirmar destino, ruta y diámetro |
| Caja/registro | 5 + 1 posiciones teóricas | **No trasladar como compra** sin levantamiento |
| Rack 42U | 13 como escenario de un rack por ER/TR | No trasladar como definitivo; capacidad y primer piso pendientes |

## Fórmulas Excel equivalentes para explicar, no pegadas automáticamente

- Paneles por TR: `=REDONDEAR.MAS(Puertos_TR/48;0)+SI(RESIDUO(Puertos_TR;48)=0;1;0)`.
- Cable de cobre: `=Enlaces*Longitud_promedio_m*(1+Desperdicio_pct/100)`.
- Terminaciones de fibra: `=Enlaces*Fibras_por_enlace*2`.
- Adaptadores LC dúplex: `=REDONDEAR.MAS(Terminaciones_fibra/2;0)`.

Los nombres de funciones y separadores pueden variar según idioma/configuración de Excel. El estudiante debe introducir y probar las fórmulas en su instalación.

## Tratamiento de `J43`

La copia conserva intacta la fórmula preexistente `J43=SUM(J2:J41)` porque todavía no hay instrucción docente que autorice eliminarla. Las celdas económicas de los renglones deben permanecer vacías y no se incorporará ningún monto. Antes de la entrega final debe confirmarse con el docente si `J43` se conserva o se deja sin fórmula.

## Reglas para completar la copia

1. Sustituir ejemplos únicamente en la copia de trabajo, nunca en el original.
2. No reordenar ni renombrar hojas o columnas; replicar estilos al agregar filas.
3. No trasladar resultados `N/D`, estados “pendiente” ni posiciones teóricas como cantidades comprables.
4. Mantener I y J sin precios/montos.
5. Probar apertura, recálculo y conservación de formato después de cada edición manual.
