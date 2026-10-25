"""Controles automáticos de integridad y coherencia para la Fase 2B."""

from __future__ import annotations

import csv
import hashlib
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")


ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "07_imagenes" / "fase2b"
ORIGINAL = ROOT / "06_excel" / "Plantilla Actividades de comprobación.xlsx"
WORKING = ROOT / "06_excel" / "Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx"
RESULTS = ROOT / "04_calculos" / "resultados_fase2b.csv"
EXPECTED_HASH = "707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6"


checks = []


def check(condition, label, detail=""):
    checks.append((bool(condition), label, detail))


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(65536), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def png_size(path):
    with path.open("rb") as fh:
        header = fh.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("firma PNG inválida")
    return struct.unpack(">II", header[16:24])


def validate_images():
    svgs = sorted(IMAGES.glob("[0-9][0-9]_*.svg"))
    pngs = sorted(IMAGES.glob("[0-9][0-9]_*.png"))
    check(len(svgs) == 9, "Cantidad de SVG", f"observados={len(svgs)}")
    check(len(pngs) == 9, "Cantidad de PNG", f"observados={len(pngs)}")
    combined = ""
    for svg in svgs:
        root = ET.parse(svg).getroot()
        check(root.tag.endswith("svg"), f"XML SVG válido: {svg.name}")
        combined += svg.read_text(encoding="utf-8")
    for png in pngs:
        size = png_size(png)
        check(size == (1600, 1000), f"PNG 1600×1000: {png.name}", f"observado={size}")
    required = [
        "EDIFICIO EXISTENTE", "EDIFICIO A", "EDIFICIO B", "E1: ER-P ↔ ER-A",
        "E2: ER-P ↔ ER-B", "E3: ER-A ↔ ER-B", "LAB-A-Pxx-L05", "LAB-B-Pxx-L06",
        "AT-16", "TR-A-Pxx", "TR-B-Pxx", "4 paneles Cat 6A × 48 puertos",
        "5 paneles Cat 6A × 48 puertos", "48 fibras terminadas", "84 fibras terminadas",
    ]
    for token in required:
        check(token in combined, f"Referencia cruzada SVG: {token}")


def validate_results():
    with RESULTS.open(encoding="utf-8", newline="") as fh:
        data = {row["id"]: row for row in csv.DictReader(fh)}
    expected = {
        "A_LABS": "20", "B_LABS": "42", "TOTAL_LABS": "62",
        "A_AREAS": "320", "B_AREAS": "672", "TOTAL_AREAS": "992",
        "A_RJ45": "640", "B_RJ45": "1344", "TOTAL_RJ45": "1984",
        "A_PANELES_TR": "4", "B_PANELES_TR": "5", "TOTAL_PANELES": "51",
        "TOTAL_TR": "11", "FIBRAS_TERM_VERTICAL": "264",
        "FIBRAS_TERM_EXTERIOR": "144", "PIGTAILS_Y_EMPALMES": "408",
        "ADAPTADORES_LC_DUPLEX": "204", "POSICIONES_CAJAS_145M": "5",
    }
    for key, value in expected.items():
        observed = data.get(key, {}).get("resultado")
        check(observed == value, f"Resultado {key}", f"esperado={value}; observado={observed}")
    check(data["A_CABLE_COBRE"]["resultado"] == "N/D", "Metraje cobre A permanece pendiente")
    check(data["B_CABLE_COBRE"]["resultado"] == "N/D", "Metraje cobre B permanece pendiente")


def validate_excel():
    h_original = sha256(ORIGINAL)
    h_working = sha256(WORKING)
    check(h_original == EXPECTED_HASH, "Hash del Excel original preservado", h_original)
    check(h_working == h_original, "Copia Excel byte a byte preservada", h_working)
    for path in (ORIGINAL, WORKING):
        with zipfile.ZipFile(path) as book:
            check(book.testzip() is None, f"Integridad OOXML: {path.name}")
            workbook = ET.fromstring(book.read("xl/workbook.xml"))
            names = [node.attrib["name"] for node in workbook.iter() if node.tag.endswith("sheet")]
            check(names == ["Cotización técnica", "Herramientas"], f"Hojas conservadas: {path.name}", str(names))
            formula_found = False
            for member in (n for n in book.namelist() if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")):
                root = ET.fromstring(book.read(member))
                for cell in (node for node in root.iter() if node.tag.endswith("c") and node.attrib.get("r") == "J43"):
                    for child in cell:
                        if child.tag.endswith("f") and child.text == "SUM(J2:J41)":
                            formula_found = True
            check(formula_found, f"Fórmula J43 conservada: {path.name}")


def main():
    validate_images()
    validate_results()
    validate_excel()
    failed = [item for item in checks if not item[0]]
    for passed, label, detail in checks:
        suffix = f" — {detail}" if detail else ""
        print(f"{'OK' if passed else 'FALLO'}: {label}{suffix}")
    print(f"RESUMEN: {len(checks) - len(failed)}/{len(checks)} controles aprobados")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
