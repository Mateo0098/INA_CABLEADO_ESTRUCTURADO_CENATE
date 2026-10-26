"""Crea el libro de escenario Fase 3B usando solo la plantilla INA original.

El script modifica las partes de hoja OOXML necesarias y preserva el resto del
paquete (incluidos estilos, dibujos, tema y relaciones) mediante zipfile.
Las fórmulas se almacenan con valores en caché y recálculo automático al abrir.
"""

from __future__ import annotations

import copy
import hashlib
import shutil
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCEL_DIR = ROOT / "06_excel"
PACKAGE_DIR = ROOT / "08_entrega" / "PAQUETE_REVISION_FASE3B"
TEMPLATE = next(path for path in EXCEL_DIR.glob("Plantilla*.xlsx") if "TRABAJO" not in path.name)
OUTPUT = EXCEL_DIR / "INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx"
PACKAGED_OUTPUT = PACKAGE_DIR / OUTPUT.name
MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"m": MAIN, "r": REL}


def item(name, category, specification, brand, model, unit, formula, value, source):
    return {
        "name": name,
        "category": category,
        "specification": specification,
        "brand": brand,
        "model": model,
        "unit": unit,
        "formula": formula,
        "value": value,
        "supplier": "No verificado localmente",
        "source": source,
    }


MATERIALS = [
    item("Cable horizontal Cat 6A U/UTP", "Cableado horizontal de cobre", "U/UTP Cat 6A CMP; caja de 305 m; Ø nominal 5,8 mm. Cubierta candidata; verificar ambiente.", "Panduit", "PUP6AHD04BU-G", "Caja 305 m", "ROUNDUP(22428/305,0)+ROUNDUP(47028.24/305,0)", 229, "Matriz Fase 2D 2D-CU-01; modelo cobre Fase 2D"),
    item("Patch panel Cat 6A, 48 puertos", "Terminación de cobre", "48 puertos; 2RU; 19 pulgadas; punchdown.", "Panduit", "NK6XPPG48Y", "Panel", "4*4+5*7", 51, "Matriz Fase 2D 2D-CU-02; resultados Fase 2B"),
    item("Jack RJ45 Cat 6A Mini-Com", "Salida de usuario", "UTP; 8P8C; dos por cada área doble en el escenario adoptado.", "Panduit", "CJ6X88TGBU", "Unidad", "(4*5+7*6)*16*2", 1984, "Matriz Fase 2D 2D-CU-03; supuesto adoptado Fase 3B"),
    item("Placa doble para dos módulos Mini-Com", "Salida de usuario", "Dos posiciones; una placa por área doble.", "Panduit", "CFPL2WHY", "Unidad", "(4*5+7*6)*16", 992, "Matriz Fase 2D 2D-CU-04"),
    item("Caja de salida para placa doble", "Salida de usuario", "Compatible con placa doble; tipo de montaje genérico, sujeto a arquitectura del recinto.", "Genérica académica", "Especificación preliminar; sin modelo", "Unidad", "(4*5+7*6)*16", 992, "Matriz Fase 2D 2D-CU-06; cantidad derivada de áreas"),
    item("Patch cord Cat 6A de usuario", "Cordón de cobre", "UTP 28 AWG; RJ45-RJ45; 7 ft.", "Panduit", "UTP28X7BU", "Unidad", "(4*5+7*6)*16*2", 1984, "Matriz Fase 2D 2D-CU-05; fabricante"),
    item("Patch cord Cat 6A para rack", "Cordón de cobre", "UTP 28 AWG; RJ45-RJ45; 7 ft; capacidad pasiva, sin switches.", "Panduit", "UTP28X7BU", "Unidad", "(4*5+7*6)*16*2", 1984, "Matriz Fase 2D 2D-CU-05; supuesto una terminación por enlace"),
    item("Cable exterior OS2 24F para E1", "Fibra exterior", "24 fibras OS2 indoor/outdoor para ducto; longitud de escenario E1.", "Corning", "024EUK-T3601D2M", "m de cable", "(145+50+2*(3+5))*1.05", 221.55, "Matriz Fase 2D 2D-FO-01A; E1 asumido hacia ER-A"),
    item("Cable exterior OS2 24F para E2", "Fibra exterior", "24 fibras OS2 indoor/outdoor para ducto; x adoptada = 75 m (supuesto académico).", "Corning", "024EUK-T3601D2M", "m de cable", "(145+75+16)*1.05", 247.8, "Matriz Fase 2D 2D-FO-01B; x=3 intervalos teóricos de 25 m"),
    item("Cable exterior OS2 24F para E3", "Fibra exterior", "24 fibras OS2 indoor/outdoor para ducto; y adoptada = 50 m (supuesto académico).", "Corning", "024EUK-T3601D2M", "m de cable", "(50+16)*1.05", 69.3, "Matriz Fase 2D 2D-FO-01C; y=2 intervalos teóricos de 25 m"),
    item("Cable vertical OS2 12F — edificio A", "Backbone vertical", "12 fibras OS2 OFNR; Ø nominal 6,1 mm; longitudes y reserva según escenario.", "Corning", "012E81-33131-24", "m de cable", "(16+19.5+23+26.5)*1.05", 89.25, "Matriz Fase 2D 2D-FO-02A; memoria Fase 2D"),
    item("Cable vertical OS2 12F — edificio B", "Backbone vertical", "12 fibras OS2 OFNR; Ø nominal 6,1 mm; longitudes y reserva según escenario.", "Corning", "012E81-33131-24", "m de cable", "(16+19.5+23+26.5+30+33.5+37)*1.05", 194.775, "Matriz Fase 2D 2D-FO-02B; memoria Fase 2D"),
    item("Cassette CCH preterminado 12F", "Terminación óptica", "12F LC dúplex UPC OS2; pigtails/protectores del conjunto integrados.", "Corning", "CCH-CS12-A9-P00RE", "Cassette", "(4+7)*2", 22, "Matriz Fase 2D 2D-FO-03; D-015"),
    item("Cassette CCH preterminado 24F", "Terminación óptica", "24F LC dúplex UPC OS2; componentes de terminación integrados.", "Corning", "CCH-CS24-A9-P00RE", "Cassette", "3*2", 6, "Matriz Fase 2D 2D-FO-04; D-015"),
    item("Housing óptico CCH 1U", "Distribución óptica", "1U; dos posiciones CCH; once TR y ER principal.", "Corning", "CCH-01U", "Unidad", "11+1", 12, "Matriz Fase 2D 2D-FO-05; ER-P sujeto a espacio"),
    item("Housing óptico CCH 3U", "Distribución óptica", "3U; seis posiciones CCH; asignación para ER-A.", "Corning", "CCH-03U", "Unidad", "1", 1, "Matriz Fase 2D 2D-FO-06"),
    item("Housing óptico CCH 4U", "Distribución óptica", "4U; doce posiciones CCH; asignación para ER-B.", "Corning", "CCH-04U", "Unidad", "1", 1, "Matriz Fase 2D 2D-FO-07"),
    item("Patch cord óptico OS2 LC/UPC dúplex", "Cordón de fibra", "LC/UPC dúplex a LC/UPC dúplex; 3 m; un circuito dúplex por enlace en ambos extremos.", "Corning", "040402R5120003M", "Unidad", "(11+3)*2", 28, "Matriz Fase 2D 2D-FO-08; supuesto 1 circuito/enlace × 2 extremos"),
    item("Gabinete de telecomunicaciones 42U", "Rack", "19 pulgadas; 600 × 1 070 mm; capacidad de equipos activos pendiente.", "APC / Schneider Electric", "AR3100B2", "Unidad", "11+2", 13, "Matriz Fase 2D 2D-RK-01; cantidad propuesta"),
    item("Organizador horizontal de cobre 1U", "Gestión de cable", "19 pulgadas; horizontal; uno por patch panel.", "APC / Schneider Electric", "AR8425A", "Unidad", "4*4+5*7", 51, "Matriz Fase 2D 2D-RK-02"),
    item("Organizador horizontal óptico 1U", "Gestión de cable", "Horizontal; uno por housing contabilizado.", "APC / Schneider Electric", "AR8425A", "Unidad", "12+1+1", 14, "Matriz Fase 2D 2D-RK-03"),
    item("Conjunto de equipotencialidad para rack", "Puesta a tierra", "Especificación genérica; compatible con rack y sistema eléctrico institucional; referencia por seleccionar.", "Genérica académica", "Sin modelo; sujeto a diseño eléctrico", "Conjunto", "11+2", 13, "Matriz Fase 2D 2D-RK-04; cantidad por racks propuestos"),
    item("Bandeja portacables perforada", "Canalización interior", "100 × 50 mm; tramo de 3 m; sección preliminar genérica; ocupación, soportes y accesorios por validar.", "Genérica académica", "Sección preliminar 100×50 mm", "Tramo 3 m", "ROUNDUP((472+892.5)*1.05/3,0)", 478, "Memoria Fase 2D; selección dimensional preliminar Fase 3B"),
    item("Tubería de protección para dos cables Cat 6A", "Canalización interior", "PVC telecomunicaciones; diámetro nominal 25 mm; tramos de 3 m; verificar diámetro interior y ocupación con ficha final.", "Genérica académica", "Ø nominal 25 mm; preliminar", "Tramo 3 m", "ROUNDUP(992*3*1.05/3,0)", 1042, "Matriz Fase 2D 2D-CA-02; memoria Fase 2D; selección preliminar Fase 3B"),
    item("Ducto exterior nuevo para fibra", "Canalización exterior", "Ducto telecomunicaciones Ø nominal 50 mm; 50 m propuestos; ocupación final según diámetro exterior de cables.", "Genérica académica", "Ø nominal 50 mm; preliminar", "m de ducto", "50", 50, "Matriz Fase 2D 2D-CA-05; ruta/destino aún por validar"),
    item("Posiciones de cajas o registros exteriores", "Infraestructura exterior", "5 posiciones teóricas en tramo existente + 1 en tramo nuevo; no equivale a compra de seis cajas.", "No aplica", "Requiere inspección de sitio", "Posición teórica", "5+1", 6, "Matriz Fase 2D 2D-CA-06; referencia de 25 m no normativa"),
    item("Etiquetas para identificar enlaces de cobre", "Consumible de identificación", "Etiquetas compatibles con cableado; dos por enlace como supuesto (un extremo en cada terminación); genérico.", "Genérica académica", "Sin modelo seleccionado", "Etiqueta", "1984*2", 3968, "D-011 sistema de identificación; supuesto 2 etiquetas/enlace"),
    item("Pigtails LC/UPC comprados por separado", "Terminación óptica", "No comprar por separado mientras se mantenga el cassette preterminado con terminaciones integradas.", "No aplica", "Integrados en cassettes CCH", "Unidad", "0", 0, "Matriz Fase 2D 2D-FO-09; control de no duplicación"),
    item("Adaptadores LC dúplex comprados por separado", "Terminación óptica", "No comprar por separado mientras se mantenga el cassette con adaptadores integrados.", "No aplica", "Integrados en cassettes CCH", "Unidad", "0", 0, "Matriz Fase 2D 2D-FO-10; control de no duplicación"),
]

TOOLS = [
    ("Guía pasacables/juego de tiro (reutilizable; 1 juego)", 1),
    ("Soportes de bobina (reutilizables; unidades)", 2),
    ("Herramientas de impacto compatibles Cat 6A (reutilizables; unidades)", 2),
    ("Juegos de cortador/pelador de cobre (reutilizables; juegos)", 2),
    ("Fusionadora para fibra OS2 (equipo reutilizable compartido)", 1),
    ("Cortadora de precisión y peladora de fibra (juego reutilizable)", 1),
    ("Fuente y medidor óptico OS2 (juego reutilizable)", 1),
    ("OTDR compatible con OS2 (equipo reutilizable; sujeto a práctica)", 1),
    ("Certificador Cat 6A con adaptadores de enlace permanente (equipo reutilizable)", 1),
    ("Etiquetadora (equipo reutilizable; etiquetas son consumible)", 1),
    ("Herramientas de rack y nivel (juego reutilizable)", 1),
    ("Lubricante de tiro: material consumible, no herramienta; cuantificar según cable, ducto y método", "Variable; no incluido"),
]

NOTES = [
    ("ADVERTENCIA DE ESCENARIO — NO ES MEDICIÓN DE CAMPO", 11),
    ("Adoptados para el ejercicio: 16 áreas dobles por laboratorio, 2 RJ45 por área, 1 TR por piso, reserva de cobre de 3 m/enlace y 5 % de desperdicio. Geometría y recorridos internos son supuestos Fase 2D.", 3),
    ("E1 usa 145 m de ducto reportado + 50 m propuestos y suma 16 m internos/reservas antes del 5 %. E2 adopta x=75 m (3 intervalos teóricos de 25 m); E3 adopta y=50 m (2 intervalos). x/y no son mediciones; los esquemas no están a escala y 25 m no es norma.", 8),
    ("Cable exterior resultante del escenario: E1 221,55 m; E2 247,8 m; E3 69,3 m. Fibra vertical OS2 12F: A 89,25 m; B 194,775 m. No confundir metros de ducto con metros de cable.", 3),
    ("Canalización genérica preliminar: bandeja 100×50 mm en tramos de 3 m; derivaciones PVC nominal 25 mm para dos Cat 6A Ø5,8 mm; ducto exterior nominal 50 mm. Confirmar diámetros interiores, ocupación, soportes, accesorios y trazado con fichas finales.", 8),
    ("Fibra activa: 1 circuito LC dúplex por cada uno de 11 enlaces verticales y 3 exteriores; 2 patch cords por enlace, uno por extremo (28 unidades). No se iluminan todas las fibras. Pigtails/adaptadores separados = 0 porque se consideran integrados en los cassettes.", 3),
    ("I/J quedan vacías. La fórmula monetaria J43 del original se elimina solo en esta copia y el rótulo se sustituye por ‘CANTIDADES SIN COSTOS’; el original permanece intacto. Proveedores locales no verificados. Contenido preparado con asistencia de IA; revisión y comprensión del estudiante requeridas.", 8),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def preserve_namespaces(xml_bytes: bytes) -> None:
    for _, (prefix, uri) in ET.iterparse(__import__("io").BytesIO(xml_bytes), events=("start-ns",)):
        try:
            ET.register_namespace(prefix, uri)
        except ValueError:
            pass


def serialize(root: ET.Element, original: bytes) -> bytes:
    preserve_namespaces(original)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def row_for(sheet_data: ET.Element, row_num: int) -> ET.Element:
    row = sheet_data.find(f"m:row[@r='{row_num}']", NS)
    if row is None:
        row = ET.Element(f"{{{MAIN}}}row", {"r": str(row_num)})
        rows = list(sheet_data)
        later = next((n for n, existing in enumerate(rows) if int(existing.attrib["r"]) > row_num), None)
        sheet_data.insert(later if later is not None else len(rows), row)
    return row


def cell_for(row: ET.Element, ref: str, style: str | None = None) -> ET.Element:
    cell = row.find(f"m:c[@r='{ref}']", NS)
    if cell is None:
        cell = ET.Element(f"{{{MAIN}}}c", {"r": ref})
        col = "".join(ch for ch in ref if ch.isalpha())
        col_num = 0
        for ch in col:
            col_num = col_num * 26 + ord(ch.upper()) - 64
        existing = list(row)
        before = None
        for index, current in enumerate(existing):
            current_ref = current.attrib.get("r", "")
            current_col = "".join(ch for ch in current_ref if ch.isalpha())
            num = 0
            for ch in current_col:
                num = num * 26 + ord(ch.upper()) - 64
            if num > col_num:
                before = index
                break
        row.insert(before if before is not None else len(existing), cell)
    if style is not None:
        cell.attrib["s"] = style
    return cell


def clear_cell(cell: ET.Element) -> None:
    for child in list(cell):
        cell.remove(child)
    cell.attrib.pop("t", None)


def put_inline(row: ET.Element, ref: str, value: str, style: str | None = None) -> None:
    cell = cell_for(row, ref, style)
    clear_cell(cell)
    cell.attrib["t"] = "inlineStr"
    inline = ET.SubElement(cell, f"{{{MAIN}}}is")
    text = ET.SubElement(inline, f"{{{MAIN}}}t")
    if value[:1].isspace() or value[-1:].isspace():
        text.attrib[f"{{{XML}}}space"] = "preserve"
    text.text = value


def put_formula(row: ET.Element, ref: str, formula: str, value: int | float, style: str | None = None) -> None:
    cell = cell_for(row, ref, style)
    clear_cell(cell)
    f = ET.SubElement(cell, f"{{{MAIN}}}f")
    f.text = formula
    v = ET.SubElement(cell, f"{{{MAIN}}}v")
    v.text = str(value)


def find_sheet_paths(package: zipfile.ZipFile) -> dict[str, str]:
    workbook = ET.fromstring(package.read("xl/workbook.xml"))
    relationships = ET.fromstring(package.read("xl/_rels/workbook.xml.rels"))
    rels = {node.attrib["Id"]: node.attrib["Target"] for node in relationships}
    found = {}
    for sheet in workbook.findall("m:sheets/m:sheet", NS):
        target = rels[sheet.attrib[f"{{{REL}}}id"]].lstrip("/")
        if not target.startswith("xl/"):
            target = "xl/" + target
        found[sheet.attrib["name"]] = target
    return found


def make_sheets(template_bytes: bytes) -> dict[str, bytes]:
    import io

    with zipfile.ZipFile(io.BytesIO(template_bytes)) as package:
        paths = find_sheet_paths(package)
        if list(paths) != ["Cotización técnica", "Herramientas"]:
            raise ValueError(f"Hojas inesperadas: {list(paths)}")
        sheet1 = ET.fromstring(package.read(paths["Cotización técnica"]))
        sheet2 = ET.fromstring(package.read(paths["Herramientas"]))

        data = sheet1.find("m:sheetData", NS)
        assert data is not None
        # Elimina contenido didáctico de las filas de materiales, conservando estilos.
        for row_num in range(2, 42):
            row = row_for(data, row_num)
            for cell in list(row.findall("m:c", NS)):
                clear_cell(cell)

        for offset, record in enumerate(MATERIALS, start=2):
            row = row_for(data, offset)
            for column, key in (("A", "name"), ("B", "category"), ("C", "specification"), ("D", "brand"), ("E", "model"), ("F", "unit"), ("H", "supplier"), ("K", "source")):
                put_inline(row, f"{column}{offset}", record[key])
            put_formula(row, f"G{offset}", record["formula"], record["value"], style="5")
            # I/J se mantienen vacías sin importes.

        # El total monetario preexistente no tiene uso en la actividad sin costos.
        total_row = row_for(data, 43)
        put_inline(total_row, "A43", "CANTIDADES DE MATERIALES — SIN COSTOS", style="11")
        clear_cell(cell_for(total_row, "J43", "10"))

        # Notas visibles al pie, sin agregar hojas/columnas ni alterar encabezados.
        for row_num, (text, style) in enumerate(NOTES, start=45):
            row = row_for(data, row_num)
            row.attrib.update({"ht": "30" if row_num == 45 else "42", "customHeight": "1"})
            put_inline(row, f"A{row_num}", text, style=str(style))
        merges = sheet1.find("m:mergeCells", NS)
        if merges is None:
            merges = ET.Element(f"{{{MAIN}}}mergeCells")
            children = list(sheet1)
            index = next((i + 1 for i, c in enumerate(children) if c.tag == f"{{{MAIN}}}sheetData"), len(children))
            sheet1.insert(index, merges)
        existing_merges = {node.attrib["ref"] for node in merges}
        for row_num in range(45, 45 + len(NOTES)):
            ref = f"A{row_num}:K{row_num}"
            if ref not in existing_merges:
                ET.SubElement(merges, f"{{{MAIN}}}mergeCell", {"ref": ref})
        merges.attrib["count"] = str(len(merges))
        dimension = sheet1.find("m:dimension", NS)
        if dimension is not None:
            dimension.attrib["ref"] = "A1:K51"

        tools_data = sheet2.find("m:sheetData", NS)
        assert tools_data is not None
        for row_num in range(2, 42):
            row = row_for(tools_data, row_num)
            for cell in list(row.findall("m:c", NS)):
                clear_cell(cell)
        for row_num, (name, quantity) in enumerate(TOOLS, start=2):
            row = row_for(tools_data, row_num)
            put_inline(row, f"A{row_num}", name, style="16" if row_num % 2 == 0 else "18")
            if isinstance(quantity, int):
                put_formula(row, f"B{row_num}", str(quantity), quantity, style="17" if row_num % 2 == 0 else "19")
            else:
                put_inline(row, f"B{row_num}", quantity, style="17" if row_num % 2 == 0 else "19")

        workbook = ET.fromstring(package.read("xl/workbook.xml"))
        calc = workbook.find("m:calcPr", NS)
        if calc is None:
            calc = ET.SubElement(workbook, f"{{{MAIN}}}calcPr")
        calc.attrib.update({"calcMode": "auto", "fullCalcOnLoad": "1", "forceFullCalc": "1"})

        return {
            paths["Cotización técnica"]: serialize(sheet1, package.read(paths["Cotización técnica"])),
            paths["Herramientas"]: serialize(sheet2, package.read(paths["Herramientas"])),
            "xl/workbook.xml": serialize(workbook, package.read("xl/workbook.xml")),
        }


def main() -> None:
    if OUTPUT.exists() or PACKAGED_OUTPUT.exists():
        raise FileExistsError("El libro de destino ya existe; no se sobrescriben archivos.")
    original_hash = sha256(TEMPLATE)
    template_bytes = TEMPLATE.read_bytes()
    replacements = make_sheets(template_bytes)
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as target:
        import io

        with zipfile.ZipFile(io.BytesIO(template_bytes)) as source:
            for info in source.infolist():
                data = replacements.get(info.filename, source.read(info.filename))
                target.writestr(info, data)
    if sha256(TEMPLATE) != original_hash:
        raise RuntimeError("El original cambió durante la creación.")
    shutil.copy2(OUTPUT, PACKAGED_OUTPUT)
    image_package = PACKAGE_DIR / "IMAGENES_REVISION"
    image_package.mkdir(parents=True, exist_ok=True)
    for image_path in (ROOT / "07_imagenes" / "fase2b").glob("[0-9][0-9]_*.*"):
        shutil.copy2(image_path, image_package / image_path.name)
    shutil.copy2(ROOT / "04_calculos" / "MEMORIA_CANTIDADES_FASE3B.md", PACKAGE_DIR / "MEMORIA_CANTIDADES_FASE3B.md")
    print(f"Libro creado: {OUTPUT.relative_to(ROOT)}")
    print(f"Paquete de revisión: {PACKAGE_DIR.relative_to(ROOT)}")
    print(f"SHA-256 original preservado: {original_hash}")


if __name__ == "__main__":
    main()
