"""Validación OOXML, fórmulas y trazabilidad del XLSX Fase 3B (stdlib)."""

from __future__ import annotations

import ast
import hashlib
import math
import re
import struct
import zipfile
import xml.etree.ElementTree as ET
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "06_excel" / "INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx"
PACKED = ROOT / "08_entrega" / "PAQUETE_REVISION_FASE3B" / BOOK.name
TEMPLATE = next(p for p in (ROOT / "06_excel").glob("Plantilla*.xlsx") if "TRABAJO" not in p.name)
IMAGES = ROOT / "07_imagenes" / "fase2b"
MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"m": MAIN, "r": REL}
checks: list[tuple[bool, str, str]] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append((bool(ok), label, detail))


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            h.update(block)
    return h.hexdigest().upper()


def formula_value(expr: str) -> Decimal:
    """Evalúa únicamente aritmética y ROUNDUP de las fórmulas de cantidad."""
    tree = ast.parse(expr, mode="eval")

    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return Decimal(str(node.value))
        if isinstance(node, ast.BinOp) and type(node.op) in (ast.Add, ast.Sub, ast.Mult, ast.Div):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add): return left + right
            if isinstance(node.op, ast.Sub): return left - right
            if isinstance(node.op, ast.Mult): return left * right
            return left / right
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = visit(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "ROUNDUP" and len(node.args) == 2:
            value, digits = visit(node.args[0]), int(visit(node.args[1]))
            scale = Decimal(10) ** digits
            return Decimal(math.ceil(value * scale)) / scale
        raise ValueError(f"Elemento no admitido en fórmula: {ast.dump(node)}")

    return visit(tree)


def workbook_cells(zf: zipfile.ZipFile):
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    relsroot = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rels = {e.attrib["Id"]: e.attrib["Target"] for e in relsroot}
    shared = []
    if "xl/sharedStrings.xml" in zf.namelist():
        ss = ET.fromstring(zf.read("xl/sharedStrings.xml"))
        shared = ["".join(t.text or "" for t in si.findall(".//m:t", NS)) for si in ss.findall("m:si", NS)]
    result = {}
    for sheet in wb.findall("m:sheets/m:sheet", NS):
        target = rels[sheet.attrib[f"{{{REL}}}id"].lstrip("/")]
        if not target.startswith("xl/"):
            target = "xl/" + target
        root = ET.fromstring(zf.read(target))
        cells = {}
        for cell in root.findall(".//m:sheetData/m:row/m:c", NS):
            ref = cell.attrib["r"]
            formula = cell.find("m:f", NS)
            value = cell.find("m:v", NS)
            inline = cell.find("m:is", NS)
            text = ""
            if inline is not None:
                text = "".join(t.text or "" for t in inline.findall(".//m:t", NS))
            elif value is not None:
                text = value.text or ""
                if cell.attrib.get("t") == "s" and text:
                    text = shared[int(text)]
            cells[ref] = {
                "text": text,
                "formula": formula.text if formula is not None else None,
                "style": cell.attrib.get("s"),
            }
        result[sheet.attrib["name"]] = (root, cells, target)
    return wb, result


def main() -> None:
    check(BOOK.is_file(), "XLSX generado presente")
    check(PACKED.is_file(), "Copia incluida en paquete 08_entrega")
    if not BOOK.is_file() or not PACKED.is_file():
        raise SystemExit("Falta el libro de salida.")

    check(sha(TEMPLATE) == "707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6", "Plantilla original conserva hash controlado")
    check(sha(BOOK) == sha(PACKED), "XLSX en 06_excel y 08_entrega idénticos")
    check((ROOT / "08_entrega/PAQUETE_REVISION_FASE3B/MEMORIA_CANTIDADES_FASE3B.md").is_file(), "Memoria Fase 3B incluida en paquete")
    packaged_images = ROOT / "08_entrega/PAQUETE_REVISION_FASE3B/IMAGENES_REVISION"
    check(len(list(packaged_images.glob("[0-9][0-9]_*.*"))) == 18, "Paquete incluye nueve SVG y nueve PNG")
    for image in IMAGES.glob("[0-9][0-9]_*.*"):
        packaged = packaged_images / image.name
        check(packaged.is_file() and sha(packaged) == sha(image), f"Imagen del paquete idéntica: {image.name}")
    with zipfile.ZipFile(BOOK) as zf:
        check(zf.testzip() is None, "Integridad ZIP/OOXML")
        xml_files = [n for n in zf.namelist() if n.endswith((".xml", ".rels"))]
        xml_bad = []
        for name in xml_files:
            try: ET.fromstring(zf.read(name))
            except ET.ParseError as exc: xml_bad.append((name, str(exc)))
        check(not xml_bad, "Todas las partes XML y relaciones analizan", str(xml_bad[:2]))
        workbook, sheets = workbook_cells(zf)
        with zipfile.ZipFile(TEMPLATE) as original:
            check(hashlib.sha256(zf.read("xl/styles.xml")).digest() == hashlib.sha256(original.read("xl/styles.xml")).digest(), "Catálogo de estilos idéntico al original")
            _, original_sheets = workbook_cells(original)
            if list(original_sheets) == list(sheets):
                styles_preserved = True
                for name in sheets:
                    original_cells = original_sheets[name][1]
                    output_cells = sheets[name][1]
                    for ref, old_cell in original_cells.items():
                        if ref in output_cells and old_cell.get("style") != output_cells[ref].get("style"):
                            styles_preserved = False
                            break
                check(styles_preserved, "Estilos de todas las celdas originales conservados")
        check(list(sheets) == ["Cotización técnica", "Herramientas"], "Dos hojas originales en el orden previsto", str(list(sheets)))
        calc = workbook.find("m:calcPr", NS)
        check(calc is not None and calc.attrib.get("calcMode") == "auto" and calc.attrib.get("fullCalcOnLoad") == "1", "Recálculo automático al abrir configurado")

        if all(name in sheets for name in ("Cotización técnica", "Herramientas")):
            matroot, materials, matpath = sheets["Cotización técnica"]
            _, tools, _ = sheets["Herramientas"]
            dim = matroot.find("m:dimension", NS)
            check(dim is not None and dim.attrib.get("ref") == "A1:K51", "Columnas A–K y notas al pie dentro de la hoja", str(dim.attrib if dim is not None else None))
            headers = [materials.get(f"{col}1", {}).get("text") for col in "ABCDEFGHIJK"]
            check(headers == ["Material o equipo", "Categoría o tipo", "Especificaciones técnicas", "Marca", "Modelo o referencia", "Unidad de medida", "Cantidad", "Proveedor", "Precio unitario (₡)", "Precio total (₡)", "Fuente"], "Encabezados A–K conservados")

            # Las fórmulas y sus cachés se evalúan sin abrir Excel.
            material_formulas = []
            cached = {}
            for row in range(2, 31):
                cell = materials.get(f"G{row}", {})
                formula = cell.get("formula")
                if formula is not None:
                    material_formulas.append(row)
                    try:
                        calculated = formula_value(formula)
                        cached_value = Decimal(cell["text"])
                        check(calculated == cached_value, f"Fórmula/caché G{row}", f"f={formula}; calc={calculated}; cache={cached_value}")
                        cached[row] = calculated
                    except Exception as exc:
                        check(False, f"Fórmula válida G{row}", str(exc))
            check(material_formulas == list(range(2, 31)), "29 filas materiales tienen fórmulas funcionales", str(material_formulas))
            expected = {2:229,3:51,4:1984,5:992,6:992,7:1984,8:1984,9:221.55,10:247.8,11:69.3,12:89.25,13:194.775,14:22,15:6,16:12,17:1,18:1,19:28,20:13,21:51,22:14,23:13,24:478,25:1042,26:50,27:6,28:3968,29:0,30:0}
            for row, wanted in expected.items():
                value = cached.get(row)
                check(value is not None and value == Decimal(str(wanted)), f"Cantidad fila {row}", f"esperado={wanted}; observado={value}")

            all_text = "\n".join(v["text"] for v in materials.values())
            names = [materials[f"A{r}"]["text"] for r in range(2, 31)]
            check(len(names) == len(set(names)), "Sin renglones de materiales duplicados")
            forbidden = re.findall(r"#(?:REF!|VALUE!|DIV/0!|NAME\?|N/A)", all_text, re.I)
            check(not forbidden, "Sin errores de fórmula expuestos en celdas")
            check(not re.search(r"ejemplo|proveedor [a-z]|ref\. didáctica", all_text, re.I), "Ejemplos didácticos retirados")
            check(all(materials.get(f"I{r}", {}).get("text", "") == "" and materials.get(f"J{r}", {}).get("text", "") == "" for r in range(2, 42)), "Precios y costos I/J vacíos")
            check(materials.get("J43", {}).get("formula") is None and materials.get("J43", {}).get("text", "") == "", "J43 sin fórmula monetaria en la copia final")
            check("CANTIDADES DE MATERIALES" in materials.get("A43", {}).get("text", ""), "Rótulo de total económico sustituido por cantidades")
            check(materials.get("G29", {}).get("text") == "0" and materials.get("G30", {}).get("text") == "0", "Pigtails/adaptadores separados en cero; sin duplicación")
            check("No verificado localmente" in all_text, "Proveedores no inventados")
            check("x=75 m" in all_text and "y=50 m" in all_text, "Estimaciones exteriores declaradas")
            check("1 circuito LC dúplex por cada uno" in all_text, "Escenario de fibra activa declarado")
            check(materials.get("A45", {}).get("text", "").startswith("ADVERTENCIA"), "Notas de supuestos visibles en hoja")

            tool_numeric = []
            for row in range(2, 13):
                cell = tools.get(f"B{row}", {})
                if cell.get("formula") is not None:
                    value = formula_value(cell["formula"])
                    check(value == Decimal(cell["text"]), f"Cantidad herramienta B{row}", f"f={cell['formula']}; v={cell['text']}")
                    tool_numeric.append(row)
            check(tool_numeric == list(range(2, 13)), "11 herramientas reutilizables con cantidad", str(tool_numeric))
            check("consumible" in tools.get("A13", {}).get("text", "").lower() and "Variable" in tools.get("B13", {}).get("text", ""), "Lubricante distinguido como consumible variable")
            check(not re.search(r"ejemplo|proveedor [a-z]|ref\. didáctica", "\n".join(v["text"] for v in tools.values()), re.I), "Ejemplos retirados de Herramientas")

    # Coherencia material/diagrama: revisar los nueve SVG, no volver a calcular.
    svgs = sorted(IMAGES.glob("[0-9][0-9]_*.svg"))
    pngs = sorted(IMAGES.glob("[0-9][0-9]_*.png"))
    check(len(svgs) == len(pngs) == 9, "Nueve diagramas fuente y nueve PNG")
    texts = {p.name: p.read_text(encoding="utf-8") for p in svgs}
    exterior = texts.get("01_backbone_exterior.svg", "")
    check("x = 75 m (supuesto)" in exterior and "y = 50 m (supuesto)" in exterior, "Diagrama exterior alineado con E2/E3")
    for name in ("02_planta_tipica_edificio_A.svg", "03_planta_tipica_edificio_B.svg"):
        check("Bandeja 100×50 mm preliminar" in texts.get(name, ""), f"Canalización de planta coherente: {name}")
    for name in ("04_laboratorio_tipico_A.svg", "05_laboratorio_tipico_B.svg"):
        check("Tubería Ø25 mm preliminar" in texts.get(name, ""), f"Bajante coherente: {name}")
    for name in ("06_ER_A.svg", "08_ER_B.svg"):
        check("Ducto Ø50 mm preliminar" in texts.get(name, ""), f"Ducto óptico coherente: {name}")
    for name in ("07_TR_A.svg", "09_TR_B.svg"):
        txt = texts.get(name, "")
        check("28 cords en total" in txt and "Bandeja 100×50 mm" in txt and "Ø25 mm" in txt, f"TR/cantidades/ductos coherentes: {name}")
    for path in pngs:
        data = path.read_bytes()
        size = struct.unpack(">II", data[16:24]) if data[:8] == b"\x89PNG\r\n\x1a\n" else None
        check(size == (1600, 1000), f"PNG válido 1600×1000: {path.name}")

    failures = [(label, detail) for ok, label, detail in checks if not ok]
    for ok, label, detail in checks:
        print(f"{'OK' if ok else 'ERROR'}: {label}" + (f" — {detail}" if detail else ""))
    print(f"RESUMEN FASE 3B: {len(checks)-len(failures)}/{len(checks)} controles aprobados")
    print(f"XLSX_SHA256={sha(BOOK)}")
    print(f"TEMPLATE_SHA256={sha(TEMPLATE)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
