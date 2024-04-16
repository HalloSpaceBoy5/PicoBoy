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
time.sleep(0.2)
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
        pgb.create_text("Settings",-1,10,ttcolor)
        pgb.create_text("PicoBoy            "+version,10,225,ttcolor)
        options=["Drawing Background","Color Background", "Exit"]
        for i,option in enumerate(options):
            pgb.rect(10,25+i*30,220,20,white)
            pgb.rect(11,26+i*30,218,18,black)
            if i==opt:
                pgb.fill_rect(12,27+i*30,216,16,selectcolor)
            pgb.create_text(option,-1,32+i*30,ttcolor)
        if pgb.button_up() and opt>0:
            opt-=1
            pgb.show()
            time.sleep(0.1)
        if pgb.button_down() and opt<len(options)-1:
            opt+=1
            pgb.show()
            time.sleep(0.1)
        if pgb.button_A():
            if opt==1:
                time.sleep(0.2)
                while True:
                    pgb.fill(bgcolor565)
                    pgb.create_text("Choose a background color",-1,-1,ttcolor)
                    pgb.create_text("using the left and right",-1,125,ttcolor)
                    pgb.create_text("buttons.",-1,140,ttcolor)
                    pgb.create_text("Press A to exit",-1,220,ttcolor)
                    if runcheck:
                        runcheck=False
                    if pgb.button_A():
                        return
                    if pgb.button_B():
                        time.sleep(0.2)
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
                        pgb.create_text("Choose a background color",-1,-1,ttcolor)
                        pgb.create_text("using the left and right",-1,125,ttcolor)
                        pgb.create_text("buttons.",-1,140,ttcolor)
                        pgb.create_text("Press A to exit",-1,220,ttcolor)
                        pgb.show()
                        time.sleep(0.2)
            if opt==0:
                time.sleep(0.2)
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
                    options.append("Exit")
                    pgb.create_text("Choose a background",-1,10,ttcolor)
                    for i,option in enumerate(options):
                        pgb.rect(10,25+i*30,220,20,white)
                        pgb.rect(11,26+i*30,218,18,black)
                        if i==opt:
                            pgb.fill_rect(12,27+i*30,216,16,selectcolor)
                        pgb.create_text(option,-1,32+i*30,ttcolor)
                    pgb.create_text(f"Page {page+1}/{int((len(bgs)-1)/4)+1}",-1,172,ttcolor)
                    pgb.create_text("Use the left/right buttons",-1,190,ttcolor)
                    pgb.create_text("to scroll your backgrounds",-1,200,ttcolor)
                    pgb.create_text("Drawing backgrounds won't",-1,215,ttcolor)
                    pgb.create_text("show in the settings menu.",-1,225,ttcolor)
                    if pgb.button_up() and opt>0:
                        opt-=1
                        pgb.show()
                        time.sleep(0.1)
                    if pgb.button_down() and opt<len(options)-1:
                        opt+=1
                        pgb.show()
                        time.sleep(0.1)
                    if pgb.button_left():
                        time.sleep(0.2)
                        if page==0:
                            page=int((len(bgs)-1)/4)
                        else:
                            page-=1
                    if pgb.button_right():
                        time.sleep(0.2)
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
                            time.sleep(0.2)
                            return
                    if pgb.button_B():
                        time.sleep(0.2)
                        break
                    pgb.show()
            if opt==2:
                return
        if pgb.button_B():
            return
        pgb.show()    

vpin=machine.ADC(29)
pastpercentage=[]
while True:
    pgb.fill(bgcolor565)
    pgb.create_text("Settings",-1,10,ttcolor)
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
    options=["Change Brightness", "Change Volume", "Change Background", "Data Upload Mode", "Toggle Animation: "+str(animated), "Exit"]
    if tcolor==0:
        ottcolor=white
    else:
        ottcolor=black
    for i,option in enumerate(options):
        pgb.rect(10,25+i*30,220,20,white)
        pgb.rect(11,26+i*30,218,18,black)
        if i==opt:
            pgb.fill_rect(12,27+i*30,216,16,selectcolor)
        pgb.create_text(option,-1,32+i*30,ttcolor)
    if pgb.button_up() and opt>0:
        opt-=1
        pgb.show()
        time.sleep(0.1)
    if pgb.button_down() and opt<len(options)-1:
        opt+=1
        pgb.show()
        time.sleep(0.1)
    if pgb.button_A():
        if opt==0:
            time.sleep(0.2)
            while True:
                pgb.fill(bgcolor565)
                pgb.rect(20,110,200,20,ttcolor)
                brightness=pgb.bl.duty_u16()-10000
                width=int((brightness/55000)*198)
                percentage=int((brightness/55000)*100)
                pgb.fill_rect(21,111,width,18,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                pgb.create_text("Use the left and right",-1,140,ttcolor)
                pgb.create_text("buttons to change the",-1,150,ttcolor)
                pgb.create_text("brightness.",-1,160,ttcolor)
                pgb.create_text("Press A to exit.",-1,220,ttcolor)
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
                    time.sleep(0.0825)
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
                    time.sleep(0.0825)
                if pgb.button_A() or pgb.button_B():
                    time.sleep(0.2)
                    break
                pgb.show()
        if opt==1:
            time.sleep(0.2)
            while True:
                pgb.fill(bgcolor565)
                pgb.rect(20,110,200,20,ttcolor)
                volume=pgb.vol
                width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
                percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
                pgb.fill_rect(21,111,width,18,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                pgb.create_text("Use the left and right",-1,140,ttcolor)
                pgb.create_text("buttons to change the",-1,150,ttcolor)
                pgb.create_text("volume.",-1,160,ttcolor)
                pgb.create_text("Press A to exit.",-1,220,ttcolor)
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
                    time.sleep(0.0825)
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
                    time.sleep(0.0825)
                    pgb.sound(0)
                if pgb.button_A() or pgb.button_B():
                    time.sleep(0.2)
                    break
                pgb.show()
        if opt==2:
            time.sleep(0.2)
            pgb.show()
            background()
            time.sleep(0.2)
        if opt==3:
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
        if opt==4:
            if animated:
                animated=False
            else:
                animated=True
            with open("animated.conf", "w") as w:
                w.write(str(animated))
            time.sleep(0.1)
        if opt==5:
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



