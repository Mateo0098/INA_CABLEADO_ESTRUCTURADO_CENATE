# Reporte de cierre — checkpoint de implementación Fase 2B

**Fecha:** 2026-10-25  
**Rama:** `desarrollo-proyecto`  
**Commit de implementación:** `268c4cc08c6af79d4aae32a7daf5d1874b2dbdeb`  
**Estado:** bloque funcional verificable; la entrega completa continúa abierta por datos de campo y revisión humana.

## Alcance ejecutado

- Implementación de los nueve diseños requeridos como SVG editable y PNG 1600×1000.
- Modelo reproducible de capacidad de cobre, fibra, terminaciones, paneles, patch cords, ductos y cajas de referencia.
- Matriz técnica de materiales candidatos sin precios, con fuentes oficiales cuando se verificó un modelo.
- Copia de trabajo identificada del Excel y correspondencia para traslado manual.
- Control automatizado de coherencia, integridad gráfica, resultados y OOXML.

No se realizó una nueva auditoría general de requisitos ni se presentó el checkpoint como diseño constructivo.

## Entradas utilizadas

| Entrada | Clasificación | Uso |
|---|---|---|
| 4 pisos × 5 laboratorios en A; 7 × 6 en B | Dato establecido por docente | Plantas y capacidad |
| 85 m² A; 75 m² B; mínimo 16 áreas dobles | Dato establecido por docente | Laboratorios y cálculo |
| Dos RJ45 por área doble | Supuesto de diseño | Capacidad provisional de cobre |
| Cat 6A, paneles de 48 puertos | Supuesto de diseño | Modelo pasivo |
| OS2, 12 fibras verticales y 24 exteriores | Supuesto de diseño | Backbone y terminaciones |
| 145 m existentes; 50 m nuevos; ~25 m entre cajas | Datos/propuesta reportados por estudiante | Referencias rotuladas; no cantidades cerradas |
| `x`, `y`, reservas y rutas interiores | Decisión/medición pendiente | Permanecen como variables o `N/D` |

## Archivos principales creados

- `03_diseno/generar_diagramas_fase2b.py`
- `03_diseno/exportar_svg_png.ps1`
- `04_calculos/entradas_fase2b.csv`
- `04_calculos/modelo_calculos_fase2b.py`
- `04_calculos/resultados_fase2b.csv`
- `04_calculos/MEMORIA_CALCULOS_FASE2B.md`
- `05_materiales/MATRIZ_TECNICA_FASE2B.md`
- `06_excel/Plantilla Actividades de comprobación_TRABAJO_FASE2B.xlsx`
- `06_excel/CORRESPONDENCIA_FASE2B.md`
- `07_imagenes/fase2b/` — nueve SVG, nueve PNG y guía de regeneración.
- `09_auditorias/validar_fase2b.py`

Se actualizaron `README.md`, `DECISIONES.md` y `PENDIENTES.md` con el estado comprobado.

## Resultados técnicos verificados

| Control | Resultado |
|---|---:|
| Laboratorios A / B / total | 20 / 42 / 62 |
| Áreas dobles A / B / total | 320 / 672 / 992 |
| Enlaces RJ45 A / B / total | 640 / 1 344 / 1 984 |
| Paneles 48 puertos A / B / total | 16 / 35 / 51 |
| TR | 11 |
| Terminaciones de fibra verticales / exteriores | 264 / 144 |
| Pigtails/empalmes si se terminan todas las fibras | 408 |
| Adaptadores LC dúplex bajo el mismo supuesto | 204 |

Los resultados RJ45 y de terminación óptica están condicionados por supuestos explícitos; no son mediciones.

## Verificaciones ejecutadas

Comando:

```powershell
python 09_auditorias/validar_fase2b.py
```

Resultado: **63/63 controles aprobados**.

- Nueve SVG válidos como XML.
- Nueve PNG válidos de 1600×1000.
- Presencia de los tres edificios, tres enlaces, cinco/seis laboratorios, 16 áreas, paneles y fibras esperadas.
- Resultados matemáticos clave cotejados.
- Metrajes de cobre mantenidos como `N/D`.
- Original y copia Excel íntegros como OOXML.
- Dos hojas y fórmula `J43=SUM(J2:J41)` conservadas.
- SHA-256 original y copia: `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`.
- Revisión visual manual de los nueve PNG ejecutada; se corrigieron solapamientos detectados.
- Sintaxis de tres scripts Python y un script PowerShell comprobada.
- `git diff --check` sin errores; solo advertencias informativas de conversión LF/CRLF.

## Problemas e inconsistencias reales

1. Cuatro paneles de 48 puertos cubren exactamente 192 enlaces en un TR B, pero dejan cero reserva. Se documentó la regla provisional de agregar un panel cuando la división es exacta; requiere aceptación del estudiante.
2. No se ha confirmado que “área doble” signifique dos RJ45.
3. No existen longitudes suficientes para calcular cable de cobre, cable vertical ni dos de las tres rutas exteriores.
4. La referencia de cajas cada 25 m produce posiciones teóricas, no una cantidad de compra.
5. Un rack 42U por cuarto no está validado contra activos, energía, fondo, carga, ventilación o acceso.
6. El original Excel exige columnas económicas vacías, pero conserva una fórmula en `J43`; sigue pendiente consulta docente.
7. El enunciado prohíbe generar automáticamente el Excel con IA; por ello la copia se preservó sin poblar y se preparó correspondencia para traslado manual por el estudiante.

## Trabajo necesario para completar la entrega

- Confirmación docente de área doble y `J43`.
- Levantamiento de rutas y verificación de ductos/cajas.
- Porcentajes de reserva/desperdicio aprobados.
- Cálculo de ocupación con diámetros reales.
- Cierre de familias ODF/cassette, rack, patch cords, activos, potencia y herramientas.
- Revisión humana y traslado manual al Excel; prueba de fórmulas y eliminación de ejemplos en la copia.
- Revisión final de coherencia y preparación de la defensa de al menos ocho minutos.

## Procedencia de IA

OpenAI Codex se utilizó para apoyo organizativo, generación reproducible de diagramas, estructura de fórmulas, redacción y controles. El estudiante debe revisar, comprender, corregir y defender cada contenido. Las especificaciones comerciales se vincularon a fuentes oficiales y no se adoptaron como selección definitiva.
