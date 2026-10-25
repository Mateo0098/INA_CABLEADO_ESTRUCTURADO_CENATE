"""Controles de cierre técnico y paquete de revisión de la Fase 2C."""

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
SOURCE_IMAGES = ROOT / "07_imagenes" / "fase2b"
PACKAGE = ROOT / "08_entrega" / "PAQUETE_REVISION_FASE2C"
PACKAGE_IMAGES = PACKAGE / "01_imagenes_revision"
RESULTS = ROOT / "04_calculos" / "resultados_fase2b.csv"
MATERIALS = ROOT / "05_materiales" / "MATRIZ_TECNICA_FASE2C.md"
PLAN = ROOT / "06_excel" / "PLAN_FILAS_MATERIALES_FASE2C.csv"
ORIGINAL = next((ROOT / "06_excel").glob("Plantilla Actividades de comprobaci*n.xlsx"))
WORKING = next((ROOT / "06_excel").glob("*_TRABAJO_FASE2B.xlsx"))

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
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Firma PNG inválida: {path}")
    return struct.unpack(">II", header[16:24])


def validate_images():
    source_svgs = sorted(SOURCE_IMAGES.glob("[0-9][0-9]_*.svg"))
    source_pngs = sorted(SOURCE_IMAGES.glob("[0-9][0-9]_*.png"))
    package_svgs = sorted(PACKAGE_IMAGES.glob("[0-9][0-9]_*.svg"))
    package_pngs = sorted(PACKAGE_IMAGES.glob("[0-9][0-9]_*.png"))
    check(len(source_svgs) == len(source_pngs) == 9, "Nueve pares fuente SVG/PNG")
    check(len(package_svgs) == len(package_pngs) == 9, "Nueve pares empaquetados SVG/PNG")
    text = ""
    for svg in source_svgs:
        root = ET.parse(svg).getroot()
        check(root.tag.endswith("svg"), f"SVG válido: {svg.name}")
        text += svg.read_text(encoding="utf-8")
    for png in source_pngs:
        check(png_size(png) == (1600, 1000), f"PNG 1600×1000: {png.name}")
    for source, packed in zip(source_svgs + source_pngs, package_svgs + package_pngs):
        check(source.name == packed.name and sha256(source) == sha256(packed), f"Imagen empaquetada idéntica: {source.name}")
    for token in ("2 cables independientes", "E1: ER-P ↔ ER-A", "5 paneles Cat 6A × 48 puertos"):
        check(token in text, f"Rotulación técnica presente: {token}")


def validate_calculations():
    with RESULTS.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    data = {row["id"]: row for row in rows}
    check(len(rows) == 44, "Cantidad de resultados reproducibles", f"observados={len(rows)}")
    expected = {
        "TOTAL_RJ45": "1984", "TOTAL_PANELES": "51", "TOTAL_TR": "11",
        "CASSETTES_CCH_12F": "22", "CASSETTES_CCH_24F": "6",
        "PIGTAILS_COMPRA_SEPARADA": "0", "ADAPTADORES_COMPRA_SEPARADA": "0",
        "POSICIONES_CAJAS_145M": "5", "POSICIONES_CAJAS_50M": "1",
        "E1_RUTA_BASE": "195", "A_DESNIVEL_VERTICAL_MIN": "21.0",
        "B_DESNIVEL_VERTICAL_MIN": "73.5", "TOTAL_DESNIVEL_VERTICAL_MIN": "94.5",
    }
    for key, value in expected.items():
        observed = data.get(key, {}).get("resultado")
        check(observed == value, f"Resultado {key}", f"esperado={value}; observado={observed}")
    check(data["A_CABLE_COBRE"]["resultado"] == data["B_CABLE_COBRE"]["resultado"] == "N/D", "Metrajes de cobre no inventados")


def validate_materials_and_plan():
    text = MATERIALS.read_text(encoding="utf-8")
    ids = [
        "MAT-CU-01", "MAT-CU-02", "MAT-CU-03", "MAT-CU-04", "MAT-CU-05", "MAT-CU-06",
        "MAT-FO-01", "MAT-FO-02", "MAT-FO-03", "MAT-FO-04", "MAT-FO-05", "MAT-FO-06", "MAT-FO-07",
        "MAT-RK-01", "MAT-RK-02", "MAT-CA-01", "MAT-CA-02", "MAT-CA-03", "MAT-CA-04",
    ]
    for material_id in ids:
        check(material_id in text, f"Material Fase 2B trazado: {material_id}")
    for status in ("Producto identificado", "Familia identificada", "Sin referencia verificada", "Infraestructura por verificar"):
        check(status in text, f"Clasificación comercial definida: {status}")
    with PLAN.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    planned_rows = [int(row["fila_excel"]) for row in rows]
    check(planned_rows == list(range(2, 19)), "Plan Excel cubre filas 2–18 sin huecos", str(planned_rows))
    check(all("precio" not in " ".join(row.values()).lower() for row in rows), "Plan Excel sin precios")
    check(all(row["accion_estudiante"].strip() for row in rows), "Cada fila Excel tiene acción de revisión")


def validate_excel_and_package():
    check(sha256(ORIGINAL) == sha256(WORKING), "Original y copia Excel permanecen idénticos")
    package_book = next((PACKAGE / "03_excel_provisional").glob("*_TRABAJO_FASE2B.xlsx"))
    check(sha256(package_book) == sha256(WORKING), "Excel provisional empaquetado idéntico")
    for book_path in (ORIGINAL, WORKING, package_book):
        with zipfile.ZipFile(book_path) as book:
            check(book.testzip() is None, f"OOXML abre sin corrupción: {book_path.name}")
            workbook = ET.fromstring(book.read("xl/workbook.xml"))
            names = [node.attrib["name"] for node in workbook.iter() if node.tag.endswith("sheet")]
            check(names == ["Cotización técnica", "Herramientas"], f"Hojas conservadas: {book_path.name}", str(names))
    hash_file = PACKAGE / "SHA256SUMS.csv"
    with hash_file.open(encoding="utf-8-sig", newline="") as stream:
        hash_rows = list(csv.DictReader(stream))
    check(len(hash_rows) == 33, "Inventario hash del paquete", f"observados={len(hash_rows)}")
    for row in hash_rows:
        path = PACKAGE / Path(row["ruta"])
        check(path.is_file() and sha256(path) == row["sha256"], f"Hash de paquete: {row['ruta']}")


def main():
    validate_images()
    validate_calculations()
    validate_materials_and_plan()
    validate_excel_and_package()
    failures = [item for item in checks if not item[0]]
    for passed, label, detail in checks:
        suffix = f" — {detail}" if detail else ""
        print(f"{'OK' if passed else 'FALLO'}: {label}{suffix}")
    print(f"RESUMEN FASE 2C: {len(checks)-len(failures)}/{len(checks)} controles aprobados")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
