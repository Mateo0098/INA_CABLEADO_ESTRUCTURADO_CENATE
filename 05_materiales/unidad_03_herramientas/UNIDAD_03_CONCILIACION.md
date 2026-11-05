# Unidad 03 — conciliación funcional, kits y alternativas

Fecha: 2026-11-04. Elaboración asistida por Codex; revisión humana pendiente. Esta tabla concilia necesidades expresas y filas de la matriz; no inventa nombres de una lista histórica nominal de 94 referencias que no fue suministrada. Los conteos iniciales 22/18/24/30 son entradas conceptuales del encargo, no criterio para eliminar funciones.

## Conteos y trazabilidad

| Origen | Referencias conceptuales declaradas | Filas funcionales depuradas | Diferencia | Motivo verificable |
|---|---:|---:|---:|---|
| 03A | 22 | 26 | +4 | Separación de brocas por sustrato, limpieza, medios de acceso y trazado; no son 26 compras definitivas |
| 03B | 18 | 22 | +4 | Desglose del sistema de certificación, consumibles, calificación opcional y alternativa de servicio |
| 03C | 24 | 30 | +6 | Cubiertas 12F/24F diferenciadas, controles U02 y servicios de fusión/pérdida/OTDR; no 30 kits adicionales |
| 03D | 30 | 30 | 0 | Necesidades de seguridad y operación preservadas; portátil común anclada en 03B, otros recursos detallados |
| Total | 94 | 108 | +14 | Conteo de filas funcionales: incluye componentes condicionados y alternativas que no se suman como compra |

La tabla siguiente enlaza todas las filas con grupos funcionales del encargo. Cada fila CSV conserva origen; cuando un recurso se comparte, su campo de duplicación y esta tabla conservan los usuarios adicionales. No existe correspondencia uno a uno demostrable con las 94 referencias sin sus nombres originales.

| Necesidad conceptual cubierta | Filas U03 (prefijo U03-) | Tratamiento |
|---|---|---|
| Corte de rejilla, bordes, varilla y sujeción | 03A-001 a 004 | Funciones distintas; no reemplazar cortadora de canasta por cortapernos universal |
| Perforación, limpieza, anclajes y apriete | 03A-005 a 014 | Brocas por sustrato; extracción, cepillo y soplado condicionados; torque independiente |
| Conduit, medición y trazado | 03A-015 a 020; 03A-026 | Escariador PVC distinto de limado metálico; plomada sustituible por función láser solo con verificación |
| Tendido, bobinas, detección y acceso | 03A-021 a 025 | Dos soportes como par funcional; escalera/plataforma/andamio según tarea |
| Preparación y terminación jack/panel | 03B-001 a 006 | Pelado/corte compartibles por técnico; EGJT-1 y PDT110 son distintos |
| Continuidad, localización, calificación | 03B-007 a 009 | No sustituyen certificación; calificador opcional según diagnóstico |
| Certificación, bases y adaptadores | 03B-010 a 016 | Sistema y componentes con regla de descuento de kit; canal no reemplaza permanente |
| Software, registro y etiquetado | 03B-017 a 021 | Portátil común para 03B/03C/03D; etiquetas ya U02; ribbon separado |
| Certificación contratada | 03B-022 | Alternativa excluyente a ejecución propia del mismo alcance |
| Fusión y preparación de fibra | 03C-001 a 012 | Equipo, útiles, repuestos, energía, mesa y residuos separados; revisar kit |
| Inspección de conectores | 03C-013/014 | Sonda y puntas LC/UPC compatibles; no sumarlas si kit las contiene |
| Fuente, potencia y OLTS | 03C-015 a 017 | Fuente+medidor alternativos al OLTS; no sumar las tres compras completas |
| OTDR, lanzamiento y recepción | 03C-018 a 020 | Diagnóstico independiente de OLTS; dos bobinas cumplen extremos diferentes |
| Referencia, acoplamiento, VFL, análisis y limpieza | 03C-021 a 026 | VFL/software descontables si integrados; limpieza consumible permanece U02 |
| Protección de empalmes | 03C-027 | Cero compra adicional U03 condicionado al kit U02; no 408 mangas extra |
| Servicios de fibra | 03C-028 a 030 | Fusión, pérdida y eventos son prestaciones distintas; alternativa por operación |
| EPP individual y accesorios | 03D-001 a 011 | Sin cantidades cerradas; revisar exposición, talla, compatibilidad y reposición |
| Seguridad de área y emergencia | 03D-012 a 017 | No duplicar recursos institucionales; LOTO no autoriza trabajo energizado |
| Comprobaciones eléctricas y ambiente | 03D-018 a 021 | Instrumentos distintos; ausencia de tensión requiere método autorizado |
| Administración, diagnóstico, respaldo e iluminación | 03D-022 a 026 y portátil 03B-018 | Uso secuencial compartido; procedimientos previstos, no resultados físicos |
| Limpieza general, filtros, repuestos y residuos | 03D-027 a 030 | Consumos separados de reutilizables y de limpieza óptica U02 |

## Regla de kits y exclusiones de compra

| Grupo | Compra/uso que se compara | Componentes o duplicación condicionada |
|---|---|---|
| Jacks TG U02-02B-026 | Empaque exacto CJ6X88TGBU individual o variante a cotizar | EGJT-1 incluida en -24/-C según plano Panduit; descontar antes de comprar 03B-004 |
| Sistema DSX 03B-010 | Un sistema propio, alquilado o institucional | Principal -011, remoto -012, par permanente -013, canal -014, batería -015 y cargador -016 se revisan contra lista de empaque; no compras adicionales automáticas |
| Certificación de cobre | Equipo propio/alquilado + operador O servicio -022 | No cobrar presupuestariamente dos veces los mismos 1984 enlaces; repetición R_cu separada |
| Fusionadora 03C-001 | Compra, alquiler, existente o servicio -028 | Cleaver -002, sujetadores -007, batería -009 y cargador -010 podrían estar incluidos; verificar |
| Abridores de cubiertas | 03C-004 y -005 | Compartir un útil solo si ficha prueba compatibilidad con ambas construcciones; no eliminar función por similitud |
| Medición óptica | OLTS -017 O pareja fuente -015 + medidor -016; servicio -029 alternativo | No comprar fuente/medidor adicionales por funciones integradas; OLTS y OTDR no son alternativas funcionales equivalentes |
| OTDR 03C-018 | Compra, alquiler, existente o servicio -030 | Lanzamiento -019 y recepción -020 se verifican contra kit; no son la misma función |
| Sonda/VFL/software | 03C-013/014, -023/024 y 03B-017 | Verificar inclusión y licencia; compartir base Versiv solo con generación compatible y agenda sin simultaneidad |
| Portátil y diagnóstico | 03B-018; usuarios 03C y 03D | Una portátil común; 03D-023 no es una segunda computadora ni un nuevo certificador |
| Acceso elevado | 03A-024/025; EPP 03D-011 | Alternativas por tarea y evaluación; protección contra caídas no se elimina por alquilar plataforma |
| Dotación existente | Todas las filas reutilizables | Ninguna existencia institucional se presume; inventariar aptitud y agenda |

## Interfaz con Unidad 02 intacta

| Necesidad | Referencia única de materiales | Tratamiento U03 |
|---|---|---|
| Etiquetas de toma/cable/cassette | U02-02B-027/028; U02-02D-021/022 | 03B-020 conserva necesidad con 0 adicional; impresora y ribbon sí se revisan aparte |
| Limpieza óptica consumible | U02-02D-023 | 03C-026 registra 0 adicional; útiles reutilizables -025 solo porción no consumible no incluida |
| Protectores de fusión | U02-02D-006/007/028 | 03C-027 registra 0 adicional condicionado; confirmar especialmente kit 24F |
| Adhesivo PVC y lubricante de tiro | U02-02B-016/017 | No crear otra compra U03; consumo se resuelve con método/producto |
| Tornillos, tuercas, varillas, anclajes y perfiles | U02-02A; U02-02B; U02-02C según función | U03 aporta herramientas de instalación; no compra de nuevo esos materiales |
| Patch cords de fábrica y conectores permanentes | U02-02B/02C/02D | No conectores macho ni crimpadoras; cables de referencia U03 son instrumentos de prueba reutilizables distintos |
| Adaptadores LC integrados en cassette | U02-02D-027 | No confundir con acopladores de referencia U03-03C-022 |

**Resultado:** 108 filas no equivalen a 108 adquisiciones ni 108 unidades. No hay suma global válida de cantidades heterogéneas ni de filas alternativas. Aprobados método, kit y simultaneidad, la Unidad 04 podrá construir escenarios de compra neta y servicios, conservando las exclusiones. No se corrigió ni se reescribió la matriz de Unidad 02.
