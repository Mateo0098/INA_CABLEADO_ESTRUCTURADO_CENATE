# Auditoría estructural de la plantilla Excel

- **Archivo inspeccionado:** `06_excel/Plantilla Actividades de comprobación.xlsx`
- **Método:** lectura directa del contenido OOXML; el libro no fue abierto para edición ni guardado
- **SHA-256:** `707F1812D1DA9033A2792E51E0EBBFE63D202DEF6F6945236E0AB5D6028013F6`
- **Tamaño:** 15 866 bytes
- **Estado de procedencia:** aceptada como plantilla oficial operativa mediante F-005 §5 y confirmación del estudiante; original preservado

## Resumen del libro

- Dos hojas visibles: `Cotización técnica` y `Herramientas`.
- No hay hojas ocultas registradas.
- No hay protección de libro ni de hojas.
- No hay nombres definidos ni validaciones de datos.
- Se detectan 20 estilos de celda, 6 fuentes, 9 rellenos y 3 bordes.
- Existe un formato numérico personalizado para colones: `₡ #,##0`.

## Hoja `Cotización técnica`

- Rango declarado: `A1:K43`.
- Fila 1 congelada; panel activo desde `A2`.
- Celda combinada: `A43:I43`.
- Filas 2 a 41: 40 renglones didácticos precargados.
- No hay autofiltro ni validaciones de datos.
- No hay celdas protegidas.

### Columnas originales

| Columna | Encabezado original | Contenido observado | Tratamiento en la primera actividad |
|---|---|---|---|
| A | Material o equipo | Nombre del elemento | Completar en copia de trabajo con elementos calculados |
| B | Categoría o tipo | Clasificación técnica | Completar cuando aplique |
| C | Especificaciones técnicas | Descripción técnica | Debe ser clara, precisa, verificable e incluir características aplicables |
| D | Marca | Marcas rotuladas como ejemplo | No adoptar como selección del proyecto |
| E | Modelo o referencia | Referencias rotuladas como didácticas | No adoptar como referencia real |
| F | Unidad de medida | Unidad | Usar la unidad correspondiente al material o equipo |
| G | Cantidad | Cantidades didácticas precargadas | No usar como cantidades del proyecto |
| H | Proveedor | Proveedores rotulados como ejemplo | No adoptar como proveedor real |
| I | Precio unitario (₡) | Vacío en `I2:I41` | Debe permanecer vacío |
| J | Precio total (₡) | Vacío en `J2:J41`; `J43` contiene fórmula | Los precios deben permanecer vacíos; revisar la fórmula solo en copia de trabajo cuando haya instrucción oficial |
| K | Fuente | Vacío en `K2:K41` | Completar en fase de selección con enlace confiable y verificable |

### Fórmulas

| Celda | Fórmula | Valor almacenado |
|---|---|---:|
| `J43` | `SUM(J2:J41)` | 0 |

No se detectaron fórmulas de precio por renglón ni otras fórmulas.

### Contenido precargado

Las filas 2 a 41 contienen materiales, especificaciones, marcas identificadas como “ejemplo”, referencias didácticas, unidades, cantidades y proveedores de ejemplo. Ese contenido forma parte del archivo recibido; **no fue creado ni completado durante esta fase**. No está verificado contra el proyecto CENATE.

Riesgos principales:

- La fila de cable de fibra contiene una cantidad de ejemplo de 150, que no corresponde al recorrido preliminar contextual de 195 m y no debe reutilizarse.
- Las cantidades, racks, equipos y marcas de ejemplo no representan los dos edificios ni los tres enlaces requeridos.
- La presencia de ejemplos puede confundirse con un diseño aprobado si se edita directamente el original.

## Hoja `Herramientas`

- Rango declarado: `A1:B41`.
- Encabezados: `Herramientas` y `Cantidad`.
- Solo las dos celdas de encabezado contienen valores.
- No contiene fórmulas, protección, validaciones, celdas combinadas ni paneles congelados.

## Campos obligatorios

El archivo no contiene marcadores técnicos de obligatoriedad, comentarios, validaciones ni protección. F-005 §5.2 resuelve la duda documental: deben completarse **todos los campos aplicables** con información clara, precisa y técnicamente fundamentada. Marca, modelo, especificaciones y fuente deben permitir verificar el producto; los campos no aplicables deberán tratarse de forma consistente y justificable, sin alterar columnas.

## Compatibilidad con las instrucciones oficiales

| Exigencia F-005 | Compatibilidad observada | Control futuro |
|---|---|---|
| Materiales y equipos | Hoja `Cotización técnica`, columnas A–K | Sustituir ejemplos únicamente en copia de trabajo |
| Herramientas | Hoja `Herramientas`, columnas A–B | Agregar filas necesarias sin alterar encabezados |
| Conservar columnas, orden, colores y formatos | La estructura está definida y respaldada por hash | Comparar copia final contra original |
| Agregar filas | Compatible con el formato existente | Replicar estilos y fórmulas según corresponda |
| Fórmulas automáticas | Las celdas aceptan fórmulas; solo existe `J43` en el original | Incorporar en copia de trabajo las fórmulas técnicas necesarias y probar recálculo |
| Fuentes verificables | Columna K `Fuente` | Completar con enlaces permitidos y actuales |
| Sin precios en Actividad 1 | `I2:J41` están vacías | Mantenerlas sin montos |

La plantilla es estructuralmente compatible con F-005. No contiene fórmulas de cantidades ya preparadas, por lo que su desarrollo corresponde a la futura copia de trabajo y deberá ser realizado y comprendido por el estudiante, sin generación automática por IA.

### Ambigüedad económica controlada

F-005 §5.4 ordena que las columnas económicas permanezcan vacías. El original, sin embargo, incluye el rótulo de total y `J43=SUM(J2:J41)` con resultado almacenado 0. Como F-005 §5.1 también prohíbe modificar la estructura original, no se altera F-002. En la copia de entrega se mantendrán `I2:J[n]` sin montos; antes de finalizar deberá confirmarse con el docente si la fórmula preexistente de `J43` debe conservarse intacta o dejarse sin fórmula. Esta ambigüedad no autoriza introducir precios.

## Restricciones de preservación

1. No editar ni guardar el archivo original controlado.
2. Verificar su SHA-256 antes y después de cualquier traslado.
3. Crear una copia de trabajo con nombre y versión diferentes cuando se autorice la siguiente fase.
4. No eliminar, renombrar o reordenar hojas, columnas o encabezados; conservar colores, formatos y demás elementos originales.
5. Mantener vacíos los campos económicos durante la primera actividad.
6. No tratar el contenido didáctico precargado como cantidades, materiales o productos seleccionados.
7. Solo se permite agregar filas necesarias; las columnas auxiliares temporales deben eliminarse antes de entregar.
8. Conservar fórmulas técnicas funcionales en la copia final y poder demostrarlas durante la defensa.
