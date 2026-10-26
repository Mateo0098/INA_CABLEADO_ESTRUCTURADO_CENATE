# Corrección crítica de compatibilidad del XLSX final

**Fecha:** 2026-10-25 · **Fase:** 4 · **Rama:** `desarrollo-proyecto`  
**Objetivo:** corregir la incompatibilidad confirmada por Microsoft Excel sin cambiar las cantidades ni el diseño académico.

## Diagnóstico y causa

Se inspeccionaron `AGENTS.md`, el índice y el reporte anterior, la plantilla INA, las dos copias defectuosas y `09_auditorias/crear_excel_fase3b.py`.

La plantilla tiene 14 partes ZIP, firma `PK` y cero errores del Open XML SDK; Excel 16.0 la abre con dos hojas. El libro Fase 3B también tenía ZIP íntegro, pero Excel lo rechazó (HRESULT `0x800A03EC`). El Open XML SDK reportó seis errores `MC_InvalidIgnorableAttribute`/`MC_InvalidRequiresAttribute`.

La causa fue la serialización manual con `xml.etree.ElementTree` en el generador Fase 3B: ElementTree descartó algunas declaraciones `xmlns` de prefijos de compatibilidad no usados como etiquetas, mientras dejó esos prefijos en `mc:Ignorable`/`mc:Requires`. Al quedar referencias a prefijos no declarados (`x15`, `xr`, `xr6`, `xr10`, `xr2`, `x14ac`), Excel consideró inválido el libro. Las fórmulas/cachés no fueron la causa reportada por el SDK.

## Corrección

Se regeneró desde la plantilla original con Microsoft Excel 16 por COM. Los materiales, herramientas, notas y fórmulas se tomaron de las estructuras ya aprobadas en `crear_excel_fase3b.py`. Durante la carga se desactivó `AutoFillFormulasInLists` únicamente en esa instancia para evitar que la tabla impusiera una sola fórmula calculada en toda la columna; el valor previo se restauró al cerrar Excel. No se cambió configuración global.

Se conservaron las dos hojas, los estilos de la plantilla y todas las cantidades aprobadas: 229 cajas Cat 6A de 305 m, 1 984 jacks, 51 paneles, longitudes de fibra y canalización del escenario, herramientas y ausencia de precios. La plantilla INA no se modificó; su SHA-256 permanece `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`.

## Verificaciones realizadas

- Microsoft Excel **16.0** abrió la plantilla original con dos hojas.
- Excel rechazó la versión defectuosa con HRESULT `0x800A03EC`; el SDK encontró seis errores de prefijos OOXML en ella.
- Excel abrió el XLSX regenerado, guardó la copia de prueba `09_auditorias/evidencias/Excel_COM/INA_CENATE_ACTIVIDAD_1_COMPLETADA_EXCEL_COM_TEST.xlsx`, reabrió esa copia y abrió la ruta final de entrega con dos hojas.
- Validación mediante Excel de las 29 fórmulas y cantidades de materiales, 11 cantidades numéricas de herramientas, ausencia de importes en I/J y limpieza de J43.
- Open XML SDK de Microsoft: **cero errores** para `06_excel/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx` y la copia del paquete; la copia defectuosa respaldada conserva los seis errores diagnósticos.
- Comparación de estilos originales: **545 celdas estilizadas** conservan formato equivalente. Excel normalizó índices/serialización del catálogo al guardar; la comparación se hizo por formato y no por igualdad binaria de `styles.xml`.
- ZIP/XML íntegros; fórmulas frente a resultados/cachés aprobados; ambas copias finales idénticas. El inventario SHA-256 del paquete se actualizó.

## Archivos

**Modificados:** `06_excel/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx`, `08_entrega/ENTREGA_FINAL_INA_CENATE/01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx`, `08_entrega/ENTREGA_FINAL_INA_CENATE/INVENTARIO_SHA256.txt`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`, `09_auditorias/ULTIMO_REPORTE_CODEX.md`.

**Creados:** `09_auditorias/regenerar_excel_fase4.ps1`; respaldo defectuoso y copia Excel de prueba en `09_auditorias/evidencias/Excel_COM/`; este reporte.

**No modificados:** plantilla INA, fórmulas/datos fuente Fase 3B, cálculos, cantidades técnicas, imágenes y rama `main`. El resto del paquete final no cambió.

**SHA-256 XLSX final:** `0B27F59C51CD1C6CB51EC5AB3E93725BD96F3ADEC13A93807340DD282E69C0F4`.  
**SHA-256 respaldo defectuoso:** `1A1CC4B4A825C21BF7C421B106235D9C921BCA4A42C384209E4F9408A7B7D530`.

## Estado

- **HECHO:** sustituidas las dos copias finales y respaldado el XLSX defectuoso fuera de la carpeta de entrega.
- **VERIFICADO:** Excel 16 abrió el archivo final; Open XML SDK reportó cero errores; cantidades, fórmulas, hojas, precios, copia e inventario comprobaron correctamente.
- **PENDIENTE:** revisión académica personal de los supuestos; no afecta la apertura ni la integridad del XLSX.

**Implementación:** commit `a688fa64b5a809fb5302a739350adb5d104ef3d5` (`fix: regenerar XLSX final con Excel COM`) en `desarrollo-proyecto`. El reporte y el índice se incorporan en el commit documental siguiente; su SHA final se confirma en la respuesta terminal. Siguiente acción mínima: revisar el XLSX corregido y continuar con la preparación académica de la entrega.
