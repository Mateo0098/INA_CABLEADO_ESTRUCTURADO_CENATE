"""Dos prototipos A3 vectoriales de detalle medio para evaluación académica.

Parte de los datos aprobados de Fase 5. La geometría arquitectónica, los
recorridos y los detalles de fijación son ilustrativos y no son mediciones.
No modifica la colección vigente de nueve láminas.
"""
from __future__ import annotations

from pathlib import Path
import fitz

from generar_planos_fase5 import Sheet, INK, BLUE, TEAL, ORANGE, GRAY, LIGHT, PALE, WHITE, RED, GREEN

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "08_entrega/PROTOTIPOS_GRAFICOS_FASE5B"
OLD = ROOT / "08_entrega/ENTREGA_FINAL_INA_CENATE/06_PLANOS_TECNICOS/PDF_A3"
SVG, PDF, PNG = (OUT / d for d in ("SVG_EDITABLE", "PDF_A3", "PNG"))
STEEL = "#6A7983"
STEEL_LIGHT = "#DCE3E8"
PORT_DARK = "#182C38"
RESERVE = "#D7E0E6"
CAT = "#176B87"
FIBER = "#7865A5"
TRAY = "#B96825"


class PrototypeSheet(Sheet):
    def footer(self, note):
        self.line(42,1076,1638,1076,"#AEB9C2",2)
        self.rect(42,1083,1596,76,WHITE,"#82909B",1.5,0)
        self.line(42,1121,1638,1121,"#AEB9C2",1)
        for x in (1160,1320,1450): self.line(x,1083,x,1159,"#AEB9C2",1)
        self.txt(56,1108,"PROYECTO: INA CENATE | ELTT12000 | CABLEADO ESTRUCTURADO",15,INK,True)
        self.txt(1174,1108,"FECHA 2026-10-28",13,INK,True)
        self.txt(1333,1108,"REV. P1",13,INK,True)
        self.txt(1462,1108,f"LÁMINA {self.no:02d}/09",13,INK,True)
        self.txt(56,1147,note,13,GRAY)
        self.txt(1174,1147,"VERTICAL 1U" if self.scale.startswith("Escala vertical") else "SIN ESCALA",12,INK,True)
        self.txt(1333,1147,"IA: apoyo visual",12,GRAY)
        self.txt(1462,1147,"NO CONSTRUCTIVO",11,RED,True)


def tag_start(s: Sheet, **data):
    attrs = " ".join(f'data-{k.replace("_", "-")}="{v}"' for k, v in data.items())
    s.svg.append(f"<g {attrs}>")


def tag_end(s: Sheet):
    s.svg.append("</g>")


def jack(s: Sheet, x: float, y: float, w: float, h: float, assigned=True, detail=False):
    """Front-face RJ45 outline: bezel, recessed throat, contact strip and latch notch."""
    rim = CAT if assigned else STEEL
    face = "#E8F4F7" if assigned else "#F0F3F5"
    s.rect(x, y, w, h, face, rim, 1.25, 1)
    s.rect(x+2, y+2, w-4, h-4, PORT_DARK if assigned else "#B7C2C9", PORT_DARK if assigned else STEEL, .6, 1)
    s.rect(x+w*.25, y+h*.63, w*.50, h*.23, face, face, 0, 0)
    n = 8 if detail else 4
    for i in range(n):
        xx = x+3.3+(w-6.6)*(i+.5)/n
        s.line(xx, y+2.8, xx, y+max(4.6,h*.32), "#D9B65A" if assigned else "#81919A", .65 if detail else .45)


def panel_face(s: Sheet, x, y, w, h, panel, assigned, detail=False):
    s.rect(x, y, w, h, "#E4E9ED", INK, 2, 2)
    s.rect(x+5, y+5, w-10, h-10, "#FAFBFC", STEEL, 1, 0)
    for sx in (x+9, x+w-9):
        s.circ(sx, y+h/2, 2.4, WHITE, STEEL, 1)
    if detail:
        s.txt(x+17,y+21,f"PP-A-Pxx-{panel:02d}  /  48 RJ45 Cat 6A",17,INK,True)
        left=x+18; pitch=(w-36)/24; pw=pitch-5
        for i in range(48):
            row=i//24; col=i%24; xx=left+col*pitch; yy=y+40+row*80
            tag_start(s,view="detalle",panel=f"PP{panel:02d}",port=f"{i+1:02d}",assigned=str(i<assigned).lower())
            jack(s,xx,yy,pw,26,i<assigned,True)
            tag_end(s)
            s.txt(xx+pw/2, yy+42, f"{i+1:02d}",9,INK,True,"middle")
            if col in (5,11,17): s.line(xx+pitch-2,yy-5,xx+pitch-2,yy+50,STEEL_LIGHT,1)
        for block in range(4):
            row,half=divmod(block,2)
            xx=left+half*12*pitch
            s.txt(xx+6*pitch, y+99+row*80,
                  f"B{block+1}: {block*12+1:02d}–{(block+1)*12:02d}",11,GRAY,True,"middle")
    else:
        s.txt(x+14,y+h/2+5,f"PP{panel:02d}",12,INK,True)
        left=x+70; pitch=(w-83)/24; pw=pitch-3.4
        for i in range(48):
            row=i//24; col=i%24; xx=left+col*pitch; yy=y+7+row*14
            tag_start(s,view="rack",panel=f"PP{panel:02d}",port=f"{i+1:02d}",assigned=str(i<assigned).lower())
            jack(s,xx,yy,pw,10.5,i<assigned)
            tag_end(s)
        for col in (6,12,18):
            xx=left+col*pitch-2
            s.line(xx,y+4,xx,y+h-4,STEEL,1.5)


def organizer(s: Sheet, x, y, w, h, label):
    s.rect(x,y,w,h,"#D9E0E3",INK,1.5,2)
    s.rect(x+17,y+5,w-34,h-10,"#F7F8F7",STEEL,1,2)
    # Four open wire management fingers and their retaining lip.
    for i in range(5):
        xx=x+45+i*(w-90)/4
        s.poly([(xx-11,y+4),(xx-11,y+h-4),(xx+11,y+h-4),(xx+11,y+4)],STEEL,2)
        s.line(xx-11,y+5,xx+11,y+5,INK,1)
    s.txt(x+w/2,y+h/2+5,label,11,INK,True,"middle")


def optical(s: Sheet, x, y, w, h):
    s.rect(x,y,w,h,"#DAE4E8",INK,2,2)
    s.rect(x+8,y+4,w-16,h-8,"#F5F8F9",STEEL,1,1)
    s.txt(x+16,y+h/2+5,"CCH-01U",12,INK,True)
    s.rect(x+105,y+4,185,h-8,"#DFE6EB",STEEL,1,1)
    for i in range(6):
        xx=x+112+i*29
        s.rect(xx,y+6,23,h-12,"#305A76",INK,1,1)
        s.circ(xx+8,y+h/2,2.1,WHITE,WHITE,.3)
        s.circ(xx+16,y+h/2,2.1,WHITE,WHITE,.3)
    s.txt(x+300,y+h/2+5,"12F LC dúplex / 6 adaptadores",11,INK,True)
    s.rect(x+w-58,y+4,47,h-8,RESERVE,STEEL,1,0)
    s.txt(x+w-35,y+h/2+4,"VACÍO",8,GRAY,True,"middle")


def rack_prototype():
    s=PrototypeSheet(7,"P-TR-A","PROTOTIPO · ELEVACIÓN FRONTAL TR-A",
            "Gabinete 19 in · 42U · 4 paneles de 48 RJ45 · 160 asignados / 32 libres",
            "Escala vertical: 1U constante; ancho ilustrativo")
    s.txt(1605,181,"PROTOTIPO EN EVALUACIÓN · REV. P1",16,RED,True,"end")
    x,y,w,uh=84,218,705,17.55
    bottom=y+42*uh
    # Cabinet body, removable open front, plinth, horizontal members.
    s.rect(x,y,w,bottom-y+28,"#F4F6F7",INK,4,3)
    s.rect(x+10,y+13,w-20,bottom-y-3,WHITE,STEEL,2,1)
    s.rect(x+36,y,33,bottom-y,"#C6D0D5",INK,2,0)
    s.rect(x+w-68,y,33,bottom-y,"#C6D0D5",INK,2,0)
    s.rect(x+80,y,w-160,bottom-y,WHITE,STEEL,1.3,0)
    s.rect(x+14,bottom+3,w-28,20,"#354653",INK,1,0)
    for xx in (x+32,x+w-32): s.rect(xx,bottom+22,42,8,INK,INK,0,0)
    s.txt(x+w/2,y-10,"BASTIDOR TR-A  /  FRENTE ABIERTO",14,INK,True,"middle")
    # 42U rail with three-hole pattern and complete U numbering.
    for u in range(1,43):
        yy=bottom-u*uh
        s.txt(x+22,yy+uh*.72,f"{u:02d}",10,INK,True,"middle")
        s.txt(x+w-18,yy+uh*.72,f"{u:02d}",10,INK,True,"middle")
        for xx in (x+53,x+w-52):
            for frac in (.24,.48,.72):
                s.rect(xx-2,yy+uh*frac-1.5,4,3,"#43515B","#43515B",.2,1)
        s.line(x+80,yy,x+w-80,yy,"#E5EAED",.5)
    fx=x+93; fw=w-186
    optical(s,fx,bottom-uh,fw,uh-1)
    organizer(s,fx,bottom-2*uh,fw,uh-1,"ORGANIZADOR ÓPTICO")
    for p in range(1,5):
        u=3+(p-1)*3
        py=bottom-(u+1)*uh
        panel_face(s,fx,py,fw,2*uh-1,p,48 if p<4 else 16)
        organizer(s,fx,bottom-(u+2)*uh,fw,uh-1,f"ORGANIZADOR HORIZONTAL · PP{p:02d}")
    # Side cable duct and permanent horizontal cable bundles, behind panel faces.
    ductx=x+w-83
    s.rect(ductx,y+30,15,bottom-y-56,"#D2DBDF",STEEL,1,1)
    for yy in range(int(y+37),int(bottom-40),22): s.line(ductx+3,yy,ductx+12,yy,STEEL,1)
    for p in range(1,5):
        py=bottom-(4+(p-1)*3)*uh+9
        s.poly([(ductx+7,py),(ductx-13,py),(ductx-23,py+8)],CAT,2.2,dash="4 3")
    s.txt(x+w/2,440,"U15–U42 · ESPACIO LIBRE / EQUIPO ACTIVO POR DEFINIR",15,GRAY,True,"middle")
    # Representative front patch cord: one passive RJ45 to organizer; open end.
    pcx=fx+70+(2+.5)*(fw-83)/24
    pcy=bottom-4*uh+10
    s.poly([(pcx,pcy),(pcx,pcy-20),(pcx+31,pcy-28),(pcx+31,pcy-40)],GREEN,3.5)
    s.circ(pcx+31,pcy-41,4,WHITE,GREEN,2)
    s.txt(110,1020,"FRONTAL: cordón mostrado solo como ejemplo; extremo libre, sin switch asignado.",14,GRAY)
    # Right detail: one complete PP04, physical 48 sockets, port numbers and reserve color.
    s.panel(830,216,775,350,"DETALLE A  /  PP04  ·  48 CONECTORES RJ45")
    panel_face(s,850,265,735,223,4,16,True)
    s.rect(860,513,17,13,"#E8F4F7",CAT,1,1); s.txt(884,525,"01–16: asignados al cableado horizontal",14,INK)
    s.rect(1230,513,17,13,"#F0F3F5",STEEL,1,1); s.txt(1255,525,"17–48: reserva libre",14,INK)
    s.txt(860,550,"Asignado = toma prevista; no implica conexión a un switch activo.",13,GRAY)
    # Optical detail with true 6 duplex openings and one empty CCH slot.
    s.panel(830,582,775,190,"DETALLE B  /  TERMINACIÓN ÓPTICA PASIVA")
    s.rect(852,623,708,90,"#E2E8EB",INK,2,2)
    s.rect(867,636,468,64,WHITE,STEEL,1,0)
    for i in range(6):
        xx=884+i*70
        s.rect(xx,646,47,43,"#315C78",INK,1.5,2)
        s.circ(xx+15,667,7,WHITE,INK,1.3); s.circ(xx+32,667,7,WHITE,INK,1.3)
        s.txt(xx+23,705,f"{2*i+1:02d}/{2*i+2:02d}",10,INK,True,"middle")
    s.rect(1360,636,177,64,RESERVE,STEEL,1.5,0)
    s.txt(1448,674,"BAHÍA SIN USAR",13,GRAY,True,"middle")
    s.poly([(858,665),(838,665),(838,741),(938,741)],FIBER,3)
    s.txt(953,746,"OS2 12F desde ER-A · 1 cassette integrado",14,FIBER,True)
    # Legend and U schedule.
    s.panel(830,788,775,260,"LEYENDA / OCUPACIÓN 42U")
    for yy,col,label in [(837,CAT,"Cat 6A permanente: entrada posterior agrupada"),
                         (867,GREEN,"Cordón frontal representativo; extremo sin conectar"),
                         (897,FIBER,"Backbone vertical OS2 12F; cassette con adaptadores")]:
        s.line(853,yy-5,900,yy-5,col,4); s.txt(912,yy,label,13,INK)
    s.txt(852,936,"U01 óptica  ·  U02 org. óptico  ·  U03–14 cuatro pares panel/organizador",13,INK,True)
    s.txt(852,963,"Paneles: 4 × 48 = 192 posiciones; 160 asignadas; 32 libres.",14,INK,True)
    s.txt(852,989,"U15–42 libres. Montaje y patching final sujetos a revisión.",13,GRAY)
    s.txt(852,1017,"Símbolos de frente ilustrativos; sin equipos activos instalados.",13,GRAY)
    s.footer("PROTOTIPO P1: geometría frontal ilustrativa. Cantidades según Excel; revisión humana pendiente.")
    return s


def arc(s: Sheet,cx,cy,r,start,end,color=STEEL):
    import math
    pts=[(cx+r*math.cos(math.radians(start+(end-start)*i/12)),cy+r*math.sin(math.radians(start+(end-start)*i/12))) for i in range(13)]
    s.poly(pts,color,1.2,"none","3 3")


def wall_room(s: Sheet,x,y,w,h,label,area,door_x,door_side):
    # Double wall line with doorway gap and leaf/swing. All dimensions schematic.
    s.rect(x,y,w,h,WHITE,INK,4,0)
    s.rect(x+7,y+7,w-14,h-14,WHITE,"#9CA8B0",1.3,0)
    dy=y+h if door_side=="bottom" else y
    s.rect(door_x,dy-7 if door_side=="bottom" else dy-2,48,12,WHITE,WHITE,0,0)
    s.line(door_x-3,dy-8,door_x-3,dy+8,INK,2)
    s.line(door_x+51,dy-8,door_x+51,dy+8,INK,2)
    if door_side=="bottom":
        s.line(door_x,dy,door_x,dy-47,INK,2)
        arc(s,door_x,dy,47,-90,0)
    else:
        s.line(door_x,dy,door_x,dy+47,INK,2)
        arc(s,door_x,dy,47,0,90)
    s.txt(x+22,y+35,label,20,INK,True)
    s.txt(x+22,y+58,f"{area} m² supuestos · 16 WA dobles",12,GRAY)
    s.txt(x+22,y+78,"32 enlaces RJ45 Cat 6A",12,CAT,True)


def tray_h(s: Sheet,x1,x2,y,width=25):
    s.rect(x1,y-width/2,x2-x1,width,"#F7ECDD",TRAY,2,1)
    s.line(x1,y-width/2+4,x2,y-width/2+4,"#D59459",1)
    s.line(x1,y+width/2-4,x2,y+width/2-4,"#D59459",1)
    for xx in range(int(x1)+9,int(x2)-6,18): s.line(xx,y-width/2+4,xx,y+width/2-4,TRAY,.65)


def tray_v(s: Sheet,x,y1,y2,width=23):
    s.rect(x-width/2,y1,width,y2-y1,"#F7ECDD",TRAY,2,1)
    s.line(x-width/2+4,y1,x-width/2+4,y2,"#D59459",1)
    s.line(x+width/2-4,y1,x+width/2-4,y2,"#D59459",1)
    for yy in range(int(y1)+8,int(y2)-6,18): s.line(x-width/2+4,yy,x+width/2-4,yy,TRAY,.65)


def tube(s: Sheet,points,nominal=True):
    # Two parallel traces in orthogonal runs, with centerline in pale background.
    for (x1,y1),(x2,y2) in zip(points,points[1:]):
        if abs(x1-x2)<1:
            s.line(x1-3,y1,x2-3,y2,CAT,1.7)
            s.line(x1+3,y1,x2+3,y2,CAT,1.7)
        else:
            s.line(x1,y1-3,x2,y2-3,CAT,1.7)
            s.line(x1,y1+3,x2,y2+3,CAT,1.7)
    for x,y in points[1:-1]: s.circ(x,y,4,WHITE,CAT,1)


def outlet(s: Sheet,x,y):
    s.rect(x-15,y-10,30,21,WHITE,CAT,1.6,2)
    s.rect(x-11,y-6,11,12,PORT_DARK,CAT,.7,1)
    s.rect(x+1,y-6,11,12,PORT_DARK,CAT,.7,1)
    for dx in (-8,-5,4,7): s.line(x+dx,y-4,x+dx,y-1,"#D9B65A",.6)


def plan_prototype():
    s=PrototypeSheet(2,"P-PLA-A","PROTOTIPO · CANALIZACIONES EDIFICIO A",
            "Planta académica típica: 5 laboratorios / TR-A · bandeja 100 × 50 mm · tubo nominal Ø25 mm")
    s.txt(1605,181,"PROTOTIPO EN EVALUACIÓN · REV. P1",16,RED,True,"end")
    # Architectural shell and central corridor. No measured dimensions are claimed.
    s.rect(56,217,1164,775,"#FAFBFB",INK,2)
    s.rect(79,501,1116,184,"#F3F6F7","#CAD4D9",1)
    s.txt(90,536,"PASILLO CENTRAL",14,GRAY,True)
    s.txt(90,553,"2,4 m SUPUESTO",11,GRAY,True)
    rooms=[(92,235,302,262,"LAB A-01",355,"bottom",247),
           (418,235,302,262,"LAB A-02",681,"bottom",572),
           (744,235,302,262,"LAB A-03",1007,"bottom",897),
           (188,689,378,276,"LAB A-04",520,"top",368),
           (591,689,378,276,"LAB A-05",923,"top",776)]
    for x,y,w,h,label,door,side,_ in rooms: wall_room(s,x,y,w,h,label,85,door,side)
    # A small TR at the corridor end: enclosure, visible rack, ingress point.
    s.rect(1066,689,130,276,"#EDF3F4",INK,4)
    s.rect(1073,696,116,262,WHITE,"#9CA8B0",1.3)
    s.rect(1062,725,12,55,WHITE,WHITE,0)
    s.line(1066,726,1120,726,INK,2); arc(s,1066,726,54,0,90)
    s.txt(1131,721,"TR-A",17,INK,True,"middle")
    s.rect(1094,770,76,126,"#D9E1E5",INK,2,2)
    for yy in range(784,886,16):
        s.rect(1102,yy,60,8,WHITE,STEEL,1,0)
        s.circ(1111,yy+4,1.3,CAT,CAT,.1)
    s.txt(1131,924,"42U / 19 in",12,GRAY,True,"middle")
    # Two-edge ladder tray and five tee branches. The top two edge lines continue to TR.
    tray_h(s,112,1076,590,27)
    for i,xx in enumerate((247,572,897,368,776)):
        top=i<3
        y1,y2=(497,576) if top else (604,689)
        tray_v(s,xx,y1,y2,22)
        wall_y=497 if top else 689
        for sx in (xx-14,xx+14): s.line(sx,wall_y-8,sx,wall_y+8,STEEL,1.8)
        # Tee mouth with flanged plate, transition box and conduit run.
        s.rect(xx-15,578 if top else 589,30,23,"#F4DDC1",TRAY,1.4,1)
        by=462 if top else 707
        s.rect(xx-16,by-13,32,26,"#E5EBEE",INK,1.8,2)
        s.circ(xx,by,3,TRAY,TRAY,1)
        s.txt(xx-22,by+4,f"TB-{i+1:02d}",11,INK,True,"end")
        ey=374 if top else 808
        tube(s,[(xx,by-13 if top else by+13),(xx,ey)])
        outlet(s,xx,ey)
        s.txt(xx+21,ey+5,f"TO-{i+1:02d}",11,CAT,True)
        # Second representative outlet branch within same room.
        x2=xx+67
        if top:
            tube(s,[(xx+16,by),(x2,by),(x2,ey-5)])
            outlet(s,x2,ey-5)
        else:
            tube(s,[(xx+16,by),(x2,by),(x2,ey+5)])
            outlet(s,x2,ey+5)
    # Tray elbow and TR entry. Insets are physical illustrative transition components.
    tray_v(s,1032,590,742,27)
    tray_h(s,1032,1097,742,27)
    s.rect(1020,577,25,27,"#EACDAA",TRAY,1.5,2)
    s.rect(1068,727,31,29,"#D9E2E5",INK,1.7,2)
    s.txt(982,626,"CODO 90°",11,TRAY,True)
    s.txt(1061,775,"INGRESO TR",11,INK,True,"end")
    # Support and hanger glyphs on principal tray.
    for xx in (160,455,735,1010):
        s.line(xx,564,xx,579,STEEL,2)
        s.line(xx-10,564,xx+10,564,STEEL,2)
        s.circ(xx,560,2,WHITE,STEEL,1)
        s.line(xx-14,606,xx+14,606,STEEL,1.5)
        s.line(xx-14,606,xx-14,601,STEEL,1.5)
        s.line(xx+14,606,xx+14,601,STEEL,1.5)
    s.txt(78,1008,"Rutas, muros y pasamuros supuestos. Dos salidas por laboratorio ilustran la distribución; no son las 16 WA completas.",13,GRAY)
    s.txt(78,1034,"Cada laboratorio: 16 WA dobles × 2 RJ45 = 32 enlaces. TR-A: 5 × 32 = 160 enlaces Cat 6A.",13,INK,True)
    # Enlarged details on the right.
    s.panel(1242,216,365,340,"DETALLE A · TRANSICIÓN")
    s.txt(1258,273,"Bandeja 100 × 50 mm",14,TRAY,True)
    tray_h(s,1260,1527,319,42)
    s.rect(1370,296,62,45,"#E9D2B6",TRAY,2,2)
    s.rect(1380,339,43,38,"#DDE6E9",INK,2,2)
    s.circ(1401,356,4,WHITE,INK,1)
    s.line(1394,377,1394,479,CAT,2)
    s.line(1408,377,1408,479,CAT,2)
    s.line(1399,381,1399,475,"#78A9BA",1)
    s.line(1403,381,1403,475,"#78A9BA",1)
    s.rect(1385,473,32,22,WHITE,CAT,1.5,2)
    s.line(1274,289,1274,295,STEEL,2); s.line(1263,288,1285,288,STEEL,2)
    s.txt(1258,409,"Caja de transición",12,INK)
    s.line(1365,404,1390,367,INK,1)
    s.txt(1258,439,"Tubo Ø25 nominal",12,CAT,True)
    s.txt(1450,460,"2 × Cat 6A",11,CAT,True)
    s.txt(1258,525,"Soporte y fijación ilustrativos",11,GRAY)
    s.panel(1242,572,365,249,"DETALLE B · SALIDA DOBLE")
    tube(s,[(1405,620),(1405,660)])
    s.rect(1351,658,108,94,"#E5E9EB",INK,2,3)
    s.rect(1360,667,90,77,WHITE,STEEL,1.5,2)
    jack(s,1370,690,32,29,True,True)
    jack(s,1409,690,32,29,True,True)
    s.circ(1365,705,2,STEEL,STEEL,1)
    s.circ(1445,705,2,STEEL,STEEL,1)
    s.txt(1405,774,"WA doble · 2 × RJ45 Cat 6A",12,CAT,True,"middle")
    s.txt(1405,793,"Placa / caja de salida ilustrativa",11,GRAY,False,"middle")
    s.panel(1242,837,365,211,"LEYENDA DE CANALIZACIÓN")
    tray_h(s,1262,1315,883,14); s.txt(1328,888,"Bandeja aérea · 100 × 50 mm",11,INK)
    tube(s,[(1264,916),(1312,916)]); s.txt(1328,921,"Tubo nominal Ø25 mm",11,INK)
    s.rect(1276,943,20,17,"#E5EBEE",INK,1.3,1); s.txt(1328,956,"Caja de transición a tubo",11,INK)
    outlet(s,1286,983); s.txt(1328,988,"Salida doble RJ45",11,INK)
    s.line(1264,1014,1312,1014,CAT,2); s.txt(1328,1019,"Cableado Cat 6A permanente",11,INK)
    s.footer("PROTOTIPO P1: recorridos, ubicación de salidas y fijaciones ilustrativos; verificar en campo.")
    return s


def save_sheet(s: Sheet, stem: str):
    sp,pp=SVG/f"{stem}.svg",PDF/f"{stem}.pdf"
    s.finish(sp,pp)
    d=fitz.open(pp)
    dpi=300
    d[0].get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72),alpha=False).save(PNG/f"{stem}.png")
    d.close()


def add_comparison_page(dst, old, new, title, old_clip, new_clip, prototype):
    p=dst.new_page(width=1190.551,height=841.89)
    p.draw_rect(fitz.Rect(16,16,1175,826),color=(.13,.20,.25),width=1.5)
    p.insert_text((35,54),title,fontsize=23,fontname="hebo",color=(.13,.20,.25))
    p.insert_text((35,78),"FASE 5  /  VIGENTE",fontsize=13,fontname="hebo",color=(.34,.43,.48))
    p.insert_text((612,78),f"PROTOTIPO {prototype}  /  EN EVALUACION",fontsize=13,fontname="hebo",color=(.10,.39,.50))
    for x,src,clip in ((36,old,old_clip),(612,new,new_clip)):
        full=fitz.Rect(x,93,x+542,483)
        detail=fitz.Rect(x,528,x+542,775)
        p.draw_rect(full,color=(.7,.75,.78),width=.8)
        p.draw_rect(detail,color=(.7,.75,.78),width=.8)
        p.show_pdf_page(full,src,0,keep_proportion=True)
        p.show_pdf_page(detail,src,0,clip=clip,keep_proportion=True)
    p.insert_text((36,510),"AMPLIACION FASE 5",fontsize=12,fontname="hebo",color=(.34,.43,.48))
    p.insert_text((612,510),"AMPLIACION PROTOTIPO",fontsize=12,fontname="hebo",color=(.10,.39,.50))
    p.insert_text((36,803),"Comparacion visual vectorial · detalles ampliados sin escala de obra",fontsize=11,fontname="helv",color=(.36,.44,.49))


def comparison():
    d=fitz.open()
    old_r=fitz.open(OLD/"07_tr_a.pdf"); new_r=fitz.open(PDF/"P1_TR_A.pdf")
    old_p=fitz.open(OLD/"02_pla_a.pdf"); new_p=fitz.open(PDF/"P2_PLANTA_A.pdf")
    # Source clip coordinates use PDF points; drawings use 1680x1188 logical units.
    k=1190.551/1680
    add_comparison_page(d,old_r,new_r,"01  /  ELEVACION TR-A",
                        fitz.Rect(200*k,650*k,800*k,1060*k),fitz.Rect(82*k,660*k,790*k,1000*k),"P1")
    add_comparison_page(d,old_p,new_p,"02  /  PLANTA DE CANALIZACIONES A",
                        fitz.Rect(130*k,420*k,980*k,820*k),fitz.Rect(80*k,490*k,1050*k,870*k),"P2")
    d.save(OUT/"COMPARATIVO_FASE5_VS_PROTOTIPOS.pdf",garbage=4,deflate=True)
    for x in (d,old_r,new_r,old_p,new_p): x.close()


def main():
    for d in (SVG,PDF,PNG): d.mkdir(parents=True,exist_ok=True)
    save_sheet(rack_prototype(),"P1_TR_A")
    save_sheet(plan_prototype(),"P2_PLANTA_A")
    comparison()
    print("Creados 2 SVG, 2 PDF A3, 2 PNG y comparativo vectorial de 2 páginas.")


if __name__=="__main__": main()
