# Prototipos gráficos de Fase 5B — INA CENATE

**Estado histórico desde 2026-10-29:** los dos prototipos sirvieron de base gráfica para las nueve láminas Fase 5C. La colección vigente está en `08_entrega/ENTREGA_FINAL_INA_CENATE/06_PLANOS_TECNICOS/`.

| Prototipo | SVG editable | PDF A3 horizontal | PNG a 300 ppp |
|---|---|---|---|
| P1 — elevación frontal TR-A | `SVG_EDITABLE/P1_TR_A.svg` | `PDF_A3/P1_TR_A.pdf` | `PNG/P1_TR_A.png` |
| P2 — planta de canalizaciones A | `SVG_EDITABLE/P2_PLANTA_A.svg` | `PDF_A3/P2_PLANTA_A.pdf` | `PNG/P2_PLANTA_A.png` |

`COMPARATIVO_FASE5_VS_PROTOTIPOS.pdf` documenta la comparación histórica entre Fase 5 y Fase 5B. Conserva texto y trazos vectoriales; no representa el conjunto vigente.

## Datos y límites

- **Dato de diseño aprobado en el repositorio:** TR-A tiene cuatro paneles pasivos de 48 posiciones, 160 posiciones asignadas y 32 libres; cada uno de los cinco laboratorios supuestos tiene 16 WA dobles y 32 enlaces Cat 6A. El backbone vertical hacia TR-A es OS2 12F y termina en un cassette integrado en housing CCH-01U.
- **Especificación de fabricante verificada, no selección definitiva:** el candidato [Panduit NK6XPPG48Y](https://www.panduit.com/content/dam/panduit/en/website/about-us/thought-leadership/documents/111369255.pdf) tiene 48 puertos Cat 6A y ocupa 2U. El [housing Corning CCH-01U](https://www.corning.com/catalog/coc/documents/selection-guides/LAN-2564-AEN.pdf) ocupa 1U y admite dos posiciones de cassette. El [cassette CCH-CS12-A9-P00RE](https://www.corning.com/catalog/coc/documents/product-family-specifications/pfss/c/en-US/cch-pigtailed-splice-cassette_CALA_AEN.pdf) es de 12 fibras OS2 con seis adaptadores LC dúplex integrados. Consulta: 2026-10-28. El dibujo frontal es un símbolo de ingeniería genérico; no reproduce un producto para compra.
- **Supuesto de diseño:** planta de cinco laboratorios, pasillo central, ubicación del TR, muros, puertas, pasamuros, recorridos, cajas, soportes y puntos representativos. La sección preliminar de bandeja es 100 × 50 mm y el tubo nominal es Ø25 mm. Las dos salidas dibujadas en cada laboratorio muestran ejemplos de ruta; las 16 WA completas se cuantifican, pero no se ubican aquí.
- **Pendiente:** medición de campo, ocupación de bandeja/tubo, método de fijación, coordinación arquitectónica y revisión académica personal. Ningún puerto de panel se presenta como conectado a un switch activo.

## Regeneración y control

Desde la raíz del repositorio:

```powershell
python 09_auditorias/generar_prototipos_fase5b.py
python 09_auditorias/validar_prototipos_fase5b.py
```

El generador usa geometría SVG y ReportLab para PDF vectorial, y PyMuPDF únicamente para el PNG y el montaje del comparativo. La autoría gráfica y documental contó con asistencia de OpenAI Codex; requiere revisión humana del contenido técnico y académico.
