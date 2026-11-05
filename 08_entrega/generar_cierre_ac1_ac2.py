"""Genera el cierre AC1/AC2 a partir de fuentes versionadas del proyecto.

El archivo Presupuesto FINAL.xlsx solicitado no se encontró en el repositorio;
por ello se crea una salida nueva que cubre sus siete funciones comerciales.
"""
from __future__ import annotations

import csv
import shutil
import zipfile
from datetime import date
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "08_entrega/CIERRE_AC1_AC2_2026-11-05"
AC1 = ROOT / "08_entrega/ENTREGA_FINAL_INA_CENATE"
GANTT = ROOT / "gantt/GANTT_INA_CABLEADO_2026-2027.xlsx"

USD_CRC = 454.65  # BCCR/MONEX venta, 2026-11-04; fuente registrada en fuentes CSV.
IVA = 0.13
ADMIN = 0.10
UTILIDAD = 0.15
IMPREVISTOS = 0.05
LABOR_INTERNAL = 13935679.31514  # cache comprobada del Gantt canónico.

# (Grupo, descripción, cantidad, unidad, unitario, moneda, IVA, evidencia, fuente, estado)
LINES = [
    ("Cableado Cat 6A", "Cable Cat 6A 305 m (cómputo académico)", 229, "carrete", 210, "USD", "Excluido", "ESTIMADO", "Lanprosa LTK-CAT6AB, precio publicado 2026-11-05; no es CMP histórico", "Incluido parcial"),
    ("Terminaciones cobre", "Jack Panduit CJ6X88TGBU Cat 6A", 1984, "unidad", 5268.64, "CRC", "No confirmado", "PUBLICADO", "Circuito Cinco, 2026-11-05", "Incluido parcial"),
    ("Canalización", "Canasta Cablofil 300 mm x 3 m (redondeo global académico)", 478, "tramo", 45968.40, "CRC", "Incluido", "ESTIMADO", "Capris CF105/300 EZ, precio publicado 2026-11-05; sección/diseño pendientes", "Incluido parcial"),
    ("Racks", "Gabinete 42U Lantek", 13, "unidad", 540, "USD", "Excluido", "ESTIMADO", "Lanprosa LTK-GAB420608, precio publicado 2026-11-05; modelo no adjudicado", "Incluido parcial"),
    ("Terminaciones cobre", "Patch panel 48 puertos comparable", 51, "unidad", 16, "USD", "Excluido", "ESTIMADO", "Lanprosa LTK-PPC648, referencia comercial; Cat 6A exacto pendiente", "Incluido parcial"),
    ("Equipo activo", "Switch acceso MikroTik CRS354-48G-4S+2Q+RM", 44, "unidad", 320703, "CRC", "Excluido", "PUBLICADO", "Ticomer OF-001, 2026-11-05", "Incluido provisional"),
    ("Equipo activo", "Switch distribución MikroTik CRS317-1G-16S+RM", 2, "unidad", 261849, "CRC", "Excluido", "PUBLICADO", "Ticomer OF-003, 2026-11-05", "Incluido provisional"),
    ("Óptica", "Transceptor SFP+ MikroTik S+31DLC10D", 28, "unidad", 119105, "CRC", "No confirmado", "PUBLICADO", "CQNet OF-004, 2026-11-05; disponibilidad insuficiente", "Incluido provisional"),
    ("Herramientas/servicios", "Certificación cobre/fibra, fusión y OTDR", None, "servicio", None, "CRC", "Pendiente", "PENDIENTE", "U03: compra/alquiler/servicio excluyentes; no hay oferta comparable", "Excluido por pendiente"),
    ("Fibra óptica", "Cable OS2 12F vertical y OS2 24F exterior", None, "m", None, "CRC", "Pendiente", "PENDIENTE", "U02: 284,025 m vertical y 538,65 m exterior académicos; producto y presentación pendientes", "Excluido por pendiente"),
    ("Canalización", "Conduit, fijaciones, herrajes, bajantes y accesorios", None, "lote", None, "CRC", "Pendiente", "PENDIENTE", "U02: falta despiece físico y sustrato", "Excluido por pendiente"),
]


def crc(line):
    group, name, qty, unit, price, currency, iva_status, evidence, source, status = line
    if qty is None or price is None:
        return None
    net = qty * price * (USD_CRC if currency == "USD" else 1)
    # Precio publicado con IVA no confirmado no recibe una segunda aplicación.
    return net if iva_status == "No confirmado" else net * (1 + IVA)


def title(ws, text, cells=10):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=cells)
    c = ws.cell(1, 1, text)
    c.font = Font(bold=True, color="FFFFFF", size=16)
    c.fill = PatternFill("solid", fgColor="1F4E78")
    c.alignment = Alignment(horizontal="center")
    ws.row_dimensions[1].height = 28


def finish_sheet(ws):
    ws.freeze_panes = "A3"
    ws.sheet_view.showGridLines = False
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)
    for col in ws.columns:
        index = col[0].column
        ws.column_dimensions[get_column_letter(index)].width = min(48, max(12, max(len(str(c.value or "")) for c in col) + 2))


def build_book():
    wb = Workbook()
    cot = wb.active; cot.title = "Cotización"
    labor = wb.create_sheet("Mano de obra")
    sale = wb.create_sheet("Precio de venta")
    profit = wb.create_sheet("Ganancias")
    chrono = wb.create_sheet("Cronograma Gantt")
    hol = wb.create_sheet("Feriados CR")
    proforma = wb.create_sheet("Factura proforma")
    detail = wb.create_sheet("Detalle partidas")
    sources = wb.create_sheet("Fuentes y precios")
    assumptions = wb.create_sheet("Supuestos y pendientes")
    params = wb.create_sheet("Parámetros")

    title(params, "PARÁMETROS EDITABLES DEL PRESUPUESTO", 3)
    params.append(["Parámetro", "Valor", "Fuente / condición"])
    values = [
        ("Fecha emisión", date(2026, 11, 5), "Solicitud de cierre"),
        ("Tipo cambio USD→CRC", USD_CRC, "Referencia BCCR/MONEX venta 2026-11-04; actualizar al cotizar"),
        ("IVA referencia", IVA, "Tarifa general Hacienda; confirmar factura/exención"),
        ("Imprevistos", IMPREVISTOS, "Supuesto comercial editable"),
        ("Gastos administrativos", ADMIN, "Supuesto comercial editable"),
        ("Utilidad", UTILIDAD, "Supuesto comercial editable"),
        ("Escenario switches", 44, "44 base; 51 es alternativa no acumulable"),
        ("Costo laboral interno", LABOR_INTERNAL, "Gantt canónico, 26 actividades; hipótesis TMED"),
        ("Vigencia proforma", "15 días", "Sujeta a cotizaciones, disponibilidad y revisión técnica"),
    ]
    for r in values: params.append(r)
    for r in range(3, 9): params.cell(r, 2).fill = PatternFill("solid", fgColor="DCEAF5")
    for r in (5, 6, 7): params.cell(r, 2).number_format = "0.0%"
    params["B4"].number_format = '#,##0.00'

    title(detail, "DETALLE COMPLETO DE PARTIDAS — BASE U02/U03", 13)
    headers = ["ID", "Origen", "Grupo", "Descripción", "Unidad funcional", "Cantidad de diseño", "Cantidad comercial", "Oferta/estimación", "Precio unitario", "Moneda", "IVA", "Costo CRC", "Estado"]
    detail.append(headers)
    indexed = {}
    for line in LINES:
        indexed.setdefault(line[1], line)
    # Preserve all source IDs; commercial selections appear on matching category rows.
    for file, origin in [(ROOT / "05_materiales/unidad_02_ampliacion/UNIDAD_02_MATRIZ_MAESTRA_MATERIALES.csv", "U02"), (ROOT / "05_materiales/unidad_03_herramientas/UNIDAD_03_MATRIZ_MAESTRA_HERRAMIENTAS.csv", "U03")]:
        with file.open(encoding="utf-8-sig", newline="") as fh:
            for r in csv.DictReader(fh):
                ident = r["ID único"]
                desc = r.get("Componente") or r.get("Herramienta equipo o consumible")
                unit = r.get("Unidad funcional", "")
                rawq = r.get("Cantidad calculada o variable") or r.get("Cantidad de referencia") or "PENDIENTE"
                group = "Material/activo" if origin == "U02" else "Herramienta/servicio"
                detail.append([ident, origin, group, desc, unit, rawq, "PENDIENTE", "No adjudicado", None, "CRC", "Pendiente", "PENDIENTE", "Pendiente de cantidad/precio/selección"])
    detail.auto_filter.ref = f"A2:M{detail.max_row}"

    title(sources, "FUENTES Y ESTIMACIONES PRESUPUESTARIAS", 11)
    sources.append(["Grupo", "Descripción", "Cantidad", "Unidad", "Precio unitario", "Moneda", "IVA", "Importe CRC", "Clasificación", "Fuente / fecha", "Estado"])
    for line in LINES:
        group, desc, qty, unit, price, currency, tax, evidence, source, status = line
        sources.append([group, desc, qty, unit, price, currency, tax, crc(line), evidence, source, status])
    sources.auto_filter.ref = f"A2:K{sources.max_row}"

    title(cot, "COTIZACIÓN PRELIMINAR — INFRAESTRUCTURA INA CENATE", 9)
    cot.append(["Grupo comercial", "Concepto", "Cantidad", "Unidad", "Evidencia", "Subtotal CRC", "IVA/estado", "Estado", "Fuente"])
    for line in LINES:
        group, desc, qty, unit, price, currency, tax, evidence, source, status = line
        cot.append([group, desc, qty or "PENDIENTE", unit, evidence, crc(line) if crc(line) is not None else "PENDIENTE", tax, status, source])
    cot.append(["Materiales/equipos valorados", None, None, None, None, f"=SUM(F3:F{cot.max_row})", "No incluye pendientes", "PARCIAL", None])
    cot.auto_filter.ref = f"A2:I{cot.max_row}"

    title(labor, "MANO DE OBRA — VÍNCULO CON GANTT CANÓNICO", 9)
    labor.append(["Actividad", "Etapa", "Técnicos", "Días", "Horas", "Salario directo CRC", "Cargas/provisiones CRC", "Costo interno CRC", "Observación"])
    gw = load_workbook(GANTT, data_only=True)
    g = gw["Mano de obra"]
    for r in range(5, 31):
        activity, stage, technicians = g.cell(r,2).value, g.cell(r,3).value, g.cell(r,4).value
        days = (g.cell(r,7).value or 0) + (g.cell(r,8).value or 0)
        hours = (g.cell(r,9).value or 0) + (g.cell(r,10).value or 0)
        wage, burdens, total = g.cell(r,13).value or 0, g.cell(r,14).value or 0, g.cell(r,15).value or 0
        labor.append([activity, stage, technicians, days, hours, wage, burdens, total, g.cell(r,16).value])
    labor.append(["TOTAL GANTT", None, None, "=SUM(D3:D28)", "=SUM(E3:E28)", "=SUM(F3:F28)", "=SUM(G3:G28)", "=SUM(H3:H28)", "74 días hábiles; costo interno, no tarifa comercial"])
    labor.auto_filter.ref = "A2:I29"

    title(sale, "PRECIO DE VENTA — ESCENARIO BASE 44 SWITCHES", 4)
    sale.append(["Concepto", "Importe CRC", "Estado", "Base"])
    sale_rows = [
        ("Materiales y equipos valorados", "='Cotización'!F14", "PARCIAL", "Solo líneas valoradas"),
        ("Mano de obra interna", "='Mano de obra'!H29", "PROVISIONAL", "Gantt 26 actividades / TMED"),
        ("Herramientas y servicios especializados", "PENDIENTE", "PENDIENTE", "No sumar compra y servicio"),
        ("Costos directos valorados", "=SUM(B3:B4)", "PARCIAL", "Excluye partidas pendientes"),
        ("Imprevistos", "=B6*'Parámetros'!B6", "PROVISIONAL", "Parámetro editable"),
        ("Gastos administrativos", "=(B6+B7)*'Parámetros'!B7", "PROVISIONAL", "Parámetro editable"),
        ("Costo antes de utilidad", "=SUM(B6:B8)", "PARCIAL", "No es costo completo"),
        ("Utilidad", "=B9*'Parámetros'!B8", "PROVISIONAL", "Parámetro editable"),
        ("Precio de venta antes de IVA", "=B9+B10", "PARCIAL", "No incluye pendientes"),
        ("IVA referencia", "=B11*'Parámetros'!B5", "PROVISIONAL", "Confirmar condición tributaria"),
        ("TOTAL PROFORMA PARCIAL", "=B11+B12", "INCOMPLETO", "Servicios/fibra/canalización pendientes"),
    ]
    for row in sale_rows: sale.append(row)

    title(profit, "GANANCIAS — USO INTERNO", 4)
    profit.append(["Indicador", "Importe CRC", "Porcentaje", "Nota"])
    for row in [
        ("Costo directo parcial", "='Precio de venta'!B6", None, "No incluye costos pendientes"),
        ("Gastos administrativos", "='Precio de venta'!B8", "='Parámetros'!B7", "Supuesto"),
        ("Utilidad bruta propuesta", "='Precio de venta'!B10", "='Parámetros'!B8", "Supuesto; no es impuesto"),
        ("Precio antes de IVA", "='Precio de venta'!B11", None, "Parcial"),
    ]: profit.append(row)

    title(chrono, "CRONOGRAMA GANTT — REFERENCIA DEL PRESUPUESTO", 7)
    chrono.append(["Inicio", date(2026,11,2), "Fin", date(2027,2,16), "Días hábiles", 74, "Fuente: gantt/GANTT_INA_CABLEADO_2026-2027.xlsx"])
    chrono.append(["Etapa", "Actividades", "Costo interno CRC", "Estado", "", "", ""])
    for r in range(33,39): chrono.append([g.cell(r,1).value, None, g.cell(r,6).value, "Supuesto laboral", "", "", ""])
    chrono.append(["Advertencia", "El costo laboral es interno; no equivale al precio de venta. El año 2027 usa proyección pendiente de confirmar.", None, None, None, None, None])

    title(hol, "FERIADOS COSTA RICA — REFERENCIA GANTT", 3)
    hol.append(["Fecha", "Feriado", "Fuente"])
    gh = gw["Feriados CR"]
    for r in range(4, gh.max_row+1): hol.append([gh.cell(r,1).value, gh.cell(r,2).value, "Gantt canónico"])

    title(proforma, "FACTURA PROFORMA — PRESUPUESTO PRELIMINAR", 6)
    proforma.append(["Proforma N.º", "PRO-CENATE-2026-1105", "Fecha", date(2026,11,5), "Vigencia", "15 días"])
    proforma.append(["Emisor", "[PENDIENTE: razón social, identificación, teléfono y correo]", None, None, None, None])
    proforma.append(["Cliente", "INA CENATE — [PENDIENTE: contacto y datos fiscales]", None, None, None, None])
    proforma.append(["Proyecto", "Suministro e instalación de infraestructura de cableado estructurado y fibra óptica para dos edificios del complejo INA CENATE.", None, None, None, None])
    proforma.append([])
    proforma.append(["Concepto", "Alcance", "Subtotal antes IVA CRC", "IVA CRC", "Total CRC", "Estado"])
    proforma.append(["Materiales/equipos", "Partidas valoradas del escenario base", "='Cotización'!F14", 0, "=C7", "PARCIAL"])
    proforma.append(["Mano de obra", "26 actividades y 74 días hábiles", "='Precio de venta'!B4", 0, "=C8", "PROVISIONAL"])
    proforma.append(["Administración, imprevistos y utilidad", "Parámetros editables", "='Precio de venta'!B7+'Precio de venta'!B8+'Precio de venta'!B10", 0, "=C9", "PROVISIONAL"])
    proforma.append(["IVA referencia", "Aplicación tributaria por confirmar", 0, "='Precio de venta'!B12", "=D10", "PROVISIONAL"])
    proforma.append(["TOTAL PROFORMA PARCIAL", None, "=SUM(C7:C10)", "=SUM(D7:D10)", "=SUM(E7:E10)", "INCOMPLETA"])
    proforma.append([])
    proforma.append(["Condiciones", "Este documento no es comprobante fiscal electrónico. Incluye precios publicados y estimaciones marcadas; faltan cotizaciones de fibra, canalización/accesorios, servicios especializados y confirmación de disponibilidad. No constituye oferta firme ni autorización de compra.", None, None, None, None])
    proforma.append(["Alcance", "Edificios A y B: 62 laboratorios, 1.984 enlaces Cat 6A de escenario, 11 TR y 2 ER nuevos. Cantidades académicas, pendientes de validación de campo.", None, None, None, None])

    title(assumptions, "SUPUESTOS, PENDIENTES Y CONTROLES", 4)
    assumptions.append(["Clasificación", "Elemento", "Estado", "Acción"])
    for row in [
        ("Dato docente", "62 laboratorios; 992 áreas dobles", "Usado como base", "Confirmar con docente si cambia alcance"),
        ("Resultado académico", "1.984 enlaces, 229 carretes Cat6A, 478 tramos canasta", "Provisional", "Despiece físico y validación de instalación"),
        ("Precio publicado", "Switches Ticomer, transceptor CQNet, jack Circuito Cinco", "No es cotización firme", "Confirmar stock, IVA y vigencia"),
        ("Estimación", "Cable Cat6A, canasta, racks y paneles comparables", "Separada de publicada", "Cotizar referencias exactas"),
        ("Pendiente", "Fibra, conduit, herrajes, servicios de certificación/fusión", "Excluido de total", "Obtener cotización comparable"),
        ("Supuesto laboral", "TMED, cargas/provisiones y proyección 2027", "Provisional", "Validar categoría, régimen y tarifa comercial"),
        ("Control", "44 switches en base; 7 adicionales solo para 51", "Aplicado", "No sumar alternativa ampliada"),
    ]: assumptions.append(row)

    for ws in wb.worksheets:
        finish_sheet(ws)
        if ws.max_row >= 2:
            for cell in ws[2]:
                cell.font = Font(bold=True, color="FFFFFF")
                cell.fill = PatternFill("solid", fgColor="4F81BD")
        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, (int, float)) and cell.column >= 2:
                    cell.number_format = '#,##0.00;[Red](#,##0.00)'
    for ws in (cot, sources, labor, sale, profit, proforma):
        for row in ws.iter_rows(min_row=3):
            for c in row:
                if c.column in (6,8,12) and isinstance(c.value, (int,float)):
                    c.number_format = '₡#,##0.00;[Red](₡#,##0.00)'
    # make states easy to scan
    for ws in (cot, sources, assumptions):
        for row in ws.iter_rows(min_row=3):
            text = " ".join(str(c.value or "") for c in row).upper()
            if "PENDIENTE" in text:
                for c in row: c.fill = PatternFill("solid", fgColor="FFF2CC")
            elif "ESTIMADO" in text:
                for c in row: c.fill = PatternFill("solid", fgColor="FCE4D6")
    wb.calculation.fullCalcOnLoad = True
    wb.calculation.forceFullCalc = True
    wb.calculation.calcMode = "auto"
    return wb


def pdf_proforma(total):
    pdf = OUT / "FACTURA_PROFORMA_CENATE.pdf"
    doc = SimpleDocTemplate(str(pdf), pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.4*cm, bottomMargin=1.4*cm)
    sty = getSampleStyleSheet(); story = []
    story += [Paragraph("FACTURA PROFORMA — PRESUPUESTO PRELIMINAR", sty["Title"]), Spacer(1, 0.25*cm)]
    story += [Paragraph("Proforma: PRO-CENATE-2026-1105 &nbsp;&nbsp; Fecha: 2026-11-05 &nbsp;&nbsp; Vigencia: 15 días", sty["Normal"]), Spacer(1, 0.15*cm)]
    story += [Paragraph("Emisor: [PENDIENTE: razón social, identificación, teléfono y correo]. Cliente: INA CENATE — [PENDIENTE: contacto y datos fiscales].", sty["Normal"]), Spacer(1, 0.25*cm)]
    story += [Paragraph("Proyecto: Suministro e instalación de infraestructura de cableado estructurado y fibra óptica para dos edificios del complejo INA CENATE.", sty["BodyText"]), Spacer(1, 0.3*cm)]
    data = [["Concepto", "Alcance", "Total CRC", "Estado"],
            ["Materiales y equipos", "Partidas valoradas del escenario base", f"CRC {sum(x for x in map(crc, LINES) if x is not None):,.2f}", "Parcial"],
            ["Mano de obra", "26 actividades / 74 días hábiles", f"CRC {LABOR_INTERNAL:,.2f}", "Provisional"],
            ["TOTAL PROFORMA PARCIAL", "Incluye indirectos, utilidad e IVA de referencia", f"CRC {total:,.2f}", "INCOMPLETA"]]
    table = Table(data, colWidths=[4.0*cm, 7.0*cm, 3.6*cm, 2.1*cm])
    table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1F4E78")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("GRID",(0,0),(-1,-1),0.3,colors.grey),("VALIGN",(0,0),(-1,-1),"TOP"),("BACKGROUND",(0,3),(-1,3),colors.HexColor("#D9EAD3")),("FONTNAME",(0,3),(-1,3),"Helvetica-Bold"),("PADDING",(0,0),(-1,-1),6)]))
    story += [table, Spacer(1, 0.4*cm)]
    story += [Paragraph("Condiciones: esta proforma es preliminar y no es comprobante fiscal electrónico. Los precios publicados y estimados están identificados en el XLSX adjunto. El total no incluye componentes obligatorios aún pendientes de cotización: fibra óptica, conduit, herrajes, accesorios y servicios especializados de fusión/certificación. No constituye oferta firme ni autorización de compra.", sty["BodyText"])]
    doc.build(story)


def write_docs(total):
    sources_csv = OUT / "FUENTES_Y_ESTIMACIONES_PRESUPUESTO.csv"
    with sources_csv.open("w", encoding="utf-8", newline="") as fh:
        out = csv.writer(fh); out.writerow(["Grupo","Descripción","Cantidad","Unidad","Precio_unitario","Moneda","IVA","Importe_CRC","Clasificación","Fuente_fecha","Estado"])
        for line in LINES:
            out.writerow([*line[:7], crc(line), *line[7:]])
    (OUT / "NOTAS_DEL_PRESUPUESTO.md").write_text(f"""# Notas del presupuesto AC2

Fecha: 2026-11-05. Presupuesto académico preliminar generado desde U02 (115 registros), U03 (108 filas), U04C y el Gantt canónico (26 actividades, 74 días hábiles).

## Resultado

El total parcial mostrado en la proforma es **₡{total:,.2f}**. Incluye únicamente las líneas con importe verificable o estimado señalado y mano de obra interna del Gantt, con 5 % de imprevistos, 10 % administrativos, 15 % de utilidad e IVA de referencia 13 %. No es presupuesto completo ni oferta firme.

## Pendientes excluidos del total

- Cable OS2 vertical/exterior, terminaciones de fibra y disponibilidad de ópticos.
- Conduit, bajantes, herrajes, fijaciones y accesorios: falta despiece físico.
- Compra, alquiler o servicio de fusión, OLTS, OTDR y certificación: son alternativas excluyentes sin oferta comparable.
- Confirmación de stock, IVA y vigencia para precios publicados; tipo de cambio USD→CRC de referencia BCCR/MONEX venta ₡454,65 al 2026-11-04, actualizable.

Las cantidades 229 carretes y 478 tramos son cómputos académicos históricos y se presentan como tales. Las fuentes, URL, fecha y clasificación PUBLICADO/ESTIMADO/PENDIENTE están en `FUENTES_Y_ESTIMACIONES_PRESUPUESTO.csv` y en el libro.
""", encoding="utf-8")
    (OUT / "CORREO_ENTREGA_AC2.md").write_text("""Asunto: ACTIVIDAD DE COMPROBACIÓN 2

Estimado cliente:

Adjunto remitimos la propuesta preliminar para el suministro e instalación de infraestructura de cableado estructurado y fibra óptica para los dos edificios del complejo INA CENATE. Se incluyen el presupuesto editable y la factura proforma, con el detalle de fuentes, cantidades de escenario y supuestos de cálculo.

La propuesta separa los precios publicados de las estimaciones presupuestarias y señala expresamente los componentes que requieren cotización técnica, disponibilidad y validación de campo antes de una contratación definitiva. La factura proforma no constituye comprobante fiscal electrónico ni oferta firme mientras permanezcan esos pendientes.

Como complemento técnico, se adjunta nuevamente la documentación final de la Actividad de Comprobación 1: las nueve láminas técnicas y el libro académico consolidado.

Atentamente,

[PENDIENTE: nombre, cargo, empresa, identificación, teléfono y correo del emisor]
""", encoding="utf-8")
    (OUT / "ACTIVIDAD_1_REENVIO" / "INDICE_REENVIO_AC1.md").write_text("""# Reenvío Actividad de Comprobación 1

Incluye la copia consolidada del Excel académico final y nueve láminas técnicas PDF A3 de `08_entrega/ENTREGA_FINAL_INA_CENATE/`. Los archivos son copias de entrega: los originales históricos permanecen intactos. El escenario continúa sujeto a revisión académica y validación de campo.
""", encoding="utf-8")


def copy_ac1():
    dest = OUT / "ACTIVIDAD_1_REENVIO"
    (dest / "PLANOS_TECNICOS_PDF_A3").mkdir(parents=True, exist_ok=True)
    for src in sorted((AC1 / "06_PLANOS_TECNICOS/PDF_A3").glob("*.pdf")):
        shutil.copy2(src, dest / "PLANOS_TECNICOS_PDF_A3" / src.name)
    shutil.copy2(AC1 / "01_EXCEL/INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx", dest / "INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx")


def validate(path: Path):
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
    w = load_workbook(path, data_only=False)
    assert {"Cotización", "Mano de obra", "Precio de venta", "Ganancias", "Cronograma Gantt", "Feriados CR", "Factura proforma"}.issubset(w.sheetnames)
    text = "\n".join(str(c.value or "") for ws in w.worksheets for row in ws.iter_rows() for c in row)
    assert "#REF!" not in text and "#DIV/0!" not in text


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    copy_ac1()
    material = sum(x for x in map(crc, LINES) if x is not None)
    direct = material + LABOR_INTERNAL
    total = (direct * (1 + IMPREVISTOS) * (1 + ADMIN) * (1 + UTILIDAD)) * (1 + IVA)
    wb = build_book()
    budget = OUT / "PRESUPUESTO_FINAL_CENATE.xlsx"
    wb.save(budget); validate(budget)
    pdf_proforma(total); write_docs(total)
    with zipfile.ZipFile(OUT / "CIERRE_AC1_AC2_2026-11-05.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for p in OUT.rglob("*"):
            if p.is_file() and p.name != "CIERRE_AC1_AC2_2026-11-05.zip": z.write(p, p.relative_to(OUT))
    print(f"Presupuesto: {budget}; proforma parcial: CRC {total:,.2f}")


if __name__ == "__main__": main()
