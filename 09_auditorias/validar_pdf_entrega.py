"""Comprueba integridad textual, formato y representación de los PDF de entrega."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import unicodedata
import xml.etree.ElementTree as ET

import markdown
import pymupdf

from generar_pdf_entrega import DOCUMENTS, PACKAGE, SOURCES


ORIGINAL_SHA256 = {
    "MEMORIA_TECNICA_RESUMIDA.md": "0a94f4716f64002d198be09fcb195ec09d95f786f33336a060b1ce4e4a7a59ca",
    "GUIA_DEFENSA_INDIVIDUAL_8_MIN.md": "25a27bfa45e89548c9d8a3fdba408417f9edad5d9b2ed346dc45e452cb794573",
}


def comparable(value: str) -> str:
    value = unicodedata.normalize("NFC", value).casefold()
    return re.sub(r"\s+", "", value)


def source_fragments(source: Path) -> list[str]:
    html = markdown.markdown(source.read_text(encoding="utf-8"),
                             extensions=["tables", "sane_lists"])
    root = ET.fromstring(f"<root>{html}</root>")
    fragments = []
    for node in root.iter():
        if node.tag in ("h1", "h2", "h3", "th", "td", "p"):
            fragments.append("".join(node.itertext()))
        elif node.tag == "li" and not node.findall("p"):
            fragments.append("".join(node.itertext()))
    return [x for x in fragments if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render-dir", type=Path)
    args = parser.parse_args()
    if args.render_dir:
        args.render_dir.mkdir(parents=True, exist_ok=True)
    assert not list(PACKAGE.rglob("*.md")), "Hay Markdown de lectura dentro del paquete"
    planos = PACKAGE / "06_PLANOS_TECNICOS"
    expected_pdf = {str(PACKAGE / target) for _, target, _ in DOCUMENTS}
    expected_pdf.update(str(path) for path in (planos / "PDF_A3").glob("*.pdf"))
    expected_pdf.add(str(planos / "PLANOS_TECNICOS_INA_CENATE_9_LAMINAS.pdf"))
    assert len(list((planos / "PDF_A3").glob("*.pdf"))) == 9
    assert {str(path) for path in PACKAGE.rglob("*.pdf")} == expected_pdf
    files = sorted(path for path in PACKAGE.rglob("*") if path.is_file()
                   and path.name != "INVENTARIO_SHA256.txt" and not path.name.startswith("~$"))
    expected_inventory = "".join(
        f"{hashlib.sha256(path.read_bytes()).hexdigest().upper()}  {path.relative_to(PACKAGE).as_posix()}\n"
        for path in files
    )
    assert (PACKAGE / "INVENTARIO_SHA256.txt").read_text(encoding="utf-8") == expected_inventory, "Inventario SHA-256 desactualizado"
    for source_name, target, short_title in DOCUMENTS:
        source = SOURCES / source_name
        pdf_path = PACKAGE / target
        if source_name in ORIGINAL_SHA256:
            actual_sha = hashlib.sha256(source.read_bytes()).hexdigest()
            assert actual_sha == ORIGINAL_SHA256[source_name], source_name
        with pymupdf.open(pdf_path) as doc:
            assert len(doc) > 0, pdf_path
            full_text = "".join(page.get_text() for page in doc)
            assert "\ufffd" not in full_text, f"Carácter sustituto en {pdf_path}"
            comparable_pdf = comparable(full_text)
            missing = [fragment for fragment in source_fragments(source)
                       if comparable(fragment) not in comparable_pdf]
            assert not missing, f"Texto fuente ausente en {pdf_path}: {missing[:3]!r}"
            for i, page in enumerate(doc, 1):
                assert abs(page.rect.width - 595.2756) < 0.5
                assert abs(page.rect.height - 841.8898) < 0.5
                page_text = page.get_text()
                assert len(page_text.strip()) > 100, f"Página vacía {pdf_path}:{i}"
                assert f"{short_title} · Página {i}" in page_text, (pdf_path, i)
                assert "�" not in page_text, (pdf_path, i)
                blocks = [block for block in page.get_text("blocks") if block[4].strip()]
                assert all(35 <= b[0] and b[2] <= 560 and 20 <= b[1] and b[3] <= 825
                           for b in blocks), f"Texto fuera del área imprimible {pdf_path}:{i}"
                if args.render_dir:
                    name = source.stem.lower().replace("_", "-")
                    out = args.render_dir / f"{name}_{i:02d}.png"
                    page.get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False).save(out)
            print(f"OK {target}: {len(doc)} página(s), {len(source_fragments(source))} fragmentos de texto conservados")


if __name__ == "__main__":
    main()
