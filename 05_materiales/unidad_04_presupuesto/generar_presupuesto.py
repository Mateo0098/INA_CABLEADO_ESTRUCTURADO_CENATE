"""Genera el presupuesto independiente de U04C desde las matrices y ofertas CSV.

Requiere openpyxl>=3.1. Los precios web son provisionales y las fórmulas
quedan sin cache hasta abrir el libro en un motor de cálculo.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
U02 = ROOT / "05_materiales/unidad_02_ampliacion/UNIDAD_02_MATRIZ_MAESTRA_MATERIALES.csv"
U03 = ROOT / "05_materiales/unidad_03_herramientas/UNIDAD_03_MATRIZ_MAESTRA_HERRAMIENTAS.csv"
OFFERS = HERE / "UNIDAD_04C_OFERTAS.csv"
OUTPUT = HERE / "PRESUPUESTO_INTEGRADO_RED_OPERATIVA.xlsx"


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def number_from_reference(raw: str):
    match = re.fullmatch(r"(\d+(?:[.,]\d+)?)\s+(?:REFERENCIA|BASE|CANDIDATOS)", raw.strip())
    return float(match.group(1).replace(",", ".")) if match else None


def build():
    a, b, offers = read_csv(U02), read_csv(U03), read_csv(OFFERS)
    ids = [r["ID único"] for r in a + b]
    if len(a) != 115 or len(b) != 108 or len(ids) != len(set(ids)):
        raise ValueError("Conteo o IDs de matrices inválidos")
    if len({o["ID_oferta"] for o in offers}) != len(offers) or any(o["ID_partida"] not in ids for o in offers):
        raise ValueError("Oferta repetida o sin partida válida")

    wb = Workbook()
    summary = wb.active
    summary.title = "01_RESUMEN"
    p = wb.create_sheet("02_PARTIDAS")
    q = wb.create_sheet("03_COTIZACIONES")
    scenarios = wb.create_sheet("04_ESCENARIOS")
    imp = wb.create_sheet("05_IMPORTACIONES")
    params = wb.create_sheet("06_PARAMETROS")
    pending = wb.create_sheet("07_PENDIENTES")
    control = wb.create_sheet("08_CONTROL_Y_FUENTES")

    params.append(["Parámetro", "Valor", "Fuente / estado"])
    for row in [
        ["Moneda base", "CRC", "Definición del presupuesto U04C"],
        ["Tipo de cambio USD→CRC", None, "PENDIENTE: registrar fuente y fecha; no usar valor arbitrario"],
        ["Fuente tipo de cambio", None, "PENDIENTE"],
        ["Fecha tipo de cambio", None, "PENDIENTE, AAAA-MM-DD"],
        ["IVA general de referencia", 0.13, "Hacienda, Generalidades IVA, actualizado 2024-09-24; confirmar aplicabilidad por oferta"],
        ["Escenario de acceso", 44, "Unidad 01: 44 base o 51 ampliado; propuesta no aprobada"],
        ["Número de cuadrillas", 1, "Supuesto U03; pendiente aprobación"],
        ["Modalidad instrumentos", "Compra", "Compra / Servicio; selección pendiente"],
        ["Reserva adicional aprobada", None, "PENDIENTE; no duplicar 5 % ya incorporado en U02"],
        ["Fecha de consulta comercial", "2026-11-05", "Consulta web registrada por Codex"],
    ]:
        params.append(row)
    params["B6"].number_format = "0%"
    dv_s = DataValidation(type="list", formula1='"44,51"')
    params.add_data_validation(dv_s); dv_s.add(params["B7"])
    dv_m = DataValidation(type="list", formula1='"Compra,Servicio"')
    params.add_data_validation(dv_m); dv_m.add(params["B9"])

    q_headers = ["ID partida", "ID oferta", "Proveedor", "País", "Fabricante", "Modelo/SKU", "Descripción comercial", "Unidad venta", "Contenido kit", "Precio publicado", "Moneda", "IVA estado", "Disponibilidad", "Cantidad disponible", "Fecha consulta", "Vigencia", "URL evidencia", "Compatibilidad técnica", "Estado verificación", "Elegibilidad"]
    q.append(q_headers)
    for o in offers:
        q.append([o[k] if k not in ("Precio_publicado", "Cantidad_disponible") or not o[k] else float(o[k]) for k in o])
    # La búsqueda de oferta usa ID único; no se selecciona una alternativa por menor precio.
    h = ["ID", "Unidad origen", "Subsistema", "Descripción", "Especificación técnica", "Modelo candidato", "Cantidad funcional", "Unidad funcional", "Unidad comercial", "Factor conversión", "Cantidad comercial", "Reserva/desperdicio", "Escenario", "Modalidad adquisición", "Estado aprobación", "Oferta seleccionada", "Precio unitario", "Moneda", "IVA estado", "IVA aplicable", "Costo neto CRC", "IVA CRC", "Costo calculado CRC", "Estado precio", "Estado cantidad", "Observaciones", "Dependencias/duplicación", "Grupo económico", "Activo escenario"]
    p.append(h)
    selected = {"U02-02C-025": "OF-001", "U02-02C-026": "OF-002", "U02-02C-027": "OF-003"}
    for source, rows in (("U02", a), ("U03", b)):
        for r in rows:
            ident = r["ID único"]
            if source == "U02":
                name = r["Componente"]; raw = r["Cantidad calculada o variable"]
                qty = number_from_reference(raw)
                unit = r["Unidad funcional"]
                commercial = r["Unidad comercial de compra"]
                model = r["Marca/modelo candidato"]
                duplication = r["Control de duplicaciones"]
                reserve = r["Reserva o desperdicio"]
                notes = r["Pendiente técnico"]
                spec = r["Especificación requerida"]
                modality = "Compra"
                group = "Equipo activo" if "Switch" in name or "Transceptor" in name or "DAC" in name else "Material"
                scenario = "Adicional 51" if ident in ("U02-02C-026", "U02-02D-014") else "Base"
                if ident in ("U02-02C-026", "U02-02D-014"):
                    qty = 7  # Solo siete unidades adicionales; no sumar 51 a la base.
                if "0 JUSTIFICADO" in raw.upper():
                    qty = 0; scenario = "Incluido en kit"
            else:
                name = r["Herramienta equipo o consumible"]; raw = r["Cantidad de referencia"]
                qty = number_from_reference(raw)
                unit = r["Unidad funcional"]; commercial = r["Unidad comercial"]
                model = r["Modelo o referencia candidata"]
                duplication = r["Recurso compartido o duplicación"] + " | " + r["Referencia a Unidad 02"]
                reserve = ""; notes = r["Pendiente técnico"]
                spec = r["Especificación requerida"]
                modality = "Compra"
                group = "Servicio" if "Servicio" in name else ("EPP" if ident.startswith("U03-03D") else "Herramienta")
                scenario = "Alternativa servicio" if group == "Servicio" else "Base"
                if scenario == "Alternativa servicio": modality = "Servicio"
            # Cantidades de referencia U03 son dotaciones funcionales, no compras aprobadas.
            if source == "U03": qty = None
            if ident == "U02-02B-029":
                # 229 cajas académicas, ya redondeadas; la conversión real depende del despiece.
                qty = None
            rowno = p.max_row + 1
            p.append([ident, source, r.get("Subsistema", r.get("Subunidad de origen")), name, spec, model,
                      qty, unit, commercial, 1 if qty is not None and ident in selected else None,
                      None, reserve, scenario, modality, "Provisional; revisión humana", selected.get(ident),
                      None, None, None, None, None, None, None, None, None, notes,
                      duplication, group, None])
            n = rowno
            p[f"K{n}"] = f'=IF(OR(G{n}="",J{n}=""),"PENDIENTE",ROUNDUP(G{n}/J{n},0))'
            p[f"Q{n}"] = f'=IF(P{n}="","",IFERROR(VLOOKUP(P{n},\'03_COTIZACIONES\'!$B$2:$T$100,9,FALSE),""))'
            p[f"R{n}"] = f'=IF(P{n}="","",IFERROR(VLOOKUP(P{n},\'03_COTIZACIONES\'!$B$2:$T$100,10,FALSE),""))'
            p[f"S{n}"] = f'=IF(P{n}="","",IFERROR(VLOOKUP(P{n},\'03_COTIZACIONES\'!$B$2:$T$100,11,FALSE),""))'
            p[f"T{n}"] = f'=IF(OR(S{n}="Incluido",S{n}="Excluido"),\'06_PARAMETROS\'!$B$6,"")'
            p[f"AC{n}"] = f'=IF(M{n}="Incluido en kit",0,IF(M{n}="Adicional 51",IF(\'06_PARAMETROS\'!$B$7=51,1,0),IF(M{n}="Alternativa servicio",IF(\'06_PARAMETROS\'!$B$9="Servicio",1,0),IF(AND(\'06_PARAMETROS\'!$B$9="Servicio",OR(A{n}="U03-03B-010",A{n}="U03-03C-001",A{n}="U03-03C-017",A{n}="U03-03C-018")),0,1))))'
            p[f"U{n}"] = f'=IF(OR(AC{n}=0,NOT(ISNUMBER(K{n})),NOT(ISNUMBER(Q{n})),NOT(ISNUMBER(T{n})),R{n}="",COUNTIFS(\'03_COTIZACIONES\'!$A$2:$A$100,A{n},\'03_COTIZACIONES\'!$B$2:$B$100,P{n})<>1,AND(R{n}="USD",NOT(ISNUMBER(\'06_PARAMETROS\'!$B$3)))),"PENDIENTE",K{n}*Q{n}*IF(R{n}="CRC",1,\'06_PARAMETROS\'!$B$3)/IF(S{n}="Incluido",1+T{n},1))'
            p[f"V{n}"] = f'=IF(NOT(ISNUMBER(U{n})),"PENDIENTE",IF(S{n}="Incluido",K{n}*Q{n}*IF(R{n}="CRC",1,\'06_PARAMETROS\'!$B$3)-U{n},IF(ISNUMBER(T{n}),U{n}*T{n},"PENDIENTE")))'
            p[f"W{n}"] = f'=IF(OR(NOT(ISNUMBER(U{n})),NOT(ISNUMBER(V{n}))),"PENDIENTE",U{n}+V{n})'
            p[f"X{n}"] = f'=IF(P{n}="","Sin precio",IF(NOT(ISNUMBER(Q{n})),"Sin precio","Precio web provisional"))'
            p[f"Y{n}"] = f'=IF(NOT(ISNUMBER(K{n})),"Sin cantidad comercial","Referencia provisional")'

    end = p.max_row
    summary.append(["UNIDAD 04C — PRESUPUESTO PARCIAL DOCUMENTADO", "Valor / estado"])
    for title, formula in [
        ("Materiales", f'=SUMIFS(\'02_PARTIDAS\'!$W$2:$W${end},\'02_PARTIDAS\'!$AB$2:$AB${end},"Material")'),
        ("Equipos activos", f'=SUMIFS(\'02_PARTIDAS\'!$W$2:$W${end},\'02_PARTIDAS\'!$AB$2:$AB${end},"Equipo activo")'),
        ("Herramientas", f'=SUMIFS(\'02_PARTIDAS\'!$W$2:$W${end},\'02_PARTIDAS\'!$AB$2:$AB${end},"Herramienta")'),
        ("EPP", f'=SUMIFS(\'02_PARTIDAS\'!$W$2:$W${end},\'02_PARTIDAS\'!$AB$2:$AB${end},"EPP")'),
        ("Servicios instalación/certificación", f'=SUMIFS(\'02_PARTIDAS\'!$W$2:$W${end},\'02_PARTIDAS\'!$AB$2:$AB${end},"Servicio")'),
        ("Logística", "PENDIENTE"),
        ("IVA incluido en subtotal valorado", f'=SUM(\'02_PARTIDAS\'!$V$2:$V${end})'),
        ("Subtotal cuantificado y valorado, CRC", f'=SUM(\'02_PARTIDAS\'!$W$2:$W${end})'),
        ("Partidas activas sin precio", f'=COUNTIFS(\'02_PARTIDAS\'!$AC$2:$AC${end},1,\'02_PARTIDAS\'!$X$2:$X${end},"Sin precio")'),
        ("Partidas activas sin cantidad comercial", f'=COUNTIFS(\'02_PARTIDAS\'!$AC$2:$AC${end},1,\'02_PARTIDAS\'!$Y$2:$Y${end},"Sin cantidad comercial")'),
        ("Cobertura de costo calculable", f'=COUNTIFS(\'02_PARTIDAS\'!$AC$2:$AC${end},1,\'02_PARTIDAS\'!$W$2:$W${end},">=0")/COUNTIF(\'02_PARTIDAS\'!$AC$2:$AC${end},1)'),
        ("Total completo", "NO DISPONIBLE: componentes obligatorios pendientes"),
        ("Estado", "INCOMPLETO — cifras valoradas son provisionales"),
    ]:
        summary.append([title, formula])
    summary["B12"].number_format = "0.0%"

    scenarios.append(["Modalidad", "Acceso", "Switches base", "Switches adicionales", "Subtotal switches valorados CRC", "Costo completo", "Condición"])
    for modality in ("A Compra nacional", "B Servicio/alquiler", "C Importación selectiva"):
        for count in (44, 51):
            row = scenarios.max_row + 1
            scenarios.append([modality, count, 44, 0 if count == 44 else 7,
                              f'=(44*\'03_COTIZACIONES\'!J2+2*\'03_COTIZACIONES\'!J4+D{row}*\'03_COTIZACIONES\'!J3)*(1+\'06_PARAMETROS\'!B6)',
                              "NO DISPONIBLE", "B/C sin oferta comparable o costo integral; no sumar compra y servicio"])
    imp.append(["ID partida", "Oferta", "Precio exterior", "Moneda", "Cantidad", "Transporte internacional", "Seguro", "CIF CRC", "Clasificación arancelaria", "Arancel %", "Arancel CRC", "Base IVA CRC", "IVA importación %", "IVA importación CRC", "Gestión aduanera", "Manejo/almacenaje", "Entrega local", "Puesto en Costa Rica CRC", "Estado"])
    for row in range(2, 22):
        imp.append([None] * 19)
        imp[f"H{row}"] = f'=IF(OR(NOT(ISNUMBER(C{row})),NOT(ISNUMBER(E{row})),NOT(ISNUMBER(F{row})),NOT(ISNUMBER(G{row})),\'06_PARAMETROS\'!B3=""),"PENDIENTE",C{row}*E{row}*IF(D{row}="CRC",1,\'06_PARAMETROS\'!B3)+F{row}+G{row})'
        imp[f"K{row}"] = f'=IF(OR(NOT(ISNUMBER(H{row})),I{row}="",NOT(ISNUMBER(J{row}))),"PENDIENTE",H{row}*J{row})'
        imp[f"L{row}"] = f'=IF(OR(NOT(ISNUMBER(H{row})),NOT(ISNUMBER(K{row}))),"PENDIENTE",H{row}+K{row})'
        imp[f"N{row}"] = f'=IF(OR(NOT(ISNUMBER(L{row})),NOT(ISNUMBER(M{row}))),"PENDIENTE",L{row}*M{row})'
        imp[f"R{row}"] = f'=IF(OR(NOT(ISNUMBER(L{row})),NOT(ISNUMBER(N{row})),NOT(ISNUMBER(O{row})),NOT(ISNUMBER(P{row})),NOT(ISNUMBER(Q{row}))),"PENDIENTE",L{row}+N{row}+O{row}+P{row}+Q{row})'
        imp[f"S{row}"] = f'=IF(ISNUMBER(R{row}),"Calculable","Incompleto: tributos/logística")'
    pending.append(["ID partida", "Descripción", "Estado costo", "Motivo principal", "Acción requerida"])
    for row in range(2, end + 1):
        pending.append([f"='02_PARTIDAS'!A{row}", f"='02_PARTIDAS'!D{row}", f"='02_PARTIDAS'!W{row}",
                        f'=IF(\'02_PARTIDAS\'!AC{row}=0,"Alternativa/incluido",IF(\'02_PARTIDAS\'!Y{row}="Sin cantidad comercial","Sin cantidad/unidad validada",IF(\'02_PARTIDAS\'!X{row}="Sin precio","Sin precio/selección",IF(\'02_PARTIDAS\'!S{row}="No confirmado","Impuestos sin confirmar","Verificar disponibilidad/aprobación"))))',
                        f"='02_PARTIDAS'!Z{row}"])
    for item in [
        ["Origen", "U02: 115 filas; U03: 108 filas; CSV originales sin modificar."],
        ["Ofertas", "CSV U04C; precio web no constituye cotización firme ni inventario suficiente."],
        ["Cantidad", "K=ROUNDUP(cantidad funcional/factor comercial,0). Factor 1 solo en switches con unidades iguales."],
        ["IVA", "Precio con IVA: neto=bruto/(1+tasa), IVA=bruto-neto. Sin IVA: IVA=neto*tasa. No confirmado: costo pendiente."],
        ["Cambio", "USD exige B3 de parámetros con fuente y fecha. Sin ello no hay conversión."],
        ["Escenarios", "7 switches de B adicional se activan solo con 51. Servicios dependen de modalidad; no se suman instrumentos equivalentes."],
        ["Importaciones", "CIF, arancel y tributos quedan pendientes hasta clasificar mercancía y verificar tasa específica."],
        ["Actualización", "Editar CSV de ofertas y regenerar, o editar libro para análisis; para persistir cambios, llevarlos al CSV/script."],
        ["Limitación", "openpyxl escribe fórmulas sin evaluarlas. Confirmar recálculo y revisión visual en Excel."],
        ["Autoría", "Codex, asistencia de IA, 2026-11-05. Revisión técnica/académica humana pendiente."],
        ["IVA fuente", "https://www.hacienda.go.cr/docs/GeneralidadesIVA.pdf (consulta 2026-11-05); tarifa general 13 %, aplicación sujeta a factura."],
    ]:
        control.append(item)

    blue = PatternFill("solid", fgColor="DCEAF5")
    orange = PatternFill("solid", fgColor="FFF1D6")
    for ws in wb:
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        ws.row_dimensions[1].height = 30
        for cell in ws[1]:
            cell.fill = PatternFill("solid", fgColor="1F4E78")
            cell.font = Font(color="FFFFFF", bold=True)
            cell.alignment = Alignment(wrap_text=True, vertical="center")
        for col in ws.columns:
            letter = get_column_letter(col[0].column)
            width = min(55, max(14, max(len(str(c.value or "")) for c in list(col)[:60]) + 2))
            ws.column_dimensions[letter].width = width
    for ws, cols in ((p, ("G", "J", "P")), (params, ("B",))):
        for col in cols:
            for cells in ws[f"{col}2:{col}{ws.max_row}"]:
                cells[0].fill = blue
    for row in range(2, p.max_row + 1):
        for col in ("K", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"):
            p[f"{col}{row}"].fill = orange
        for col in ("Q", "U", "V", "W"):
            p[f"{col}{row}"].number_format = '#,##0.00;[Red](#,##0.00)'
    for row in range(2, q.max_row + 1): q[f"J{row}"].number_format = '#,##0.00'
    for row in range(2, summary.max_row + 1):
        if row not in (10, 11, 12, 13, 14): summary[f"B{row}"].number_format = '#,##0.00'
    wb.calculation.fullCalcOnLoad = True
    wb.calculation.forceFullCalc = True
    wb.calculation.calcMode = "auto"
    wb.save(OUTPUT)
    checked = load_workbook(OUTPUT, read_only=True)
    assert len(checked.sheetnames) == 8 and checked["02_PARTIDAS"].max_row == 224
    checked.close()
    print(f"{OUTPUT}: 223 partidas, {len(offers)} ofertas, 8 hojas")


if __name__ == "__main__":
    build()
