"""Genera nueve láminas A3 vectoriales para la Fase 5.

Procedencia: composición gráfica asistida por OpenAI Codex a partir de los
requisitos y cantidades aprobados en los archivos del repositorio. Los datos
geométricos marcados como supuestos no son mediciones ni planos constructivos.
"""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape
import math
from io import BytesIO
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "08_entrega/ENTREGA_FINAL_INA_CENATE/06_PLANOS_TECNICOS"
SVG = OUT / "SVG_EDITABLE"
PDF = OUT / "PDF_A3"
PNG = OUT / "PNG"
W, H = 1680, 1188  # A3 horizontal, ratio 420:297
INK="#202D3A"; BLUE="#176B87"; TEAL="#319184"; ORANGE="#D17A35"; RED="#B44B4B"
GRAY="#667482"; LIGHT="#EEF2F5"; PALE="#F7F9FA"; GOLD="#D6AE46"; PURPLE="#7865A5"
WHITE="#FFFFFF"; BLACK="#111820"; GREEN="#418260"

class Sheet:
    def __init__(self, no, code, title, subtitle, scale="Esquemático — sin escala"):
        self.no, self.code, self.title, self.subtitle, self.scale = no, code, title, subtitle, scale
        self.svg=[]; self.buffer=BytesIO()
        self.pdf=canvas.Canvas(self.buffer,pagesize=(420/25.4*72,297/25.4*72),pageCompression=1)
        self.pdf.scale(420/25.4*72/W,420/25.4*72/W)
        self.svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 {W} {H}">',
                  '<style>text{font-family:Arial,Helvetica,sans-serif}</style>',
                  f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WHITE}"/>']
        self.rect(22,22,W-44,H-44,WHITE,INK,3,0)
        self.rect(22,22,W-44,104,INK,INK,0,0)
        self.txt(54,66,"INA · CENATE  /  CABLEADO ESTRUCTURADO",27,WHITE,True)
        self.txt(54,103,self.title,34,WHITE,True)
        self.txt(1620,63,f"LÁMINA {self.no:02d}/09",25,WHITE,True,"end")
        self.txt(1620,99,self.code,21,"#D8E4EA",True,"end")
        self.txt(54,153,self.subtitle,19,GRAY)
    def rect(self,x,y,w,h,fill=WHITE,stroke=INK,sw=2,r=0):
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        self.pdf.setFillColor(HexColor(fill)); self.pdf.setStrokeColor(HexColor(stroke)); self.pdf.setLineWidth(sw)
        self.pdf.roundRect(x,H-y-h,w,h,r,fill=1,stroke=1) if r else self.pdf.rect(x,H-y-h,w,h,fill=1,stroke=1)
    def line(self,x1,y1,x2,y2,color=INK,sw=2,dash=None):
        ds=f' stroke-dasharray="{dash}"' if dash else ''
        self.svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{ds}/>')
        self.pdf.setStrokeColor(HexColor(color)); self.pdf.setLineWidth(sw)
        self.pdf.setDash([int(v) for v in dash.split()] if dash else [])
        self.pdf.line(x1,H-y1,x2,H-y2); self.pdf.setDash()
    def poly(self, pts, color=INK, sw=3, fill="none", dash=None):
        p=" ".join(f"{x},{y}" for x,y in pts); ds=f' stroke-dasharray="{dash}"' if dash else ''
        self.svg.append(f'<polyline points="{p}" fill="{fill}" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{ds}/>')
        path=self.pdf.beginPath(); path.moveTo(pts[0][0],H-pts[0][1])
        for x,y in pts[1:]: path.lineTo(x,H-y)
        self.pdf.setStrokeColor(HexColor(color)); self.pdf.setLineWidth(sw)
        self.pdf.setFillColor(HexColor(fill if fill!="none" else WHITE)); self.pdf.setDash([int(v) for v in dash.split()] if dash else [])
        self.pdf.drawPath(path,stroke=1,fill=0); self.pdf.setDash()
    def circ(self,x,y,r,fill=WHITE,stroke=INK,sw=2):
        self.svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        self.pdf.setFillColor(HexColor(fill)); self.pdf.setStrokeColor(HexColor(stroke)); self.pdf.setLineWidth(sw); self.pdf.circle(x,H-y,r,fill=1,stroke=1)
    def txt(self,x,y,s,size=20,color=INK,bold=False,anchor="start"):
        s=str(s); weight="700" if bold else "400"
        self.svg.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color}">{escape(s)}</text>')
        self.pdf.setFillColor(HexColor(color)); self.pdf.setFont("Helvetica-Bold" if bold else "Helvetica",size)
        self.pdf.drawRightString(x,H-y,s) if anchor=="end" else self.pdf.drawCentredString(x,H-y,s) if anchor=="middle" else self.pdf.drawString(x,H-y,s)
    def textlines(self,x,y,lines,size=18,step=26,color=INK,bold=False):
        for i,s in enumerate(lines): self.txt(x,y+i*step,s,size,color,bold)
    def panel(self,x,y,w,h,title):
        self.rect(x,y,w,h,PALE,"#C8D1D8",1.5,5); self.txt(x+18,y+30,title,20,INK,True)
    def footer(self, note="Diseño académico preliminar. Revisar por el estudiante antes de entrega o uso."):
        self.line(42,1076,1638,1076,"#AEB9C2",2)
        self.rect(42,1083,1596,76,WHITE,"#82909B",1.5,0)
        self.line(42,1121,1638,1121,"#AEB9C2",1)
        for x in (1160,1320,1450): self.line(x,1083,x,1159,"#AEB9C2",1)
        self.txt(56,1108,"PROYECTO: INA CENATE | ELTT12000 | CABLEADO ESTRUCTURADO",15,INK,True)
        self.txt(1174,1108,"FECHA 2026-10-28",13,INK,True)
        self.txt(1333,1108,"REV. 0",13,INK,True)
        self.txt(1462,1108,f"LÁMINA {self.no:02d}/09",13,INK,True)
        self.txt(56,1147,note,13,GRAY)
        scale_label="VERTICAL 1U" if self.scale.startswith("Escala vertical") else "SIN ESCALA"
        self.txt(1174,1147,scale_label,12,INK,True)
        self.txt(1333,1147,"IA: apoyo visual",12,GRAY)
        self.txt(1462,1147,"NO CONSTRUCTIVO",11,RED,True)
    def finish(self, svgpath, pdfpath):
        self.svg.append('</svg>'); svgpath.write_text("\n".join(self.svg),encoding="utf-8")
        self.pdf.showPage(); self.pdf.save(); pdfpath.write_bytes(self.buffer.getvalue())

def boxlabel(s,x,y,w,h,lines,fill=WHITE,stroke=INK):
    s.rect(x,y,w,h,fill,stroke,2,4)
    for i,t in enumerate(lines): s.txt(x+w/2,y+25+i*24,t,17,INK,i==0,"middle")

def rack(s,x,y,w,unit_h,title,objects):
    total=42*unit_h
    s.rect(x,y-42,total if False else w,total+48,WHITE,INK,4,3)
    s.rect(x,y-42,w,42,LIGHT,INK,1,0); s.txt(x+w/2,y-13,title,19,INK,True,"middle")
    # bottom-to-top rack positions, each object is (U height, label, color)
    yy=y+total
    s.line(x+30,y,x+30,y+total,GRAY,2)
    for u in range(1,43):
        py=y+total-u*unit_h
        s.line(x+8,py,x+28,py,"#AAB4BC",1)
        s.txt(x+26,py+unit_h*.72,f"{u:02d}",11,GRAY,False,"end")
    for height,label,color in objects:
        yy-=height*unit_h
        s.rect(x+42,yy,w-54,height*unit_h-2,color,INK,1,1)
        s.txt(x+w/2+15,yy+height*unit_h/2+6,label,15,INK,True,"middle")
        yy-=2
    return y+total-yy

def exterior():
    s=Sheet(1,"EXT-01","BACKBONE EXTERIOR","Tres edificios · tres enlaces independientes · canalización y longitud de escenario")
    # topology schematic, clear route intersections and callouts
    boxlabel(s,100,245,350,164,["EDIFICIO EXISTENTE","ER PRINCIPAL · EXISTENTE","Sala existente; capacidad por verificar"],LIGHT,INK)
    boxlabel(s,665,245,350,164,["EDIFICIO A","ER-A · PROPIO","Acceso de fibra OS2 24F"],"#EAF4F6",BLUE)
    boxlabel(s,1230,245,350,164,["EDIFICIO B","ER-B · PROPIO","Acceso de fibra OS2 24F"],"#EAF4F6",BLUE)
    # underground route segments
    s.poly([(275,410),(275,600),(840,600),(840,412)],BLUE,9)
    s.poly([(275,600),(1405,600),(1405,412)],TEAL,7)
    s.poly([(840,600),(840,790),(1405,790),(1405,412)],PURPLE,7,dash="16 10")
    # pass-through theoretical handholes only on shared corridor route
    for i,x in enumerate([395,515,635,755,965,1085,1205]):
        s.rect(x-10,590,20,20,"#FFF5DC",ORANGE,2,2)
    # entry markers
    for x in (275,840,1405): s.rect(x-13,399,26,20,ORANGE,INK,2,2)
    s.txt(555,555,"E1 · ER principal ↔ ER-A · OS2 24F",20,BLUE,True,"middle")
    s.txt(1135,645,"E2 · ER principal ↔ ER-B · OS2 24F",20,TEAL,True,"middle")
    s.txt(1100,763,"E3 · ER-A ↔ ER-B · OS2 24F",20,PURPLE,True,"middle")
    s.panel(80,680,670,305,"LONGITUDES DE ESCENARIO — NO SON MEDICIONES")
    s.textlines(105,735,["E1 cable: 221,55 m = (145 + 50 + 16) × 1,05", "E2 cable: 247,80 m = (145 + 75 + 16) × 1,05", "E3 cable: 69,30 m = (50 + 16) × 1,05", "145 m reportados; 50 m propuestos; x=75 m e y=50 m supuestos.", "Ducto común 145 m + extensión a A 50 m: condición por validar.", "Los 16 m cubren entradas y reservas del escenario; 5 % desperdicio."],18,34)
    s.panel(800,680,800,305,"SÍMBOLOS Y CONDICIONES")
    s.line(830,745,950,745,BLUE,8); s.txt(975,752,"OS2 24F · E1",18)
    s.line(830,790,950,790,TEAL,7); s.txt(975,797,"OS2 24F · E2",18)
    s.line(830,835,950,835,PURPLE,7,dash="16 10"); s.txt(975,842,"OS2 24F · E3",18)
    s.rect(835,875,18,18,"#FFF5DC",ORANGE,2,2); s.txt(880,891,"Registro teórico, ubicación/cantidad sin validar en campo",17)
    s.txt(830,935,"Canalización subterránea existente / nueva: trazado esquemático, condición pendiente.",17,RED,True)
    s.footer("Recorridos, registros, ductos y entradas requieren levantamiento; longitudes de cable son resultados del escenario.")
    return s

def floorplan(building,labs,area,dim,panels,ports):
    no=2 if building=="A" else 3
    s=Sheet(no,f"PLA-{building}",f"DISTRIBUCIÓN DE CANASTAS Y TUBERÍAS · EDIFICIO {building}",f"Planta típica de referencia · {labs} laboratorios por piso · {area} m² por laboratorio · 1 TR/piso")
    # floor plan diagram as 3 on one side / remaining across corridor
    x0=115; labw=390; labh=230; gap=18; topn=(labs+1)//2
    for i in range(topn):
        x=x0+i*(labw+gap); y=205
        s.rect(x,y,labw,labh,"#F8FBFC",INK,3,0)
        # door gap and leaf
        s.line(x+28,y,x+90,y,WHITE,7); s.line(x+28,y,x+28,y+58,ORANGE,2)
        s.txt(x+18,y+34,f"LAB-{building}-Pxx-L{i+1:02d}",20,INK,True)
        s.txt(x+18,y+72,f"{area} m² · {dim} (supuesto)",17,GRAY)
        s.txt(x+18,y+108,"16 WA dobles · 32 puertos",17,BLUE,True)
        # branch route
        s.line(x+labw/2,y+labh,x+labw/2,560,ORANGE,5)
    botn=labs-topn
    for i in range(botn):
        x=x0+i*(labw+gap); y=605
        s.rect(x,y,labw,labh,"#F8FBFC",INK,3,0)
        s.line(x+28,y,x+90,y,WHITE,7); s.line(x+28,y,x+28,y+58,ORANGE,2)
        n=topn+i+1
        s.txt(x+18,y+34,f"LAB-{building}-Pxx-L{n:02d}",20,INK,True)
        s.txt(x+18,y+72,f"{area} m² · {dim} (supuesto)",17,GRAY)
        s.txt(x+18,y+108,"16 WA dobles · 32 puertos",17,BLUE,True)
        s.line(x+labw/2,560,x+labw/2,y,ORANGE,5)
    # corridor and main tray
    s.rect(90,475,1190,170,"#F0F2F4","#B8C1C8",1,0)
    s.txt(670,520,"PASILLO CENTRAL · ANCHO 2,4 m (SUPUESTO)",20,INK,True,"middle")
    s.line(120,570,1245,570,ORANGE,12)
    s.txt(680,558,"CANASTA PRINCIPAL · sección preliminar 100 × 50 mm",18,ORANGE,True,"middle")
    # branches down/up tie in
    for i in range(topn):
        xx=x0+i*(labw+gap)+labw/2; s.line(xx,435,xx,475,ORANGE,5)
    for i in range(botn):
        xx=x0+i*(labw+gap)+labw/2; s.line(xx,645,xx,670,ORANGE,5)
    # TR block with feeder
    s.rect(1325,425,250,300,"#FFF7E6",ORANGE,3,5)
    s.txt(1450,463,f"TR-{building}-Pxx",22,INK,True,"middle")
    s.txt(1450,498,"3 × 3 m (supuesto)",17,GRAY,False,"middle")
    s.txt(1450,547,f"{ports} puertos asignados",18,BLUE,True,"middle")
    s.txt(1450,579,f"{panels} × 48 = {panels*48} pos.",17,INK,False,"middle")
    s.txt(1450,611,f"{panels*48-ports} libres",17,GREEN,True,"middle")
    s.line(1280,570,1325,570,ORANGE,10)
    # legends
    s.panel(90,860,900,125,"LEYENDA DE CANALIZACIÓN")
    s.line(120,930,235,930,ORANGE,11); s.txt(260,938,"Canasta/bandeja principal y ramales",17)
    s.line(550,930,650,930,BLUE,4); s.txt(675,938,"Tubería a WA (trazado típico)",17)
    s.panel(1020,860,555,125,"NOTA DE DISEÑO")
    s.textlines(1045,917,["Muros/puertas esquemáticos. Tubo nominal Ø25 mm", "preliminar; confirmar ocupación y geometría."],17,26)
    s.footer("Geometría de edificio y posición de recintos son supuestos; hoja esquemática, sin escala numérica.")
    return s

def labplan(building,area,depth):
    no=4 if building=="A" else 5
    s=Sheet(no,f"WA-{building}",f"DISTRIBUCIÓN DE ÁREAS DE TRABAJO · EDIFICIO {building}",f"Laboratorio típico · {area} m² · geometría supuesta 10 × {depth} m · 16 WA dobles")
    x,y,w,h=140,230,1130,660
    s.rect(x,y,w,h,"#FCFDFD",INK,4,0)
    # door and swing
    s.line(600,y+h,720,y+h,WHITE,10); s.line(600,y+h,600,y+h-110,ORANGE,2); s.poly([(600,y+h),(710,y+h)],ORANGE,2)
    s.txt(660,y+h+35,"ACCESO",17,INK,True,"middle")
    # ceiling tray route and drop stubs
    s.poly([(230,285),(230,250),(1120,250),(1120,285)],ORANGE,10)
    s.txt(675,225,"CANASTA AÉREA PRINCIPAL · 100 × 50 mm (PRELIMINAR)",17,ORANGE,True,"middle")
    # room tables in four rows, four stations; each furniture module visibly separate
    for row in range(4):
        for col in range(4):
            xx=240+col*250; yy=330+row*130; n=row*4+col+1
            s.rect(xx,yy,175,72,"#EEF3F6","#8A98A4",2,5)
            s.txt(xx+87,yy+27,f"WA-{n:02d}",18,INK,True,"middle")
            s.txt(xx+87,yy+54,"PUESTO DOBLE",14,GRAY,False,"middle")
            # twin jacks in one faceplate, plus individual port labels
            s.rect(xx+56,yy+77,64,26,WHITE,BLUE,2,3)
            s.circ(xx+75,yy+90,5,BLUE,BLUE,1); s.circ(xx+101,yy+90,5,TEAL,TEAL,1)
            s.txt(xx+87,yy+121,"A / B",13,BLUE,True,"middle")
            cx=xx+87
            s.line(cx,250,cx,yy+75,BLUE,2,"5 5")
    # TR and cable homerun grouping
    s.rect(1340,300,245,205,"#FFF6E5",ORANGE,3,4)
    s.txt(1462,340,f"TR-{building}-Pxx",21,INK,True,"middle")
    s.textlines(1362,385,["Panel Cat 6A · 48 puertos", "Grupo de 32 enlaces", "Estrella · identificación", "de cable: A-Pxx-Lxx-WAxx-A/B"],16,30)
    s.poly([(1270,250),(1305,250),(1305,430),(1340,430)],BLUE,6)
    s.panel(1340,545,245,300,"CONTEO POR LABORATORIO")
    s.textlines(1362,600,["16 áreas WA", "2 puertos RJ45/WA", "32 conexiones Cat 6A", "1 grupo de salida al TR", "", "Asignación asumida", "según Excel corregido"],17,31)
    s.panel(140,925,1445,90,"SÍMBOLOS")
    s.rect(165,955,38,22,WHITE,BLUE,2,3); s.circ(177,966,4,BLUE,BLUE,1); s.circ(191,966,4,TEAL,TEAL,1)
    s.txt(220,973,"Área doble con RJ45-A / RJ45-B",16)
    s.line(565,966,655,966,BLUE,2,"5 5"); s.txt(675,973,"Derivación/canalización hacia puesto",16)
    s.line(1050,966,1140,966,BLUE,6); s.txt(1160,973,"Agrupación lógica de cableado Cat 6A al TR",16)
    s.footer("Representación por grupos; no se dibujan cables individuales superpuestos. Dos RJ45 por área es supuesto adoptado.")
    return s

def rack_sheet(building,kind):
    if kind=="ER":
        no=6 if building=="A" else 8; code=f"ER-{building}"; title=f"ELEVACIÓN DE EQUIPAMIENTO ÓPTICO · ER EDIFICIO {building}"
        cassette_count=6 if building=="A" else 9; housing=f"CCH-0{3 if building=='A' else 4}U · {cassette_count} cassettes"; vertical=4 if building=="A" else 7; positions=96 if building=="A" else 132
        extc="2 cassettes 24F (E1/E3)" if building=="A" else "2 cassettes 24F (E2/E3)"
        used=(3 if building=="A" else 4)+1+1+5
        open_u=42-used
        objs=[(3 if building=="A" else 4,housing,"#DDEEF3"),(1,"Organizador óptico horizontal", "#F8EBCB"),(1,"Guía / entrada backbone 12F", "#E2F0E7"),(5,"Reserva técnica · activos pendientes", "#F0ECF7"),(open_u,f"Espacio libre reservado · {open_u}U","#F8F9FA")]
        sub="Cassette integrado · terminación pasiva · activos sin selección"
    else:
        no=7 if building=="A" else 9; code=f"TR-{building}"; title=f"ELEVACIÓN FRONTAL DEL RACK · TR EDIFICIO {building}"
        panels=4 if building=="A" else 5; ports=160 if building=="A" else 192; spare=32 if building=="A" else 48
        objs=[(1,"CCH-01U · cassette 12F", "#DDEEF3"),(1,"Organizador óptico", "#F8EBCB")]
        for i in range(panels):
            assigned=min(48,max(0,ports-i*48)); reserved=48-assigned
            objs += [(2,f"PP-{building}-Pxx-{i+1:02d} · 48 puertos", "#DDEEF3" if reserved==0 else "#E2F0E7"),(1,f"Organizador · panel {i+1:02d}","#F8EBCB")]
        # Keep all 42U accounted for: named reserve plus unused capacity.
        fixed=sum(item[0] for item in objs)
        free=42-fixed-5
        objs += [(5,"Reserva técnica · activos/energía pendientes", "#F0ECF7"),(free,f"Espacio libre reservado · {free}U", "#F8F9FA")]
        sub=f"{panels} patch panels × 48 puertos · {ports} asignados · {spare} posiciones libres"
    s=Sheet(no,code,title,sub,"Escala vertical: 1U uniforme · gabinete propuesto 42U")
    rx,ry,rw,uh=210,260,500,18
    used=rack(s,rx,ry,rw,uh,f"RACK {code} · 19 in · 42U",objs)
    s.txt(rx+rw/2,ry+42*uh+40,"ELEVACIÓN FRONTAL · UNIDADES NUMERADAS DE ABAJO HACIA ARRIBA",16,GRAY,True,"middle")
    # Detailed optical terminations and cable paths
    if kind=="ER":
        s.panel(800,225,770,315,"TERMINACIÓN Y CAPACIDAD ÓPTICA")
        s.textlines(830,282,["Exterior: 2 × OS2 24F llegan a cada ER nuevo.",f"Vertical: {vertical} cables OS2 12F hacia TR; {vertical*12} fibras.",f"Capacidad por cuarto: {positions} posiciones de fibra.",housing+" · el cassette incluye pigtails / adaptadores según matriz.","El diagrama no agrega pigtails ni adaptadores sueltos.","Un par dúplex por enlace: patch cords representativos;", "transceptores y puertos activos no especificados."],18,34)
        s.panel(800,580,770,320,"ESQUEMA DE CONEXIÓN · NO A ESCALA")
        boxlabel(s,835,680,180,100,["E1 / E2 / E3","24F OS2"],"#EAF4F6",BLUE)
        boxlabel(s,1110,680,205,100,[housing,"LC dúplex"],"#F4F0FA",PURPLE)
        boxlabel(s,1410,680,125,100,["12F","TR"],"#EAF5ED",GREEN)
        s.line(1015,730,1110,730,BLUE,6); s.line(1315,730,1410,730,GREEN,6)
        s.txt(1062,710,"24F",15,BLUE,True,"middle"); s.txt(1362,710,"12F",15,GREEN,True,"middle")
        s.txt(835,835,"CCH-03U (A): 4 × 12F + 2 × 24F = 96 fibras.",17,INK,True)
        s.txt(835,870,"CCH-04U (B): 7 × 12F + 2 × 24F = 132 fibras.",17,INK,True)
        s.panel(800,930,770,115,"RUTAS")
        s.txt(830,985,"Exterior desde ducto subterráneo · reserva en rack · entrada vertical a TR",16)
    else:
        panels=4 if building=="A" else 5; ports=160 if building=="A" else 192; spare=32 if building=="A" else 48
        s.panel(800,225,770,170,"ASIGNACIÓN POR PISO")
        s.textlines(830,280,[f"{ports} salidas Cat 6A asignadas a laboratorios del piso.",f"{panels} paneles de 48 = {panels*48} posiciones físicas.",f"Libres/reserva: {spare}; no representan puertos de switch activos."],18,34)
        # panel face detail grid with 48 port marks for an example fully assigned and final panel
        s.panel(800,425,770,410,"DETALLE DE PUERTOS · 48 POSICIONES POR PANEL")
        last_assigned=16 if building=="A" else 48
        for row,(label,assigned) in enumerate([("Panel inicial · asignación",48),("Panel final · asignación",last_assigned)]):
            yy=500+row*145; s.txt(830,yy,label,17,INK,True)
            for i in range(48):
                xx=830+(i%16)*39; y2=yy+20+(i//16)*25
                col=BLUE if i<assigned else "#DCE3E8"
                s.rect(xx,y2,25,15,col,INK if i<assigned else "#AAB5BE",1,2)
            s.txt(1590,yy+58,f"{assigned} asignados",16,BLUE if assigned else GRAY,True,"end")
        s.txt(830,800,"Azul = posición asignada · gris claro = reserva libre · numeración por bloque 01–48",16)
        s.panel(800,860,770,185,"CONEXIÓN Y SALIDA")
        labs=5 if building=="A" else 6
        ranges=("PP01–03: 01–48; PP04: 01–16 asignados, 17–48 libres." if building=="A" else "PP01–04: 01–48 asignados; PP05: 01–48 libres.")
        s.textlines(830,915,["ER-"+building+" → OS2 12F → cassette CCH integrado (1 por extremo).",f"Cat 6A en estrella: grupos identificados hacia {labs} laboratorios.",ranges,"Cordones representativos; sin atribuir enlaces a puertos activos."],16,30)
    s.footer("Racks de 42U propuestos; dimensiones y capacidad final de instalación requieren validación del recinto.")
    return s

def make_all():
    for d in (SVG,PDF,PNG): d.mkdir(parents=True,exist_ok=True)
    sheets=[exterior(),floorplan("A",5,85,"10 × 8,5 m",4,160),floorplan("B",6,75,"10 × 7,5 m",5,192),labplan("A",85,"8,5"),labplan("B",75,"7,5"),rack_sheet("A","ER"),rack_sheet("A","TR"),rack_sheet("B","ER"),rack_sheet("B","TR")]
    pages=[]
    for s in sheets:
        stem=f"{s.no:02d}_{s.code.lower().replace('-','_')}"
        pp=PDF/(stem+".pdf"); sp=SVG/(stem+".svg")
        # Footer already assembled by each composition.
        s.finish(sp,pp); pages.append(pp)
        doc=fitz.open(pp); pix=doc[0].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False)
        pix.save(PNG/(stem+".png")); doc.close()
    merged=fitz.open()
    for p in pages:
        d=fitz.open(p); merged.insert_pdf(d); d.close()
    combined=OUT/"PLANOS_TECNICOS_INA_CENATE_9_LAMINAS.pdf"; merged.save(combined,garbage=4,deflate=True); merged.close()
    print(f"Hojas: {len(sheets)}; SVG {len(list(SVG.glob('*.svg')))}; PDF {len(list(PDF.glob('*.pdf')))}; PNG {len(list(PNG.glob('*.png')))}; combinado {combined.relative_to(ROOT)}")

if __name__=="__main__": make_all()
