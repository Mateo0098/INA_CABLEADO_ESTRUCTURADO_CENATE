"""Modelo reproducible de capacidad para la Fase 2B.

No sustituye el cálculo individual ni la revisión del estudiante. Mantiene como
N/D todo resultado que dependa de una medición o porcentaje aún no aprobado.
"""

from __future__ import annotations

import csv
import math
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "04_calculos" / "entradas_fase2b.csv"
OUTPUT = ROOT / "04_calculos" / "resultados_fase2b.csv"


def load_inputs():
    with INPUT.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    raw = {row["id"]: row["valor"] for row in rows}
    values = {key: (Decimal(value) if value != "" else None) for key, value in raw.items()}
    return rows, values


def fmt(value):
    if value is None:
        return "N/D"
    if isinstance(value, Decimal):
        return format(value, "f")
    return str(value)


def add(rows, result_id, expression, value, unit, classification, dependencies, state="calculado"):
    rows.append({
        "id": result_id,
        "formula": expression,
        "resultado": fmt(value),
        "unidad": unit,
        "clasificacion": classification,
        "dependencias": dependencies,
        "estado": state if value is not None else "pendiente de entradas",
    })


def main():
    _, v = load_inputs()
    out = []
    total_ports = 0
    total_areas = 0
    total_labs = 0
    total_panels = 0

    for b in ("A", "B"):
        floors = int(v[f"{b}_PISOS"])
        labs_floor = int(v[f"{b}_LABS_PISO"])
        labs = floors * labs_floor
        areas = labs * int(v["AREAS_DOBLES_LAB"])
        ports = areas * int(v["RJ45_AREA_DOBLE"])
        ports_tr = labs_floor * int(v["AREAS_DOBLES_LAB"]) * int(v["RJ45_AREA_DOBLE"])
        panel_ports = int(v["PUERTOS_PANEL_COBRE"])
        panels_tr = math.ceil(ports_tr / panel_ports)
        if ports_tr % panel_ports == 0:
            panels_tr += int(v["PANEL_ADICIONAL_SI_LLENO"])
        panels = panels_tr * floors
        capacity = panels * int(v["PUERTOS_PANEL_COBRE"])
        spare = capacity - ports
        add(out, f"{b}_LABS", f"{b}_PISOS*{b}_LABS_PISO", labs, "laboratorio", "resultado calculado", f"{b}_PISOS;{b}_LABS_PISO")
        add(out, f"{b}_AREAS", f"{b}_LABS*AREAS_DOBLES_LAB", areas, "area doble", "resultado calculado", f"{b}_LABS;AREAS_DOBLES_LAB")
        add(out, f"{b}_RJ45", f"{b}_AREAS*RJ45_AREA_DOBLE", ports, "puerto/enlace", "resultado condicionado", f"{b}_AREAS;RJ45_AREA_DOBLE", "provisional")
        add(out, f"{b}_RJ45_TR", f"{b}_LABS_PISO*AREAS_DOBLES_LAB*RJ45_AREA_DOBLE", ports_tr, "puerto/TR", "resultado condicionado", f"{b}_LABS_PISO;AREAS_DOBLES_LAB;RJ45_AREA_DOBLE", "provisional")
        add(out, f"{b}_PANELES_TR", "CEIL(RJ45_TR/PUERTOS_PANEL_COBRE)+IF(MOD(RJ45_TR,PUERTOS_PANEL_COBRE)=0,PANEL_ADICIONAL_SI_LLENO,0)", panels_tr, "panel/TR", "resultado condicionado", f"{b}_RJ45_TR;PUERTOS_PANEL_COBRE;PANEL_ADICIONAL_SI_LLENO", "provisional")
        add(out, f"{b}_PANELES_TOTAL", f"{b}_PANELES_TR*{b}_PISOS", panels, "panel", "resultado condicionado", f"{b}_PANELES_TR;{b}_PISOS", "provisional")
        add(out, f"{b}_CAPACIDAD_PANEL", f"{b}_PANELES_TOTAL*PUERTOS_PANEL_COBRE", capacity, "puerto", "resultado condicionado", f"{b}_PANELES_TOTAL;PUERTOS_PANEL_COBRE", "provisional")
        add(out, f"{b}_PUERTOS_LIBRES", f"{b}_CAPACIDAD_PANEL-{b}_RJ45", spare, "puerto", "resultado condicionado", f"{b}_CAPACIDAD_PANEL;{b}_RJ45", "provisional")
        avg = v[f"LONG_PROM_COBRE_{b}"]
        waste = v["DESPERDICIO_COBRE"]
        copper = None if avg is None or waste is None else Decimal(ports) * avg * (Decimal(1) + waste / Decimal(100))
        add(out, f"{b}_CABLE_COBRE", f"{b}_RJ45*LONG_PROM_COBRE_{b}*(1+DESPERDICIO_COBRE/100)", copper, "m cable", "resultado pendiente", f"{b}_RJ45;LONG_PROM_COBRE_{b};DESPERDICIO_COBRE")
        total_ports += ports
        total_areas += areas
        total_labs += labs
        total_panels += panels

    total_tr = int(v["A_PISOS"] + v["B_PISOS"])
    add(out, "TOTAL_LABS", "A_LABS+B_LABS", total_labs, "laboratorio", "resultado calculado", "A_LABS;B_LABS")
    add(out, "TOTAL_AREAS", "A_AREAS+B_AREAS", total_areas, "area doble", "resultado calculado", "A_AREAS;B_AREAS")
    add(out, "TOTAL_RJ45", "A_RJ45+B_RJ45", total_ports, "puerto/enlace", "resultado condicionado", "A_RJ45;B_RJ45", "provisional")
    add(out, "TOTAL_PANELES", "A_PANELES_TOTAL+B_PANELES_TOTAL", total_panels, "panel", "resultado condicionado", "A_PANELES_TOTAL;B_PANELES_TOTAL", "provisional")
    add(out, "TOTAL_TR", "A_PISOS+B_PISOS", total_tr, "TR", "resultado calculado", "A_PISOS;B_PISOS")
    add(out, "CABLES_VERTICAL", "TOTAL_TR", total_tr, "cable de fibra", "resultado condicionado", "TOTAL_TR", "provisional")
    vertical_positions = total_tr * int(v["FIBRAS_VERTICAL"]) * 2
    exterior_positions = int(v["ENLACES_EXTERIORES"]) * int(v["FIBRAS_EXTERIOR"]) * 2
    all_positions = vertical_positions + exterior_positions
    add(out, "FIBRAS_TERM_VERTICAL", "TOTAL_TR*FIBRAS_VERTICAL*2_EXTREMOS", vertical_positions, "terminacion de fibra", "resultado condicionado", "TOTAL_TR;FIBRAS_VERTICAL", "provisional")
    add(out, "FIBRAS_TERM_EXTERIOR", "ENLACES_EXTERIORES*FIBRAS_EXTERIOR*2_EXTREMOS", exterior_positions, "terminacion de fibra", "resultado condicionado", "ENLACES_EXTERIORES;FIBRAS_EXTERIOR", "provisional")
    add(out, "PIGTAILS_Y_EMPALMES", "FIBRAS_TERM_VERTICAL+FIBRAS_TERM_EXTERIOR", all_positions, "unidad", "resultado condicionado", "FIBRAS_TERM_VERTICAL;FIBRAS_TERM_EXTERIOR", "provisional")
    add(out, "ADAPTADORES_LC_DUPLEX", "CEIL(TOTAL_TERMINACIONES_FIBRA/2)", math.ceil(all_positions / 2), "adaptador duplex", "resultado condicionado", "PIGTAILS_Y_EMPALMES", "provisional")
    add(out, "PATCH_CORD_COBRE_USUARIO", "TOTAL_RJ45", total_ports, "patch cord", "resultado condicionado", "TOTAL_RJ45", "provisional")
    add(out, "PATCH_CORD_COBRE_RACK", "TOTAL_RJ45", total_ports, "patch cord", "resultado condicionado", "TOTAL_RJ45", "provisional")
    add(out, "PLACAS_DOBLES", "TOTAL_AREAS", total_areas, "placa/caja", "resultado condicionado", "TOTAL_AREAS", "provisional")
    add(out, "JACKS_CAT6A", "TOTAL_RJ45", total_ports, "jack", "resultado condicionado", "TOTAL_RJ45", "provisional")
    add(out, "DUCTO_EXISTENTE_REFERENCIA", "DUCTO_EXISTENTE", v["DUCTO_EXISTENTE"], "m ducto", "dato reportado", "DUCTO_EXISTENTE", "verificar; no comprar")
    add(out, "DUCTO_NUEVO_PROPUESTO", "DUCTO_NUEVO_A", v["DUCTO_NUEVO_A"], "m ducto", "propuesta", "DUCTO_NUEVO_A", "destino/ruta por verificar")
    theoretical_boxes = math.floor(int(v["DUCTO_EXISTENTE"]) / int(v["SEPARACION_CAJAS_REF"]))
    add(out, "POSICIONES_CAJAS_145M", "FLOOR(DUCTO_EXISTENTE/SEPARACION_CAJAS_REF)", theoretical_boxes, "posicion intermedia teorica", "resultado orientativo", "DUCTO_EXISTENTE;SEPARACION_CAJAS_REF", "no es cantidad de compra")

    fieldnames = ["id", "formula", "resultado", "unidad", "clasificacion", "dependencias", "estado"]
    with OUTPUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out)
    print(f"Generados {len(out)} resultados en {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
