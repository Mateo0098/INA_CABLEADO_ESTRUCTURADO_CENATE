"""Controles reproducibles del cierre de cantidades Fase 2D."""

from __future__ import annotations

import csv
import hashlib
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile
from decimal import Decimal
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "04_calculos" / "resultados_fase2d.csv"
MATRIX = ROOT / "05_materiales" / "MATRIZ_TECNICA_FASE2D.md"
PLAN = ROOT / "06_excel" / "PLAN_FILAS_MATERIALES_FASE2D.csv"
TOOLS = ROOT / "06_excel" / "PLAN_FILAS_HERRAMIENTAS_FASE2D.csv"
IMAGES = ROOT / "07_imagenes" / "fase2b"
PACKAGE = ROOT / "08_entrega" / "PAQUETE_REVISION_FASE2D"
ORIGINAL = next((ROOT / "06_excel").glob("Plantilla Actividades de comprobaci*n.xlsx"))
WORKING = next((ROOT / "06_excel").glob("*_TRABAJO_FASE2B.xlsx"))
EXPECTED_XLSX_HASH = "707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6"

checks = []


def check(condition, label, detail=""):
    checks.append((bool(condition), label, detail))


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def png_size(path):
    with path.open("rb") as stream:
        header = stream.read(24)
    return struct.unpack(">II", header[16:24]) if header[:8] == b"\x89PNG\r\n\x1a\n" else None


def validate_results():
    with RESULTS.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    data = {row["id"]: row for row in rows}
    check(len(rows) == 58, "58 resultados Fase 2D", f"observados={len(rows)}")
    expected = {
        "A_COBRE_RUTA_PROM": "30.375",
        "B_COBRE_RUTA_PROM": "30.325",
        "A_COBRE_MAX_CON_RESERVA": "45.7",
        "B_COBRE_MAX_CON_RESERVA": "42.7",
        "A_COBRE_CUMPLE_90M": "SI",
        "B_COBRE_CUMPLE_90M": "SI",
        "TOTAL_COBRE_REQUERIDO": "69456.24",
        "TOTAL_COBRE_CAJAS_305M": "229",
        "TOTAL_COBRE_METROS_COMERCIALES": "69845",
        "TOTAL_FIBRA_VERTICAL_REQUERIDA": "284.025",
        "E1_FIBRA_24F_REQUERIDA": "221.55",
        "TOTAL_FIBRA_24F_FORMULA": "407.4 + 1.05x + 1.05y",
        "HOUSING_CCH_01U": "12",
        "HOUSING_CCH_03U": "1",
        "HOUSING_CCH_04U": "1",
        "RACK_42U_NUEVOS": "13",
        "PIGTAILS_COMPRA_SEPARADA": "0",
        "ADAPTADORES_COMPRA_SEPARADA": "0",
    }
    for result_id, value in expected.items():
        check(result_id in data and data[result_id]["resultado"] == value, f"Resultado {result_id}", f"esperado={value}; observado={data.get(result_id, {}).get('resultado')}")
    check(Decimal(data["A_COBRE_MAX_CON_RESERVA"]["resultado"]) <= 90, "Ruta A ≤ 90 m")
    check(Decimal(data["B_COBRE_MAX_CON_RESERVA"]["resultado"]) <= 90, "Ruta B ≤ 90 m")
    check("pendiente x" in data["E2_FIBRA_24F_FORMULA"]["estado"], "E2 conserva x pendiente")
    check("pendiente y" in data["E3_FIBRA_24F_FORMULA"]["estado"], "E3 conserva y pendiente")


def validate_materials_and_excel_plan():
    matrix = MATRIX.read_text(encoding="utf-8")
    for token in (
        "PUP6AHD04BU-G", "NK6XPPG48Y", "CJ6X88TGBU", "CFPL2WHY", "UTP28X7BU",
        "024EUK-T3601D2M", "012E81-33131-24", "CCH-CS12-A9-P00RE",
        "CCH-CS24-A9-P00RE", "CCH-01U", "CCH-03U", "CCH-04U",
        "040402R5120003M", "AR3100B2", "AR8425A",
    ):
        check(token in matrix, f"Referencia trazada: {token}")
    check("Pigtail LC/UPC separado | No comprar" in matrix, "Pigtails separados excluidos")
    check("Adaptador LC dúplex separado | No comprar" in matrix, "Adaptadores separados excluidos")
    check("No se seleccionan switches" in matrix, "Activos separados del sistema pasivo")

    with PLAN.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    observed = [int(row["fila_excel"]) for row in rows]
    check(observed == list(range(2, 28)), "Plan de materiales cubre filas 2–27", str(observed))
    check(all(not row.get("precio", "") for row in rows), "Plan sin columna/precios")
    check(all(row["accion_estudiante"].strip() for row in rows), "Todas las filas tienen acción")
    by_id = {row["id_material"]: row for row in rows}
    check(by_id["2D-CU-01"]["resultado_referencia"] == "229", "Excel cobre = 229 cajas")
    check(by_id["2D-FO-01B"]["estado_resultado"] == "PENDIENTE_X", "Excel E2 no cerrado")
    check(by_id["2D-FO-01C"]["estado_resultado"] == "PENDIENTE_Y", "Excel E3 no cerrado")
    check(not any(row["id_material"] in {"2D-FO-09", "2D-FO-10"} for row in rows), "Excel no duplica accesorios ópticos")

    with TOOLS.open(encoding="utf-8", newline="") as stream:
        tool_rows = list(csv.DictReader(stream))
    check([int(row["fila_excel"]) for row in tool_rows] == list(range(2, 14)), "Herramientas cubren filas 2–13")
    check(sum(not row["cantidad_referencia"] for row in tool_rows) == 1, "Solo lubricante conserva cantidad variable")


def validate_images():
    svgs = sorted(IMAGES.glob("[0-9][0-9]_*.svg"))
    pngs = sorted(IMAGES.glob("[0-9][0-9]_*.png"))
    check(len(svgs) == len(pngs) == 9, "Nueve pares de imágenes")
    all_text = ""
    for svg in svgs:
        check(ET.parse(svg).getroot().tag.endswith("svg"), f"SVG válido: {svg.name}")
        all_text += svg.read_text(encoding="utf-8")
    for png in pngs:
        check(png_size(png) == (1600, 1000), f"PNG 1600×1000: {png.name}")
    for token in ("CCH-03U: 6 cassettes", "CCH-04U: 9 cassettes", "Máx. escenario: 45,7 m ≤ 90 m", "Máx. escenario: 42,7 m ≤ 90 m"):
        check(token in all_text, f"Imagen concuerda: {token}")


def validate_excel_and_package():
    for book in (ORIGINAL, WORKING):
        check(sha256(book) == EXPECTED_XLSX_HASH, f"Excel preservado: {book.name}")
        with zipfile.ZipFile(book) as archive:
            check(archive.testzip() is None, f"OOXML íntegro: {book.name}")
    packed_book = next((PACKAGE / "03_excel_provisional").glob("*.xlsx"))
    check(sha256(packed_book) == EXPECTED_XLSX_HASH, "Excel empaquetado sigue intacto")

    hash_file = PACKAGE / "SHA256SUMS.csv"
    with hash_file.open(encoding="utf-8-sig", newline="") as stream:
        records = list(csv.DictReader(stream))
    check(len(records) == 32, "32 artefactos inventariados", f"observados={len(records)}")
    for row in records:
        item = PACKAGE / Path(row["ruta"])
        check(item.is_file() and sha256(item) == row["sha256"], f"Hash paquete: {row['ruta']}")
    for source in sorted(IMAGES.glob("[0-9][0-9]_*.*")):
        packed = PACKAGE / "01_imagenes_revision" / source.name
        check(packed.is_file() and sha256(source) == sha256(packed), f"Imagen empaquetada idéntica: {source.name}")


def main():
    validate_results()
    validate_materials_and_excel_plan()
    validate_images()
    validate_excel_and_package()
    failures = [(label, detail) for ok, label, detail in checks if not ok]
    for ok, label, detail in checks:
        print(f"{'OK' if ok else 'ERROR'}: {label}" + (f" — {detail}" if detail else ""))
    print(f"RESUMEN FASE 2D: {len(checks)-len(failures)}/{len(checks)} controles aprobados")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
