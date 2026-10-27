"""Genera los tres PDF de lectura a partir de Markdown interno sin cambiar su contenido."""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

import markdown
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    LongTable,
    PageTemplate,
    Paragraph,
    Spacer,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "08_entrega" / "FUENTES_INTERNAS_PAQUETE_FINAL"
PACKAGE = ROOT / "08_entrega" / "ENTREGA_FINAL_INA_CENATE"
DOCUMENTS = (
    ("MEMORIA_TECNICA_RESUMIDA.md", "04_MEMORIA_TECNICA/MEMORIA_TECNICA_RESUMIDA.pdf", "Memoria técnica"),
    ("GUIA_DEFENSA_INDIVIDUAL_8_MIN.md", "05_DEFENSA/GUIA_DEFENSA_INDIVIDUAL_8_MIN.pdf", "Guía de defensa"),
    ("INDICE_ENTREGABLES.md", "INDICE_ENTREGABLES.pdf", "Índice de entregables"),
)


def setup_fonts() -> None:
    fonts = Path("C:/Windows/Fonts")
    for name, filename in (("Arial", "arial.ttf"), ("Arial-Bold", "arialbd.ttf"),
                           ("Arial-Italic", "ariali.ttf"), ("Arial-BoldItalic", "arialbi.ttf")):
        pdfmetrics.registerFont(TTFont(name, str(fonts / filename)))
    pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold",
                                  italic="Arial-Italic", boldItalic="Arial-BoldItalic")


def styles() -> dict[str, ParagraphStyle]:
    base = dict(fontName="Arial", textColor=colors.HexColor("#172635"),
                alignment=TA_LEFT, allowWidows=0, allowOrphans=0)
    return {
        "title": ParagraphStyle("title", fontSize=17, leading=22, spaceAfter=15,
                                textColor=colors.HexColor("#153951"), keepWithNext=True, **{k: v for k, v in base.items() if k != "textColor"}),
        "h2": ParagraphStyle("h2", fontSize=12.5, leading=17, spaceBefore=17, spaceAfter=8,
                             textColor=colors.HexColor("#154966"), keepWithNext=True, **{k: v for k, v in base.items() if k != "textColor"}),
        "h3": ParagraphStyle("h3", fontSize=10.5, leading=15, spaceBefore=12, spaceAfter=6,
                             textColor=colors.HexColor("#154966"), keepWithNext=True, **{k: v for k, v in base.items() if k != "textColor"}),
        "body": ParagraphStyle("body", fontSize=9.6, leading=14.7, spaceAfter=8, **base),
        "list": ParagraphStyle("list", fontSize=9.4, leading=14.2, leftIndent=17,
                               firstLineIndent=-17, spaceAfter=6, **base),
        "table": ParagraphStyle("table", fontSize=8.15, leading=11.6, spaceAfter=0,
                                splitLongWords=True, **base),
        "tablehead": ParagraphStyle("tablehead", fontName="Arial-Bold", fontSize=8.15,
                                    leading=11.6, textColor=colors.white, splitLongWords=True),
    }


def inline(node: ET.Element) -> str:
    parts = [escape(node.text or "")]
    for child in node:
        content = inline(child)
        tag = child.tag.lower()
        if tag in ("strong", "b"):
            parts.append(f"<b>{content}</b>")
        elif tag in ("em", "i"):
            parts.append(f"<i>{content}</i>")
        elif tag == "br":
            parts.append("<br/>")
        elif tag == "code":
            parts.append(content)
        elif tag == "a":
            parts.append(content)
        else:
            parts.append(content)
        parts.append(escape(child.tail or ""))
    return "".join(parts)


def make_table(node: ET.Element, sty: dict[str, ParagraphStyle], available: float) -> LongTable:
    rows = []
    for tr in node.iter("tr"):
        header = tr.find("th") is not None
        cell_style = sty["tablehead"] if header else sty["table"]
        rows.append([Paragraph(inline(cell), cell_style) for cell in tr if cell.tag in ("th", "td")])
    if not rows or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("Tabla Markdown irregular")
    n = len(rows[0])
    widths = [available * x for x in ([0.27, 0.22, 0.51] if n == 3 else ([0.46, 0.54] if n == 2 else [1 / n] * n))]
    tbl = LongTable(rows, colWidths=widths, repeatRows=1, hAlign="LEFT", splitByRow=1,
                    spaceBefore=5, spaceAfter=10)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A4B68")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -1), 0.35, colors.HexColor("#CFD9DF")),
    ]
    for row in range(2, len(rows), 2):
        commands.append(("BACKGROUND", (0, row), (-1, row), colors.HexColor("#F2F6F8")))
    tbl.setStyle(TableStyle(commands))
    return tbl


def blocks(root: ET.Element, sty: dict[str, ParagraphStyle], available: float) -> list:
    out = []
    nodes = list(root)
    for position, node in enumerate(nodes):
        tag = node.tag.lower()
        if tag in ("h1", "h2", "h3"):
            heading_style = sty[{"h1": "title", "h2": "h2", "h3": "h3"}[tag]]
            if position + 1 < len(nodes) and nodes[position + 1].tag == "table":
                heading_style = ParagraphStyle("heading_before_table", parent=heading_style,
                                               keepWithNext=False)
            out.append(Paragraph(inline(node), heading_style))
        elif tag == "p":
            out.append(Paragraph(inline(node), sty["body"]))
        elif tag == "table":
            out.append(make_table(node, sty, available))
        elif tag in ("ul", "ol"):
            for i, item in enumerate(node.findall("li"), 1):
                label = f"{i}." if tag == "ol" else "•"
                if any(child.tag in ("ul", "ol") for child in item):
                    raise ValueError("Lista anidada inesperada")
                paragraphs = item.findall("p")
                content = "<br/>".join(inline(p) for p in paragraphs) if paragraphs else inline(item)
                out.append(Paragraph(f"{label}  {content}", sty["list"]))
        elif tag == "blockquote":
            out.extend(blocks(node, sty, available))
        else:
            raise ValueError(f"Elemento Markdown no admitido: {tag}")
    return out


class NumberedDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, short_title: str):
        super().__init__(filename, pagesize=A4, leftMargin=49, rightMargin=49,
                         topMargin=49, bottomMargin=49, title=short_title,
                         author="OpenAI Codex; revisión del estudiante pendiente")
        self.short_title = short_title
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates(PageTemplate(id="standard", frames=frame, onPage=self.decorate))

    def decorate(self, canvas, doc) -> None:
        canvas.saveState()
        w, _ = A4
        canvas.setStrokeColor(colors.HexColor("#B6C5CF"))
        canvas.setLineWidth(0.45)
        canvas.line(49, 39, w - 49, 39)
        canvas.setFont("Arial", 7.8)
        canvas.setFillColor(colors.HexColor("#506473"))
        canvas.drawString(49, 25, "INA CENATE · Actividad de Comprobación N.º 1")
        canvas.drawRightString(w - 49, 25, f"{self.short_title} · Página {doc.page}")
        canvas.restoreState()


def generate(source: Path, destination: Path, short_title: str) -> None:
    md = source.read_text(encoding="utf-8")
    html = markdown.markdown(md, extensions=["tables", "sane_lists"])
    tree = ET.fromstring(f"<root>{html}</root>")
    doc = NumberedDocTemplate(str(destination), short_title)
    story = blocks(tree, styles(), doc.width)
    destination.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=[x[0] for x in DOCUMENTS])
    args = parser.parse_args()
    setup_fonts()
    for source, target, short_title in DOCUMENTS:
        if args.only and source != args.only:
            continue
        generate(SOURCES / source, PACKAGE / target, short_title)
        print(f"Generado: {target}")
