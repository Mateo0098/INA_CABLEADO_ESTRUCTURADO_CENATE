"""Escenario académico reproducible de longitudes y cantidades — Fase 2D.

Todas las distancias de planta son supuestos declarados, no mediciones. Los
resultados E2/E3 permanecen algebraicos porque x e y no tienen evidencia.
"""

from __future__ import annotations

import csv
import math
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "04_calculos" / "entradas_fase2d.csv"
OUTPUT = ROOT / "04_calculos" / "resultados_fase2d.csv"
D = Decimal


def load_inputs():
    with INPUT.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    return {row["id"]: (D(row["valor"]) if row["valor"] else None) for row in rows}


def fmt(value):
    if value is None:
        return "N/D"
    if isinstance(value, Decimal):
        return format(value.quantize(D("0.001")).normalize(), "f")
    return str(value)


def add(rows, result_id, formula, result, unit, classification, state, dependencies):
    rows.append({
        "id": result_id,
        "formula": formula,
        "resultado": fmt(result),
        "unidad": unit,
        "clasificacion": classification,
        "estado": state,
        "dependencias": dependencies,
    })


def corridor_distances(labs, facade):
    """TR al extremo este; dos filas comparten accesos longitudinales."""
    positions = []
    for index in range(math.ceil(labs / 2)):
        positions.append(facade / 2 + facade * index)
    for index in range(labs // 2):
        positions.append(facade / 2 + facade * index)
    return sorted(positions)


def main():
    v = load_inputs()
    out = []
    total_copper_required = D(0)
    total_copper_commercial = D(0)
    total_tray = D(0)

    for building in ("A", "B"):
        floors = int(v[f"{building}_PISOS"])
        labs_floor = int(v[f"{building}_LABS_PISO"])
        facade = v[f"{building}_FACHADA_LAB"]
        corridor = corridor_distances(labs_floor, facade)
        # Interior representativo: profundidad + desviación lateral media (fachada/4) + bajante.
        interior_avg = v["LAB_PROFUNDIDAD"] + facade / 4 + v["BAJANTE_PUESTO"]
        interior_max = v["LAB_PROFUNDIDAD"] + facade / 2 + v["BAJANTE_PUESTO"]
        crossing = v["ANCHO_PASILLO"] / 2
        link_lengths = [v["TR_TRAMO_INTERNO"] + crossing + distance + interior_avg for distance in corridor]
        max_path = v["TR_TRAMO_INTERNO"] + crossing + max(corridor) + interior_max
        max_with_reserve = max_path + v["RESERVA_COBRE_ENLACE"]
        links_lab = int(v["AREAS_DOBLES_LAB"] * v["RJ45_AREA_DOBLE"])
        base_floor = sum(link_lengths) * links_lab
        base_total = base_floor * floors
        links_total = floors * labs_floor * links_lab
        reserve_total = v["RESERVA_COBRE_ENLACE"] * links_total
        installed = base_total + reserve_total
        waste = installed * v["DESPERDICIO_COBRE"] / D(100)
        required = installed + waste
        boxes = math.ceil(required / v["LONGITUD_CAJA_COBRE"])
        commercial = D(boxes) * v["LONGITUD_CAJA_COBRE"]
        avg_path = sum(link_lengths) / D(labs_floor)
        corridor_spine = facade * math.ceil(labs_floor / 2)
        lab_shared_tray = v["LAB_PROFUNDIDAD"] + facade
        tray_base = floors * (corridor_spine + labs_floor * lab_shared_tray)

        prefix = f"{building}_COBRE"
        add(out, f"{prefix}_DISTANCIAS_PASILLO", "centros desde TR extremo", ";".join(fmt(x) for x in corridor), "m por laboratorio", "escenario académico", "no medido", f"{building}_LABS_PISO;{building}_FACHADA_LAB")
        add(out, f"{prefix}_INTERIOR_PROM", "LAB_PROFUNDIDAD+FACHADA/4+BAJANTE_PUESTO", interior_avg, "m/enlace", "escenario académico", "no medido", "LAB_PROFUNDIDAD;FACHADA;BAJANTE_PUESTO")
        add(out, f"{prefix}_RUTA_PROM", "PROMEDIO(TR_INTERNO+PASILLO/2+DISTANCIA+INTERIOR_PROM)", avg_path, "m/enlace", "resultado de escenario", "provisional", "geometría Fase 2D")
        add(out, f"{prefix}_RUTA_MAX", "TR_INTERNO+PASILLO/2+DISTANCIA_MAX+INTERIOR_MAX", max_path, "m/enlace", "resultado de escenario", "provisional", "geometría Fase 2D")
        add(out, f"{prefix}_MAX_CON_RESERVA", "RUTA_MAX+RESERVA_COBRE_ENLACE", max_with_reserve, "m cable/enlace", "resultado de escenario", "provisional", f"{prefix}_RUTA_MAX;RESERVA_COBRE_ENLACE")
        add(out, f"{prefix}_CUMPLE_90M", "MAX_CON_RESERVA<=MAX_ENLACE_PERMANENTE", "SI" if max_with_reserve <= v["MAX_ENLACE_PERMANENTE"] else "NO", "control", "verificación aritmética", "verificado en escenario", f"{prefix}_MAX_CON_RESERVA;MAX_ENLACE_PERMANENTE")
        add(out, f"{prefix}_BASE", "SUMA(ruta representativa*32 enlaces/lab*pisos)", base_total, "m cable horizontal", "resultado de escenario", "provisional", "rutas representativas")
        add(out, f"{prefix}_RESERVA", "ENLACES*RESERVA_COBRE_ENLACE", reserve_total, "m cable horizontal", "resultado de escenario", "provisional", "RESERVA_COBRE_ENLACE")
        add(out, f"{prefix}_DESPERDICIO", "(BASE+RESERVA)*DESPERDICIO_COBRE/100", waste, "m cable horizontal", "resultado de escenario", "provisional", "DESPERDICIO_COBRE")
        add(out, f"{prefix}_REQUERIDO", "BASE+RESERVA+DESPERDICIO", required, "m cable horizontal", "resultado de escenario", "provisional", f"{prefix}_BASE;{prefix}_RESERVA;{prefix}_DESPERDICIO")
        add(out, f"{prefix}_CAJAS_305M", "CEIL(REQUERIDO/LONGITUD_CAJA_COBRE)", boxes, "caja de 305 m", "resultado de escenario", "provisional", f"{prefix}_REQUERIDO;LONGITUD_CAJA_COBRE")
        add(out, f"{prefix}_METROS_COMERCIALES", "CAJAS_305M*305", commercial, "m cable en cajas", "resultado de escenario", "provisional", f"{prefix}_CAJAS_305M")
        add(out, f"{building}_BANDEJA_BASE", "PISOS*(LONGITUD_PASILLO+LABS*(PROFUNDIDAD+FACHADA))", tray_base, "m de bandeja compartida", "resultado de escenario", "dimensionar sección", "geometría Fase 2D")
        total_copper_required += required
        total_copper_commercial += commercial
        total_tray += tray_base

    tray_reserve = total_tray * D(5) / D(100)
    drops_base = v["TOTAL_AREAS"] * v["BAJANTE_PUESTO"]
    drops_with_reserve = drops_base * D("1.05")
    add(out, "TOTAL_COBRE_REQUERIDO", "A_COBRE_REQUERIDO+B_COBRE_REQUERIDO", total_copper_required, "m cable horizontal", "resultado de escenario", "provisional", "A_COBRE_REQUERIDO;B_COBRE_REQUERIDO")
    add(out, "TOTAL_COBRE_CAJAS_305M", "A_COBRE_CAJAS_305M+B_COBRE_CAJAS_305M", total_copper_commercial / v["LONGITUD_CAJA_COBRE"], "caja de 305 m", "resultado de escenario", "provisional", "A_COBRE_CAJAS_305M;B_COBRE_CAJAS_305M")
    add(out, "TOTAL_COBRE_METROS_COMERCIALES", "TOTAL_CAJAS*305", total_copper_commercial, "m cable en cajas", "resultado de escenario", "provisional", "TOTAL_COBRE_CAJAS_305M")
    add(out, "BANDEJA_INTERIOR_BASE", "A_BANDEJA_BASE+B_BANDEJA_BASE", total_tray, "m bandeja", "resultado de escenario", "sección pendiente", "A_BANDEJA_BASE;B_BANDEJA_BASE")
    add(out, "BANDEJA_INTERIOR_RESERVA_5", "BANDEJA_BASE*5%", tray_reserve, "m bandeja", "resultado de escenario", "provisional", "BANDEJA_INTERIOR_BASE")
    add(out, "BANDEJA_INTERIOR_TOTAL", "BANDEJA_BASE+RESERVA", total_tray + tray_reserve, "m bandeja", "resultado de escenario", "sección pendiente", "BANDEJA_INTERIOR_BASE;BANDEJA_INTERIOR_RESERVA_5")
    add(out, "BAJANTES_PROTEGIDAS", "TOTAL_AREAS", v["TOTAL_AREAS"], "bajante compartida para 2 cables", "resultado condicionado", "provisional", "TOTAL_AREAS")
    add(out, "TUBERIA_BAJANTES_BASE", "TOTAL_AREAS*BAJANTE_PUESTO", drops_base, "m de tubería/bajante", "resultado de escenario", "diámetro pendiente", "TOTAL_AREAS;BAJANTE_PUESTO")
    add(out, "TUBERIA_BAJANTES_TOTAL", "BASE*1.05", drops_with_reserve, "m de tubería/bajante", "resultado de escenario", "diámetro pendiente", "TUBERIA_BAJANTES_BASE")
    add(out, "CAJAS_SALIDA_DOBLE", "TOTAL_AREAS", v["TOTAL_AREAS"], "caja de salida", "resultado condicionado", "tipo pendiente", "TOTAL_AREAS")

    # Fibra vertical: cota + 3 m en cada cuarto + 5 m de reserva en cada extremo.
    vertical_total = D(0)
    for building in ("A", "B"):
        floors = int(v[f"{building}_PISOS"])
        elevations = [D(index) * v["ALTURA_PISO"] for index in range(floors)]
        per_link = [e + D(2) * (v["TRAMO_INTERNO_FIBRA_EXTREMO"] + v["RESERVA_FIBRA_EXTREMO"]) for e in elevations]
        base = sum(per_link)
        required = base * (D(1) + v["DESPERDICIO_FIBRA"] / D(100))
        add(out, f"{building}_FIBRA_VERTICAL_ENLACES", "cota+2*(tramo interno+reserva)", ";".join(fmt(x) for x in per_link), "m cable por enlace", "resultado de escenario", "provisional", "ALTURA_PISO;reservas Fase 2D")
        add(out, f"{building}_FIBRA_VERTICAL_BASE", "SUMA(longitudes por enlace)", base, "m cable 12F", "resultado de escenario", "provisional", f"{building}_FIBRA_VERTICAL_ENLACES")
        add(out, f"{building}_FIBRA_VERTICAL_REQUERIDA", "BASE*(1+DESPERDICIO_FIBRA/100)", required, "m cable 12F", "resultado de escenario", "provisional", f"{building}_FIBRA_VERTICAL_BASE;DESPERDICIO_FIBRA")
        vertical_total += required
    add(out, "TOTAL_FIBRA_VERTICAL_REQUERIDA", "A+B", vertical_total, "m cable 12F", "resultado de escenario", "provisional", "A_FIBRA_VERTICAL_REQUERIDA;B_FIBRA_VERTICAL_REQUERIDA")

    ext_allowance = D(2) * (v["TRAMO_INTERNO_FIBRA_EXTREMO"] + v["RESERVA_FIBRA_EXTREMO"])
    e1 = (v["DUCTO_EXISTENTE"] + v["DUCTO_NUEVO_A"] + ext_allowance) * (D(1) + v["DESPERDICIO_FIBRA"] / D(100))
    add(out, "E1_FIBRA_24F_REQUERIDA", "(145+50+2*(tramo interno+reserva))*1.05", e1, "m cable 24F", "resultado de escenario", "verificar ruta", "DUCTO_EXISTENTE;DUCTO_NUEVO_A;reservas Fase 2D")
    add(out, "E2_FIBRA_24F_FORMULA", "(145+x+16)*1.05", "169.05 + 1.05x", "m cable 24F", "fórmula con variable", "pendiente x", "DUCTO_EXISTENTE;X_RUTA_B")
    add(out, "E3_FIBRA_24F_FORMULA", "(y+16)*1.05", "16.8 + 1.05y", "m cable 24F", "fórmula con variable", "pendiente y", "Y_RUTA_A_B")
    add(out, "TOTAL_FIBRA_24F_FORMULA", "E1+E2+E3", "407.4 + 1.05x + 1.05y", "m cable 24F", "fórmula con variables", "pendiente x/y", "E1;E2;E3")

    # Cantidades de sistema pasivo coherente.
    fixed = [
        ("PATCH_CORD_COBRE_USUARIO", "TOTAL_RJ45", v["TOTAL_RJ45"], "patch cord 7 ft", "capacidad pasiva completa"),
        ("PATCH_CORD_COBRE_RACK", "TOTAL_RJ45", v["TOTAL_RJ45"], "patch cord 7 ft", "capacidad pasiva completa; activos separados"),
        ("PATCH_CORD_OPTICO_MAX", "(408 terminaciones)/2", D(204), "patch cord LC-LC dúplex", "máximo si todas las fibras se activan"),
        ("HOUSING_CCH_01U", "11 TR+ER-P", D(12), "housing", "11 nuevos + 1 sujeto a espacio existente"),
        ("HOUSING_CCH_03U", "ER-A", D(1), "housing", "6 cassettes"),
        ("HOUSING_CCH_04U", "ER-B", D(1), "housing", "9 cassettes"),
        ("RACK_42U_NUEVOS", "11 TR+2 ER", D(13), "rack", "escenario; activos pendientes"),
        ("ORGANIZADOR_HORIZONTAL_COBRE", "TOTAL_PANELES", v["TOTAL_PANELES"], "organizador 1U", "uno por panel"),
        ("ORGANIZADOR_HORIZONTAL_OPTICO", "14 housings", D(14), "organizador 1U", "uno por housing"),
        ("PIGTAILS_COMPRA_SEPARADA", "cassette pre-pigtailed", D(0), "pigtail", "evita doble conteo"),
        ("ADAPTADORES_COMPRA_SEPARADA", "cassette pre-pigtailed", D(0), "adaptador", "evita doble conteo"),
    ]
    for result_id, formula, result, unit, state in fixed:
        add(out, result_id, formula, result, unit, "resultado condicionado", state, "arquitectura Fase 2D")

    fields = ["id", "formula", "resultado", "unidad", "clasificacion", "estado", "dependencias"]
    with OUTPUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out)
    print(f"Generados {len(out)} resultados en {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
