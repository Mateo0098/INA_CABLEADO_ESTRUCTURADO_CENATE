# Reporte Codex — últimos bloqueos del Entregable 2

**Fecha:** 2026-11-05

**Rama:** `desarrollo-proyecto`
**Alcance:** correcciones puntuales del cierre AC1/AC2. No se modificaron arquitectura, matrices U02/U03/U04C, planos, Gantt fuente ni plantilla original.

## HECHO

- Se retiró del costo el panel Lanprosa LTK-PPC648: es una referencia Cat 6 y no se presenta como sustituto técnico ni selección aprobada de panel Cat 6A.
- Se añadió la valoración académica explícita del **cable OS2 24F exterior**: 11 paquetes equivalentes de 50 m, a USD 50 por paquete. El cálculo duplica exclusivamente el precio publicado del cable OS2 12F/50 m Lanprosa LTK-FIBSM12 ya documentado para representar 24F; no afirma que exista un SKU 24F exterior ni que sea compatible.
- Cassettes/housings, herrajes y fijaciones, paneles Cat 6A y servicio de fusión/OLTS/OTDR/certificación continúan visibles como `PENDIENTE`, sin costo cero. ELVATRON publica instrumentos, pero no se encontró una tarifa comparable de servicio que permita valorarlos sin inventar un alquiler o compra duplicada.
- Se copió sin modificación `gantt/GANTT_INA_CABLEADO_2026-2027.xlsx` a `GANTT_CANONICO/` dentro del paquete. La hoja `Cronograma Gantt` usa ahora el vínculo relativo `GANTT_CANONICO/GANTT_INA_CABLEADO_2026-2027.xlsx`, válido tras extraer el ZIP.
- Se corrigieron Excel, PDF y notas: el conduit y el cable OS2 exterior se describen como valoraciones académicas parciales; ya no se declaran completamente pendientes.

## RESULTADO

- Total de proforma parcial: **CRC 135.898.559,10**.
- El presupuesto **no está completo**. El total excluye costos indispensables sin fundamento comercial o técnico suficiente: paneles Cat 6A, cassettes/housings, herrajes/fijaciones/accesorios y servicios especializados.
- Precios con IVA incluido se convierten a base neta; los precios sin IVA incorporan IVA una vez en el modelo; los precios de IVA no confirmado permanecen identificados. Mano de obra reutiliza el costo interno del Gantt, sin sumar servicio especializado.

## VERIFICADO

- `PRESUPUESTO_FINAL_CENATE.xlsx` abre mediante `openpyxl`, conserva las siete hojas de la plantilla y no contiene `#REF!`, `#DIV/0!`, `#VALUE!` ni `#NAME?`.
- PDF de proforma: una página, texto extraíble y total `CRC 135,898,559.10` comprobado.
- ZIP: 17 archivos, prueba de integridad correcta, incluye el Gantt canónico. La copia del Gantt tiene el mismo SHA-256 que su fuente.
- Actividad 1 permanece en el paquete con nueve planos y Excel sin cambios.

## LIMITACIÓN

Microsoft Excel COM no estuvo disponible en esta sesión (`0x80070520`, sesión de inicio terminada). El libro solicita recálculo completo al abrirse; no se declara una prueba visual ni un guardado por Microsoft Excel.

## ARCHIVOS MODIFICADOS

- `08_entrega/generar_cierre_ac1_ac2.py`
- Archivos regenerados de `08_entrega/CIERRE_AC1_AC2_2026-11-05/`, incluido el ZIP y `GANTT_CANONICO/GANTT_INA_CABLEADO_2026-2027.xlsx`
- `09_auditorias/ULTIMO_REPORTE_CODEX.md` y este reporte.

**Siguiente acción mínima viable:** obtener cotizaciones compatibles para los cuatro conceptos pendientes y abrir el XLSX en Microsoft Excel para revisión visual y recálculo antes de emitir una proforma definitiva.
