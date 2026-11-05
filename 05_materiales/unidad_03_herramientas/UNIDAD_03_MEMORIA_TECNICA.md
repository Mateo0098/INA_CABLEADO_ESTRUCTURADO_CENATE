# Unidad 03 — memoria técnica de herramientas y pruebas previstas

Fecha: 2026-11-04. Responsable documental: Codex, asistencia de IA. **Revisión técnica y académica humana pendiente** por el estudiante y responsables de instalación, seguridad y TI. La IA no es fuente técnica. Este inventario prepara la Unidad 04; no contiene precios, órdenes de compra ni certificación ejecutada. No se realizaron mediciones, pruebas físicas ni modificaciones de infraestructura.

## Entradas y clasificación

| Entrada con unidad | Clasificación | Fundamento |
|---|---|---|
| 20 + 42 = 62 laboratorios; mínimo 16 áreas dobles/laboratorio | Datos docentes y suma calculada | `03_diseno/UNIDAD_01_ARQUITECTURA_RED_ACTIVA.md`, tabla de requisitos |
| 62 × 16 = 992 áreas; 992 × 2 = 1984 enlaces permanentes Cat 6A | Resultado condicionado al supuesto de dos RJ45/área doble | Confirmación docente pendiente; no medición |
| 11 TR, dos ER nuevos; 11 + 2 = 13 racks propuestos | Escenario de un TR/piso y resultado de diseño | Unidad 01 y memoria de Unidad 02 |
| Tres enlaces exteriores OS2 24F y once verticales OS2 12F | Supuesto de diseño de capacidad | `05_materiales/unidad_02_ampliacion/UNIDAD_02_MEMORIA_DE_CANTIDADES.md` |
| 11 × 12 + 3 × 24 = 204 fibras físicas; hasta 204 × 2 = 408 fusiones | Resultado calculado del escenario, sin medición | Terminación de todas las fibras en ambos extremos |
| 14 circuitos dúplex activos iniciales, usando 28 fibras | Hipótesis de activación calculada | No significa 204 enlaces independientes ni 204 circuitos activos |
| 44 switches base / 51 ampliado | Alternativas calculadas, no acumulables | Unidad 01; no modificar su diseño en esta intervención |
| C=1 frente de trabajo secuencial; T=2 técnicos de cobre | Supuesto de planificación para comparar recursos | No determina dotación total de obra, plazo ni seguridad |
| Herramientas y kits específicos Panduit/Fluke citados abajo | Especificaciones de fabricante verificadas documentalmente en el alcance indicado | Consulta 2026-11-04; modelo final, kit y adquisición pendientes |

No se aportan mediciones de campo. Las fórmulas son escenarios reproducibles para revisión, no cantidades previstas convertidas en mediciones. Fuentes internas examinadas: `AGENTS.md`, `README.md`, `DECISIONES.md`, `PENDIENTES.md`, `09_auditorias/ULTIMO_REPORTE_CODEX.md`, reporte Unidad 02 indicado por ese índice, matriz CSV/memoria/pendientes Unidad 02, matriz histórica Fase 2D y arquitectura Unidad 01. El commit remoto `fe13277` incorporó únicamente el Gantt complementario y sus registros antes de esta etapa; no se usa su duración como productividad demostrada.

## Dimensionamiento reproducible

Ejecutar `python 05_materiales/unidad_03_herramientas/generar_matriz.py`. El generador conserva entradas, unidades, criterios y fuentes por fila. Las cantidades con `REFERENCIA` expresan dotación funcional de escenario, **no compra neta**. `PENDIENTE` significa desconocido; `0 ADICIONAL U03` conserva una necesidad comprada en U02; `No aplica, con justificación` excluye únicamente esa compra adicional, no la función. No se deja una celda vacía para representar cero.

Para recurso reutilizable por frente: `necesidad = dotación × C_simultáneos`. Para útil personal de terminación: `necesidad = dotación × T_simultáneos`. Compra neta por referencia compatible: `max(0; necesidad − existentes aptos − incluidos en kits)`. No descontar equipo existente sin inventario, condición, disponibilidad de agenda y calibración cuando corresponda. No sumar sistemas completos y sus subcomponentes: las filas desglosadas sirven para revisar la lista de empaque.

Los soportes de bobina representan dos unidades de apoyo para un sistema funcional, no dos pares comerciales; confirmar eje, freno, masa y presentación. Certificador, fusionadora, OLTS y OTDR se modelan como una estación de especialidad usada secuencialmente, sin multiplicarlos por 1984 enlaces, 204 fibras ni 13 racks. Si actividades coinciden, revisar agenda o agregar dotación explícita. Una sola portátil atiende 03B/03C/03D de forma secuencial; su respaldo de resultados y configuraciones son funciones distintas, con permisos diferentes. Etiquetadora, instrumentos ambientales e iluminación también pueden compartirse; EPP de asignación individual y candados LOTO se rigen por el procedimiento, no se reparten como una herramienta común.

Consumos: `techo(consumo requerido / rendimiento de empaque)` tras aprobar producto, exposición, jornada y reposición. La matriz separa electrodos, filtros, cinta de transferencia, limpieza y repuestos. Los filtros del extractor y del respirador requieren referencias comerciales distintas cuando se elijan los equipos; la fila funcional no autoriza un filtro universal. Las brocas SDS-Plus se tratarán como útiles de desgaste de inventario, con diámetro y cantidad pendientes, separadas de brocas para metal/otros sustratos. No convertir un juego genérico en surtido comprado sin despiece.

## 03A — instalación mecánica prevista

Secuencia propuesta: verificar servicios ocultos y sustrato, aprobar soporte/anclaje, trazar y nivelar, sujetar piezas, cortar, eliminar rebabas y tratar acabado si fabricante lo exige, perforar con control de polvo, limpiar según anclaje, montar y apretar según ficha; verificar bordes y ruta antes del tendido. La cortadora de rejilla necesita aprobación para la familia, diámetro de alambre y acabado elegidos. Una cortadora de pernos convencional no queda aceptada para cualquier canasta. No se adopta sección troncal 100×50 mm: Unidad 02 mantiene ese bloqueo.

Anclaje y concreto determinan diámetro, profundidad, limpieza, herramienta de instalación y torque; no hay selección de broca ni valor N·m definitivo. Extractor y cepillos/soplador no se sustituyen entre sí sin aprobación del fabricante del anclaje. La llave dinamométrica necesita rango y calibración adecuados; el atornillador no acredita torque final. PVC: cortar perpendicularmente, escariar y montar conforme al producto aprobado; adhesivo/lubricante permanecen en U02. Tendido: radios y esfuerzos máximos se toman del cable exacto, con bobinas controladas; no se especifica fuerza ficticia. Escalera, andamio y plataforma son alternativas por tarea; no comprar los tres automáticamente.

## 03B — terminación y certificación de cobre previstas

**Jack:** el candidato Mini-Com `CJ6X88TGBU` pertenece a `CJ6X88TG**`. Las instrucciones [PN511G-SPA, ©2022](https://www.panduit.com/content/dam/panduit/en/products/media/9/29/729/4729/110934729.pdf), tres páginas, muestran CJAST, CWST y EGJT-1. Aplicar preparación correspondiente al cable real MaTriX/no MaTriX; no extrapolar el ajuste a cualquier cable. La herramienta EGJT-1 cierra el conjunto TG, no es una crimpadora de RJ45 macho ni herramienta de impacto 110.

El [plano Panduit 01874-40](https://www.panduit.com/content/dam/panduit/en/products/media/0/50/950/5950/106655950.pdf) identifica el sufijo BU y distingue empaques: individual sin EGJT-1; -24 y -C con herramienta por empaque según su tabla. Confirmar revisión y SKU cotizado antes de restar esas herramientas. La compra no puede ser automáticamente dos EGJT-1 más todas las incluidas.

**Panel:** el candidato NetKey `NK6XPPG48Y` es punchdown, 48 puertos, 2U, conforme al [catálogo Panduit de paneles](https://www.panduit.com/content/dam/panduit/en/products/media/8/78/678/0678/61760678.pdf). Las instrucciones [NK410E, ©2017](https://www.panduit.com/content/dam/panduit/en/products/media/5/15/015/5015/102005015.pdf), dos páginas, incluyen ese modelo y muestran PDT110. Seguir posición de corte, alivio, esquema T568A/B aprobado y límite de destrenzado del manual. Mantener métodos y útiles de retrabajo separados por conector. Preparar una terminación piloto para aprobación humana antes de producción; **no ejecutada**. Los 1984 enlaces implican 1984 extremos jack y 1984 posiciones de panel terminadas en este escenario; no 3968 jacks nuevos. Los patch cords de fábrica de U02 no necesitan conectores macho ni crimpadora.

| Nivel de prueba | Propósito | Límite |
|---|---|---|
| Verificación | Mapa de hilos/continuidad y localización | No demuestra ancho de banda ni cumplimiento Cat 6A |
| Calificación | Estimar capacidad para una aplicación con equipo apropiado | No sustituye certificación normativa |
| Certificación | Comparar parámetros del enlace con límite Cat 6A/Class EA aprobado | Exige instrumento, adaptadores, calibración, configuración y registro adecuados |

El [DSX CableAnalyzer, ficha de familia sin revisión visible en página](https://www.flukenetworks.com/edocs/datasheet-dsx-8000-cableanalyzer) confirma que DSX2-5000 cubre Cat 6A. Es candidato, no adjudicación. La [lista oficial de accesorios](https://www.flukenetworks.com/edocs/industrial-ethernet-cableanalyzer-kit) identifica DSX-PLA004S para enlace permanente y DSX-CHA004S para canal, además de batería/cargador. Se verifica compatibilidad documental, no que estén todos incluidos en cualquier kit DSX2-5000. No sustituir los adaptadores permanentes por los de canal para aceptar 1984 enlaces permanentes.

Procedimiento previsto: aprobar norma/edición y límite, cable y NVP, mapa de IDs, calibración, estado de adaptadores y referencia del instrumento según manual; ejecutar autotest por enlace y conservar parámetros/gráficas/resultado; diagnosticar y corregir fallas, repetir conservando trazabilidad, exportar archivos nativos y reporte. Wiremap, longitud, pérdida de inserción, NEXT/PSNEXT, ACR y retorno se revisan dentro del conjunto exigido por el límite seleccionado; criterios adicionales de diafonía exógena o desequilibrio quedan pendientes del procedimiento aprobado, sin inventar muestreo ni umbrales. `N_ejecuciones = 1984 + R_cu`, con R_cu desconocido. Los tiempos nominales de autotest no equivalen a jornada productiva: faltan desplazamiento, conexión, registro, retrabajo y entrega. Software LinkWare PC es candidato; registrar versión, licencia y condiciones de nube separadas.

## 03C — fusión, pérdida y eventos previstos

Fusión: preparar cubierta según cable 12F/24F real, retirar recubrimiento, limpiar, cortar con cleaver, fusionar con parámetros aprobados, proteger con mangas del cassette y alojar respetando radio. Registrar fibra, extremo, cassette y empalme. La estimación de pérdida de la fusionadora no es aceptación OLTS. Hasta `204 × 2 = 408 fusiones`; retrabajo `R_fus` aparte. Cleaver, sujetadores, batería y cargador podrían venir en kit: las filas son componentes condicionados, sin compra adicional automática. Electrodos y cuchilla de cleaver son desgaste diferente de protectores de empalme.

Pérdida: inspeccionar-limpiar-inspeccionar conectores, comprobar fibra sin servicio óptico, establecer referencia según método aprobado y cordones de calidad de referencia, medir OS2 a 1310/1550 nm y contrastar presupuesto/límite aprobado. El [CertiFiber Pro OLTS](https://www.flukenetworks.com/content/datasheet-certifiber-pro-optical-loss-test-set-0), ficha web sin revisión visible, confirma esas longitudes en módulos monomodo. Modelo de kit exacto pendiente; no se adjudica variante multimodo por similitud de nombre. Fuente y medidor quedan como funciones dentro del OLTS o pareja alternativa; no se compran otra vez si el OLTS las cubre.

Escenario: `204 fibras × 2 longitudes × 1 sentido = 408 resultados de pérdida`, sin equivaler a 408 botones TEST ni a 408 fusiones. Si se exige bidireccional: `204 × 2 × 2 = 816 resultados`, antes de `R_opt`. Cantidad final depende de fibras incluidas, referencia y sentidos aprobados. Se cuentan fibras de reserva si el alcance aprobado exige todas; 14 circuitos activos no limitan automáticamente el alcance a 28 fibras.

OTDR: diagnóstico de distancia, conectores, empalmes y otros eventos; registrar índice, rango, pulso, umbrales, longitudes y sentidos. Bobina de lanzamiento y de recepción permiten evaluar extremos; longitud se determina con zona muerta/resolución del equipo, sin seleccionar 100 m arbitrariamente. `N_trazas = N_fibras_OTDR × N_longitudes × N_sentidos + R_trazas`, aún pendiente. El fabricante distingue [OLTS y OTDR](https://regression.flukenetworks.com/edocs/olts-otdr-complete-testing-strategy): OTDR no sustituye pérdida directa OLTS. Esta página es fuente técnica del fabricante, no norma de aceptación. Puntas de inspección LC/UPC y acopladores de prueba deben coincidir con sonda/instrumento; no confundirlos con adaptadores permanentes integrados de U02.

## 03D — seguridad y puesta en servicio previstas

Las filas de EPP permanecen sin cantidad hasta evaluar tarea, exposición, usuarios y requisitos institucionales: `dotación × personas expuestas + reposición − existentes aptos`. Cascos, lentes, careta, guantes, calzado, protección auditiva/respiratoria y accesorios requieren compatibilidad conjunta. No se fijan niveles de protección, filtros ni certificaciones de producto sin evaluación y ficha. Trabajo en altura requiere método de acceso, estructura, anclaje, formación y rescate aprobados; un arnés aislado no forma un sistema completo. El inventario es una lista de necesidades para revisión, no un procedimiento autorizado de trabajo seguro.

Delimitar áreas según tránsito y operación. LOTO y candados requieren procedimiento institucional y personal autorizado; botiquín y recursos de emergencia solo se agregan si la cobertura institucional resulta insuficiente. Multímetro, puntas y detector se seleccionan según tensión/categoría y procedimiento por responsable eléctrico competente. **El detector sin contacto no demuestra ausencia de tensión.** No se asignan trabajos energizados a la cuadrilla ordinaria de telecomunicaciones ni se autoriza intervenir circuitos reales. Termohigrómetro registra °C/%HR según ubicación, horario y requisitos de equipos; no se inventan rangos aceptables.

Puesta en servicio prevista en entorno de prueba autorizado: inventariar firmware/puertos de equipos y ER principal; respaldar configuración inicial; comprobar consola, interfaces, VLAN y aislamiento; verificar DAC/SFP+, niveles ópticos y contadores; revisar gateways, OSPF o alternativa, anuncios y rutas de retorno; ensayar fallas E1/E2/E3 y recuperación contra tiempos de aceptación aún pendientes; restaurar respaldo en entorno aprobado y registrar resultado. Alcance: 44 o 51 switches y dos distribuidores candidatos según Unidad 01. Definir IP/VLAN/permisos y plan de retorno antes de ejecutar. **Ninguno de esos ensayos se ha realizado** y no se modificó infraestructura INA. Portátil, cables de consola, software, repositorio de respaldo e iluminación son recursos diferenciados; las credenciales/configuraciones reales no se incorporarán al repositorio académico.

## Adquisición y evidencia nacional

| Recurso | Escenarios comparables para Unidad 04 | Evidencia que falta |
|---|---|---|
| Mecánica y útiles comunes | Existentes aptos / compra / alquiler por jornada | Inventario, productividad y agenda; modelo/kit |
| Fusionadora, DSX, OLTS, OTDR | Compra / alquiler / servicio especializado / existentes aptos | Oferta nacional, disponibilidad de alquiler, operador, calibración, accesorios, soporte y entregables |
| EPP y consumibles | Compra o dotación institucional; reposición por uso | Asignación individual, evaluación de riesgo y presentación |
| Certificación/fusión contratadas | Servicio alternativo a ejecución con equipo propio | Alcance por unidad, archivos, repetición de fallas, responsabilidad y aceptación |

No se confirma alquiler nacional ni se inventan tarifas. Comparación futura: alcance equivalente, plazo, traslados, formación, calibración, accesorios, mantenimiento, repeticiones y propiedad de archivos; reservar costo de importación para Unidad 04.

Consulta nacional 2026-11-04, responsable Codex: [ELVATRON, DSX](https://tiendacr.elvatron.com/products/certificador-de-cobre-dsx) y [colección de certificación](https://tiendacr.elvatron.com/collections/certificacion-de-cableado) publican familias DSX, CertiFiber y OptiFiber. La colección indica agotado; no acredita stock del SKU DSX2-5000 ni alquiler. [Fluke Networks](https://www.flukenetworks.com/content/south-america-contact-information) identifica ELVATRON como centro de servicio en Costa Rica, sin demostrar alcance de calibración para cada modelo. No se copiaron precios visibles. Para fusionadora y demás referencias sin oferta exacta comprobada se registra **pendiente de cotización nacional**; posible importación solo tras búsqueda nacional documentada. Capris, IESA, Electroega, EPA Costa Rica y ADIMATEC son canales propuestos de consulta, sin afirmar inventario ni atribuirles modelos. No se incorporan proveedores extranjeros como opción de compra seleccionada.

## Conciliación y límites

`UNIDAD_03_CONCILIACION.md` conserva cada función y señala componentes/alternativas. Referencias a U02 son IDs de su CSV intacto: etiquetas U02-02B-027/028 y U02-02D-021/022; limpieza U02-02D-023; protectores U02-02D-028 y cassettes -006/007; adhesivo U02-02B-016 y lubricante -017. Los recursos de prueba reutilizables no son patch cords de producción ni adaptadores permanentes del cassette. No duplicar velcro, fijaciones, anclajes, placas, paneles, conectores o cables ya registrados en U02. Tratamiento anticorrosivo de bordes, si requerido, se resolverá con accesorios de canalización U02 y ficha; no producto inventado.

Las cuatro subunidades se consolidan funcionalmente: no se entregó una lista nominal original de 94 referencias, solo conteos y necesidades. Por ello la conciliación no inventa equivalencia individual con una lista histórica inexistente; identifica la cobertura de las necesidades expresas, desgloses nuevos, compartidos y alternativas. Las fuentes web sin revisión visible se identifican así; su fecha de consulta no se presenta como fecha de edición. Revisión humana, fichas exactas, cantidades netas, calibración, seguridad y disponibilidad permanecen abiertas en `UNIDAD_03_PENDIENTES.md`.
