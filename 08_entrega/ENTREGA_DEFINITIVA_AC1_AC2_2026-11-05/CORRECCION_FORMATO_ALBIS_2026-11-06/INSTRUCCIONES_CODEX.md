# AC2 — Corrección obligatoria al machote EXACTO del profesor Albis (2026-11-06)

## Objetivo único
Reemplazar **solo los archivos de AC2 rechazados** por versiones derivadas directamente del libro original `insumos_entregable_2/Presupuesto FINAL.xlsx`. No rediseñar ninguna hoja. La factura proforma PDF debe generarse visualmente **desde la hoja original "Factura proforma"**, no mediante un diseño nuevo. Los archivos se publican en **esta misma carpeta** y se sincronizan con el repositorio local.

## Fuentes inalterables
- Machote original del profesor: `insumos_entregable_2/Presupuesto FINAL.xlsx` (conservarlo intacto).
- Datos económicos: `08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05/DATOS_PRESUPUESTO_CHATGPT_37_PARTIDAS.csv` (37 conceptos; siete PUBLICADO y 30 ESTIMADO).
- Gantt completo original: `gantt/GANTT_INA_CABLEADO_2026-2027.xlsx`; consultar `gantt/README.md`. 26 actividades, del 2026-11-02 al 2027-02-16, 74 días hábiles y **4.744 horas-técnico** calculadas como técnicos × días de cada actividad × 8 h.
- Costo interno de mano de obra del Gantt: **₡13.935.679,31514** (dato de referencia para reconciliar, NO pegar como solución en la proforma).
- Tipo de cambio académico: 454,65 CRC/USD; IVA de venta referencial 13%; costo directo + imprevistos 5%, administración 10%, utilidad 15% (confirmar orden de la plantilla y usar sus propias fórmulas).

## Restricción principal e innegociable
**Formato visual idéntico al machote** de Albis: nombres y orden de las siete hojas, estilos, colores, anchos de columnas, alturas, combinaciones de celdas, tipografía, bordes, orientación, áreas de impresión, encabezados, leyendas y estructura. NINGÚN diseño nuevo, hojas auxiliares agregadas, tablas propias, portada, ni expansión de columnas a voluntad. Trabajar en **copia binaria del machote**; escribir solamente valores en celdas de entrada y, cuando haya `#REF!` o incompatibilidad real, restaurar mínimamente referencias/formulación coherente. No borrar fórmulas que ya funcionen.

## Hojas requeridas (exactamente)
1. `Cotización`: 27 filas de materiales de la plantilla, **filas 7–33**. Consolidar los 37 registros en 27 renglones compatibles, sin perder costos; unidades y precio por conjunto si una fila agrupa varios artículos. Orden de agrupación sugerido:
   1) cable Cat6A; 2) jacks; 3) placas y cajas WA; 4) patch cords cobre; 5) rotulación; 6) paneles Cat6A; 7) gabinetes y tierra; 8) organizadores; 9) PDU+UPS; 10) canastas; 11) soportes y uniones; 12) conduit; 13) accesorios conduit y bajantes; 14) puesta a tierra; 15) switches acceso; 16) switches distribución; 17) DAC; 18) FO 12F; 19) FO 24F; 20) ODF+cassettes; 21) pigtails+adaptadores+protectores; 22) patch cords FO; 23) SFP+; 24) uso de certificador/OLTS/OTDR/fusionadora; 25) herramientas; 26) EPP; 27) fletes. Conservar fórmulas de importes y subtotal del machote (p. ej. G7:G33, G37).
2. `Mano de obra`: **NO importe fijo copiado del Gantt**. Las 4.744 horas-técnico de la hoja Gantt incorporada deben alimentar **mediante fórmulas del machote** el cálculo de costos de la mano de obra, con tasa horaria y cargas justificadas y derivadas del Gantt original. Conservar apartados y fórmulas existentes; no duplicar certificaciones ni supervisión.
3. `Precio de venta`: calcular importes a partir de Cotización + Mano de obra + parámetros existentes. Evitar sumar herramientas, EPP o transporte dos veces. IVA en venta una vez; precios de compra con IVA incluido deben llevarse a neto correctamente.
4. `Ganancias`: respetar el formato y formulación original del profesor.
5. `Cronograma Gantt`: **insertar los resultados del Gantt ya realizado EN ESTA HOJA**, no colocar únicamente un enlace o nota. Pegar las 26 tareas con inicio, fin, días, técnicos y horas, usando su área original y filas existentes; restaurar/actualizar las barras y las fórmulas que las relacionan. Días hábiles, feriados y dependencias del Gantt fuente, sin rediseñar ni crear tareas nuevas. Las horas deben alimentar la hoja Mano de obra automáticamente. Si el diseño del machote contempla menos tareas, utilizar sus filas ya formateadas dentro de la hoja (incluidas filas inferiores) sin desplazar el resto de hojas.
6. `Feriados CR`: conservar el listado del machote; emplearlo para el Gantt.
7. `Factura proforma`: completar todos los campos del machote con datos del proyecto y sus filas de costo, enlazando fórmulas a las otras hojas. Sin inventar identificaciones legales; campos sin evidencia quedan claramente editables. Importe idéntico a Precio de venta.

## Validación de aceptación
- Comparar libro original y salida: **mismos 7 nombres y orden de pestañas; mismos anchos/altos, estilos, bordes, combinaciones, rango de impresión** salvo correcciones estrictamente necesarias y justificadas.
- Confirmar 26 actividades, 4.744 horas-técnico, fechas y cómputo; que alterar horas en la hoja Gantt cambie en cadena Mano de obra, Precio de venta y Factura proforma. **No aprobar si hay un importe laboral quemado / codificado.**
- Excel sin `#REF!`, `#VALUE!`, `#DIV/0!`, etc; fórmulas recalculadas. Si Microsoft Excel disponible, **abrir, recalcular y guardar** desde Excel. Si no, validar con herramienta de cálculo disponible; documentar exactamente qué no se pudo verificar.
- PDF generado por exportación o impresión de hoja `Factura proforma`, mismo color, celdas, tamaño y diseño. Validar visualmente render de Excel frente al PDF.
- Total previo como **referencia de conciliación**, no requisito forzado: ₡216.518.234,86. Si el funcionamiento genuino del machote genera otro total, mostrar el monto REAL, su causa y garantizar Excel=PDF.
- Las 30 estimaciones económicas siguen identificadas como académicas, nunca como ofertas firmes.
- Probar XLSX y PDF abriendo archivos finales; no confiar solamente en que son ZIP válidos.

## Salidas finales en ESTA carpeta
- `PRESUPUESTO_AC2_MACHOTE_ALBIS.xlsx`
- `FACTURA_PROFORMA_AC2_MACHOTE_ALBIS.pdf`
- `FUENTES_Y_SUPUESTOS_AC2.csv` (copia del archivo fuente)
- `CORRECCION_AC2_MACHOTE_ALBIS.zip`
- `VERIFICACION_FORMATO_Y_FORMULAS.md` (máximo una página, resultados y limitaciones).

No sobrescribir los originales ni la entrega anterior de AC1.

## Publicación
1. Leer `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`; comprobar rama y estado Git.
2. Trabajar solo en `desarrollo-proyecto` y sincronizar con seguridad.
3. Generar archivos en la ruta de esta instrucción, **desde el equipo local** para que estén ya presentes al finalizar; publicar commit y push a `origin/desarrollo-proyecto`.
4. Reportar en `09_auditorias/REPORTES_CODEX/` y actualizar `09_auditorias/ULTIMO_REPORTE_CODEX.md` brevemente. En la terminal imprimir solamente commit SHA, ruta final y estado.
