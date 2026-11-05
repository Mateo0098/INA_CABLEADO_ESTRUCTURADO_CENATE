"""Inventario documental U03. Python estándar; ejecutar desde cualquier carpeta."""
import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent
FECHA = '2026-11-04'
FUENTES = {
 'PROY': '05_materiales/unidad_02_ampliacion/UNIDAD_02_MEMORIA_DE_CANTIDADES.md',
 'TG': 'https://www.panduit.com/content/dam/panduit/en/products/media/9/29/729/4729/110934729.pdf',
 'PACK': 'https://www.panduit.com/content/dam/panduit/en/products/media/0/50/950/5950/106655950.pdf',
 'IDC': 'https://www.panduit.com/content/dam/panduit/en/products/media/5/15/015/5015/102005015.pdf',
 'DSX': 'https://www.flukenetworks.com/edocs/datasheet-dsx-8000-cableanalyzer',
 'ACC': 'https://www.flukenetworks.com/edocs/industrial-ethernet-cableanalyzer-kit',
 'OLTS': 'https://www.flukenetworks.com/content/datasheet-certifiber-pro-optical-loss-test-set-0',
 'CR': 'https://tiendacr.elvatron.com/collections/certificacion-de-cableado',
}
COLS = ['ID único','Subunidad de origen','Categoría','Herramienta equipo o consumible','Función técnica','Actividad de instalación o prueba','Especificación requerida','Compatibilidad','Unidad funcional','Unidad comercial','Cantidad de referencia','Fórmula de cantidad o criterio','Escenario de cuadrilla','Estado de cantidad','Modalidades de adquisición posibles','Fabricante candidato','Modelo o referencia candidata','Proveedor nacional','Fuente y fecha','Componentes incluidos en kit','Recurso compartido o duplicación','Referencia a Unidad 02','Estado de verificación','Pendiente técnico','Clasificación de evidencia','Estado de selección']
rows = []
def add(sub, nombre, funcion, spec, *, qty='1 REFERENCIA', formula='C=1 frente secuencial; necesidad=1×C; compra=max(0; necesidad-existentes aptos-incluidos)', cat='Reutilizable', unit='unidad', modal='Compra | Alquiler | Equipo existente, por confirmar', model='PENDIENTE', maker='PENDIENTE', fuente='PROY', kit='Contenido comercial PENDIENTE; desglosar antes de adquirir', dup='Uso secuencial; no sumar una copia por actividad', u02='Sin compra equivalente identificada', pendiente='Modelo, ficha, inventario existente y cotización nacional', compat=None):
    i = sum(r['Subunidad de origen'].split(';')[0] == sub for r in rows)+1
    source = FUENTES.get(fuente, fuente)
    proveedor='Pendiente de cotización nacional; posible importación solo tras búsqueda nacional documentada'
    estado='Requisito funcional propuesto; ficha/modelo pendientes'
    if fuente in ('DSX','OLTS'):
        proveedor='ELVATRON Costa Rica; familia publicada; variante exacta y alquiler pendientes'
        source += '; '+FUENTES['CR']
        estado='Capacidad de familia verificada; oferta publicada agotada; kit y disponibilidad por confirmar'
    elif fuente in ('TG','IDC','ACC','PACK'):
        estado='Compatibilidad documental verificada; suministro nacional pendiente'
    rows.append(dict(zip(COLS,[f'U03-{sub}-{i:03}',sub,cat,nombre,funcion,funcion,spec,compat or spec,unit,'unidad; empaque por confirmar',qty,formula,'C=1 frente secuencial; T=2 técnicos como supuesto; seguridad según riesgo', 'Supuesto de referencia; compra pendiente' if 'REFERENCIA' in qty else 'Decisión pendiente o exclusión documentada',modal,maker,model,proveedor,source+'; consulta '+FECHA+'; responsable Codex',kit,dup,u02,estado,pendiente,'Supuesto de diseño; revisión técnica humana pendiente','Candidato no adjudicado' if model!='PENDIENTE' else 'Pendiente de selección'])))

# 03A: cada necesidad mecánica conserva fila propia.
for n,f,s in [
 ('Cortadora de rejilla','Cortar canasta electrosoldada','Cabezal y capacidad aprobados para alambre/acabado de canasta; no asumir cortapernos universal'),
 ('Desbarbador y limas','Eliminar rebabas metálicas','Perfil compatible; dejar bordes seguros sin dañar cables'),
 ('Cortadora de varilla roscada','Cortar suspensión','Capacidad, diámetro y paso de rosca del sistema por definir'),
 ('Tornillo de banco','Sujetar piezas durante corte','Mordazas y mesa estables; tamaño según piezas'),
 ('Rotomartillo','Perforar concreto','Energía, portabroca y extracción según sustrato; no escoger por cantidad de enlaces'),
 ('Brocas SDS-Plus para concreto','Perforar para anclajes','Diámetro y profundidad solo con anclaje seleccionado; verificar portabroca SDS-Plus'),
 ('Brocas para otros materiales','Perforar metal u otros sustratos','Material, diámetro y velocidad conforme a pieza; distintas de SDS-Plus'),
 ('Extractor de polvo','Capturar polvo en perforación','Sistema y filtración aprobados para polvo generado; compatible con rotomartillo'),
 ('Cepillos de perforación','Limpiar orificios de anclaje','Diámetro, desgaste y secuencia según fabricante del anclaje'),
 ('Soplador o bomba de limpieza de orificios','Completar limpieza de anclajes','Solo si procedimiento del anclaje lo exige; no sustituir con aspiración sin aprobación'),
 ('Atornillador','Montar perfiles y accesorios','Puntas y control de apriete compatibles; no reemplaza torque controlado'),
 ('Dados y puntas','Accionar fijaciones','Medidas, encastre y uso manual/impacto según fijación; juego sin solapamiento con llaves'),
 ('Llaves de boca y ajustables','Sujetar tuercas y perfiles','Aperturas según tuercas; contrasujeción cuando proceda'),
 ('Llave dinamométrica','Aplicar torque especificado','Rango y precisión según fabricante; calibración vigente; no inventar N·m'),
 ('Cortatubos PVC','Cortar conduit','Diámetros y espesor del PVC elegido'),
 ('Escariador de conduit','Eliminar rebabas en PVC','Compatible con diámetro interior y exterior; distinto del desbarbador metálico'),
 ('Flexómetro','Medir rutas y piezas','Longitud y resolución apropiadas; unidades m/mm'),
 ('Nivel láser','Alinear soportación','Alcance, precisión y visibilidad según sitio; accesorios por verificar'),
 ('Escuadra','Trazar cortes','Tamaño según perfil y tubería'),
 ('Plomada','Trasladar verticales','Alternativa a función equivalente del láser solo si aprobada y utilizable'),
 ('Guía pasacables','Guiar tendido de cobre y fibra','Longitud, radio, esfuerzo de tracción y terminales compatibles con cable y ruta'),
 ('Soportes de bobinas','Desenrollar con control','Capacidad por masa y diámetro; eje y freno según bobina; no improvisar apoyo'),
 ('Detector de instalaciones ocultas','Inspeccionar antes de perforar','Sustrato y profundidad compatibles; lectura no garantiza ausencia de servicios'),
 ('Escalera apropiada','Acceder a altura limitada','Altura, apoyo y capacidad conforme a evaluación; uso institucional aprobado'),
 ('Andamio o plataforma elevadora','Trabajar en altura prolongada','Alternativa de acceso por altura/alcance/suelo; operador competente; plan de rescate'),
 ('Útiles de trazado','Marcar cortes y perforaciones','Marcador y línea de trazado compatibles con superficie'),
]:
    add('03A',n,f,s,qty='2 REFERENCIA' if n=='Soportes de bobinas' else ('PENDIENTE' if n in ('Escalera apropiada','Andamio o plataforma elevadora','Brocas SDS-Plus para concreto','Brocas para otros materiales','Cepillos de perforación') else '1 REFERENCIA'), unit='juego' if n in ('Dados y puntas','Llaves de boca y ajustables','Desbarbador y limas') else 'unidad',formula='2 soportes×C; confirmar si kit se vende como par' if n=='Soportes de bobinas' else ('Según riesgo, método y ficha; PENDIENTE no equivale a cero' if n in ('Escalera apropiada','Andamio o plataforma elevadora','Brocas SDS-Plus para concreto','Brocas para otros materiales','Cepillos de perforación') else '1×C; compra=max(0; necesidad-existentes aptos-incluidos)'))

# 03B: jacks TG y panel IDC separados; los componentes se individualizan sin sumarlos al kit.
add('03B','Pelacables de cobre','Preparar cubierta Cat 6A','Ajustar al cable exacto; no marcar aislamiento; PN511G-SPA distingue MaTriX/no MaTriX',qty='2 REFERENCIA',formula='T=2; 1 por técnico; descontar existentes',maker='Panduit',model='CJAST',fuente='TG')
add('03B','Cortadora de cobre','Recortar cubierta y conductores','Corte limpio; uso conforme al jack y al panel; no utilizar cortadora de canasta',qty='2 REFERENCIA',formula='1×T=2; descontar herramientas existentes',maker='Panduit',model='CWST',fuente='TG')
add('03B','Útiles de preparación de pares','Ordenar pares y separador','Seguir secuencia PN511G-SPA/NK410E; no imponer desenrollador universal',qty='PENDIENTE',formula='Solo auxiliares exigidos no incluidos en pelado/corte; no comprar herramienta innecesaria')
add('03B','Herramienta auxiliar TG','Cerrar jack CJ6X88TGBU','EGJT-1 según PN511G-SPA; no usar impacto 110 sobre jack TG',qty='2 REFERENCIA',formula='T=2; compra=max(0; T-EGJT incluidos en empaque-EGJT existentes)',maker='Panduit',model='EGJT-1',fuente='PACK',kit='Empaque individual sin EGJT-1; -24 y -C incluyen herramienta según plano 01874-40; comprobar referencia cotizada',u02='U02-02B-026')
add('03B','Herramienta de impacto de panel','Terminar NK6XPPG48Y','PDT110; filo hacia descarte; esquema T568A/B aprobado; conservar trenzado según NK410E',qty='2 REFERENCIA',formula='1×T=2 si dos técnicos terminan paneles; compartir por programación',maker='Panduit',model='PDT110',fuente='IDC',u02='U02-02C-028')
add('03B','Útiles de extracción y retrabajo','Desmontar jack o módulo sin daño','Método de liberación de pestañas PN511G-SPA/NK410E; no asumir misma herramienta',qty='PENDIENTE',formula='Herramientas adicionales solo si manual las requiere; revisar piezas reutilizables',fuente='IDC')
add('03B','Comprobador de continuidad','Verificar mapa de hilos','Detectar abiertos, cortos e inversión; no certifica Cat 6A; alcance de pares divididos según modelo')
add('03B','Generador de tonos y sonda','Localizar cable','Compatibilidad con red activa/desconectada según modelo; desconectar antes de uso si requerido',unit='juego')
add('03B','Calificador de transmisión','Evaluar soporte de aplicación','Capacidad de transmisión según equipo; no certificación normativa Cat 6A',qty='PENDIENTE',modal='Alternativa excluyente | Compra | Alquiler | Equipo existente, por confirmar',formula='Opcional si aporta diagnóstico; no sustituye ni reduce 1984 certificaciones')
add('03B','Certificador Cat 6A completo','Certificar enlaces permanentes','Límite Cat 6A/Class EA aprobado; calibración vigente; equipo equivalente debe documentar precisión y reportes',unit='sistema',modal='Compra | Alquiler | Servicio especializado contratado | Equipo existente, por confirmar',maker='Fluke Networks',model='DSX2-5000 o equivalente por verificar',fuente='DSX',kit='Principal/remota, módulos, adaptadores, baterías/cargadores y software: cotejar SKU/lista de empaque; filas componentes no adicionales')
for n,sp,mo in [('Unidad principal','Base Versiv compatible y módulo de cobre','PENDIENTE: base del kit DSX2-5000'),('Unidad remota','Remoto compatible con generación de base/módulo','PENDIENTE: remoto del kit DSX2-5000'),('Adaptadores de enlace permanente','Par Cat 6A/Class EA para principal y remoto','DSX-PLA004S'),('Adaptadores de canal','Par Cat 6A; solo prueba de canal adicional aprobada','DSX-CHA004S'),('Baterías de certificador','Autonomía según jornada y estado; no contar las incluidas de nuevo','VERSIV-BATTERY'),('Cargadores de certificador','Alimentación y clavija compatibles; cantidad por base/remoto','VERSIV-ACUN')]:
    add('03B',n,'Componente del sistema de certificación',sp,qty='PENDIENTE' if 'canal' in n or 'Baterías' in n or 'Cargadores' in n else '1 REFERENCIA',formula='Necesidad según kit; compra separada=max(0; requerido-incluido-existente); adaptadores de canal no sustituyen permanentes',maker='Fluke Networks',model=mo,fuente='ACC',dup='SUBCOMPONENTE U03-03B-010; no sumar al sistema como compra adicional',unit='par' if 'Adaptadores' in n else 'unidad')
add('03B','Software de resultados y licencias','Exportar resultados originales y reportes','LinkWare PC candidato; versión, sistema operativo, licencia y servicios de nube por confirmar',unit='licencia',qty='PENDIENTE',formula='N_licencias según usuarios/contrato; distinguir PC y nube',maker='Fluke Networks',model='LinkWare PC; condiciones pendientes',fuente='DSX')
add('03B','Portátil compartida','Registrar pruebas y administrar red','Puertos USB/Ethernet, almacenamiento, respaldo, sistema compatible con software; uso 03B/03C/03D secuencial',dup='Única portátil común 03B; 03C; 03D; aumentar solo por simultaneidad')
add('03B','Etiquetadora','Imprimir identificación permanente','Compatible con soportes y formato institucional; etiquetas U02 no vuelven a comprarse')
add('03B','Etiquetas de cable y toma','Identificar enlaces','Formato, adhesivo, cubierta e impresora compatibles',cat='Consumible referenciado',qty='0 ADICIONAL U03',formula='Compra en U02; 1984 tomas + 3968 extremos de cable de referencia; no sumarlas aquí',modal='No aplica, con justificación',u02='U02-02B-027; U02-02B-028; U02-02D-021; U02-02D-022',dup='Necesidad preservada en U02; cero adicional no significa cero requerido')
add('03B','Cinta de transferencia o cartucho','Alimentar etiquetadora','Separar tinta/ribbon de etiquetas; si térmica directa, no aplica justificado',cat='Consumible',qty='PENDIENTE',formula='techo(etiquetas_totales/rendimiento_por_cartucho); descontar incluidos',modal='Consumible')
add('03B','Servicio de certificación de cobre','Obtener resultados por enlace','Entregar archivos nativos, PDF, IDs, calibración, límite, fallas y repetición',cat='Servicio',qty='1984 REFERENCIA',formula='1984 enlaces iniciales; ejecuciones=1984+R_cu; R_cu repeticiones desconocidas',unit='enlace permanente',modal='Servicio especializado contratado | Alternativa excluyente',dup='Alternativa a uso propio U03-03B-010; no presupuestar ambas certificaciones completas')

# 03C: separar fusión, pérdida y eventos.
for n,f,sp in [
 ('Fusionadora monomodo','Fusionar extremos OS2','Compatible con fibras del cable/pigtail, protección y bandeja; programa y prueba de arco aprobados'),
 ('Cleaver de precisión','Preparar cara de fibra','Longitud de corte y fibra según fusionadora; verificar inclusión en kit'),
 ('Peladoras de fibra','Retirar recubrimiento','Diámetros de buffer y revestimiento según cable/pigtail exactos'),
 ('Abridor de cubierta 12F','Abrir cable vertical','Verificar construcción Corning 012E81-33131-24; evitar dañar fibras'),
 ('Abridor de cubierta 24F','Abrir cable exterior','Verificar construcción Corning 024EUK-T3601D2M; compartir con 12F solo con compatibilidad demostrada'),
 ('Tijeras para aramida','Cortar elementos de tracción','Solo si cable contiene aramida; no usar para vidrio ni conductores'),
 ('Sujetadores y adaptadores de fusión','Posicionar fibras','Diámetro y tipo de fibra compatibles con fusionadora elegida'),
 ('Electrodos de repuesto','Mantener arco de fusión','Referencia exacta de fusionadora y vida útil; no confundir con 408 protectores'),
 ('Baterías de fusionadora','Sostener jornada de fusión','Autonomía por ciclos de fusión/calefacción; descontar batería incluida'),
 ('Cargador de fusionadora','Cargar equipo','Tensión, conector y clavija según equipo; descontar incluido'),
 ('Mesa de trabajo de fibra','Preparar empalmes limpios','Superficie estable y limpia; protección de viento/lluvia según emplazamiento'),
 ('Recipiente de fragmentos','Contener vidrio residual','Cierre seguro y descarte institucional; nunca desechar fibras sobre mesa/piso'),
 ('Sonda de inspección','Inspeccionar conectores','Vídeo preferido; método de aceptación de cara final aprobado; no observar fibra activa con microscopio directo'),
 ('Puntas LC/UPC','Acceder a conectores y adaptadores','Geometría para férula LC y acceso bulkhead; compatible con sonda; UPC distinto de APC'),
 ('Fuente óptica 1310/1550 nm','Emitir señal para medir pérdida','Monomodo; estabilidad y conectores acordes al procedimiento; incluida funcionalmente en OLTS'),
 ('Medidor de potencia','Medir potencia y pérdida con referencia','Calibración a 1310/1550 nm; interfaz LC/UPC; incluido funcionalmente en OLTS'),
 ('OLTS monomodo','Medir pérdida de inserción','OS2 1310/1550 nm, referencia documentada y límites aprobados; no reemplazar por OTDR'),
 ('OTDR monomodo','Diagnosticar eventos','1310/1550 nm; zona muerta y resolución aptas para enlaces cortos y empalmes; no sustituye OLTS'),
 ('Bobina de lanzamiento','Resolver primer conector en OTDR','OS2, longitud según OTDR/pulso/zona muerta; extremo de enlace LC/UPC'),
 ('Bobina de recepción','Resolver último conector en OTDR','OS2, longitud según procedimiento; independiente de lanzamiento'),
 ('Cables de referencia óptica','Establecer referencia OLTS','OS2 de calidad de referencia, conectores acordes al instrumento y LC/UPC del enlace'),
 ('Acopladores ópticos de prueba','Conectar cordones de referencia','Baja pérdida y geometría/pulido coincidentes; no retirar adaptadores de U02 para contarlos como compra'),
 ('Localizador visual de fallas','Localizar continuidad o defectos cercanos','Conector LC compatible; verificar si integrado en OLTS; no certifica pérdida'),
 ('Software de análisis óptico','Archivar pérdidas y trazas','Compatibilidad con OLTS/OTDR y archivos nativos; licencia por confirmar'),
 ('Útiles reutilizables de limpieza óptica','Preparar limpieza de conectores','Separar aplicadores reutilizables de líquido/toallitas; inspeccionar-limpiar-inspeccionar'),
]:
    fuente='OLTS' if n=='OLTS monomodo' else 'PROY'
    modelo='CertiFiber Pro; SKU monomodo PENDIENTE' if n=='OLTS monomodo' else 'PENDIENTE'
    mod='Compra | Alquiler | Servicio especializado contratado | Equipo existente, por confirmar' if n in ('Fusionadora monomodo','OLTS monomodo','OTDR monomodo') else 'Compra | Alquiler | Equipo existente, por confirmar'
    q='PENDIENTE' if n in ('Electrodos de repuesto','Baterías de fusionadora','Cargador de fusionadora','Puntas LC/UPC','Cables de referencia óptica','Acopladores ópticos de prueba','Software de análisis óptico','Fuente óptica 1310/1550 nm','Medidor de potencia') else '1 REFERENCIA'
    du='Descontar kit fusionadora U03-03C-001; comprobar empaque antes de comprar separado' if n in ('Cleaver de precisión','Sujetadores y adaptadores de fusión','Baterías de fusionadora','Cargador de fusionadora') else 'Uso común de especialidad; no duplicar por cable/enlace'
    if n in ('Fuente óptica 1310/1550 nm','Medidor de potencia'):
        mod='Alternativa excluyente | Compra | Alquiler | Equipo existente, por confirmar'
        du='Función incluida en OLTS U03-03C-017; compra separada solo si se adopta pareja fuente+medidor en lugar de OLTS'
    if n=='Software de análisis óptico': du='Compartir licencia de resultados 03B si compatible; no adquirir dos licencias iguales'
    if n=='Localizador visual de fallas': du='Compra separada=max(0; requerido-integrado OLTS/OTDR-existente)'
    add('03C',n,f,sp,qty=q,model=modelo,maker='Fluke Networks' if fuente=='OLTS' else 'PENDIENTE',fuente=fuente,modal='Consumible' if n=='Electrodos de repuesto' else mod,dup=du,cat='Consumible' if n=='Electrodos de repuesto' else ('Software' if n=='Software de análisis óptico' else 'Reutilizable'),formula='Según vida útil y kit; compra=max(0; requerido-incluido-existente)' if q=='PENDIENTE' else '1 estación secuencial; descontar kit/existentes; no multiplicar por 204 fibras')
add('03C','Limpieza óptica consumible','Limpiar fibra y conectores','Líquido, toallitas sin pelusa y limpiadores desechables compatibles; separar métodos de fibra desnuda/conector',cat='Consumible referenciado',qty='0 ADICIONAL U03',formula='Necesidad y consumo se resuelven en U02-02D-023; no recomprar en U03',modal='No aplica, con justificación',u02='U02-02D-023',dup='Función retenida; única compra consumible en U02')
add('03C','Protectores de fusión','Proteger empalmes','Dimensión compatible con horno/bandeja; contenidos en cassettes según arquitectura U02',cat='Consumible referenciado',qty='0 ADICIONAL U03',formula='Hasta 408 requeridos funcionales; descontar los contenidos en cassettes U02; faltantes solo tras lista de empaque',modal='No aplica, con justificación',u02='U02-02D-006; U02-02D-007; U02-02D-028',dup='No adquirir 408 adicionales; confirmar kit 24F antes de cerrar')
add('03C','Servicio de fusión','Terminar extremos','Técnico especializado; registro fibra/cassette/empalme y control posterior por OLTS',cat='Servicio',qty='408 REFERENCIA MÁXIMA',unit='fusión',formula='(11×12+3×24)×2=408 si todas terminadas; más R_fus por retrabajo pendiente',modal='Servicio especializado contratado | Alternativa excluyente',dup='Alternativa al uso propio de fusionadora; no sumar dos ejecuciones del mismo trabajo')
add('03C','Servicio de medición de pérdida','Evaluar fibras a dos longitudes','Procedimiento, referencia, sentidos y límite aprobados; archivos nativos e IDs',cat='Servicio',qty='408 REFERENCIA EN UN SENTIDO',unit='resultado fibra-longitud de onda-sentido',formula='204 fibras×2 longitudes×1 sentido=408 resultados; 2 sentidos=816 si aprobado; +R_opt',modal='Servicio especializado contratado | Alternativa excluyente',dup='Alternativa al uso propio de OLTS; 408 resultados distintos de 408 fusiones')
add('03C','Servicio OTDR','Documentar eventos y diagnóstico','Sentidos, longitudes, pulsos y criterios aprobados; trazas y análisis',cat='Servicio',qty='PENDIENTE',unit='traza',formula='N_fibras_OTDR×N_longitudes×N_sentidos + R_trazas; no inferir de fusiones',modal='Servicio especializado contratado | Alternativa excluyente',dup='Alternativa al uso propio OTDR; independiente de aceptación OLTS')

# 03D: EPP sin número de personas inventado; seguridad requiere procedimiento.
for n,f,sp in [
 ('Casco','Proteger cabeza','Tipo según riesgo; accesorios compatibles sin perforar casco'),
 ('Accesorios de casco','Compatibilizar protección','Barboquejo/soportes según acceso y ficha; no duplicar accesorios incluidos'),
 ('Lentes de seguridad','Proteger ojos','Cobertura contra partículas y fragmentos de fibra; graduación si aplica'),
 ('Careta facial','Proteger rostro durante corte','Solo cuando evaluación lo requiera; complemento de lentes'),
 ('Guantes anticorte','Manipular rejilla y metal','Nivel de protección/destreza según bordes y herramienta; restricciones cerca de partes rotatorias'),
 ('Guantes de manipulación fina','Manipular fibra y conectores','Compatibilidad con precisión/limpieza; no sustituyen anticorte en rejilla'),
 ('Calzado de seguridad','Proteger pies','Riesgo de impacto, perforación y deslizamiento; talla por usuario'),
 ('Protección auditiva','Controlar exposición a ruido','Atenuación y compatibilidad con casco según evaluación de ruido'),
 ('Protección respiratoria','Controlar exposición residual','Contaminante, filtro y ajuste según evaluación; no sustituye extracción'),
 ('Chaleco de alta visibilidad','Aumentar visibilidad de personal','Necesidad según tránsito/área y política institucional'),
 ('Sistema contra caídas','Proteger trabajo en altura','Arnés, conexión, anclaje verificado y rescate; no contar solo arnés como sistema completo'),
 ('Conos y barreras','Delimitar zona','Perímetro, tránsito, estabilidad y visibilidad según trabajo'),
 ('Cintas y señales de seguridad','Comunicar riesgo','Delimitación y mensajes institucionales; no sustituyen barrera física requerida'),
 ('Dispositivos LOTO','Aislar energía con personal autorizado','Compatibilidad con dispositivos reales; procedimiento institucional de bloqueo'),
 ('Candados LOTO','Asegurar bloqueo individual','Compatibles con dispositivo; identificación y control personal según procedimiento'),
 ('Botiquín adicional','Atender emergencia','Solo si recursos existentes no cubren área y riesgo; responsable de atención'),
 ('Recursos de emergencia adicionales','Responder a incidentes','Rescate/comunicación/control de derrame según riesgo; validar recursos institucionales'),
 ('Multímetro','Realizar comprobaciones autorizadas','Categoría de medición, tensión, puntas y calibración según circuito/procedimiento; responsable eléctrico competente'),
 ('Detector de tensión','Advertir presencia potencial','Sin contacto solo indicación preliminar; no demuestra ausencia de tensión'),
 ('Comprobador de tomas','Comprobar tomas autorizadas','Tipo de toma y tensión; límites del diagnóstico; no certifica instalación eléctrica'),
 ('Termohigrómetro','Registrar condiciones ambientales','Rango, precisión y puntos según requisitos de equipos y sala; unidad °C y %HR'),
 ('Cables de consola y adaptadores','Administrar equipos','USB/serie/pinout y controlador según equipo exacto; no asumir consola universal'),
 ('Diagnóstico de conectividad','Evaluar red de prueba autorizada','Ping, trazado, contadores y prueba de tráfico en entorno autorizado; compartir portátil 03B'),
 ('Software de configuración y monitoreo','Configurar y observar red prevista','Versiones, licencias, permisos y compatibilidad con equipos de Unidad 01'),
 ('Respaldo de configuraciones','Conservar y recuperar configuración','Repositorio institucional autorizado con acceso restringido, versiones y prueba de restauración'),
 ('Iluminación portátil','Iluminar trabajo','Autonomía, alimentación y grado de protección según ambiente; no usar tomas no verificadas'),
 ('Productos de limpieza general','Mantener mesa y herramientas','Ficha de seguridad y compatibilidad; excluir limpieza óptica contabilizada U02'),
 ('Filtros de extracción y respiración','Renovar medios filtrantes','Referencias distintas según extractor/respirador; consumo según exposición, fabricante y estado'),
 ('Repuestos de corte y desgaste','Mantener herramientas','Cuchillas/discos/puntas solo compatibles y no incluidos; vida útil documentada'),
 ('Bolsas y recipientes de residuos generales','Controlar residuos','Clasificar metal/polvo/químicos; fragmentos de fibra en recipiente 03C específico'),
]:
    con=n in ('Cintas y señales de seguridad','Productos de limpieza general','Filtros de extracción y respiración','Repuestos de corte y desgaste','Bolsas y recipientes de residuos generales')
    personal=n in ('Casco','Accesorios de casco','Lentes de seguridad','Careta facial','Guantes anticorte','Guantes de manipulación fina','Calzado de seguridad','Protección auditiva','Protección respiratoria','Chaleco de alta visibilidad','Sistema contra caídas')
    add('03D',n,f,sp,qty='PENDIENTE',formula='N_personas_expuestas×dotación_por_persona + reposiciones - existentes aptos - incluidos; PENDIENTE' if personal else 'Según área, riesgo, jornada y contenido de kit; descontar existentes aptos e incluidos',cat='Consumible' if con else ('EPP' if personal else 'Recurso operativo'),modal='Consumible' if con else 'Compra | Alquiler | Equipo existente, por confirmar',pendiente='Procedimiento institucional, evaluación de riesgo, personas, simultaneidad, inventario y ficha')

def generate():
    with (BASE/'UNIDAD_03_MATRIZ_MAESTRA_HERRAMIENTAS.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=COLS); w.writeheader(); w.writerows(rows)
    print(f'{len(rows)} filas; '+str({s:sum(r['Subunidad de origen']==s for r in rows) for s in ('03A','03B','03C','03D')}))

if __name__=='__main__': generate()
