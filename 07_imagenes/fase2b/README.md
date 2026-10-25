# Diagramas técnicos Fase 2B

## Inventario

| N.º | SVG editable | PNG de entrega | Código |
|---:|---|---|---|
| 1 | `01_backbone_exterior.svg` | `01_backbone_exterior.png` | EXT-01 |
| 2 | `02_planta_tipica_edificio_A.svg` | `02_planta_tipica_edificio_A.png` | PLA-A |
| 3 | `03_planta_tipica_edificio_B.svg` | `03_planta_tipica_edificio_B.png` | PLA-B |
| 4 | `04_laboratorio_tipico_A.svg` | `04_laboratorio_tipico_A.png` | LAB-A |
| 5 | `05_laboratorio_tipico_B.svg` | `05_laboratorio_tipico_B.png` | LAB-B |
| 6 | `06_ER_A.svg` | `06_ER_A.png` | ER-A |
| 7 | `07_TR_A.svg` | `07_TR_A.png` | TR-A |
| 8 | `08_ER_B.svg` | `08_ER_B.png` | ER-B |
| 9 | `09_TR_B.svg` | `09_TR_B.png` | TR-B |

Los SVG se regeneran con:

```powershell
python 03_diseno/generar_diagramas_fase2b.py
```

Los PNG 1600×1000 se regeneran en Windows con Chrome instalado:

```powershell
03_diseno/exportar_svg_png.ps1
```

## Arquitectura común representada

- Tres enlaces exteriores distintos: ER-P–ER-A, ER-P–ER-B y ER-A–ER-B.
- 24 fibras OS2 por enlace exterior; 12 fibras OS2 por cada enlace ER–TR.
- Un ER y un TR separado por piso; total 2 ER nuevos y 11 TR.
- Cada laboratorio contiene 16 áreas dobles; la interpretación provisional es dos puertos RJ45 por área.
- Cableado horizontal Cat 6A en estrella: 160 enlaces/TR en A y 192 enlaces/TR en B.
- Paneles de 48 puertos: 4/TR en A y 5/TR en B.
- Los equipos activos están pendientes y no se deducen de la capacidad pasiva.

## Geometría y distancias

Los dibujos no están a escala. Las geometrías 10×8,5 m (A), 10×7,5 m (B), pasillo de 2,4 m, TR de 3×3 m, ER de 4×4 m, ubicación en planta baja y alineación vertical son **supuestos de diseño**, no mediciones.

Solo se muestran como referencias reportadas 145 m de ducto existente, 50 m de ducto nuevo propuesto y separación orientativa de 25 m entre cajas. `x` e `y` permanecen como variables. Ningún SVG acredita que un enlace de cobre cumpla 90 m: cada ruta debe medirse.

## Procedencia y revisión

Generados el 2026-10-25 con apoyo visual de OpenAI Codex a partir de fuentes internas del repositorio. Requieren revisión, comprensión y aprobación del estudiante antes de entrega o defensa. No son planos constructivos.
