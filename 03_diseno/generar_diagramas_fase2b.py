"""Genera los nueve diagramas SVG de la Fase 2B.

Procedencia: apoyo visual producido con IA (OpenAI Codex), 2026-10-25.
Requiere revisión técnica humana antes de entrega. No son planos constructivos.
"""

from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "07_imagenes" / "fase2b"
W, H = 1600, 1000

COLORS = {
    "ink": "#183153",
    "blue": "#1479b8",
    "cyan": "#dff3fb",
    "orange": "#e57c23",
    "green": "#238b57",
    "red": "#c73e3a",
    "gray": "#687481",
    "light": "#f4f7fa",
    "yellow": "#fff2b8",
    "purple": "#7654a7",
}


def line(x1, y1, x2, y2, color=None, width=4, dash=None, marker=False):
    attrs = [f'x1="{x1}"', f'y1="{y1}"', f'x2="{x2}"', f'y2="{y2}"',
             f'stroke="{color or COLORS["ink"]}"', f'stroke-width="{width}"',
             'fill="none"']
    if dash:
        attrs.append(f'stroke-dasharray="{dash}"')
    if marker:
        attrs.append('marker-end="url(#arrow)"')
    return f"<line {' '.join(attrs)}/>"


def rect(x, y, w, h, fill="white", stroke=None, sw=3, rx=8):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke or COLORS["ink"]}" stroke-width="{sw}"/>')


def text(x, y, value, size=24, weight="normal", anchor="start", fill=None):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" fill="{fill or COLORS["ink"]}">{escape(str(value))}</text>')


def multiline(x, y, lines, size=22, step=30, weight="normal", anchor="start", fill=None):
    return "".join(text(x, y + i * step, v, size, weight, anchor, fill) for i, v in enumerate(lines))


def circle(x, y, r=8, fill=None, stroke=None, sw=2):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill or COLORS["blue"]}" '
            f'stroke="{stroke or "white"}" stroke-width="{sw}"/>')


def base(title, code, subtitle):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#183153"/></marker></defs>',
        '<style>text{font-family:Arial,Helvetica,sans-serif}.small{font-size:18px}.tiny{font-size:15px}</style>',
        rect(12, 12, W - 24, H - 24, "white", COLORS["ink"], 4, 0),
        rect(12, 12, W - 24, 94, COLORS["ink"], COLORS["ink"], 0, 0),
        text(42, 56, title, 33, "bold", fill="white"),
        text(42, 88, subtitle, 19, fill="#dce9f6"),
        text(1555, 63, code, 24, "bold", "end", "white"),
    ]


def footer(parts):
    parts.extend([
        line(32, 915, 1568, 915, COLORS["gray"], 2),
        text(42, 944, "CLASIFICACIÓN: datos oficiales + supuestos de diseño rotulados + resultados calculados.", 17, "bold"),
        text(42, 970, "No es plano a escala ni constructivo. Revisión humana obligatoria. Generado con apoyo visual de OpenAI Codex, 2026-10-25.", 16, fill=COLORS["gray"]),
        "</svg>",
    ])
    return "".join(parts)


def building(parts, x, y, w, h, name, er, floors):
    parts += [rect(x, y, w, h, COLORS["light"], COLORS["ink"], 4, 4),
              text(x + w / 2, y + 42, name, 27, "bold", "middle")]
    floor_h = (h - 70) / floors
    for i in range(floors):
        yy = y + 60 + i * floor_h
        parts.append(line(x + 8, yy, x + w - 8, yy, COLORS["gray"], 2))
        parts.append(text(x + 18, yy + floor_h / 2 + 7, f"P{floors-i}", 17, "bold"))
    parts += [rect(x + w - 92, y + h - 62, 72, 42, COLORS["yellow"], COLORS["orange"], 3, 4),
              text(x + w - 56, y + h - 35, er, 17, "bold", "middle")]


def exterior():
    p = base("Backbone exterior — tres edificios", "EXT-01", "Arquitectura lógica y canalización subterránea de referencia")
    building(p, 100, 230, 350, 520, "EDIFICIO EXISTENTE", "ER-P", 4)
    building(p, 625, 320, 300, 430, "EDIFICIO A", "ER-A", 4)
    building(p, 1120, 180, 350, 570, "EDIFICIO B", "ER-B", 7)
    p += [
        line(394, 725, 394, 770, COLORS["blue"], 5), line(869, 725, 869, 810, COLORS["blue"], 5),
        line(1414, 725, 1414, 850, COLORS["purple"], 5),
        line(394, 770, 869, 770, COLORS["blue"], 10),
        line(869, 810, 1414, 810, COLORS["green"], 10, "22 12"),
        line(394, 850, 1414, 850, COLORS["purple"], 7, "12 10"),
        text(630, 758, "E1: ER-P ↔ ER-A | 145 + 50 = 195 m base", 17, "bold", "middle", COLORS["blue"]),
        text(1140, 798, "E3: ER-A ↔ ER-B = y m (pendiente)", 17, "bold", "middle", COLORS["green"]),
        text(904, 840, "E2: ER-P ↔ ER-B = 145 m + x solo si se verifica el tramo compartido", 16, "bold", "middle", COLORS["purple"]),
    ]
    for xx in [455, 515, 575, 635, 695, 755]:
        p += [rect(xx, 760, 18, 18, COLORS["yellow"], COLORS["orange"], 2, 2)]
    p += [text(800, 880, "OS2, 24 fibras/enlace · subterráneo · cajas ~25 m solo como referencia · x/y/capacidad pendientes", 16, "bold", "middle", COLORS["red"])]
    return footer(p)


def floor_plan(building_id, labs, area, dims, panels):
    code = f"PLA-{building_id}"
    p = base(f"Planta típica — Edificio {building_id}", code,
             f"Pisos idénticos como supuesto | {labs} laboratorios/piso | 1 TR/piso")
    x0, y0, labw, labh = 90, 180, 350, 220
    top = (labs + 1) // 2
    bottom = labs - top
    for i in range(top):
        x = x0 + i * (labw + 18)
        p += [rect(x, y0, labw, labh, COLORS["cyan"], COLORS["blue"], 3),
              text(x + 20, y0 + 38, f"LAB-{building_id}-Pxx-L{i+1:02d}", 19, "bold"),
              text(x + 20, y0 + 72, f"{area} m² | {dims} (supuesto)", 17),
              text(x + 20, y0 + 105, "16 áreas dobles | 32 RJ45", 17, "bold")]
    for i in range(bottom):
        x = x0 + i * (labw + 18)
        num = top + i + 1
        p += [rect(x, 610, labw, labh, COLORS["cyan"], COLORS["blue"], 3),
              text(x + 20, 648, f"LAB-{building_id}-Pxx-L{num:02d}", 19, "bold"),
              text(x + 20, 682, f"{area} m² | {dims} (supuesto)", 17),
              text(x + 20, 715, "16 áreas dobles | 32 RJ45", 17, "bold")]
    corridor_y = 455
    p += [rect(70, corridor_y, 1260, 95, "#eef1f4", COLORS["gray"], 3),
          text(700, corridor_y + 38, "PASILLO CENTRAL — 2,4 m propuestos (no medido)", 20, "bold", "middle"),
          line(120, corridor_y + 68, 1280, corridor_y + 68, COLORS["orange"], 12),
          text(700, corridor_y + 88, "Bandeja principal Cat 6A; derivaciones protegidas a cada laboratorio", 16, anchor="middle")]
    tr_x = 1370
    p += [rect(tr_x, 365, 165, 280, COLORS["yellow"], COLORS["orange"], 4),
          text(tr_x + 82, 405, f"TR-{building_id}-Pxx", 21, "bold", "middle"),
          multiline(tr_x + 82, 445, ["3 × 3 m", "supuesto", f"{labs*32} RJ45", f"{panels} paneles", "48 puertos"], 18, 32, anchor="middle")]
    p += [line(1330, corridor_y + 68, tr_x, corridor_y + 68, COLORS["orange"], 12)]
    for i in range(top):
        cx = x0 + i * (labw + 18) + labw / 2
        p += [line(cx, corridor_y, cx, y0 + labh, COLORS["orange"], 5)]
    for i in range(bottom):
        cx = x0 + i * (labw + 18) + labw / 2
        p += [line(cx, corridor_y + 95, cx, 610, COLORS["orange"], 5)]
    p += [text(85, 870, f"Control: {labs} × 32 = {labs*32} enlaces/piso; capacidad {panels} × 48 = {panels*48} puertos.", 19, "bold"),
          text(85, 898, "Cada ruta física deberá medirse y comprobarse ≤ 90 m; el dibujo no acredita distancia.", 18, fill=COLORS["red"])]
    return footer(p)


def laboratory(building_id, area, depth):
    p = base(f"Laboratorio típico — Edificio {building_id}", f"LAB-{building_id}",
             f"Geometría de referencia 10 × {depth} m = {area} m² | 16 áreas dobles")
    p += [rect(190, 165, 1100, 680, "#fbfcfd", COLORS["ink"], 5, 0),
          rect(690, 810, 140, 35, "white", "white", 0, 0),
          text(760, 875, "PUERTA / acceso de referencia", 17, "bold", "middle"),
          line(255, 220, 1225, 220, COLORS["orange"], 12),
          text(740, 205, "Bandeja aérea perimetral propuesta", 18, "bold", "middle", COLORS["orange"])]
    positions = []
    for row in range(4):
        for col in range(4):
            positions.append((355 + col * 210, 320 + row * 115, row * 4 + col + 1))
    for x, y, n in positions:
        p += [rect(x, y, 145, 70, COLORS["cyan"], COLORS["blue"], 2),
              text(x + 72, y + 25, f"AT-{n:02d}", 16, "bold", "middle"),
              circle(x + 57, y + 49, 7, COLORS["blue"]), circle(x + 87, y + 49, 7, COLORS["green"]),
              line(x + 72, y, x + 72, 220, COLORS["orange"], 2, "8 6")]
    p += [multiline(1315, 240, ["LEYENDA", "AT = área doble", "● azul = RJ45-A", "● verde = RJ45-B", "Línea = bajante", "protegida propuesta"], 17, 29, "bold"),
          text(245, 895, "Resultado calculado: 16 áreas × 2 puertos = 32 salidas y 32 enlaces Cat 6A por laboratorio.", 19, "bold")]
    return footer(p)


def rack(parts, x, y, title, units):
    rack_h = max(580, 85 + sum(max(35, u * 22) + 10 for _, u, _ in units))
    parts += [rect(x, y, 330, rack_h, "#eef1f4", COLORS["ink"], 5, 4),
              text(x + 165, y + 38, title, 22, "bold", "middle")]
    yy = y + 65
    for label, u, color in units:
        h = max(35, u * 22)
        parts += [rect(x + 35, yy, 260, h, color, COLORS["ink"], 2, 2),
                  text(x + 165, yy + h / 2 + 7, label, 16, "bold", "middle")]
        yy += h + 10


def er_room(building_id, vertical_fibers, total_positions, trs):
    p = base(f"Cuarto de equipos ER — Edificio {building_id}", f"ER-{building_id}",
             "Esquema funcional de terminación óptica; equipo activo pendiente de selección")
    rack(p, 625, 205, "RACK 19\" / 42U PROPUESTO", [
        (f"ODF exterior: 48 fibras (2 × 24f)", 4, COLORS["cyan"]),
        (f"ODF vertical: {vertical_fibers} fibras ({trs} × 12f)", 5, "#dff5e8"),
        ("Bandejas de empalme + organizadores", 3, COLORS["yellow"]),
        ("Espacio reservado — activos/PDU/UPS", 7, "#f2eafd"),
    ])
    p += [rect(80, 235, 390, 180, COLORS["cyan"], COLORS["blue"], 4),
          text(275, 275, "LLEGADAS EXTERIORES", 22, "bold", "middle"),
          multiline(110, 315, ["24f OS2 desde ER principal", f"24f OS2 desde ER {'B' if building_id=='A' else 'A'}", "Ducto subterráneo (capacidad pendiente)"], 18, 32),
          line(470, 325, 625, 325, COLORS["blue"], 8, marker=True),
          rect(1100, 235, 390, 220, "#dff5e8", COLORS["green"], 4),
          text(1295, 275, "BACKBONE VERTICAL", 22, "bold", "middle"),
          multiline(1135, 315, [f"{trs} cables independientes", "12 fibras OS2 por ER–TR", f"{vertical_fibers} fibras terminadas", "Longitudes: variables por medir"], 18, 32),
          line(955, 350, 1100, 350, COLORS["green"], 8, marker=True),
          rect(80, 545, 390, 210, COLORS["yellow"], COLORS["orange"], 4),
          text(275, 585, "CONTINUIDAD ÓPTICA", 22, "bold", "middle"),
          multiline(110, 625, ["Cable → empalme por fusión", "→ pigtail LC/UPC OS2", "→ adaptador LC dúplex", "→ patch cord → activo (pendiente)"], 18, 31),
          line(470, 650, 625, 650, COLORS["orange"], 6, marker=True),
          multiline(1120, 560, ["Capacidad mínima mostrada:", f"{total_positions} posiciones de fibra", "No equivale a transceptores activos.", "Rack 42U: hipótesis; capacidad final pendiente."], 18, 31, "bold"),
          text(1290, 735, "ER y TR del primer piso son recintos separados; no se duplican equipos.", 16, "bold", "middle", COLORS["red"])]
    return footer(p)


def tr_room(building_id, labs, panels, ports, spare):
    p = base(f"Cuarto de telecomunicaciones TR — Edificio {building_id}", f"TR-{building_id}",
             f"Un TR por piso | {labs} laboratorios | {ports} enlaces Cat 6A")
    rack(p, 630, 195, "RACK 19\" / 42U PROPUESTO", [
        ("ODF 12f OS2 + bandeja de empalme", 2, COLORS["cyan"]),
        ("Organizador óptico", 1, COLORS["yellow"]),
        (f"{panels} paneles Cat 6A × 48 puertos", panels * 2, "#dff5e8"),
        (f"Organizadores horizontales ({panels}U ref.)", panels, COLORS["yellow"]),
        ("Espacio reservado — switches/PDU/UPS", 7, "#f2eafd"),
    ])
    p += [rect(80, 245, 395, 175, COLORS["cyan"], COLORS["blue"], 4),
          text(277, 285, f"DESDE ER-{building_id}", 22, "bold", "middle"),
          multiline(115, 325, ["1 cable OS2 de 12 fibras", "fusión + pigtail LC/UPC", "adaptador + patch cord óptico"], 18, 32),
          line(475, 335, 630, 335, COLORS["blue"], 8, marker=True),
          rect(1090, 220, 420, 280, "#dff5e8", COLORS["green"], 4),
          text(1300, 262, "DISTRIBUCIÓN HORIZONTAL", 22, "bold", "middle"),
          multiline(1120, 305, [f"{labs} laboratorios × 32 = {ports} enlaces", f"Capacidad: {panels} × 48 = {panels*48} puertos", f"Reserva de posiciones: {spare}", "Cable Cat 6A en estrella", "Cada enlace permanente ≤ 90 m"], 18, 33),
          line(960, 365, 1090, 365, COLORS["green"], 8, marker=True),
          rect(1050, 570, 480, 190, COLORS["yellow"], COLORS["orange"], 4),
          multiline(1080, 615, ["PATCH CORDS", f"Cobre: cantidad base = {ports} en rack + {ports} en usuario", "Fibra: cantidad depende de pares activos (pendiente)", "No se infiere un switch por cada posición pasiva."], 18, 34, "bold"),
          text(90, 560, "Canalización hacia áreas", 21, "bold"),
          line(95, 600, 515, 600, COLORS["orange"], 14),
          multiline(100, 650, ["Bandeja de pasillo + derivaciones", "Dimensión: pendiente de diámetro real", "y cálculo de ocupación."], 18, 32)]
    return footer(p)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    diagrams = {
        "01_backbone_exterior.svg": exterior(),
        "02_planta_tipica_edificio_A.svg": floor_plan("A", 5, 85, "10 × 8,5 m", 4),
        "03_planta_tipica_edificio_B.svg": floor_plan("B", 6, 75, "10 × 7,5 m", 5),
        "04_laboratorio_tipico_A.svg": laboratory("A", 85, "8,5"),
        "05_laboratorio_tipico_B.svg": laboratory("B", 75, "7,5"),
        "06_ER_A.svg": er_room("A", 48, 96, 4),
        "07_TR_A.svg": tr_room("A", 5, 4, 160, 32),
        "08_ER_B.svg": er_room("B", 84, 132, 7),
        "09_TR_B.svg": tr_room("B", 6, 5, 192, 48),
    }
    for name, content in diagrams.items():
        (OUT / name).write_text(content, encoding="utf-8")
    print(f"Generados {len(diagrams)} SVG en {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
