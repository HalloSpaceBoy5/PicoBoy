# Original OS for PicoBoy by HalloSpaceBoy

# INIT IMPORTS
from micropython import const
from PicoGameBoy import PicoGameBoy
from time import sleep
from array import array
from os import rename, listdir, remove
from sys import exit
from machine import reset, ADC
from Functions import Functions

# INIT VARS
BLACK = PicoGameBoy.color(0,0,0)
WHITE = PicoGameBoy.color(255,255,255)
pgb = PicoGameBoy()
vpin = ADC(29)
games=listdir("/games")
loop=0
gamenum=len(games)-1
title=0
pastpercentage=[]
pastpercent=101




# INITIALIZATIONS

# LOAD CONFIGS
bootlogo=True
try:
    x=open("/noboot", "r")
    x.close()
    remove("/noboot")
    bootlogo=False
    try:
        with open("gameselection.conf", "r") as r:
            title=int(r.read())
    except:
        "config nonexistent"
except:
    bootlogo=True
    
try:
    with open("language.conf") as r:
        language=int(r.read())
    if language>4:
        raise
except:
    language=0
    
try:
    with open("/animated.conf") as r:
        if r.read()=="True":
            animated=True
        else:
            animated=False
except:
    animated=True

with open("Main Text.csv") as w:
    data=w.read().split("\n")[language]
    data=data.split(", ")
    ng=data[0]
    s=data[1]
    ni=data[2].split("/")
    dum=data[3].split("/")
    gfs=data[4].split("/")
    ic=data[5].split("/")
    del data

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
    gamenum=0
    games=["No Games"]

try:
    with open("background.conf","r") as r:
        data=r.read()
    try:    
        bindex=int(data)
        bgimage=False
        bgcolor=bgcolors[bindex]
    except:
        bgimage=True
        bindex=8
        bgcolor=(69,69,69)
        bgcolor565=PicoGameBoy.color(69,69,69)
        bgimagefile=data[:]
except:
    bindex=8
    bgimage=False
    
if bindex>len(bgcolors)-1:
    bindex=8
bgcolor=bgcolors[bindex]
bgcolor565=PicoGameBoy.color(*bgcolor)


arrowright=array('h',[0,0,0,20,20,10])
arrowleft=array('h',[0,0,0,20,-20,10])
arrowrightbg=array('h',[0,0,0,30,30,15])
arrowleftbg=array('h',[0,0,0,30,-30,15])
c1=array('h',[0,0,0,5,5,0])
c2=array('h',[0,0,0,-5,5,0])
c3=array('h',[0,0,0,5,-5,0])
c4=array('h',[0,0,0,-5,-5,0])


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
if tcolor==0:
    ttcolor=PicoGameBoy.color(0,0,0)
    
# INIT OFFLOADED FUNCTIONS
Functions=Functions(pgb, ttcolor, ottcolor, ic)

# LOAD BACKGROUND
if bgimage:
    try:
        with open(bgimagefile, "r") as r:
            r.read()
        imagedata=Functions.getimagedata(bgimagefile)
    except:
        bindex=8
        bgimage=False



# RENDER BOOT LOGO
if bootlogo:
    pgb.fill(BLACK)
    Functions.readchunk("logo.pbimg",88,50,64,64,False)
    Functions.readchunk("logo-text.pbimg",69,150,102,15,False)
    pgb.show_screen()
    pgb.sound(98)
    sleep(0.2)
    pgb.sound(0)
    pgb.sound(185)
    sleep(0.2)
    pgb.sound(0)
    pgb.sound(164)
    sleep(0.2)
    pgb.sound(0)
    sleep(0.9)
    
# BEGIN RENDERING HOME SCREEN

if bgimage:
    Functions.draw_image(imagedata)

if bgimage:
    pgb.fill_rect(15,15,208,30,bgcolor565)
    pgb.fill_rect(15,10,208,5,bgcolor565)
    pgb.fill_rect(15,45,208,5,bgcolor565)
    pgb.fill_rect(10,15,5,30,bgcolor565)
    pgb.fill_rect(223,15,5,30,bgcolor565)
    pgb.poly(10,10,array('h',[5,5,0,5,5,0]),bgcolor565,True)
    pgb.poly(222,10,array('h',[0,5,5,5,0,0]),bgcolor565,True)
    pgb.poly(10,49,array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
    pgb.poly(222,49,array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
else:
    pgb.fill(PicoGameBoy.color(*bgcolor))
Functions.readchunk_mask("picoboy-color.pbimg",0,0,240,60)


    
# INIT RENDERING FUNTIONS

# RECORD AND RENDER BATTERY PERCENTAGE
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
    
# RENDER BATTERY OUTLINE (For custom bgs)
def draw_battery_backing():
    battx=9
    batty=183
    pgb.fill_rect(battx-2,batty-4,24,55,bgcolor565)
    pgb.fill_rect(battx-5-2,batty-4,5,55,bgcolor565)
    pgb.fill_rect(battx+20+2,batty-4,5,55,bgcolor565)
    pgb.fill_rect(battx-2,batty-9,24,5,bgcolor565)
    pgb.fill_rect(battx-2,batty+51,24,5,bgcolor565)
    pgb.poly(battx-5-2,batty-9,array('h',[5,5,0,5,5,0]),bgcolor565,True)
    pgb.poly(battx+19+2,batty-9,array('h',[0,5,5,5,0,0]),bgcolor565,True)
    pgb.poly(battx-5-2,batty+55,array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
    pgb.poly(battx+19+2,batty+55,array('h',[0,0,0,-5,5,-5]),bgcolor565,True)

# RENDER OS MAIN SCREEN INSTANCE
def render(f=True, j=False):
        if bgimage:
            Functions.draw_image(imagedata,7)
        else:
            pgb.fill_rect(0,65,240,140,bgcolor565)
        pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,65,int(len(games[title]) * 8)+10,140,bgcolor565)
        pgb.fill_rect(55,65,130,140,bgcolor565)
        
        #Text rect
        pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-10,65,5,140,bgcolor565)
        pgb.fill_rect(int(120)+ int(len(games[title])/2 * 8)+5,65,5,140,bgcolor565)
        pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,60,int(len(games[title]) * 8)+10,5,bgcolor565)
        pgb.fill_rect(int(120)- int(len(games[title])/2 * 8)-5,205,int(len(games[title]) * 8)+10,5,bgcolor565)
        pgb.poly(int(120)- int(len(games[title])/2 * 8)-10,60,array('h',[5,5,0,5,5,0]),bgcolor565,True)
        pgb.poly(120+int(int(len(games[title]) * 8)/2)+5,60,array('h',[0,5,5,5,0,0]),bgcolor565,True)
        pgb.poly(int(120)- int(len(games[title])/2 * 8)-10,209,array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
        pgb.poly(120+int(int(len(games[title]) * 8)/2)+5,209,array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
        
        #App rect
        pgb.fill_rect(50,65,5,140,bgcolor565)
        pgb.fill_rect(185,65,5,140,bgcolor565)
        pgb.fill_rect(55,60,130,5,bgcolor565)
        pgb.fill_rect(55,205,130,5,bgcolor565)
        pgb.poly(50,60,array('h',[5,5,0,5,5,0]),bgcolor565,True)
        pgb.poly(184,60,array('h',[0,5,5,5,0,0]),bgcolor565,True)
        pgb.poly(50,209,array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
        pgb.poly(184,209,array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
        
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
        pgb.poly(int(120)- int(len("".join(pos)+"S")/2 * 8)-10,220,array('h',[5,5,0,5,5,0]),bgcolor565,True)
        pgb.poly(120+int(int(len("".join(pos)+"S") * 8)/2)+4,220,array('h',[0,5,5,5,0,0]),bgcolor565,True)
        pgb.poly(int(120)- int(len("".join(pos)+"S")/2 * 8)-10,240,array('h',[0,-5,5,0,5,-5]),bgcolor565,True)
        pgb.poly(120+int(int(len("".join(pos)+"S") * 8)/2)+4,240,array('h',[0,0,0,-5,5,-5]),bgcolor565,True)
        ##########
        if j:
            return
        pgb.create_text("".join(pos)+"S", x=-1, y=228,color=ttcolor)
        if not games==["No Games"]:
            pgb.create_text(games[title],-1,65,ttcolor)
        else:
            pgb.create_text(ng,-1,65,ttcolor)
        try:
            if not games==["No Games"]:
                Functions.readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60,80,120,120)
            else:
                Functions.readchunk(games[title]+".pbimg",60,80,120,120)
        except:
            pgb.fill_rect(60,80,120,120,ttcolor)
            for g,h in enumerate(ni):
                pgb.create_text(h,-1,int(140-((len(ni)/2)*12))+(g*12),ottcolor)
            sleep(0.015)
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
            
     
# MAIN OS OPERATIONS

# RENDER HOME SCREEN
if title<=gamenum :
    render()
    onsett=False
else:
    onsett=True


# BEGIN HOMESCREEN MAINLOOP
while True:
    # MEM TEST
    #print(mem_free())
    if pgb.button_left() and title>0 and not onsett:
        if animated and not bgimage:
            incr=20
            draw_battery_backing()
            for i in range(12): #3 is good
                i+=1
                pgb.fill_rect(0,78,240,130,bgcolor565)
                try:
                    Functions.readchunk(games[title-1]+"/"+games[title-1]+" (Title Image).pbimg",-180+(i*incr),81,120,120)
                except:
                    pgb.fill_rect(-180+(i*incr),81,120,120,ttcolor)
                    for g,h in enumerate(ni):
                        pgb.create_text(h,((120-(len(h)*4))-240)+(i*incr),int(140-((len(ni)/2)*12))+(g*12),ottcolor)
                    sleep(0.015)
                try:
                    Functions.readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60+(i*incr),80,120,120)
                except:
                    pgb.fill_rect(60+(i*incr),80,120,120,ttcolor)
                    for g,h in enumerate(ni):
                        pgb.create_text(h,(120-(len(h)*4))+(i*incr),int(140-((len(ni)/2)*12))+(g*12),ottcolor)
                    sleep(0.015)
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
            sleep(0.1)
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
                        Functions.readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60-(i*incr),81,120,120)
                except:
                        pgb.fill_rect(60-(i*incr),80,120,120,ttcolor)
                        for g,h in enumerate(ni):
                            pgb.create_text(h,(120-(len(h)*4))-(i*incr),int(140-((len(ni)/2)*12))+(g*12),ottcolor)
                        sleep(0.015)
                try:
                    Functions.readchunk(games[title+1]+"/"+games[title+1]+" (Title Image).pbimg",300-(i*incr),80,120,120)
                except:
                    pgb.fill_rect(300-(i*incr),80,120,120,ttcolor)
                    for g,h in enumerate(ni):
                        pgb.create_text(h,240+(120-(len(h)*4))-(i*incr),int(140-((len(ni)/2)*12))+(g*12),ottcolor)
                    sleep(0.015)
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
            sleep(0.1)
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
                        if not games==["No Games"]:
                            Functions.readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60-(i*incr),81,120,120)
                        else:
                            Functions.readchunk("No Games.pbimg",60-(i*incr),81,120,120)
                    except:
                        pgb.fill_rect(60-(i*incr),81,120,120,ttcolor)
                        for g,h in enumerate(ni):
                            pgb.create_text(h,(120-(len(h)*4))-(i*incr),int(140-((len(ni)/2)*12))+(g*12),ottcolor)
                        sleep(0.015)
                    Functions.readchunk("settings.pbimg",300-(i*incr),80,120,120)
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
                sleep(0.1)
            if not bgimage:
                pgb.fill_rect(0,78,240,130,bgcolor565)
            onsett=False
            render(j=True)
            pos=""
            for g in games:
                pos+="."
            pgb.create_text(pos+"0", x=-1, y=228,color=ttcolor)
            pgb.create_text(s,-1,65,ttcolor)
            Functions.readchunk("settings.pbimg",60,80,120,120)
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
                    rename("./main.py", "./title.py")
                    rename("settings.py", "./main.py")
                    pgb.fill(PicoGameBoy.color(0,0,0))
                    pgb.show()
                    reset()
                    break
                if pgb.button_select() and pgb.button_B() and pgb.button_down():
                    pgb.fill(bgcolor565)
                    pgb.create_text(dum[0],-1,20,ttcolor)
                    pgb.create_text(dum[1],-1, 45,ttcolor)
                    pgb.create_text(dum[2],-1,57,ttcolor)
                    pgb.create_text(dum[3],-1,69,ttcolor)
                    pgb.create_text(dum[4],-1,81,ttcolor)
                    pgb.create_text(dum[5],-1,200,ttcolor)
                    pgb.create_text(dum[6],-1,212,ttcolor)
                    pgb.create_text(dum[7],-1,224,ttcolor)
                    Functions.readchunk_mask("Data Upload Mode.pbimg", 72,90,100,100,cmask=PicoGameBoy.color(31,17,9))
                    pgb.show()
                    exit()
                if pgb.button_left():
                    if animated and not bgimage:
                        incr=20
                        draw_battery_backing()
                        for i in range(12): #3 is good
                            i+=1
                            pgb.fill_rect(0,80,240,130,bgcolor565)
                            try:
                                if not games==["No Games"]:
                                    Functions.readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",-180+(i*incr),81,120,120)
                                else:
                                    Functions.readchunk(games[title]+".pbimg",-180+(i*incr),81,120,120)
                            except:
                                pgb.fill_rect(-180+(i*incr),81,120,120,ttcolor)
                                for g,h in enumerate(ni):
                                    pgb.create_text(h,((120-(len(h)*4 ))-240)+(i*incr),int(140-((len(ni)/2)*12))+(g*12),ottcolor)
                                sleep(0.015)
                            Functions.readchunk("settings.pbimg",60+(i*incr),80,120,120)
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
                        sleep(0.1)
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
        pgb.fill(bgcolor565)
        pgb.create_text(dum[0],-1,20,ttcolor)
        pgb.create_text(dum[1],-1, 45,ttcolor)
        pgb.create_text(dum[2],-1,57,ttcolor)
        pgb.create_text(dum[3],-1,69,ttcolor)
        pgb.create_text(dum[4],-1,81,ttcolor)
        pgb.create_text(dum[5],-1,200,ttcolor)
        pgb.create_text(dum[6],-1,212,ttcolor)
        pgb.create_text(dum[7],-1,224,ttcolor)
        Functions.readchunk_mask("Data Upload Mode.pbimg", 72,90,100,100,cmask=PicoGameBoy.color(31,17,9))
        pgb.show()
        try:
            remove("/out.bin")
        except:
            ""
        with open("/out.bin", "ab") as w:
            for i in range(240):
                data=pgb.sbuffer[i*480:i*480+480]
                w.write(data)
        break
    draw_battery()
    pgb.show()
    draw_battery_backing()
    if (pgb.button_A() or pgb.button_start()) and not games==["No Games"]:
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
            sleep(0.1)
            pgb.fill_rect(10,90,220,24+(len(gfs)*12),PicoGameBoy.color(50,50,50))
            for i,f in enumerate(gfs):
                pgb.create_text(f, -1,105+(i*12),PicoGameBoy.color(255,255,255))
            pgb.show()
            while True:
                pgb.show()
                if pgb.any_button():
                    pgb.fill_rect(10,90,220,100,bgcolor565)
                    try:
                        Functions.readchunk(games[title]+"/"+games[title]+" (Title Image).pbimg",60,80,120,120)
                    except:
                        pgb.fill_rect(60,80,120,120,ttcolor)
                        pgb.create_text("No Image",-1,140,ottcolor)
                        sleep(0.1)
                    if title==0:
                        pgb.poly(200,130,arrowright,ttcolor,True)
                    else:
                        pgb.poly(200,130,arrowright,ttcolor,True)
                        pgb.poly(40,130,arrowleft,ttcolor,True)
                    pgb.poly(60,80,c1,bgcolor565,True)
                    pgb.poly(60,200,c2,bgcolor565,True)
                    pgb.poly(180,80,c3,bgcolor565,True)
                    pgb.poly(180,200,c4,bgcolor565,True)
                    sleep(0.1)
                    break
                    
        if go:
            with open("gameselection.conf", "w") as w:
                w.write(str(title))
            rename("./main.py", "./title.py")
            rename("./"+games[title]+"/"+games[title]+".py", "./main.py")
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            reset()
            break

        
        
        

 