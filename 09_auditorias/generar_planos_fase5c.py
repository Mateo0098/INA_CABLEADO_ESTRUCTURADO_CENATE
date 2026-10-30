"""Láminas A3 de Fase 5C. Geometría académica ilustrativa, no levantamiento.

Reutiliza los símbolos físicos aprobados en los prototipos P1 y P2. La salida se
construye primero en una carpeta de trabajo; la promoción al paquete es aparte.
"""
from __future__ import annotations

from pathlib import Path
import sys
import fitz
from xml.sax.saxutils import escape
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_prototipos_fase5b as p
from generar_planos_fase5 import Sheet, INK, GRAY, WHITE, RED

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "08_entrega/PLANOS_FASE5C_TRABAJO"
PDF, PNG, SVG = (OUT / k for k in ("PDF_A3", "PNG", "SVG_EDITABLE"))
pdfmetrics.registerFont(TTFont("ArialC", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("ArialC-Bold", "C:/Windows/Fonts/arialbd.ttf"))


class FinalSheet(p.PrototypeSheet):
    def __init__(self, no, code, title, subtitle, scale="Esquemático — sin escala"):
        code = {"P-TR-A": "TR-A", "P-PLA-A": "PLA-A"}.get(code, code)
        title = title.replace("PROTOTIPO · ", "")
        super().__init__(no, code, title, subtitle, scale)

    def txt(self, x, y, value, size=20, color=INK, bold=False, anchor="start"):
        if "PROTOTIPO EN EVALUACIÓN" in str(value):
            return
        if self.code == "TR-B":
            value = str(value).replace("PP-A-Pxx-", "PP-B-Pxx-")
        value=str(value)
        self.svg.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}" fill="{color}">{escape(value)}</text>')
        self.pdf.setFillColor(HexColor(color))
        self.pdf.setFont("ArialC-Bold" if bold else "ArialC",size)
        from generar_planos_fase5 import H
        if anchor=="end": self.pdf.drawRightString(x,H-y,value)
        elif anchor=="middle": self.pdf.drawCentredString(x,H-y,value)
        else: self.pdf.drawString(x,H-y,value)

    def footer(self, note=""):
        note = note.replace("PROTOTIPO P1: ", "")
        self.line(42, 1076, 1638, 1076, "#AEB9C2", 2)
        self.rect(42, 1083, 1596, 76, WHITE, "#82909B", 1.5, 0)
        self.line(42, 1121, 1638, 1121, "#AEB9C2", 1)
        for x in (1160, 1320, 1450):
            self.line(x, 1083, x, 1159, "#AEB9C2", 1)
        self.txt(56, 1108, "PROYECTO: INA CENATE | ELTT12000 | CABLEADO ESTRUCTURADO", 15, INK, True)
        self.txt(1174, 1108, "FECHA 2026-10-29", 13, INK, True)
        self.txt(1333, 1108, "REV. C", 13, INK, True)
        self.txt(1462, 1108, f"LÁMINA {self.no:02d}/09", 13, INK, True)
        self.txt(56, 1147, note[:115], 12, GRAY)
        self.txt(1174, 1147, "VERTICAL 1U" if self.scale.startswith("Escala vertical") else "SIN ESCALA", 12, INK, True)
        self.txt(1333, 1147, "IA: apoyo visual", 12, GRAY)
        self.txt(1462, 1147, "NO CONSTRUCTIVO", 11, RED, True)


def leader(s, points, label, tx, ty, color=INK):
    s.poly(points, color, 1.25)
    s.circ(*points[0], 3, WHITE, color, 1)
    s.txt(tx, ty, label, 12, color, True)


def building(s, x, y, w, name, er):
    s.rect(x, y, w, 210, "#F6F8F9", INK, 3)
    s.rect(x+8, y+8, w-16, 194, WHITE, "#AEBBC2", 1)
    s.rect(x+28, y+44, 92, 127, "#E5ECEF", INK, 2)
    for i in range(4):
        s.rect(x+37, y+55+i*25, 74, 15, WHITE, p.STEEL, 1)
        for j in range(4): s.circ(x+45+j*13, y+63+i*25, 1.5, p.FIBER, p.FIBER, .2)
    s.txt(x+140, y+71, name, 20, INK, True)
    s.txt(x+140, y+107, er, 17, p.FIBER, True)
    s.txt(x+140, y+137, "Rack / terminación OS2", 12, GRAY)
    s.rect(x+w/2-17, y+199, 34, 18, "#E6D3B4", p.TRAY, 2)
    s.txt(x+w/2, y+247, "ENTRADA SELLADA*", 11, p.TRAY, True, "middle")


def exterior():
    s=FinalSheet(1,"EXT-01","BACKBONE EXTERIOR · TRES EDIFICIOS",
                 "ER principal existente · ER-A · ER-B | E1 / E2 / E3: cable OS2 24F | recorridos de escenario")
    building(s,75,226,445,"EDIFICIO EXISTENTE","ER PRINCIPAL")
    building(s,618,226,445,"EDIFICIO A","ER-A")
    building(s,1160,226,445,"EDIFICIO B","ER-B")
    # Ducto representado con dos bordes, cable por eje y registros con tapas.
    s.rect(112,592,1455,74,"#EEF1F0",p.STEEL,2)
    s.line(112,602,1567,602,p.TRAY,3)
    s.line(112,655,1567,655,p.TRAY,3)
    for x in (289,839,1382):
        s.rect(x-31,568,62,122,"#E3E8E8",INK,2)
        s.rect(x-26,571,52,13,"#B9C5C9",INK,1)
        s.line(x-19,577,x+19,577,p.STEEL,1)
        s.rect(x-12,460,24,110,"#EDF1F2",p.TRAY,2)
        for dx in (-6,6): s.line(x+dx,466,x+dx,565,p.FIBER,1.7)
        s.txt(x,707,f"R-{(289,839,1382).index(x)+1:02d}*",12,INK,True,"middle")
    for x in (470,640,1020,1190):
        s.rect(x-22,605,44,46,"#E6E9E9",INK,1.5)
        s.rect(x-19,608,38,7,"#B6C2C5",INK,1)
        s.line(x-10,611,x+10,611,p.STEEL,1)
    for x1,x2,yy,color,label in ((289,839,618,p.CAT,"E1 · 221,55 m*"),
                                  (289,1382,631,p.FIBER,"E2 · 247,80 m*"),
                                  (839,1382,644,p.GREEN,"E3 · 69,30 m*")):
        s.line(x1,yy,x2,yy,color,3)
        s.txt(111,yy+4,label,12,color,True)
    # Distinct proposed branch segment and reserve loops at building entries.
    s.line(465,591,665,591,p.TRAY,4,dash="11 6")
    for x in (289,839,1382):
        s.circ(x+37,536,19,WHITE,p.FIBER,2)
        s.circ(x+37,536,11,WHITE,p.FIBER,1)
        leader(s,[(x+37,517),(x+55,499)],"RESERVA*",x+60,501,p.FIBER)
    s.panel(75,752,705,286,"CORTE Y SÍMBOLOS DE CANALIZACIÓN")
    s.rect(108,810,194,118,"#ECEFEF",p.STEEL,2)
    s.rect(130,833,150,73,WHITE,p.TRAY,3)
    for yy,col in ((848,p.CAT),(870,p.FIBER),(892,p.GREEN)):
        s.circ(170,yy,8,WHITE,col,2); s.circ(210,yy,8,WHITE,col,2)
    s.txt(328,840,"Ducto existente / propuesto*: trazado esquemático",14,INK)
    s.txt(328,869,"3 cables independientes OS2 24F, E1–E3",14,INK)
    s.txt(328,898,"Registros, entradas y reservas: ubicación teórica",14,INK)
    s.txt(108,985,"* Supuesto de diseño; no es una medición de campo.",14,RED,True)
    s.panel(804,752,801,286,"LONGITUDES Y ALCANCE DEL ESCENARIO")
    s.textlines(830,808,["E1: (145 + 50 + 16) × 1,05 = 221,55 m de cable.",
                          "E2: (145 + 75 + 16) × 1,05 = 247,80 m de cable.",
                          "E3: (50 + 16) × 1,05 = 69,30 m de cable.",
                          "145 m reportados; 50 m y distancias de escenario por verificar.",
                          "OS2 24F exterior; OS2 12F vertical (ver láminas 06–09)."],16,39)
    s.footer("Longitudes de escenario, no mediciones. Geometría, registros y reservas sujetos a verificación en campo.")
    return s


def floor_b():
    s=FinalSheet(3,"PLA-B","CANASTAS Y TUBERÍAS · EDIFICIO B",
                 "Planta académica típica · 6 laboratorios de 75 m² supuestos · bandeja 100 × 50 mm · tubo nominal Ø25 mm")
    s.rect(65,218,1165,775,"#FAFBFB",INK,2)
    s.rect(77,501,1135,184,"#F3F6F7","#CAD4D9",1)
    s.txt(95,536,"PASILLO CENTRAL · 2,4 m SUPUESTO",14,GRAY,True)
    centers=(260,590,920)
    for row in range(2):
        for i,cx in enumerate(centers):
            x=cx-150; y=236 if row==0 else 690
            lab=i+1+row*3; side="bottom" if row==0 else "top"
            p.wall_room(s,x,y,300,260,f"LAB B-{lab:02d}",75,cx+80,side)
    s.rect(1068,690,135,275,"#EDF3F4",INK,4)
    s.rect(1080,765,110,150,"#D9E1E5",INK,2)
    for y in range(782,902,17):
        s.rect(1091,y,88,9,WHITE,p.STEEL,1)
        for j in range(6): s.circ(1100+j*12,y+4,1.4,p.CAT,p.CAT,.1)
    s.txt(1135,733,"TR-B · 42U",16,INK,True,"middle")
    s.txt(1135,943,"5 × 48 = 240",12,INK,True,"middle")
    p.tray_h(s,102,1060,590,27)
    p.tray_v(s,1038,590,743,27); p.tray_h(s,1038,1090,743,27)
    for row in range(2):
        for i,cx in enumerate(centers):
            lab=i+1+row*3
            top=row==0
            p.tray_v(s,cx,496 if top else 603,577 if top else 690,22)
            s.rect(cx-15,578 if top else 589,30,23,"#F4DDC1",p.TRAY,1.4)
            by=461 if top else 707; ey=373 if top else 806
            s.rect(cx-16,by-13,32,26,"#E5EBEE",INK,1.8,2)
            s.txt(cx-22,by+4,f"TB-B{lab:02d}",11,INK,True,"end")
            p.tube(s,[(cx,by-13 if top else by+13),(cx,ey)])
            p.outlet(s,cx,ey)
            s.txt(cx+21,ey+4,f"TO-B{lab:02d}",11,p.CAT,True)
            p.tube(s,[(cx+16,by),(cx+67,by),(cx+67,ey)])
            p.outlet(s,cx+67,ey)
    for x in (160,455,735,1010):
        s.line(x,564,x,579,p.STEEL,2)
        s.line(x-10,564,x+10,564,p.STEEL,2)
        s.circ(x,560,2,WHITE,p.STEEL,1)
        s.line(x-14,606,x+14,606,p.STEEL,1.5)
    s.txt(79,1011,"Rutas, muros, soportes y salidas ilustrativos. 2 salidas por lab dibujadas como muestra; no equivalen a las 16 WA.",12,GRAY)
    s.txt(79,1035,"6 laboratorios × 16 WA dobles × 2 RJ45 = 192 enlaces Cat 6A por piso; TR-B: 5 × 48 = 240 posiciones.",13,INK,True)
    s.panel(1245,216,362,350,"DETALLE · TRANSICIÓN")
    p.tray_h(s,1265,1560,316,38)
    s.line(1283,278,1283,297,p.STEEL,2)
    s.line(1272,278,1294,278,p.STEEL,2)
    s.circ(1283,275,2.5,WHITE,p.STEEL,1)
    s.rect(1370,294,64,44,"#E9D2B6",p.TRAY,2)
    s.rect(1380,337,44,40,"#DDE6E9",INK,2)
    p.tube(s,[(1402,377),(1402,481)])
    p.outlet(s,1402,491)
    s.textlines(1268,411,["Caja bandeja → tubo", "Tubo nominal Ø25 mm", "2 × Cat 6A hacia WA", "Soporte ilustrativo"],12,28)
    s.panel(1245,584,362,240,"DETALLE · SALIDA DOBLE")
    p.tube(s,[(1412,631),(1412,678)])
    s.rect(1350,675,124,99,"#E5E9EB",INK,2)
    s.rect(1360,685,104,80,WHITE,p.STEEL,1.5)
    p.jack(s,1373,710,34,29,True,True); p.jack(s,1418,710,34,29,True,True)
    s.txt(1412,801,"2 × RJ45 Cat 6A",12,p.CAT,True,"middle")
    s.panel(1245,842,362,200,"LEYENDA")
    p.tray_h(s,1265,1310,886,13); s.txt(1327,892,"Bandeja 100 × 50",11,INK)
    p.tube(s,[(1266,920),(1310,920)]); s.txt(1327,925,"Tubo nominal Ø25",11,INK)
    p.outlet(s,1287,957); s.txt(1327,962,"WA doble / 2 RJ45",11,INK)
    s.rect(1274,990,25,21,"#E5EBEE",INK,1); s.txt(1327,1005,"Transición / caja",11,INK)
    s.footer("Geometría y recorridos supuestos; confirmar instalación, fijaciones y ocupación antes de construir.")
    return s


def desk(s,x,y,num):
    s.rect(x,y,159,110,"#F1F4F4",INK,1.5,3)
    s.rect(x+10,y+10,139,67,WHITE,p.STEEL,1.2,2)
    s.line(x+79,y+11,x+79,y+76,p.STEEL,1)
    for dx in (25,95):
        s.rect(x+dx,y+22,40,30,"#E0E8EA",INK,1)
        s.rect(x+dx+5,y+56,30,5,p.STEEL,p.STEEL,.2)
    p.outlet(s,x+79,y+88)
    s.txt(x+79,y+103,f"WA-{num:02d}",12,INK,True,"middle")


def wa_sheet(building):
    no=4 if building=="A" else 5
    area=85 if building=="A" else 75
    s=FinalSheet(no,f"WA-{building}",f"ÁREAS DE TRABAJO · EDIFICIO {building}",
       f"Laboratorio típico {area} m² · 16 WA dobles · 32 puertos RJ45 Cat 6A · planta y mobiliario supuestos")
    s.rect(80,236,1125,750,WHITE,INK,4)
    s.rect(89,245,1107,732,WHITE,p.STEEL,1.2)
    s.rect(77,809,14,100,WHITE,WHITE,0)
    s.line(80,810,177,810,INK,2); p.arc(s,80,810,97,0,90)
    s.txt(112,272,f"LAB {building} / {area} m² · geometría académica supuesta",15,INK,True)
    p.tray_h(s,145,1145,310,20)
    for row in range(4):
        for col in range(4):
            n=row*4+col+1
            x=140+col*255; y=360+row*145
            desk(s,x,y,n)
            cx=x+79
            # Segmentos de tubo doble desde la bandeja de distribución.
            if row==0: p.tube(s,[(cx,320),(cx,y-5)])
            else: p.tube(s,[(cx,y-15),(cx,y)])
    for row in range(1,4):
        yy=345+row*145
        p.tray_h(s,145,1145,yy,15)
    s.rect(1130,296,42,29,"#E7EAEB",INK,1.5)
    s.poly([(1151,309),(1191,309),(1222,309)],p.CAT,3,dash="7 4")
    s.txt(1205,293,f"HACIA TR-{building}",13,p.CAT,True,"end")
    s.txt(110,1015,"16 placas dobles identificadas WA-01–WA-16; cada símbolo muestra 2 bocas RJ45; 32 enlaces permanentes Cat 6A.",14,INK,True)
    s.panel(1230,218,379,360,"DETALLE · PUESTO DOBLE")
    s.rect(1260,270,317,170,"#EEF2F3",INK,2)
    s.rect(1280,286,277,126,WHITE,p.STEEL,1.5)
    s.rect(1365,365,105,67,"#E1E8EB",INK,2)
    p.jack(s,1375,379,39,34,True,True); p.jack(s,1422,379,39,34,True,True)
    s.txt(1417,464,"RJ45-A            RJ45-B",12,INK,True,"middle")
    s.txt(1255,502,"Placa, caja y conectores ilustrativos.",12,GRAY)
    s.txt(1255,531,"2 cables Cat 6A por WA; ruta agrupada.",12,p.CAT,True)
    s.panel(1230,596,379,447,"RUTA Y LEYENDA")
    p.tray_h(s,1257,1355,659,17); s.txt(1371,664,"Bandeja de distribución*",12,INK)
    p.tube(s,[(1263,706),(1352,706)]); s.txt(1371,711,"Tubería nominal Ø25*",12,INK)
    p.outlet(s,1300,750); s.txt(1371,755,"WA doble · 2 × RJ45",12,INK)
    s.line(1259,799,1357,799,p.CAT,3,dash="8 4"); s.txt(1371,804,"Cat 6A permanente",12,INK)
    s.textlines(1258,858,["Ruta agrupada hacia TR; no se dibujan", "32 cables individuales superpuestos.",
                          "* Posición y recorrido supuestos.","Escala: esquemático, sin escala."],12,28)
    s.footer("16 WA dobles × 2 RJ45 = 32 salidas por laboratorio. Mobiliario y canalizaciones supuestos.")
    return s


def rack_frame(s,x=84,y=218,w=705,uh=17.55):
    bottom=y+42*uh
    s.rect(x,y,w,bottom-y+28,"#F4F6F7",INK,4,3)
    s.rect(x+10,y+13,w-20,bottom-y-3,WHITE,p.STEEL,2,1)
    for xx in (x+36,x+w-68): s.rect(xx,y,33,bottom-y,"#C6D0D5",INK,2)
    s.rect(x+80,y,w-160,bottom-y,WHITE,p.STEEL,1.3)
    s.rect(x+14,bottom+3,w-28,20,"#354653",INK,1)
    for u in range(1,43):
        yy=bottom-u*uh
        for xx in (x+53,x+w-52):
            for f in (.24,.48,.72): s.rect(xx-2,yy+uh*f-1.5,4,3,"#43515B","#43515B",.2,1)
        s.txt(x+22,yy+uh*.72,f"{u:02d}",10,INK,True,"middle")
        s.txt(x+w-18,yy+uh*.72,f"{u:02d}",10,INK,True,"middle")
        s.line(x+80,yy,x+w-80,yy,"#E5EAED",.5)
    duct=x+w-83
    s.rect(duct,y+30,15,bottom-y-56,"#D2DBDF",p.STEEL,1,1)
    for yy in range(int(y+37),int(bottom-40),22): s.line(duct+3,yy,duct+12,yy,p.STEEL,1)
    return bottom, x+93, w-186, uh, duct


def cassette(s,x,y,w,h,kind,caption=True):
    p.tag_start(s,view="detalle" if caption else "rack",cassette=f"{kind}F")
    s.rect(x,y,w,h,"#DFE8EB",INK,1.4,2)
    s.rect(x+5,y+5,w-10,h-10,"#F7FAFB",p.STEEL,1)
    n=6 if kind==12 else 12
    pitch=(w-32)/n
    for i in range(n):
        xx=x+17+i*pitch
        s.rect(xx-5,y+h/2-8,10,16,"#315C78",INK,.6,1)
        s.circ(xx-1.5,y+h/2,1.4,WHITE,WHITE,.2)
        s.circ(xx+1.5,y+h/2,1.4,WHITE,WHITE,.2)
    if caption:
        s.txt(x+w/2,y+h+14,f"{kind}F · {n} × LC dúplex",10,p.FIBER,True,"middle")
    p.tag_end(s)


def er_sheet(building):
    is_a=building=="A"; no=6 if is_a else 8
    housing="CCH-03U" if is_a else "CCH-04U"
    v=4 if is_a else 7; pos=96 if is_a else 132; hu=3 if is_a else 4
    s=FinalSheet(no,f"ER-{building}",f"ELEVACIÓN FRONTAL · ER EDIFICIO {building}",
       f"Gabinete 19 in · 42U · {housing} · {v} cassettes 12F + 2 cassettes 24F · {pos} fibras")
    bottom,fx,fw,uh,duct=rack_frame(s)
    s.txt(436,203,f"ER-{building} / FRENTE ABIERTO",14,INK,True,"middle")
    hy=bottom-hu*uh
    s.rect(fx,hy,fw,hu*uh-1,"#DFE8EB",INK,2)
    s.txt(fx+13,hy+16,housing,12,INK,True)
    # Each removable front cassette has its own visible duplex apertures.
    counts=[12]*v+[24,24]
    cols=3; rows=2 if is_a else 3
    cw=(fw-35)/cols; ch=(hu*uh-21)/rows
    for i,kind in enumerate(counts):
        row,col=divmod(i,cols)
        cassette(s,fx+10+col*cw,hy+21+row*ch,cw-8,ch-3,kind,False)
    p.organizer(s,fx,bottom-(hu+1)*uh,fw,uh-1,"ORGANIZADOR ÓPTICO")
    s.rect(fx,bottom-(hu+2)*uh,fw,uh-1,"#DCE6E8",INK,1)
    s.txt(fx+fw/2,bottom-(hu+1.45)*uh,"GUÍA DE ENTRADA / RADIO DE CURVATURA ILUSTRATIVO",11,INK,True,"middle")
    s.poly([(duct+7,bottom-(hu+1)*uh),(duct-16,bottom-(hu+1)*uh),(duct-28,hy+15)],p.FIBER,2.5)
    s.txt(430,467,f"U{hu+3:02d}–U42 · RESERVA DE ESPACIO",15,GRAY,True,"middle")
    s.panel(831,218,773,298,"DETALLE A · FRENTE ÓPTICO PASIVO")
    s.rect(853,268,720,183,"#E2E9EC",INK,2)
    s.txt(875,297,f"{housing} / cassettes integrados",15,INK,True)
    for i,kind in enumerate((12,12,24,24)):
        xx=872+i*171
        cassette(s,xx,321,160,89,kind)
    s.txt(865,482,"Vista ampliada representativa; total indicado en tabla de ocupación.",13,GRAY)
    s.panel(831,532,773,263,"CABLES Y CONEXIONES")
    s.line(864,597,954,597,p.FIBER,5); s.txt(974,603,"Exterior: 2 × OS2 24F hacia ER",15,INK)
    s.line(864,645,954,645,p.GREEN,5); s.txt(974,651,f"Vertical: {v} × OS2 12F hacia TR-{building}",15,INK)
    s.poly([(864,693),(922,693),(922,716),(954,716)],p.CAT,3)
    s.circ(956,716,4,WHITE,p.CAT,1)
    s.txt(974,721,"Patch cord óptico ilustrativo; extremo libre",15,INK)
    s.txt(862,765,"Sin switches o equipos activos instalados en este diseño.",14,GRAY)
    s.panel(831,811,773,231,"OCUPACIÓN Y RESERVA 42U")
    s.textlines(858,864,[f"U01–U{hu:02d}: {housing} · {v} × 12F + 2 × 24F = {pos} fibras.",
                          f"U{hu+1:02d}: organizador óptico; U{hu+2:02d}: guía de entrada.",
                          f"U{hu+3:02d}–U42: espacio libre para crecimiento / activos por definir.",
                          "Cassettes incluyen conectores/adaptadores; sin conteo doble."],14,37)
    s.footer("Montaje y rutas esquemáticos; capacidades según matriz y Excel. Validar fabricante y recinto.")
    return s


def tr_b():
    s=FinalSheet(9,"TR-B","ELEVACIÓN FRONTAL · TR EDIFICIO B",
       "Gabinete 19 in · 42U · 5 paneles de 48 RJ45 · 192 asignados / 48 libres",
       "Escala vertical: 1U constante; ancho ilustrativo")
    bottom,fx,fw,uh,duct=rack_frame(s)
    s.txt(436,203,"TR-B / FRENTE ABIERTO",14,INK,True,"middle")
    p.optical(s,fx,bottom-uh,fw,uh-1)
    p.organizer(s,fx,bottom-2*uh,fw,uh-1,"ORGANIZADOR ÓPTICO")
    for pn in range(1,6):
        u=3+(pn-1)*3
        py=bottom-(u+1)*uh
        assigned=48 if pn<=4 else 0
        p.panel_face(s,fx,py,fw,2*uh-1,pn,assigned)
        p.organizer(s,fx,bottom-(u+2)*uh,fw,uh-1,f"ORGANIZADOR HORIZONTAL · PP{pn:02d}")
        s.poly([(duct+7,py+9),(duct-15,py+9),(duct-25,py+16)],p.CAT,2,dash="4 3")
    s.txt(435,442,"U18–U42 · ESPACIO LIBRE / ACTIVOS POR DEFINIR",15,GRAY,True,"middle")
    # One open-ended cord, explicitly not all assigned ports patched.
    s.poly([(fx+142,bottom-4*uh+12),(fx+142,bottom-4*uh-14),(fx+175,bottom-4*uh-23)],p.GREEN,3)
    s.circ(fx+177,bottom-4*uh-23,4,WHITE,p.GREEN,2)
    s.panel(831,217,773,349,"DETALLE A · PP05 / 48 PUERTOS DE RESERVA")
    p.panel_face(s,850,265,735,223,5,0,True)
    s.txt(858,531,"00 asignados en PP05; 48 posiciones RJ45 físicas libres.",14,INK,True)
    s.panel(831,582,773,185,"DETALLE B · TERMINACIÓN OS2 12F")
    s.rect(856,628,700,86,"#E2E8EB",INK,2)
    for i in range(6):
        xx=880+i*91
        s.rect(xx,645,65,47,"#315C78",INK,1)
        s.circ(xx+22,668,8,WHITE,INK,1); s.circ(xx+43,668,8,WHITE,INK,1)
        s.txt(xx+32,707,f"{2*i+1:02d}/{2*i+2:02d}",10,INK,True,"middle")
    s.txt(859,748,"CCH-01U · 1 cassette 12F integrado · ER-B → TR-B",13,p.FIBER,True)
    s.panel(831,788,773,260,"LEYENDA Y OCUPACIÓN")
    s.line(854,834,901,834,p.CAT,4); s.txt(915,840,"Cat 6A permanente posterior: 6 laboratorios × 32",13,INK)
    s.line(854,865,901,865,p.GREEN,4); s.txt(915,871,"Cordón frontal ilustrativo, extremo sin conectar",13,INK)
    s.line(854,895,901,895,p.FIBER,4); s.txt(915,901,"Backbone vertical OS2 12F · cassette pasivo",13,INK)
    s.txt(854,922,"LAB01: PP01 01–32 · LAB02: PP01 33–48 + PP02 01–16 · LAB03: PP02 17–48",11,INK)
    s.txt(854,940,"LAB04: PP03 01–32 · LAB05: PP03 33–48 + PP04 01–16 · LAB06: PP04 17–48",11,INK)
    s.txt(854,966,"U01 óptica · U02 organizador · U03–17: 5 paneles + 5 organizadores.",13,INK,True)
    s.txt(854,992,"PP01–PP04: 01–48 asignados; PP05: 01–48 libres.",14,INK,True)
    s.txt(854,1018,"192 asignados + 48 reserva = 240 posiciones; U18–42 libres.",14,INK,True)
    s.txt(854,1039,"Asignación no equivale a conexión activa de switch.",11,GRAY)
    s.footer("Puertos RJ45 pasivos dibujados. Sin switches instalados; patch cords representativos.")
    return s


def build():
    p.PrototypeSheet=FinalSheet
    sheets=[exterior(),p.plan_prototype(),floor_b(),wa_sheet("A"),wa_sheet("B"),
            er_sheet("A"),p.rack_prototype(),er_sheet("B"),tr_b()]
    stems=["01_ext_01","02_pla_a","03_pla_b","04_wa_a","05_wa_b",
           "06_er_a","07_tr_a","08_er_b","09_tr_b"]
    for d in (PDF,PNG,SVG): d.mkdir(parents=True,exist_ok=True)
    merged=fitz.open()
    for s,stem in zip(sheets,stems,strict=True):
        sp=SVG/f"{stem}.svg"; pp=PDF/f"{stem}.pdf"
        s.finish(sp,pp)
        with fitz.open(pp) as doc:
            if doc.page_count!=1: raise ValueError(stem)
            doc[0].get_pixmap(matrix=fitz.Matrix(300/72,300/72),alpha=False).save(PNG/f"{stem}.png")
            merged.insert_pdf(doc)
    merged.save(OUT/"PLANOS_TECNICOS_INA_CENATE_9_LAMINAS.pdf",garbage=4,deflate=True)
    merged.close()
    print(f"Generadas {len(sheets)} láminas en {OUT}")


if __name__=="__main__": build()
