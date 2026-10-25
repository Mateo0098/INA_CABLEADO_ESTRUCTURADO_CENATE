# Fase 2 — Diseño técnico integrado de referencia (Actividad 1)

**Fecha:** 2026-10-25  
**Estado:** propuesta preliminar consolidada para revisión del estudiante; **no es un plano constructivo ni material definitivamente seleccionado**.  
**Fuente de requisitos:** `01_requisitos/MATRIZ_REQUISITOS.md` (INA-001 a INA-076).  
**Procedencia:** síntesis de las unidades de diseño discutidas en ChatGPT; no procede de mediciones adicionales de campo.  
**Prioridad:** producir planos legibles, justificar cantidades y preparar los entregables del 29-10-2026.

## 1. Base vinculante y supuestos

| Variable | A | B | Procedencia |
|---|---:|---:|---|
| Pisos | 4 | 7 | INA-003/004 |
| Laboratorios por piso | 5 | 6 | INA-003/004 |
| Área de laboratorio | 85 m² | 75 m² | INA-003/004 |
| Áreas de trabajo dobles mínimas por laboratorio | 16 | 16 | INA-011 |
| TR mínimos por piso | 1 | 1 | INA-008, sujetos a cobertura INA-009 |
| ER por edificio | 1 | 1 | INA-005 |
| Dimensión propuesta por laboratorio | 10 × 8,5 m | 10 × 7,5 m | Supuesto; satisface área, no geometría medida |
| Pasillo central | 2,4 m | 2,4 m | Supuesto |
| Distancia entre pisos | 3,5 m | 3,5 m | Supuesto |
| ER y TR | ER en planta baja, TR alineados por piso | Igual | Supuesto |

**Interpretación pendiente:** «área de trabajo doble» = una ubicación con dos tomas RJ45, supuesto de trabajo **no confirmado con docente**. No afirmar que es la única interpretación posible.

## 2. Arquitectura

Tres enlaces exteriores **distintos**: ER principal–ER A, ER principal–ER B, ER A–ER B. Reutilizar preliminarmente 145 m de canalización existente y proponer 50 m nuevos hacia ER A. El edificio A como receptor es **hipótesis**, no medición. Otros tramos `x` (hacia B) e `y` (A–B) requieren distancias; no inventarlas. Las rutas pueden compartir ductos sin ser redundancia física.

En cada edificio: ER propio → backbone óptico en estrella → TR de cada piso → cableado horizontal de cobre en estrella hasta todas las salidas. Se modelan TR separados de ER incluso en primer piso para evitar conteo ambiguo, pendiente de verificar espacio.

Tecnologías candidatas (sin adopción comercial definitiva): fibra monomodo OS2 en exterior y vertical, conectores LC/UPC dúplex, fusión con pigtails; cobre Cat 6A y patch panels de 48 puertos; racks de 19 pulgadas y 42U como **hipótesis de espacio**. Revisar clasificación de cubierta para exterior/ducto versus interior/riser, transiciones, conexiones y fichas reales.

## 3. Plantas y laboratorios

**A:** 3 laboratorios frente a 2 con pasillo central; el sexto módulo potencial no puede asumirse completamente disponible para TR, escaleras y servicios. Con fachada de 8,5 m por laboratorio, fila de tres = 25,5 m; profundidad de dos filas y corredor = 22,4 m antes de muros. **B:** 3 frente a 3; fachada de 7,5 m por laboratorio, fila de tres = 22,5 m; profundidad = 22,4 m antes de muros. En B, TR en anexo, sin restar superficie a los seis laboratorios. Estas son **dimensiones geométricas de referencia**, no planos a escala aprobados.

En cada laboratorio: 16 ubicaciones representadas con sus dobles salidas; disposición 4 × 4 o dos grupos de ocho son alternativas visuales, **no dos diseños simultáneamente aprobados**. Seleccionar una sola antes de dibujar. Canalización aérea de pasillo con derivaciones y bajantes protegidas hasta cada estación; revisar que el mobiliario central tenga alimentación físicamente posible. Puertas, pasos, escaleras, recorridos y holguras de sillas deben dibujarse de manera coherente. Para cada puerto calcular recorrido **físico**, no distancia en línea recta, y verificar **enlace permanente de cobre ≤90 m**; cordones del canal se tratan por separado.

## 4. Cálculos de control: capacidad, no lista definitiva de compra

Derivados de los requisitos y del supuesto de 2 RJ45/área:

| Magnitud | A | B | Total |
|---|---:|---:|---:|
| Laboratorios | 20 | 42 | 62 |
| Áreas dobles | 320 | 672 | 992 |
| Posiciones RJ45 / enlaces horizontales | 640 | 1344 | 1984 |
| TR de referencia | 4 | 7 | 11 |
| RJ45 por TR/piso | 160 | 192 | — |
| Paneles de 48 puertos por TR, con reserva | 4 | 5 | — |
| Paneles de 48 puertos en todos los TR | 16 | 35 | 51 |
| Posiciones en paneles | 768 | 1680 | 2448 |
| Posiciones no utilizadas frente a demanda | 128 | 336 | 464 |

**Importante:** estas son capacidades pasivas condicionadas por la interpretación de «doble». No implican 1984 puertos de switch activos ni 1984 computadoras.

## 5. Fibra de referencia

Propuesta: **12 fibras OS2 por enlace ER–TR**, cables independientes por TR. **24 fibras OS2 por cada enlace exterior**, tres cables/enlaces independientes conceptualmente. Esta capacidad es una decisión de diseño y no un mínimo exigido por normas.

| Terminaciones de fibra individuales en cuarto | ER A | ER B | ER principal (adicionales) |
|---|---:|---:|---:|
| Enlaces exteriores (2 × 24) | 48 | 48 | 48 |
| Backbone vertical (TR × 12) | 48 | 84 | 0 |
| **Total de posiciones de fibra por cuarto** | **96** | **132** | **48** |

En los **11 TR**, 12 posiciones por TR = **132** posiciones en conjunto. Longitud de cable y cantidad de fibras son magnitudes diferentes. Fibras terminadas ≠ transceptores activos. La capacidad efectiva de paneles depende de adaptadores, bandejas de empalme y entradas de cable, no solo del conteo de puertos.

**Hipótesis de paneles:** 96 fibras nominales para ER A; capacidad ≥132 para ER B; capacidad adicional ≥48 en ER principal. No adjudicar modelos sin ficha y método de terminación compatibles.

## 6. Longitudes y canalización: variables obligatorias

Exterior: 
- Tramo de ducto existente: `D_existente = 145 m` (verificar sitio/capacidad).
- Tramo nuevo propuesto A: `D_A = 50 m` (verificar destino y ruta).
- Recorrido base principal→A = `145 + 50 = 195 m` antes de reservas, entradas y ajustes.
- Recorrido principal→B = `145 + x` **solo si se verifica el tramo compartido**.
- Recorrido A→B = `y`, trazado aún no determinado.
- Referencia de cajas: separación aproximada 25 m comunicada en clase, **no cantidad verificada**. Sobre 145 m, posiciones intermedias teóricas 25/50/75/100/125 m, no cajas para adquirir sin inspección. Sobre 50 m, una posición intermedia teórica a 25 m.

Vertical: para cada TR `L_cable = diferencia de cotas + tramos horizontales ER/TR + rutas internas + reserva aprobada`. No multiplicar alturas por números de pisos sin definir cota de origen y planta.

Horizontal: por enlace `L_permanente = tramo TR + pasillo + acceso a laboratorio + distribución interior + bajante + holguras de terminación`. No asumir 90 m como longitud de cada cable; es el máximo permitido. En el cómputo de rollos considerar cortes, longitudes comerciales y desperdicio explícito.

Ductos/bandejas: ocupar según **diámetro exterior real de cable**, número de cables simultáneos, diámetro interior útil y método de instalación. No equiparar número de fibras con cantidad de cables. Dimensionamiento definitivo requiere ficha de cable, ducto y reglas aplicables.

## 7. Racks y paneles

Referencia por TR: rack de 19 pulgadas y 42U; panel Cat 6A de 48 puertos, modelo 2U candidato (no confundir con todos los paneles de 48 puertos, que pueden tener distintas alturas). TR A: 4 paneles → 8U de paneles; TR B: 5 → 10U. Presupuesto **ilustrativo** de organizadores horizontales 4U/5U, distribución óptica 2U, organización óptica 1U: suma pasiva A 15U y B 18U. Falta dimensionar switches, ventilación, potencia, PDU/UPS, fondo del rack, ingreso de cables y acceso; por ello **no está demostrado que un único rack de 42U sea suficiente**.

## 8. Entregables obligatorios y orden acelerado

1. **Imagen exterior:** tres edificios, tres enlaces, rutas, ductos, cajas/registro, longitudes conocidas y variables identificadas; no maquillar x/y como mediciones.
2. **Planta típica A** y **planta típica B**: recintos, TR, rutas y cantidad de laboratorios.
3. **Laboratorio típico A** y **laboratorio típico B**: 16 áreas dobles, tomas RJ45, rutas y bajantes.
4. **ER A**, **TR A**, **ER B**, **TR B**: llegada/salida de backbone, rack, patch panels, pigtails, patch cords y equipos compatibles.
5. **Excel obligatorio** a partir de copia de `06_excel/Plantilla Actividades de comprobación.xlsx`, sin modificar original, sin precios, con fórmulas verificables; hoja de herramientas ligada al método elegido.
6. **Defensa ≥8 minutos:** recorrido del diseño, cómo se llegó a las cantidades, fuentes, fórmulas, reserva y decisiones.

**Condición crítica:** las nueve imágenes finales deben representar el **mismo diseño** y concordar con cada cantidad del Excel.

## 9. Bloqueos reales para cerrar cantidades

- Significado de «área doble».
- Ubicación final del TR/ER y geometría coherente de plano.
- `x` e `y` y verificación de los 145/50 m.
- Separación/cantidad real de cajas; ductos y sus diámetros disponibles.
- Referencias verificadas de cable exterior 24f, cable interior 12f, panel óptico, panel Cat6A, rack, ductos y accesorios.
- Longitudes horizontal/vertical representativas reproducibles.
- Tratamiento de celda J43 en la copia final sin introducir montos.

**Regla de ejecución:** no rehacer la auditoría de 76 requisitos. Pasar directamente a un plano tipo acotado y una hoja auxiliar de cálculo con entradas declaradas; marcar cualquier cantidad dependiente de una medida no disponible como provisional. No modificar `main`.
