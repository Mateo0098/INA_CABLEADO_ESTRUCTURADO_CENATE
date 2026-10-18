# Arquitectura conceptual del cableado CENATE

**Estado: propuesta de conversación, NO ingeniería detallada aprobada.** Este documento transmite las alternativas discutidas con el estudiante a Codex para su revisión y desarrollo. Las fuentes vinculantes están en `01_requisitos/`.

## 1. Topología requerida

Tres enlaces interedificios de fibra óptica:

1. ER principal existente ↔ ER A.
2. ER principal existente ↔ ER B.
3. ER A ↔ ER B.

Esquema lógico (no representa rutas físicas ni asignación de ductos):

```text
             ER PRINCIPAL (INA, edificio existente)
                /                        \
          enlace 1                     enlace 2
              /                            \
          ER A --------- enlace 3 -------- ER B
            |                               |
       Backbone vertical               Backbone vertical
            |                               |
       TR por piso                     TR por piso
            |                               |
       Cableado horizontal             Cableado horizontal
       a laboratorios                  a laboratorios
```

Propuesta de distribución: ER por edificio, en planta baja, y por lo menos un TR por piso, procurando alinear los TR. El enunciado permite o exige TR adicionales según alcance horizontal; NO asumir que uno por piso siempre es suficiente.

## 2. Exterior y relaciones con el ISP

Se documentó un tramo existente de **145 m** de canalización subterránea desde el edificio del ER principal hacia la zona del patio posterior; se propone extender **50 m de nueva canalización subterránea** hasta el ER de **uno de los edificios**, aún sin identificar. Cajas separadas aproximadamente 25 m, según lo explicado en clase.

El INA ya dispone del ISP; no contratar, cotizar ni instalar el servicio de un ISP. Diferenciar recinto de entrada de servicio (EF) del ER principal cuando corresponda. La posibilidad de reutilizar ductos existentes depende de verificación de capacidad y estado.

Los tres enlaces requeridos son **distintos lógicamente**, pero pueden compartir parte del recorrido físico si se justifica y dimensiona su capacidad. No asumir tres ductos independientes ni que 195 m se replican tres veces.

## 3. Planta de piso y laboratorio

- A: 5 laboratorios de 85 m² por piso, propuesta de tres de un lado y dos del otro, con corredor central; el espacio restante para TR y áreas comunes requiere justificación arquitectónica.
- B: 6 laboratorios de 75 m² por piso, propuesta de tres a cada lado de corredor central.
- Un piso típico por edificio únicamente si todos los pisos son iguales.
- Laboratorios de estudio A: 10 x 8,5 m; B: 10 x 7,5 m.
- Se propusieron 16 áreas de trabajo dobles por laboratorio distribuidas en dos grupos de ocho; la definición exacta del puesto doble, dimensiones del mobiliario, puertas, circulación y accesibilidad siguen pendientes.
- Cobre horizontal en estrella: cada puerto de salida hasta su correspondiente terminación en el TR; máximo 90 m para enlace permanente. Los cables individuales pueden compartir canalizaciones correctamente dimensionadas.
- Posible bandeja aérea en pasillo y ramificaciones/bajantes protegidas; pendiente de comprobar altura, compatibilidad y rutas.

## 4. Representación funcional de ER

Las dos imágenes ER (una para A y otra para B) deben representar:

- Entrada de backbone desde ER principal.
- Enlace interedificios entre ER A y ER B.
- Salida de backbone vertical hacia TR del edificio.
- Rack y accesorios, sistema de terminación/distribución óptica, pigtails, adaptadores, patch cords ópticos, organizadores y canalizaciones.
- Equipos activos solo si la selección está justificada; no inventar puertos, switches ni funciones.

La interfaz exacta entre cable de fibra, empalmes/pigtails, paneles/adaptadores, latiguillos y equipos debe tener continuidad técnica y material.

## 5. Representación funcional de TR

Una imagen representativa por edificio debe mostrar:

- Llegada del backbone desde ER local.
- Rack, equipo/accesorios y terminaciones ópticas correspondientes.
- Patch panels de cobre y patch cords UTP cuando proceda.
- Canalización horizontal hacia cinco laboratorios en A o seis en B.
- Elementos y conexiones respaldados en fichas técnicas y el Excel.

## 6. Inventario conceptual (sin cantidades ni marcas)

**ER:** rack de piso/gabinete, ODF o panel de fibra, bandejas de empalme, pigtails, adaptadores, patch cords, organizadores, entrada de ducto, backbone vertical, soportes y accesorios.

**TR:** rack/gabinete, terminación óptica, pigtails/adaptadores si el método elegido los requiere, patch cords ópticos, patch panels RJ45, organizadores, patch cords UTP, canalizaciones horizontales y equipos activos si se justifican.

Las dimensiones de rack, selección OS2/OM3/etc., conectores, equipos y cantidad de fibras siguen abiertas. No dibujar accesorios contradictorios con el método real de terminación.

## 7. Imágenes esperadas

Mínimo nueve si los pisos y laboratorios son idénticos:

1. Exterior de tres edificios con tres enlaces y distancias.
2. Planta típica A.
3. Planta típica B.
4. Laboratorio típico A.
5. Laboratorio típico B.
6. ER A.
7. TR A.
8. ER B.
9. TR B.

Todo lo representado debe coincidir con cantidades y características del Excel. Puede requerirse más de una vista para detalles legibles.

## 8. Datos que NO están resueltos

Rutas físicas de los enlaces 2 y 3, edificio receptor de 50 m, ductos/cajas, distancias verticales y horizontales, geometría real de piso, áreas de trabajo, cable/fibras/terminaciones, equipos, capacidades de racks, porcentajes de reserva, selección de fabricantes y cantidades definitivas.

Codex debe confrontar este documento con las fuentes oficiales y conservar las discrepancias hasta que sean resueltas.
