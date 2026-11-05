"""Controles dirigidos de U04C; no equivale a recálculo en Excel."""
import csv
import zipfile
from pathlib import Path

from openpyxl import load_workbook

from generar_presupuesto import OFFERS, OUTPUT, U02, U03


def records(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main():
    src = records(U02) + records(U03)
    offers = records(OFFERS)
    ids = [r["ID único"] for r in src]
    assert len(src) == len(set(ids)) == 223
    assert len(offers) == 6 and all(o["ID_partida"] in ids for o in offers)
    assert sum(o["ID_partida"] == "U02-02A-001" for o in offers) == 2
    with zipfile.ZipFile(OUTPUT) as z:
        assert z.testzip() is None
    book = load_workbook(OUTPUT, data_only=False)
    assert len(book.sheetnames) == 8
    ws = book["02_PARTIDAS"]
    assert ws.max_row == 224 and [ws.cell(i, 1).value for i in range(2, 225)] == ids
    byid = {ws.cell(i, 1).value: i for i in range(2, 225)}
    assert ws.cell(byid["U02-02C-025"], 7).value == 44
    assert ws.cell(byid["U02-02C-026"], 7).value == 7
    assert ws.cell(byid["U02-02A-001"], 7).value is None
    assert ws.cell(byid["U02-02B-029"], 7).value is None
    assert ws.cell(byid["U03-03B-010"], 7).value is None
    for ident in ("U02-02C-025", "U02-02C-026", "U02-02C-027"):
        row = byid[ident]
        assert ws.cell(row, 23).data_type == "f"
        assert ws.cell(row, 21).data_type == "f"
        assert ws.cell(row, 22).data_type == "f"
    assert "Adicional 51" in ws.cell(byid["U02-02C-026"], 13).value
    assert ws.cell(byid["U02-02C-026"], 13).value == "Adicional 51"
    assert "COUNTIFS" in ws.cell(byid["U02-02C-025"], 21).value
    assert "1+T" in ws.cell(byid["U02-02C-025"], 21).value
    assert "U" in ws.cell(byid["U02-02C-025"], 22).value
    assert book["06_PARAMETROS"]["B3"].value is None
    assert book["05_IMPORTACIONES"]["R2"].data_type == "f"
    assert book["04_ESCENARIOS"]["E2"].data_type == "f"
    assert book["01_RESUMEN"]["B13"].value.startswith("NO DISPONIBLE")
    assert len(book["03_COTIZACIONES"].tables) == 0  # sin vínculos externos
    book.close()
    print("U04C: 223 IDs, 6 ofertas, 8 hojas, fórmulas y ZIP íntegro: OK")


if __name__ == "__main__":
    main()
