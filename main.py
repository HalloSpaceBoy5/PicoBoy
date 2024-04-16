# Original home screen for PicoBoy by HalloSpaceBoy
from micropython import const
from framebuf import FrameBuffer,RGB565
from PicoGameBoy import PicoGameBoy
import time
from random import randint
import array
import os
import sys
from random import randint
import machine


BLACK = PicoGameBoy.color(0,0,0)
WHITE = PicoGameBoy.color(255,255,255)
pgb = PicoGameBoy()
vpin = machine.ADC(29)
games=os.listdir("/games")
loop=0
gamenum=len(games)-1
title=0
pastpercentage=[]
pastpercent=101


def readchunk(filename, x2, y2, w, h):
    if x2>240:
        time.sleep(0.005)
        return
    buffersize=w*2
    p=240-w-x2
    if p<0:
        e=abs(240-x2)
        buffersize=e*2
    if p<0:
        p=abs(p)
    else:
        p=0
    o=0
    x=bytearray(p*2)
    with open(filename, "rb") as image_file:
        for y in range(h):
            existing_line_start = ((y + y2) * 240 + x2) * 2
            image_file.readinto(pgb.buffer[existing_line_start:existing_line_start + buffersize])
            image_file.readinto(x[0:p*2])
            o+=p



def readchunkold(filename,x2,y2,w,h,i=0,z=6):
    t=int(h/z)
    with open(filename,"rb") as r:
        for x in range(6):
            tempfb=FrameBuffer(bytearray(r.read((2*w)*t)),w,t,RGB565)
            pgb.blit(tempfb,x2,y2+x*t)
            del tempfb
     
def readchunk_mask(filename,x2,y2,w,h,cmask):
    gren=PicoGameBoy.color(0,255,0)
    with open(filename,"rb") as r:
            for x in range(h):
                tempfb=FrameBuffer(bytearray(r.read(2*w)),w,1,RGB565)
                pgb.blit(tempfb,x2,y2+x,gren)
                del tempfb

def draw_image(ts=-1):
    global imagedata
    ps=int(240/len(imagedata))
    y=-1
    for i in imagedata:
        y+=1
        x=-1
        if not ts==-1:
            if ts==0:
                skip=True
            elif y in range(0,ts):
                skip=True
            else:
                skip=False
        else:
            skip=False
        if not skip:
            for f in i:
                x+=1
                pgb.fill_rect(x*ps,y*ps,ps,ps,f)
    time.sleep(0.1)

def getimagedata():
    global imagedata
    global bgimagefile
    imagedata=[]
    with open(bgimagefile) as f:
        for i in range(30):
            comp=[]
            for x in f.readline().split(":"):
                comp.append(int(x))
            imagedata.append(comp)
    del comp
    del f


bootlogo=True
try:
    x=open("/noboot", "r")
    x.close()
    os.remove("/noboot")
    bootlogo=False
    try:
        with open("gameselection.conf", "r") as r:
            title=int(r.read())
    except:
        "config nonexistent"
except:
    bootlogo=True
if bootlogo:
    pgb.fill(BLACK)
    readchunk("logo.pbimg",88,50,64,64)
    #with open("logo.pbimg","rb") as r:
    #    data=r.read()
    #tempfb=FrameBuffer(bytearray(data),64,64,RGB565)
    #pgb.blit(tempfb,88,50)
    #del tempfb
    readchunk("logo-text.pbimg",69,150,102,15)
    #with open("logo-text.pbimg","rb") as r:
    #    data=r.read()
    #tempfb=FrameBuffer(bytearray(data),102,15,RGB565)
    #pgb.blit(tempfb,69,150)
    #del tempfb
    pgb.show_screen()
    pgb.sound(98)
    time.sleep(0.2)
    pgb.sound(0)
    pgb.sound(185)
    time.sleep(0.2)
    pgb.sound(0)
    pgb.sound(164)
    time.sleep(0.2)
    pgb.sound(0)
    time.sleep(0.9)

bgcolors=(
    (215, 0, 0),
    (227, 160, 5),
    (220, 213, 0),
    (0, 205, 0),
    (0, 0, 205),
    (141, 2, 171),
    (227, 52, 189),
    (161, 161, 161),
    (69, 69, 69),
    (0,0,0),
    (255,255,255))

if gamenum==-1:
    pgb.fill(PicoGameBoy.color(0,0,0))
    pgb.create_text("NO GAMES DETECTED",-1,50,PicoGameBoy.color(255,255,255))
    pgb.create_text("Plug your PicoBoy",-1, 100,PicoGameBoy.color(255,255,255))
    pgb.create_text("into your computer",-1,112,PicoGameBoy.color(255,255,255))
    pgb.create_text("and run the PicoBoy",-1,124,PicoGameBoy.color(255,255,255))
    pgb.create_text("Communication Software",-1,136,PicoGameBoy.color(255,255,255))
    pgb.create_text("to upload games",-1,148,PicoGameBoy.color(255,255,255))
    pgb.show()
    sys.exit()

try:
    with open("background.conf","r") as r:
        data=r.read()
    try:    
        bindex=int(data)
        bgimage=False
    except:
        bgimage=True
        bgcolor=(69,69,69)
        bgcolor565=PicoGameBoy.color(69,69,69)
        bgimagefile=data[:]
except:
    bindex=8
    bgimage=False

if bgimage:
    try:
        with open(bgimagefile, "r") as r:
            r.read()
        getimagedata()
    except:
        with open("background.conf","w") as w:
            w.write("8")
        bindex=8
        bgimage=False


arrowright=array.array('h',[0,0,0,20,20,10])
arrowleft=array.array('h',[0,0,0,20,-20,10])
arrowrightbg=array.array('h',[0,0,0,30,30,15])
arrowleftbg=array.array('h',[0,0,0,30,-30,15])
c1=array.array('h',[0,0,0,5,5,0])
c2=array.array('h',[0,0,0,-5,5,0])
c3=array.array('h',[0,0,0,5,-5,0])
c4=array.array('h',[0,0,0,-5,-5,0])

if not bgimage:
    if bindex>len(bgcolors)-1:
        bindex=8
    bgcolor=bgcolors[bindex]
    bgcolor565=PicoGameBoy.color(*bgcolor)
    pgb.fill(PicoGameBoy.color(*bgcolor))
else:
    draw_image()
if not bgimage:
    if sum(bgcolor)<765: #426
        tcolor=1
    else:
        tcolor=0
else:
    tcolor=1
if tcolor==0:
    ottcolor=PicoGameBoy.color(255,255,255)
else:
    ottcolor=PicoGameBoy.color(0,0,0)
ttcolor=PicoGameBoy.color(255,255,255)
if bgimage:
    pgb.fill_rect(15,15,208,30,bgcolor565)
    pgb.fill_rect(15,10,208,5,bgcolor565)
    pgb.fill_rect(15,45,208,5,bgcolor565)
    pgb.fill_rect(10,15,5,30,bgcolor565)
    pgb.fill_rect(223,15,5,30,bgcolor565)
    pgb.poly(10,10,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
    pgb.poly(222,10,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
    pgb.poly(10,49,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
    pgb.poly(222,49,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
readchunk_mask("picoboy-color.pbimg",0,0,240,60,bgcolor)
if tcolor==0:
    ttcolor=PicoGameBoy.color(0,0,0)
pos=[]
if title<=gamenum:
    pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,65,int(len(games[title]) * 8)+10,140,bgcolor565)
    pgb.fill_rect(55,65,130,140,bgcolor565)
    
    #Text rect
    pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-10,65,5,140,bgcolor565)
    pgb.fill_rect(int(120)+ int(len(games[title])/2 * 8)+5,65,5,140,bgcolor565)
    pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,60,int(len(games[title]) * 8)+10,5,bgcolor565)
    pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,205,int(len(games[title]) * 8)+10,5,bgcolor565)
    pgb.poly(int(120)- int(len(games[title])/2 * 8)-10,60,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
    pgb.poly(120+int(int(len(games[title]) * 8)/2)+5,60,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
    pgb.poly(int(120)- int(len(games[title])/2 * 8)-10,209,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
    pgb.poly(120+int(int(len(games[title]) * 8)/2)+5,209,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
    
    #App rect
    pgb.fill_rect(50,65,5,140,bgcolor565)
    pgb.fill_rect(185,65,5,140,bgcolor565)
    pgb.fill_rect(55,60,130,5,bgcolor565)
    pgb.fill_rect(55,205,130,5,bgcolor565)
    pgb.poly(50,60,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
    pgb.poly(184,60,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
    pgb.poly(50,209,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
    pgb.poly(184,209,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
    for i in range(title):
        pos.append(".")
    pos.append("0")
    for i in range((gamenum+1)-(title+1)):
        pos.append(".")
    pgb.fill_rect(int(120)- int(len("".join(pos)+"S")/2 * 8)-5,225,int(len("".join(pos)+"S") * 8)+10,10,bgcolor565)
    #Pos rect
    pgb.fill_rect(int(120)- int(len("".join(pos)+"S")/2 * 8)-10,225,5,10,bgcolor565)
    pgb.fill_rect(int(120)+ int(len("".join(pos)+"S")/2 * 8)+5,225,5,10,bgcolor565)
    pgb.fill_rect(int(120)- int(len("".join(pos)+"S")/2 * 8)-5,220,int(len("".join(pos)+"S") * 8)+10,5,bgcolor565)
    pgb.fill_rect(int(120)- int(len("".join(pos)+"S")/2 * 8)-5,235,int(len("".join(pos)+"S") * 8)+10,5,bgcolor565)
    pgb.poly(int(120)- int(len("".join(pos)+"S")/2 * 8)-10,220,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
    pgb.poly(120+int(int(len("".join(pos)+"S") * 8)/2)+4,220,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
    pgb.poly(int(120)- int(len("".join(pos)+"S")/2 * 8)-10,240,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
    pgb.poly(120+int(int(len("".join(pos)+"S") * 8)/2)+4,240,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
    ##########
    pgb.create_text("".join(pos)+"S", x=-1, y=228,color=ttcolor)
    if title<=gamenum:
        pgb.create_text(games[title],-1,65,ttcolor)
    else:
        pgb.create_text("Settings",-1,65,ttcolor)
    try:
        readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60,80,120,120)
    except:
        pgb.fill_rect(60,80,120,120,ttcolor)
        pgb.create_text("No Image",-1,140,ottcolor)
        time.sleep(0.1)
    if title==0:
        pgb.poly(197,125,arrowrightbg,bgcolor565,True)
        pgb.poly(200,130,arrowright,ttcolor,True)
    else:
        pgb.poly(197,125,arrowrightbg,bgcolor565,True)
        pgb.poly(43,125,arrowleftbg,bgcolor565,True)
        pgb.poly(200,130,arrowright,ttcolor,True)
        pgb.poly(40,130,arrowleft,ttcolor,True)
    pgb.poly(60,80,c1,bgcolor565,True)
    pgb.poly(60,200,c2,bgcolor565,True)
    pgb.poly(180,80,c3,bgcolor565,True)
    pgb.poly(180,200,c4,bgcolor565,True)
    pgb.show()
    onsett=False
else:
    onsett=True
    
    
def draw_battery():
    global pastpercentage
    global pastpercent
    adc_reading  = vpin.read_u16()
    adc_voltage  = (adc_reading * 3.3) / 65535
    vsys_voltage = adc_voltage * 12
    console=0
    if vsys_voltage>10:
        vsys_voltage = adc_voltage * 3
        percentage=int(int(((round(vsys_voltage,3)-1.9)/2.7)*100))
        console=1
    else:
        percentage=int(int(((round(vsys_voltage,3)-1.9)/1)*100))
        console=0
    if vsys_voltage<1.9:
        pgb.fill(BLACK)
        pgb.create_text("BATTERY CRITICALLY LOW!",-1,30,WHITE)
        pgb.create_text("Please replace the", -1, 130, WHITE)
        pgb.create_text("batteries in your PicoBoy.", -1, 145, WHITE)
        pgb.create_text("Please switch your", -1, 200, WHITE)
        pgb.create_text("PicoBoy off.", -1, 215, WHITE)
        pgb.rect(75,60,80,40,PicoGameBoy.color(255,0,0))
        pgb.fill_rect(155,70,10,20,PicoGameBoy.color(255,0,0))
        pgb.line(75,60,155,99,PicoGameBoy.color(255,0,0))
        pgb.show()
        sys.exit()
    if console==0:
        if percentage>100 and percentage<125:
            percentage=100
        if percentage<130:
            pastpercentage.append(percentage)
            if len(pastpercentage)>200:
                pastpercentage.pop(0)
            percentage=int(int(sum(pastpercentage)/len(pastpercentage)))
    elif console==1:
        if percentage>100 and percentage<110:
            percentage=100
        if percentage<110:
            pastpercentage.append(percentage)
            if len(pastpercentage)>200:
                pastpercentage.pop(0)
            percentage=int(int(sum(pastpercentage)/len(pastpercentage)))
    
        
    battx=9
    batty=183
    pgb.rect(battx,batty,20,40,ttcolor)
    pgb.fill_rect(battx+5,batty-4,10,5,ttcolor)
    if percentage>100:
        pgb.create_text("U",battx+6, batty+7,ttcolor)
        pgb.create_text("S",battx+6, batty+17,ttcolor)
        pgb.create_text("B",battx+6, batty+27,ttcolor)
        pgb.create_text("USB",battx+10-int(len(str(percentage))/2 * 8), batty+44, ttcolor)
    else:
        h=int(38*(percentage/100))
        pgb.fill_rect(battx+1,batty+1+(38-h),18,h,ttcolor)
        pgb.create_text(str(percentage)+"%",battx+10-int(len(str(percentage)+"%")/2 * 8), batty+43, ttcolor)
    
def draw_battery_backing():
    battx=9
    batty=183
    pgb.fill_rect(battx-2,batty-4,24,55,bgcolor565)
    pgb.fill_rect(battx-5-2,batty-4,5,55,bgcolor565)
    pgb.fill_rect(battx+20+2,batty-4,5,55,bgcolor565)
    pgb.fill_rect(battx-2,batty-9,24,5,bgcolor565)
    pgb.fill_rect(battx-2,batty+51,24,5,bgcolor565)
    pgb.poly(battx-5-2,batty-9,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
    pgb.poly(battx+19+2,batty-9,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
    pgb.poly(battx-5-2,batty+55,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
    pgb.poly(battx+19+2,batty+55,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)

def render(f=True):
        if bgimage:
            draw_image(7)
        else:
            pgb.fill_rect(0,65,240,140,bgcolor565)
        pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,65,int(len(games[title]) * 8)+10,140,bgcolor565)
        pgb.fill_rect(55,65,130,140,bgcolor565)
        
        #Text rect
        pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-10,65,5,140,bgcolor565)
        pgb.fill_rect(int(120)+ int(len(games[title])/2 * 8)+5,65,5,140,bgcolor565)
        pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,60,int(len(games[title]) * 8)+10,5,bgcolor565)
        pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,205,int(len(games[title]) * 8)+10,5,bgcolor565)
        pgb.poly(int(120)- int(len(games[title])/2 * 8)-10,60,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
        pgb.poly(120+int(int(len(games[title]) * 8)/2)+5,60,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
        pgb.poly(int(120)- int(len(games[title])/2 * 8)-10,209,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
        pgb.poly(120+int(int(len(games[title]) * 8)/2)+5,209,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
        
        #App rect
        pgb.fill_rect(50,65,5,140,bgcolor565)
        pgb.fill_rect(185,65,5,140,bgcolor565)
        pgb.fill_rect(55,60,130,5,bgcolor565)
        pgb.fill_rect(55,205,130,5,bgcolor565)
        pgb.poly(50,60,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
        pgb.poly(184,60,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
        pgb.poly(50,209,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
        pgb.poly(184,209,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
        
        pos=[]
        for i in range(title):
            pos.append(".")
        pos.append("0")
        for i in range((gamenum+1)-(title+1)):
            pos.append(".")
        pgb.fill_rect(int(120)- int(len("".join(pos)+"S")/2 * 8)-5,225,int(len("".join(pos)+"S") * 8)+10,10,bgcolor565)
        #Pos rect
        pgb.fill_rect(int(120)- int(len("".join(pos)+"S")/2 * 8)-10,225,5,10,bgcolor565)
        pgb.fill_rect(int(120)+ int(len("".join(pos)+"S")/2 * 8)+5,225,5,10,bgcolor565)
        pgb.fill_rect(int(120)- int(len("".join(pos)+"S")/2 * 8)-5,220,int(len("".join(pos)+"S") * 8)+10,5,bgcolor565)
        pgb.fill_rect(int(120)- int(len("".join(pos)+"S")/2 * 8)-5,235,int(len("".join(pos)+"S") * 8)+10,5,bgcolor565)
        pgb.poly(int(120)- int(len("".join(pos)+"S")/2 * 8)-10,220,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
        pgb.poly(120+int(int(len("".join(pos)+"S") * 8)/2)+4,220,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
        pgb.poly(int(120)- int(len("".join(pos)+"S")/2 * 8)-10,240,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
        pgb.poly(120+int(int(len("".join(pos)+"S") * 8)/2)+4,240,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
        ##########
        pgb.create_text("".join(pos)+"S", x=-1, y=228,color=ttcolor)
        pgb.create_text(games[title],-1,65,ttcolor)
        try:
            readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60,80,120,120)
        except:
            pgb.fill_rect(60,80,120,120,ttcolor)
            pgb.create_text("No Image",-1,140,ottcolor)
            time.sleep(0.005)
        if title==0:
            pgb.poly(197,125,arrowrightbg,bgcolor565,True)
            pgb.poly(200,130,arrowright,ttcolor,True)
        else:
            pgb.poly(197,125,arrowrightbg,bgcolor565,True)
            pgb.poly(43,125,arrowleftbg,bgcolor565,True)
            pgb.poly(200,130,arrowright,ttcolor,True)
            pgb.poly(40,130,arrowleft,ttcolor,True)
        pgb.poly(60,80,c1,bgcolor565,True)
        pgb.poly(60,200,c2,bgcolor565,True)
        pgb.poly(180,80,c3,bgcolor565,True)
        pgb.poly(180,200,c4,bgcolor565,True)
        if f:
            pgb.show()

try:
    with open("/animated.conf") as r:
        if r.read()=="True":
            animated=True
        else:
            animated=False
except:
    animated=True

while True:
    if pgb.button_left() and title>0 and not onsett:
        if animated and not bgimage:
            incr=20
            draw_battery_backing()
            for i in range(12): #3 is good
                i+=1
                pgb.fill_rect(0,78,240,130,bgcolor565)
                try:
                    readchunk(games[title-1]+"/"+games[title-1]+" (Title Image).pbimg",-180+(i*incr),81,120,120)
                except:
                    pgb.fill_rect(-180+(i*incr),81,120,120,ttcolor)
                    pgb.create_text("No Image",-152+(i*incr),140,ottcolor)
                    time.sleep(0.005)
                try:
                    readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60+(i*incr),80,120,120)
                except:
                    pgb.fill_rect(60+(i*incr),80,120,120,ttcolor)
                    pgb.create_text("No Image",84+(i*incr),140,ottcolor)
                    time.sleep(0.005)
                pgb.poly(60+(i*incr),80,c1,bgcolor565,True)
                pgb.poly(60+(i*incr),200,c2,bgcolor565,True)
                pgb.poly(180+(i*incr),80,c3,bgcolor565,True)
                pgb.poly(180+(i*incr),200,c4,bgcolor565,True)
                pgb.poly(-180+(i*incr),80,c1,bgcolor565,True)
                pgb.poly(-180+(i*incr),200,c2,bgcolor565,True)
                pgb.poly(-60+(i*incr),80,c3,bgcolor565,True)
                pgb.poly(-60+(i*incr),200,c4,bgcolor565,True)
                pgb.show()
        elif not bgimage:
            time.sleep(0.1)
        if not bgimage:
            pgb.fill_rect(0,78,240,130,bgcolor565)
        
        title-=1
        render(False)
        draw_battery_backing()
        draw_battery()
        pgb.show()
    if pgb.button_right() and title<gamenum and not onsett:
        if animated and not bgimage:
            incr=20
            draw_battery_backing()
            for i in range(12):
                i+=1
                pgb.fill_rect(0,80,240,130,bgcolor565)
                try:
                    readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60-(i*incr),81,120,120)
                except:
                        pgb.fill_rect(60-(i*incr),80,120,120,ttcolor)
                        pgb.create_text("No Image",84-(i*incr),140,ottcolor)
                        time.sleep(0.005)
                try:
                    readchunk(games[title+1]+"/"+games[title+1]+" (Title Image).pbimg",300-(i*incr),80,120,120)
                except:
                    pgb.fill_rect(300-(i*incr),80,120,120,ttcolor)
                    pgb.create_text("No Image",328-(i*incr),140,ottcolor)
                    time.sleep(0.005)
                pgb.poly(60-(i*incr),80,c1,bgcolor565,True)
                pgb.poly(60-(i*incr),200,c2,bgcolor565,True)
                pgb.poly(180-(i*incr),80,c3,bgcolor565,True)
                pgb.poly(180-(i*incr),200,c4,bgcolor565,True)
                pgb.poly(300-(i*incr),80,c1,bgcolor565,True)
                pgb.poly(300-(i*incr),200,c2,bgcolor565,True)
                pgb.poly(420-(i*incr),80,c3,bgcolor565,True)
                pgb.poly(420-(i*incr),200,c4,bgcolor565,True)
                pgb.show()
        elif not bgimage:
            time.sleep(0.1)
        if not bgimage:
            pgb.fill_rect(0,80,240,130,bgcolor565)
        title+=1
        render(False)
        draw_battery_backing()
        draw_battery()
        pgb.show()
    if (pgb.button_right() and title==gamenum) or onsett:
            if onsett:
                title-=1
            if animated and not onsett and not bgimage:
                incr=20
                draw_battery_backing()
                for i in range(12):
                    i+=1
                    pgb.fill_rect(0,80,240,130,bgcolor565)
                    try:
                        readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60-(i*incr),81,120,120)
                    except:
                        pgb.fill_rect(60-(i*incr),81,120,120,ttcolor)
                        pgb.create_text("No Image",84-(i*incr),140,ottcolor)
                        time.sleep(0.005)
                    readchunk("settings.pbimg",300-(i*incr),80,120,120)
                    pgb.poly(60-(i*incr),80,c1,bgcolor565,True)
                    pgb.poly(60-(i*incr),200,c2,bgcolor565,True)
                    pgb.poly(180-(i*incr),80,c3,bgcolor565,True)
                    pgb.poly(180-(i*incr),200,c4,bgcolor565,True)
                    pgb.poly(300-(i*incr),80,c1,bgcolor565,True)
                    pgb.poly(300-(i*incr),200,c2,bgcolor565,True)
                    pgb.poly(420-(i*incr),80,c3,bgcolor565,True)
                    pgb.poly(420-(i*incr),200,c4,bgcolor565,True)
                    pgb.show()
            elif not bgimage:
                time.sleep(0.1)
            if not bgimage:
                pgb.fill_rect(0,78,240,130,bgcolor565)
            onsett=False
            if bgimage:
                draw_image(7)
            else:
                pgb.fill_rect(0,50,240,190,bgcolor565)
            pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,65,int(len(games[title]) * 8)+10,140,bgcolor565)
            pgb.fill_rect(55,65,130,140,bgcolor565)
            
            #Text rect
            pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-10,65,5,140,bgcolor565)
            pgb.fill_rect(int(120)+ int(len(games[title])/2 * 8)+5,65,5,140,bgcolor565)
            pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,60,int(len(games[title]) * 8)+10,5,bgcolor565)
            pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,205,int(len(games[title]) * 8)+10,5,bgcolor565)
            pgb.poly(int(120)- int(len(games[title])/2 * 8)-10,60,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
            pgb.poly(120+int(int(len(games[title]) * 8)/2)+5,60,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
            pgb.poly(int(120)- int(len(games[title])/2 * 8)-10,209,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
            pgb.poly(120+int(int(len(games[title]) * 8)/2)+5,209,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
            
            #App rect
            pgb.fill_rect(50,65,5,140,bgcolor565)
            pgb.fill_rect(185,65,5,140,bgcolor565)
            pgb.fill_rect(55,60,130,5,bgcolor565)
            pgb.fill_rect(55,205,130,5,bgcolor565)
            pgb.poly(50,60,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
            pgb.poly(184,60,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
            pgb.poly(50,209,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
            pgb.poly(184,209,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
            pos=[]
            for i in range(title):
                pos.append(".")
            pos.append("0")
            for i in range((gamenum+1)-(title+1)):
                pos.append(".")
            pgb.fill_rect(int(120)- int(len("".join(pos).replace("0",".")+"0")/2 * 8)-5,225,int(len("".join(pos).replace("0",".")+"0") * 8)+10,20,bgcolor565)
            pgb.fill_rect(int(120)- int(len("".join(pos).replace("0",".")+"0")/2 * 8)-10,225,5,10,bgcolor565)
            pgb.fill_rect(int(120)+ int(len("".join(pos).replace("0",".")+"0")/2 * 8)+5,225,5,10,bgcolor565)
            pgb.fill_rect(int(120)- int(len("".join(pos).replace("0",".")+"0")/2 * 8)-5,220,int(len("".join(pos).replace("0",".")+"0") * 8)+10,5,bgcolor565)
            pgb.fill_rect(int(120)- int(len("".join(pos).replace("0",".")+"0")/2 * 8)-5,235,int(len("".join(pos).replace("0",".")+"0") * 8)+10,5,bgcolor565)
            pgb.poly(int(120)- int(len("".join(pos).replace("0",".")+"0")/2 * 8)-10,220,array.array('h',[5,5,0,5,5,0]),bgcolor565,True)
            pgb.poly(120+int(int(len("".join(pos).replace("0",".")+"0") * 8)/2)+4,220,array.array('h',[0,5,5,5,0,0]),bgcolor565,True)
            pgb.poly(int(120)- int(len("".join(pos).replace("0",".")+"0")/2 * 8)-10,240,array.array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
            pgb.poly(120+int(int(len("".join(pos).replace("0",".")+"0") * 8)/2)+4,240,array.array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
            pgb.create_text("".join(pos).replace("0",".")+"0", x=-1, y=228,color=ttcolor)
            pgb.create_text("Settings",-1,65,ttcolor)
            readchunk("settings.pbimg",60,80,120,120)
            pgb.poly(43,125,arrowleftbg,bgcolor565,True)
            pgb.poly(40,130,arrowleft,ttcolor,True)
            pgb.poly(60,80,c1,bgcolor565,True)
            pgb.poly(60,200,c2,bgcolor565,True)
            pgb.poly(180,80,c3,bgcolor565,True)
            pgb.poly(180,200,c4,bgcolor565,True)
            draw_battery_backing()
            draw_battery()
            pgb.show()
            while True:
                draw_battery()
                pgb.show()
                draw_battery_backing()
                if pgb.button_A() or pgb.button_start():
                    with open("gameselection.conf", "w") as w:
                        w.write(str(title+1))
                    os.rename("./main.py", "./title.py")
                    os.rename("settings.py", "./main.py")
                    pgb.fill(PicoGameBoy.color(0,0,0))
                    pgb.show()
                    machine.reset()
                    break
                if pgb.button_select() and pgb.button_B() and pgb.button_down():
                    pgb.fill(PicoGameBoy.color(0,0,0))
                    pgb.create_text("DATA UPLOAD MODE",-1,50,PicoGameBoy.color(255,255,255))
                    pgb.create_text("Plug your PicoBoy",-1, 100,PicoGameBoy.color(255,255,255))
                    pgb.create_text("into your computer",-1,112,PicoGameBoy.color(255,255,255))
                    pgb.create_text("and run the PicoBoy",-1,124,PicoGameBoy.color(255,255,255))
                    pgb.create_text("Communication Software.",-1,136,PicoGameBoy.color(255,255,255))
                    pgb.create_text("To exit data",-1,180,PicoGameBoy.color(255,255,255))
                    pgb.create_text("upload mode reset",-1,192,PicoGameBoy.color(255,255,255))
                    pgb.create_text("your PicoBoy.",-1,204,PicoGameBoy.color(255,255,255))
                    pgb.show()
                    sys.exit()
                if pgb.button_left():
                    if animated and not bgimage:
                        incr=20
                        draw_battery_backing()
                        for i in range(12): #3 is good
                            i+=1
                            pgb.fill_rect(0,80,240,130,bgcolor565)
                            try:
                                readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",-180+(i*incr),81,120,120)
                            except:
                                pgb.fill_rect(-180+(i*incr),81,120,120,ttcolor)
                                pgb.create_text("No Image",-152+(i*incr),140,ottcolor)
                                time.sleep(0.005)
                            readchunk("settings.pbimg",60+(i*incr),80,120,120)
                            pgb.poly(60+(i*incr),80,c1,bgcolor565,True)
                            pgb.poly(60+(i*incr),200,c2,bgcolor565,True)
                            pgb.poly(180+(i*incr),80,c3,bgcolor565,True)
                            pgb.poly(180+(i*incr),200,c4,bgcolor565,True)
                            pgb.poly(-180+(i*incr),80,c1,bgcolor565,True)
                            pgb.poly(-180+(i*incr),200,c2,bgcolor565,True)
                            pgb.poly(-60+(i*incr),80,c3,bgcolor565,True)
                            pgb.poly(-60+(i*incr),200,c4,bgcolor565,True)
                            pgb.show()
                    elif not bgimage:
                        time.sleep(0.1)
                    render(False)
                    draw_battery_backing()
                    draw_battery()
                    pgb.show()
                    break
                    
    if title>gamenum:
        title=gamenum
    elif title<0:
        title=0
    if pgb.button_select() and pgb.button_B() and pgb.button_down():
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.create_text("DATA UPLOAD MODE",-1,50,PicoGameBoy.color(255,255,255))
        pgb.create_text("Plug your PicoBoy",-1, 100,PicoGameBoy.color(255,255,255))
        pgb.create_text("into your computer",-1,112,PicoGameBoy.color(255,255,255))
        pgb.create_text("and run the PicoBoy",-1,124,PicoGameBoy.color(255,255,255))
        pgb.create_text("Communication Software.",-1,136,PicoGameBoy.color(255,255,255))
        pgb.create_text("To exit data",-1,180,PicoGameBoy.color(255,255,255))
        pgb.create_text("upload mode reset",-1,192,PicoGameBoy.color(255,255,255))
        pgb.create_text("your PicoBoy.",-1,204,PicoGameBoy.color(255,255,255))
        pgb.show()
        break
    draw_battery()
    pgb.show()
    draw_battery_backing()
    if pgb.button_A() or pgb.button_start():
        go=False
        try:
            x=open("./"+games[title]+"/"+games[title]+".py")
            while True:
                try:
                    f10=x.readline(100)
                    if "rename" in f10 or "PicoBoySDK" in f10:
                        break
                    if f10=="":
                        raise
                except:
                    raise
            x.close()
            go=True
        except:
            time.sleep(0.1)
            pgb.fill_rect(10,90,220,80,PicoGameBoy.color(50,50,50))
            pgb.create_text("Game failed to start!", -1,110,PicoGameBoy.color(255,255,255))
            pgb.create_text("This game may be corrupt.", -1, 135, PicoGameBoy.color(255,255,255))
            pgb.create_text("Press any button to exit.", -1, 150, PicoGameBoy.color(255,255,255))
            pgb.show()
            while True:
                pgb.show()
                if pgb.any_button():
                    pgb.fill_rect(10,90,220,80,bgcolor565)
                    try:
                        readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60,80,120,120)
                    except:
                        pgb.fill_rect(60,80,120,120,ttcolor)
                        pgb.create_text("No Image",-1,140,ottcolor)
                        time.sleep(0.1)
                    if title==0:
                        pgb.poly(200,130,arrowright,ttcolor,True)
                    else:
                        pgb.poly(200,130,arrowright,ttcolor,True)
                        pgb.poly(40,130,arrowleft,ttcolor,True)
                    pgb.poly(60,80,c1,bgcolor565,True)
                    pgb.poly(60,200,c2,bgcolor565,True)
                    pgb.poly(180,80,c3,bgcolor565,True)
                    pgb.poly(180,200,c4,bgcolor565,True)
                    time.sleep(0.1)
                    break
                    
        if go:
            with open("gameselection.conf", "w") as w:
                w.write(str(title))
            os.rename("./main.py", "./title.py")
            os.rename("./"+games[title]+"/"+games[title]+".py", "./main.py")
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break

        
        
        

