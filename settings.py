from micropython import const
from framebuf import FrameBuffer,RGB565
from PicoGameBoy import PicoGameBoy
from time import sleep
from random import randint
import array
import os
import sys
from random import randint
import machine
from math import ceil

try:
    os.rename("/main.py", "/settings.py")
    os.rename("/title.py", "/main.py")
except:
    ""



pgb = PicoGameBoy()
runcheck=False
black=PicoGameBoy.color(0,0,0)
white=PicoGameBoy.color(255,255,255)
opt=0
sleep(0.2)
try:
    with open("background.conf","r") as r:
        bindex=int(r.read())
except:
    bindex=8
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
bgcolor=bgcolors[bindex]
bgcolor565=PicoGameBoy.color(*bgcolor)
if sum(bgcolor)<765:
    tcolor=1
else:
    tcolor=0
if tcolor==0:
    ottcolor=PicoGameBoy.color(255,255,255)
else:
    ottcolor=PicoGameBoy.color(0,0,0)
ttcolor=PicoGameBoy.color(255,255,255)
if tcolor==0:
    ttcolor=PicoGameBoy.color(0,0,0)
    
try:
    with open("animated.conf") as r:
        if r.read()=="True":
            animated=True
        else:
            animated=False
except:
    animated=True
    
try:
    with open("VERSION") as r:
        version=r.read()
except:
    version="NULL"

selectcolor=PicoGameBoy.color(127,127,127)
if tcolor==0:
    selectcolor=PicoGameBoy.color(200,200,200)


try:
    with open("language.conf") as r:
        language=int(r.read())
    if language>4:
        raise
except:
    language=0
with open("Settings Text.csv") as w:
    data=w.read().split("\n")[language]
    textdata=tuple(data.split(", "))
    
try:
    with open("SIP.conf") as r:
        SIP=r.read()
        if SIP=="True":
            SIP=True
        else:
            SIP=False
except:
    SIP=True

with open("Main Text.csv") as w:
    data=w.read().split("\n")[language]
    data=data.split(", ")
    dum=data[3].split("/")
    del data

def readchunk_mask( filename,x2,y2,w,h,cmask=57351):
    with open(filename,"rb") as r:
            for x in range(h):
                tempfb=FrameBuffer(bytearray(r.read(2*w)),w,1,RGB565)
                pgb.blit(tempfb,x2,y2+x,cmask)
                del tempfb

def stats():
    pgb.fill(bgcolor565)
    pgb.create_text(textdata[0],-1,10,ttcolor)
    noptions=[]
    for i in textdata[1].split("\\"):
        noptions.append(i)
    for i,f in enumerate(textdata[2].split("\\")):
        pgb.create_text(f,-1,210+(i*15),ttcolor)
    while True:
        pgb.fill_rect(0,25,240,180,bgcolor565)
        for i,option in enumerate(noptions):
            pgb.rect(10,30+i*30,220,20,white)
            pgb.rect(11,31+i*30,218,18,black)
            if i==0:
                option=option+str(version)
            elif i==1:
                mversion=str(sys.implementation.version)
                mversion="V"+mversion.replace(")","").replace("(","").replace(", \'\'","").replace(", ",".")
                option=option+mversion
            elif i==2:
                stat=os.statvfs('/')
                amntfree=stat[0] * stat[3]
                storage=str(ceil(int(amntfree)/1000)-5)+"kb"
                option=option+storage
            elif i==3:
                amt=len(os.listdir("/games/"))
                option=option+str(amt)
            elif i==4:
                amt=len(os.listdir("/libs/"))
                option=option+str(amt)
            elif i==5:
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
                if percentage>100:
                    option=option+"USB"
                else:
                    option=option+str(percentage)+"%"
            pgb.create_text(option,(120- int(len(option)/2 * 8)),37+i*30,ttcolor)
        pgb.show()
        if pgb.button_B():
            sleep(0.2)
            break


def languages():
    global language
    global textdata
    opti=language
    sleep(.1)
    while True:
        pgb.fill(bgcolor565)
        pgb.create_text(textdata[3],-1,10,ttcolor)
        pgb.create_text("PicoBoy            "+version,10,225,ttcolor)
        options=["English", "Espanol", "Francais", "Deutsch", "Italiano"]
        for i,option in enumerate(options):
            pgb.rect(10,25+i*30,220,20,white)
            pgb.rect(11,26+i*30,218,18,black)
            if i==opti:
                pgb.fill_rect(12,27+i*30,216,16,selectcolor)
            pgb.create_text(option,-1,32+i*30,ttcolor)
        if pgb.button_up() and opti>0:
            opti-=1
            pgb.show()
            sleep(0.1)
        if pgb.button_down() and opti<len(options)-1:
            opti+=1
            pgb.show()
            sleep(0.1)
        if pgb.button_A():
            language=opti
            with open("language.conf", "w") as w:
                w.write(str(opti))
            with open("Settings Text.csv") as w:
                data=w.read().split("\n")[language]
                textdata=tuple(data.split(", ")[:])
            with open("Main Text.csv") as w:
                global dum
                data=w.read().split("\n")[language]
                data=data.split(", ")
                dum=data[3].split("/")
                del data
            sleep(0.1)
            return
        pgb.show()

def background():
    global bgcolor565
    global bgcolor
    global white
    global black
    global tcolor
    global ttcolor
    global runcheck
    global ottcolor
    global selectcolor
    global bindex
    opt=0
    
    while True:
        pgb.fill(bgcolor565)
        pgb.create_text(textdata[3],-1,10,ttcolor)
        pgb.create_text("PicoBoy            "+version,10,225,ttcolor)
        options=[textdata[4], textdata[5], textdata[6]]
        
        for i,option in enumerate(options):
            pgb.rect(10,25+i*30,220,20,white)
            pgb.rect(11,26+i*30,218,18,black)
            if i==opt:
                pgb.fill_rect(12,27+i*30,216,16,selectcolor)
            pgb.create_text(option,-1,32+i*30,ttcolor)
        if pgb.button_up() and opt>0:
            opt-=1
            pgb.show()
            sleep(0.1)
        if pgb.button_down() and opt<len(options)-1:
            opt+=1
            pgb.show()
            sleep(0.1)
        if pgb.button_A():
            if opt==1:
                sleep(0.2)
                while True:
                    pgb.fill(bgcolor565)
                    for f,i in enumerate(textdata[7].split("\\")):
                        pgb.create_text(i,-1,110+(f*15),ttcolor)
                    if runcheck:
                        runcheck=False
                    if pgb.button_A():
                        return
                    if pgb.button_B():
                        sleep(0.2)
                        break
                    if pgb.button_left() and bindex>0:
                        bindex-=1
                        runcheck=True
                    if pgb.button_right() and bindex<len(bgcolors)-1:
                        bindex+=1
                        runcheck=True
                    pgb.show()
                    if runcheck:
                        bgcolor=bgcolors[bindex]
                        bgcolor565=PicoGameBoy.color(*bgcolor)
                        if sum(bgcolor)<765:
                            tcolor=1
                        else:
                            tcolor=0
                        ttcolor=PicoGameBoy.color(255,255,255)
                        if tcolor==0:
                            ttcolor=PicoGameBoy.color(0,0,0)
                        with open("background.conf","w") as w:
                            w.write(str(bindex))
                        if tcolor==0:
                            ottcolor=white
                        else:
                            ottcolor=black
                        selectcolor=PicoGameBoy.color(127,127,127)
                        if tcolor==0:
                            selectcolor=PicoGameBoy.color(200,200,200)
                        pgb.fill(bgcolor565)
                        for f,i in enumerate(textdata[7].split("\\")):
                            pgb.create_text(i,-1,110+(f*15),ttcolor)
                        sleep(0.2)
            if opt==0:
                sleep(0.2)
                bgs=os.listdir("/bglist")
                page=0
                while True:
                    pgb.fill(bgcolor565)
                    options=[]
                    for x in range(4):
                        try:
                            options.append(bgs[x+(page*4)])
                        except:
                            "End of list"
                    options.append(textdata[6])
                    pgb.create_text(textdata[9],-1,10,ttcolor)


                    for i,option in enumerate(options):
                        pgb.rect(10,25+i*30,220,20,white)
                        pgb.rect(11,26+i*30,218,18,black)
                        if i==opt:
                            pgb.fill_rect(12,27+i*30,216,16,selectcolor)
                        pgb.create_text(option,-1,32+i*30,ttcolor)
                    pgb.create_text(f"{textdata[10]}{page+1}/{int((len(bgs)-1)/4)+1}",-1,172,ttcolor)
                    for f,i in enumerate(textdata[11].split("\\")):
                        pgb.create_text(i,-1,190+(f*12),ttcolor)
                    for f,i in enumerate(textdata[12].split("\\")):
                        pgb.create_text(i,-1,214+(f*12),ttcolor)


                    if pgb.button_up() and opt>0:
                        opt-=1
                        pgb.show()
                        sleep(0.1)
                    if pgb.button_down() and opt<len(options)-1:
                        opt+=1
                        pgb.show()
                        sleep(0.1)
                    if pgb.button_left():
                        sleep(0.2)
                        if page==0:
                            page=int((len(bgs)-1)/4)
                        else:
                            page-=1
                    if pgb.button_right():
                        sleep(0.2)
                        if page==int((len(bgs)-1)/4):
                            page=0
                        else:
                            page+=1
                    if pgb.button_A():
                        if opt==len(options)-1:
                            return
                        else:
                            with open("background.conf","w") as w:
                                w.write(f"/backgrounds/{bgs[opt+(page*4)]}.pbd")
                                bgcolor=bgcolors[8]
                                bindex=8
                                bgcolor565=PicoGameBoy.color(*bgcolor)
                                if sum(bgcolor)<426:
                                    tcolor=1
                                else:
                                    tcolor=0
                                ttcolor=PicoGameBoy.color(255,255,255)
                                if tcolor==0:
                                    ttcolor=PicoGameBoy.color(0,0,0)
                                if tcolor==0:
                                    ottcolor=white
                                else:
                                    ottcolor=black
                            sleep(0.2)
                            return
                    if pgb.button_B():
                        sleep(0.2)
                        break
                    pgb.show()
            if opt==2:
                return
        if pgb.button_B():
            return
        pgb.show()    

def SI_P():
    global SIP
    options=[]
    if SIP:
        options.append(textdata[27])
    else:
        options.append(textdata[26])
    options.append(textdata[6])
    opt=0
    sleep(0.25)
    while True:
        pgb.fill(bgcolor565)
        for i,f in enumerate(textdata[30].split("\\")):
            pgb.create_text(f.replace("...",""),-1,10+(15*i),white)
        pgb.create_text(textdata[23],-1,110,ttcolor)
        if SIP:
            pgb.create_text(textdata[24],-1,125,ttcolor)
        else:
            pgb.create_text(textdata[25],-1,125,ttcolor)
        pgb.create_text("PicoBoy            "+version,10,225,ttcolor)
        for i,option in enumerate(options):
            pgb.rect(10,45+i*30,220,20,white)
            pgb.rect(11,46+i*30,218,18,black)
            if i==opt:
                pgb.fill_rect(12,47+i*30,216,16,selectcolor)
            pgb.create_text(option,-1,52+i*30,ttcolor)
        if pgb.button_up() and opt>0:
            opt-=1
            pgb.show()
            sleep(0.1)
        if pgb.button_down() and opt<len(options)-1:
            opt+=1
            pgb.show()
            sleep(0.1)
        if pgb.button_A():
            sleep(0.25)
            if opt==0:
                if SIP:
                    pgb.fill(PicoGameBoy.color(200,0,0))
                    pgb.create_text(textdata[19],-1,10,PicoGameBoy.color(255,255,255))
                    for i,f in enumerate(textdata[20].split("\\")):
                        pgb.create_text(f,-1,40+(15*i),PicoGameBoy.color(255,255,255))
                    for i,f in enumerate(textdata[21].split("\\")):
                        pgb.create_text(f,-1,110+(15*i),PicoGameBoy.color(255,255,255))
                    for i,f in enumerate(textdata[22].split("\\")):
                        pgb.create_text(f,-1,195+(15*i),PicoGameBoy.color(255,255,255))
                    pgb.show()
                    while True:
                        if pgb.button_A():
                            pgb.fill_rect(15, 90, 210, 50, PicoGameBoy.color(0,0,0))
                            pgb.create_text(textdata[29]+textdata[30].split("\\")[0],-1,105, PicoGameBoy.color(255,255,255))
                            pgb.create_text(textdata[30].split("\\")[1],-1,120, PicoGameBoy.color(255,255,255))
                            pgb.show()
                            SIP=False
                            with open("SIP.conf", "w") as w:
                                w.write(str(SIP))
                            options=[]
                            options.append(textdata[26])
                            options.append(textdata[6])
                            sleep(0.5)
                            break
                        if pgb.button_B():
                            sleep(0.1)
                            break
                else:
                    pgb.fill_rect(15, 90, 210, 50, PicoGameBoy.color(0,0,0))
                    pgb.create_text(textdata[28]+textdata[30].split("\\")[0],-1,105, PicoGameBoy.color(255,255,255))
                    pgb.create_text(textdata[30].split("\\")[1],-1,120, PicoGameBoy.color(255,255,255))
                    pgb.show()
                    SIP=True
                    with open("SIP.conf", "w") as w:
                        w.write(str(SIP))
                    options=[]
                    options.append(textdata[25])
                    options.append(textdata[6])
                    sleep(0.5)
            if opt==1:
                return
        pgb.show()
        


scrollpos=0
max_on_screen=6
vpin=machine.ADC(29)
pastpercentage=[]
while True:
    pgb.fill(bgcolor565)
    pgb.create_text(textdata[3],-1,10,ttcolor)
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
    pgb.create_text("PicoBoy            "+version,10,225,ttcolor)
    if percentage>100:
        pgb.create_text("USB",100,225, ttcolor)
    else:
        pgb.create_text(str(percentage)+"%",100,225,ttcolor)
    if animated:
        ani=textdata[13]
    else:
        ani=textdata[14]
    otextdata=textdata[15].split("\\")
    options=[otextdata[0], otextdata[1], otextdata[2], otextdata[3], otextdata[4]+ani, otextdata[5], otextdata[6], otextdata[7], otextdata[8]]
    if tcolor==0:
        ottcolor=white
    else:
        ottcolor=black
    pgb.fill_rect(215,20,20, 180,selectcolor)
    pgb.fill_rect(220,25+(scrollpos*30),10, int(max_on_screen/len(options)* 123),ttcolor)
    noptions=options[0+scrollpos:max_on_screen+scrollpos]
    for i,option in enumerate(noptions):
        pgb.rect(10,25+i*30,200,20,white)
        pgb.rect(11,26+i*30,198,18,black)
        if i==opt:
            pgb.fill_rect(12,27+i*30,196,16,selectcolor)
        pgb.create_text(option,(120- int(len(option)/2 * 8))-10,32+i*30,ttcolor)
    if pgb.button_up():
        if opt>0:
            opt-=1
        elif opt==0 and scrollpos>0:
            scrollpos-=1
        pgb.show()
        sleep(0.1)
    if pgb.button_down():
        if opt<len(noptions)-1:
            opt+=1
        elif opt==len(noptions)-1 and opt+scrollpos<len(options)-1:
            scrollpos+=1
        pgb.show()
        sleep(0.1)
    if pgb.button_A():
        if opt+scrollpos==0:
            sleep(0.2)
            while True:
                pgb.fill(bgcolor565)
                pgb.rect(20,110,200,20,ttcolor)
                brightness=pgb.bl.duty_u16()-10000
                width=int((brightness/55000)*198)
                percentage=int((brightness/55000)*100)
                pgb.fill_rect(21,111,width,18,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                for f,i in enumerate(textdata[16].split("\\")):
                    pgb.create_text(i,-1,140+(15*f),ttcolor)
                pgb.create_text(textdata[17],-1,170,ttcolor)
                for f,i in enumerate(textdata[8].split("\\")):
                    pgb.create_text(i,-1,210+(15*f),ttcolor)
            
                if pgb.button_left():
                    pgb.decrease_brightness()
                    pgb.fill_rect(0,95,240,40,bgcolor565)
                    pgb.rect(20,110,200,20,ttcolor)
                    brightness=pgb.bl.duty_u16()-10000
                    width=int((brightness/55000)*198)
                    percentage=int((brightness/55000)*100)
                    pgb.fill_rect(21,111,width,18,ttcolor)
                    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                    pgb.show()
                    sleep(0.0825)
                if pgb.button_right():
                    pgb.increase_brightness()
                    pgb.fill_rect(0,95,240,40,bgcolor565)
                    pgb.rect(20,110,200,20,ttcolor)
                    brightness=pgb.bl.duty_u16()-10000
                    width=int((brightness/55000)*198)
                    percentage=int((brightness/55000)*100)
                    pgb.fill_rect(21,111,width,18,ttcolor)
                    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                    pgb.show()
                    sleep(0.0825)
                if pgb.button_A() or pgb.button_B():
                    sleep(0.2)
                    break
                pgb.show()
        if opt+scrollpos==1:
            sleep(0.2)
            while True:
                pgb.fill(bgcolor565)
                pgb.rect(20,110,200,20,ttcolor)
                volume=pgb.vol
                width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
                percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
                pgb.fill_rect(21,111,width,18,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                for f,i in enumerate(textdata[16].split("\\")):
                    pgb.create_text(i,-1,140+(15*f),ttcolor)
                pgb.create_text(textdata[18],-1,170,ttcolor)
                for f,i in enumerate(textdata[8].split("\\")):
                    pgb.create_text(i,-1,210+(15*f),ttcolor)
                if pgb.button_left():
                    pgb.decrease_vol()
                    pgb.fill_rect(0,95,240,40,bgcolor565)
                    pgb.rect(20,110,200,20,ttcolor)
                    volume=pgb.vol
                    width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
                    percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
                    pgb.fill_rect(21,111,width,18,ttcolor)
                    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                    pgb.show()
                    pgb.sound(200)
                    sleep(0.0825)
                    pgb.sound(0)
                if pgb.button_right():
                    pgb.increase_vol()
                    pgb.fill_rect(0,95,240,40,bgcolor565)
                    pgb.rect(20,110,200,20,ttcolor)
                    volume=pgb.vol
                    width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
                    percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
                    pgb.fill_rect(21,111,width,18,ttcolor)
                    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                    pgb.show()
                    pgb.sound(200)
                    sleep(0.0825)
                    pgb.sound(0)
                if pgb.button_A() or pgb.button_B():
                    sleep(0.2)
                    break
                pgb.show()
        if opt+scrollpos==2:
            sleep(0.2)
            pgb.show()
            background()
            sleep(0.2)
        if opt+scrollpos==3:
            pgb.fill(bgcolor565)
            pgb.create_text(dum[0],-1,20,ttcolor)
            pgb.create_text(dum[1],-1, 45,ttcolor)
            pgb.create_text(dum[2],-1,57,ttcolor)
            pgb.create_text(dum[3],-1,69,ttcolor)
            pgb.create_text(dum[4],-1,81,ttcolor)
            pgb.create_text(dum[5],-1,200,ttcolor)
            pgb.create_text(dum[6],-1,212,ttcolor)
            pgb.create_text(dum[7],-1,224,ttcolor)
            readchunk_mask("Data Upload Mode.pbimg", 72,90,100,100,cmask=PicoGameBoy.color(31,17,9))
            pgb.show()
            sys.exit()
        if opt+scrollpos==4:
            if animated:
                animated=False
            else:
                animated=True
            with open("animated.conf", "w") as w:
                w.write(str(animated))
            sleep(0.1)
        if opt+scrollpos==5:
            sleep(0.1)
            languages()
        if opt+scrollpos==6:
            stats()
        if opt+scrollpos==7:
            SI_P()
        if opt+scrollpos==8:
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
    if pgb.button_Home():
        homebootstop=open("/noboot", "w")
        homebootstop.close()
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()
        break
    pgb.show()



