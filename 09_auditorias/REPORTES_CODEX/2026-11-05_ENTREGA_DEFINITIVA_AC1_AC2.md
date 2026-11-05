# Reporte Codex — publicación de entrega definitiva AC1 y AC2

## HECHO

- Se generó `08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05/` desde la plantilla publicada y las 37 partidas de `DATOS_PRESUPUESTO_CHATGPT_37_PARTIDAS.csv`.
- El Excel conserva las siete funciones de la plantilla y añade fuentes y parámetros. Su fórmula usa ₡454,65/USD, mano de obra del Gantt por ₡13.935.679,31514, 5 % de imprevistos, 10 % administrativo, 15 % de utilidad y 13 % de IVA de venta.
- Base neta de materiales/equipos: ₡130.321.092,6765. Total académico: **₡216.518.234,86**.
- Se creó PDF con el mismo total, CSV de fuentes/supuestos, correo con asunto exacto, copia íntegra de AC1, copia idéntica del Gantt y ZIP consolidado.

## VERIFICADO

- XLSX abre con `openpyxl`, tiene nueve hojas y 37 filas comerciales; no contiene `#REF!`, `#DIV/0!`, `#VALUE!` ni `#NAME?`.
- PDF de una página con total `CRC 216,518,234.86`.
- ZIP válido, con 15 archivos: AC1, AC2 y Gantt. Nueve planos PDF y Excel AC1 presentes; hashes del Gantt y Excel AC1 coinciden con sus fuentes.
- Precios con IVA incluido se convierten a base neta antes de agregarlos; el IVA de venta se aplica una vez.

## PENDIENTE

- Microsoft Excel COM no estuvo disponible (`0x80070520`); no se realizó apertura visual ni guardado con Excel. El libro solicita recálculo completo al abrirse.
- Las 30 filas identificadas como estimaciones académicas siguen sin ser cotizaciones comerciales firmes.

## ARCHIVOS

- `08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05/ACTIVIDAD_2/PRESUPUESTO_FINAL_CENATE_AC2.xlsx`
- `08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05/ACTIVIDAD_2/FACTURA_PROFORMA_CENATE_AC2.pdf`
- `08_entrega/ENTREGA_DEFINITIVA_AC1_AC2_2026-11-05/ENTREGA_DEFINITIVA_AC1_AC2.zip`

**Siguiente acción mínima viable:** abrir el presupuesto en Microsoft Excel en una sesión de escritorio y reemplazar estimaciones por cotizaciones si se requiere una propuesta comercial firme.
