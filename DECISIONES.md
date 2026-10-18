# Registro de decisiones, supuestos y cuestiones pendientes

**Última actualización:** 2026-10-18
**Etapa:** inicialización del proyecto

## D-001 — Identidad y alcance académico

- **Clasificación:** dato establecido por el docente.
- **Registro:** proyecto del módulo ELTT12000 — Presupuesto de la red, Actividad de Comprobación N.º 1.
- **Entrega:** 2026-10-29.
- **Alcance:** infraestructura física de telecomunicaciones de dos edificios nuevos del complejo CENATE del INA.
- **Exclusión:** contratación y prestación del servicio ISP.
- **Fuente:** instrucciones proporcionadas por el usuario para la inicialización, 2026-10-18.

## D-002 — Programa funcional de los edificios

| Elemento | Edificio A | Edificio B | Clasificación |
|---|---:|---:|---|
| Pisos | 4 | 7 | Dato establecido por el docente |
| Laboratorios por piso | 5 | 6 | Dato establecido por el docente |
| Área por laboratorio | 85 m² | 75 m² | Dato establecido por el docente |
| Áreas de trabajo dobles por laboratorio | Mínimo 16 | Mínimo 16 | Dato establecido por el docente |
| TR | Al menos 1 por piso | Al menos 1 por piso | Dato establecido por el docente |
| ER | 1 propio | 1 propio | Dato establecido por el docente |

No se derivan en esta etapa cantidades de salidas, cables, racks, puertos ni equipos.

## D-003 — Configuración arquitectónica preliminar

| Parámetro | Valor preliminar | Clasificación |
|---|---:|---|
| Geometría de laboratorio A | 10 × 8,5 m | Supuesto de diseño |
| Geometría de laboratorio B | 10 × 7,5 m | Supuesto de diseño |
| Forma de planta | Rectangular | Supuesto de diseño |
| Circulación | Pasillo central | Supuesto de diseño |
| Repetición | Pisos típicos idénticos dentro de cada edificio | Supuesto de diseño |
| Ubicación de ER | Planta baja | Supuesto de diseño |
| Alineación de TR | Vertical | Supuesto de diseño |
| Dimensión de TR | 3 × 3 m | Supuesto de diseño |
| Dimensión de ER | 4 × 4 m | Supuesto de diseño |
| Altura entre pisos | 3,5 m | Supuesto de diseño |
| Ancho del pasillo central | 2,4 m | Supuesto de diseño |

Estos valores no son mediciones de campo ni soluciones normativamente validadas.

## D-004 — Criterios iniciales del cableado interno

- **Dato establecido por el docente:** enlace permanente de cobre con máximo de 90 m.
- **Dato establecido por el docente:** topología horizontal en estrella.
- **Dato establecido por el docente:** backbone vertical desde cada ER hasta los TR.
- **Supuesto de diseño:** bandejas y derivaciones protegidas como canalización interior preliminar.
- **Decisión pendiente:** validar recorridos, ocupación, capacidad, protección, segregación y criterios aplicables antes del diseño definitivo.

## D-005 — Backbone exterior

- **Dato establecido por el docente:** existe un ER principal en un edificio del INA.
- **Dato establecido por el docente:** hay 145 m de canalización subterránea existente desde esa zona.
- **Dato establecido por el docente:** durante la clase se indicó una separación de referencia de 25 m entre cajas de telecomunicaciones. No se interpreta todavía como requisito normativo ni se calcula una cantidad.
- **Supuesto de diseño:** se propone un tramo adicional de 50 m de canalización subterránea nueva para alcanzar el ER de uno de los edificios nuevos.
- **Resultado aritmético preliminar:** 145 m existentes + 50 m nuevos = 195 m de recorrido físico preliminar hasta ese ER. Este resultado no sustituye un levantamiento de campo.
- **Dato establecido por el docente:** se requieren los enlaces ER principal–ER A, ER principal–ER B y ER A–ER B.
- **Decisiones pendientes:** identificar cuál edificio recibe los 50 m nuevos; levantar y aprobar los otros recorridos; verificar trazados, longitudes, cajas, ductos y condiciones de la infraestructura existente.

## D-006 — Imágenes técnicas requeridas

Se registran como **dato establecido por el docente** nueve imágenes mínimas futuras:

1. Infraestructura exterior de los tres edificios.
2. Planta típica del edificio A.
3. Planta típica del edificio B.
4. Laboratorio representativo del edificio A.
5. Laboratorio representativo del edificio B.
6. ER del edificio A.
7. TR del edificio A.
8. ER del edificio B.
9. TR del edificio B.

Las imágenes de ER y TR deberán representar, según corresponda, racks, equipos y accesorios, terminaciones ópticas, patch cords, pigtails y canalizaciones. Su contenido deberá corresponder con cálculos y materiales aprobados; por ello no se generan en esta etapa.

## D-007 — Control documental

- **Decisión de gestión:** conservar originales, fuentes y evidencia; realizar cambios mediante ramas y commits acotados.
- **Dato establecido por el docente:** la plantilla Excel original del INA debe conservar estructura y formato; la primera actividad no debe incluir precios ni costos.
- **Decisión de gestión:** registrar la asistencia de IA y requerir revisión humana del contenido técnico.
- **Decisión de gestión:** no adoptar marcas, modelos, normas ni especificaciones sin una fuente verificable.

## Mediciones de campo

No se han incorporado mediciones de campo en esta etapa.

## Especificaciones verificadas de fabricante

No se han incorporado especificaciones de fabricante en esta etapa.

## Historial de cambios de decisión

| Fecha | ID | Cambio | Motivo / evidencia | Impacto |
|---|---|---|---|---|
| 2026-10-18 | D-001 a D-007 | Registro inicial | Instrucciones de inicialización del usuario | Base documental; sin diseño definitivo |
