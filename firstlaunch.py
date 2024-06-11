from PicoGameBoy import PicoGameBoy
from machine import ADC, reset
from Functions import Functions
from time import sleep
from os import remove, rename
import math
from sys import exit
from array import array
from framebuf import FrameBuffer, RGB565


BLACK = PicoGameBoy.color(0,0,0)
WHITE = PicoGameBoy.color(255,255,255)
pgb = PicoGameBoy()
ttcolor=WHITE

selectcolor=PicoGameBoy.color(127,127,127)
ottcolor=BLACK
Functions=Functions(pgb, ttcolor, ottcolor, "")
vpin = ADC(29)
pastpercentage=[]
pastpercent=101
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

# LOAD LANGUAGE


def screenshot(skipcheck):
    if pgb.button_select() or skipcheck:
        remove("out.bin")
        with open("out.bin", "ab") as w:
            for line in range(240):
                buffersize=480
                data=pgb.sbuffer[line*buffersize:(line*buffersize)+buffersize]
                w.write(data)



try:
    with open("VERSION") as r:
        version=r.read()
except:
    version="NULL"

def get_batt_percentage():
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
    return percentage


    
    

# BOOT LOGO
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
sleep(1.5)




lang=(("Choose a language.", "Hello!"), ("Elige un idioma.", "Hola!"), ("Choisissez une langue.", "Bonjour!"), ("Wahlen Sie eine Sprache.","Hallo!"), ("Scegli una lingua.","Ciao!"))

# LANGUAGE SCREEN
tick=1
index=0
opti=0
while True:
    if tick%100==0:
        index+=1
    if index>4:
        index=0
    tick+=1
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
    pgb.create_text(lang[index][1], -1, 12, WHITE)
    pgb.create_text(lang[index][0], -1, 27, WHITE)
    pgb.create_text(version,160,225,ttcolor)
    percentage=get_batt_percentage()
    if percentage>100:
        pgb.create_text("USB",10,225, ttcolor)
    else:
        pgb.create_text(str(percentage)+"%",10,225,ttcolor)
    options=["English", "Espanol", "Francais", "Deutsch", "Italiano"]
    for i,option in enumerate(options):
        pgb.rect(10,50+i*30,220,20,WHITE)
        pgb.rect(11,51+i*30,218,18,BLACK)
        if i==opti:
            pgb.fill_rect(12,52+i*30,216,16,selectcolor)
        pgb.create_text(option,-1,57+i*30,ttcolor)
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
        pgb.sound(200)
        with open("language.conf", "w") as w:
            w.write(str(opti))
        sleep(0.1)
        pgb.sound(0)
        for i in range(24):
            pgb.fill_rect(0,0,6*i,240,BLACK)
            pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
            pgb.show()
        break
    pgb.show()

with open("Intro Text.csv") as r:
    data=r.read()
data=data.split("\n")
data=data[language]
words=[]
for i in data.split(", "):
    word=i.split("/")
    words.append(tuple(word))
words=tuple(words)


def circle(x,y,r,c):
  pgb.hline(x-r,y,r*2,c)
  for i in range(1,r):
    a = int(math.sqrt(r*r-i*i)) # Pythagoras!
    pgb.hline(x-a,y+i,a*2,c) # Lower half
    pgb.hline(x-a,y-i,a*2,c) # Upper half

# WELCOME SCREEN
for i in range(24):
    i=24-i
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
    pgb.create_text(version,160,225,ttcolor)
    percentage=get_batt_percentage()
    if percentage>100:
        pgb.create_text("USB",10,225, ttcolor)
    else:
        pgb.create_text(str(percentage)+"%",10,225,ttcolor)
    for g,f in enumerate(words[0]):
        pgb.create_text(f, -1, 12+g*12, WHITE)
    for g,f in enumerate(words[1]):
        pgb.create_text(f, -1, 36+(12*g), WHITE)
    for g,f in enumerate(words[2]):
        pgb.create_text(f, -1, 90+(12*g), WHITE)
    for g,f in enumerate(words[3]):
        pgb.create_text(f, -1, 140+(12*g), WHITE)
    for g,f in enumerate(words[4]):
        pgb.create_text(f, -1, 190+(g*12), WHITE)
    pgb.fill_rect(0,0,6*i,240,BLACK)
    pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
    pgb.show()
tick=1
while True:
    tick+=1
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
    pgb.create_text(version,160,225,ttcolor)
    percentage=get_batt_percentage()
    if percentage>100:
        pgb.create_text("USB",10,225, ttcolor)
    else:
        pgb.create_text(str(percentage)+"%",10,225,ttcolor)
    if percentage<20:
        pgb.create_text("BATTERY TOO LOW!",-1,30,PicoGameBoy.color(255,255,255))
        pgb.create_text("Please replace the", -1, 130, PicoGameBoy.color(255,255,255))
        pgb.create_text("batteries in your PicoBoy.", -1, 145, PicoGameBoy.color(255,255,255))
        pgb.create_text("Please switch your", -1, 200, PicoGameBoy.color(255,255,255))
        pgb.create_text("PicoBoy off.", -1, 215, PicoGameBoy.color(255,255,255))
        pgb.rect(75,60,80,40,PicoGameBoy.color(255,0,0))
        pgb.fill_rect(155,70,10,20,PicoGameBoy.color(255,0,0))
        pgb.line(75,60,155,99,PicoGameBoy.color(255,0,0))
        pgb.sound(0)
        pgb.sound(0,2)
        pgb.sound(0,3)
        pgb.sound(0,4)
        pgb.show_screen()
        exit()
    for g,f in enumerate(words[0]):
        pgb.create_text(f, -1, 12+g*12, WHITE)
    for g,f in enumerate(words[1]):
        pgb.create_text(f, -1, 36+(12*g), WHITE)
    for g,f in enumerate(words[2]):
        pgb.create_text(f, -1, 90+(12*g), WHITE)
    for g,f in enumerate(words[3]):
        pgb.create_text(f, -1, 140+(12*g), WHITE)
    for g,f in enumerate(words[4]):
        pgb.create_text(f, -1, 190+(g*12), WHITE)
    if pgb.button_A():
        pgb.sound(200)
        sleep(0.1)
        pgb.sound(0)
        for i in range(24):
            pgb.fill_rect(0,0,6*i,240,BLACK)
            pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
            pgb.show()
        break
    pgb.show()
    
    

def dpad(x,y,k=False):
    global u
    global d
    global l
    global r
    pgb.fill_rect(x-4, y+26, 98, 38, PicoGameBoy.color(100,100,100))
    pgb.fill_rect(x+26, y-4, 38, 98, PicoGameBoy.color(100,100,100))
    pgb.fill_rect(x, y+30, 90, 30, PicoGameBoy.color(0,0,0))
    pgb.fill_rect(x+30, y, 30, 90, PicoGameBoy.color(0,0,0))
    if k:
        u=False
        d=False
        l=False
        r=False
    if u and d and l and r:
        pgb.fill_rect(x, y+30, 90, 30, PicoGameBoy.color(100,100,100))
        pgb.fill_rect(x+30, y, 30, 90, PicoGameBoy.color(100,100,100))
        pgb.blit(checkmark, x+38, y+38, mask)
    else:
        if u:
            pgb.fill_rect(x+30,y,30,30,PicoGameBoy.color(100,100,100))
            pgb.blit(checkmark, x+37,y+2, mask)
        else:
            pgb.poly(x+45,y+5,array('h',[0,0,-10,10,10,10]),WHITE,True)
        if d:
            pgb.fill_rect(x+30,y+60,30,30,PicoGameBoy.color(100,100,100))
            pgb.blit(checkmark, x+37,y+67, mask)
        else:
            pgb.poly(x+45,y+85,array('h',[0,0,-10,-10,10,-10]),WHITE,True)
        if l:
            pgb.fill_rect(x,y+30,30,30,PicoGameBoy.color(100,100,100))
            pgb.blit(checkmark, x+4,y+37, mask)
        else:
            pgb.poly(x+5,y+45,array('h',[0,0,10,-10,10,10]),WHITE,True)
        if r:
            pgb.fill_rect(x+60,y+30,30,30,PicoGameBoy.color(100,100,100))
            pgb.blit(checkmark, x+69,y+37, mask)
        else:
            pgb.poly(x+85,y+45,array('h',[0,0,-10,-10,-10,10]),WHITE,True)

def soundeffect():
    pgb.sound(200)
    sleep(0.05)
    pgb.sound(0)
    pgb.sound(300)
    sleep(0.05)
    pgb.sound(0)
    
def soundeffectbad():
    pgb.sound(200)
    sleep(0.05)
    pgb.sound(0)
    pgb.sound(100)
    sleep(0.05)
    pgb.sound(0)

# BUTTON TEST
padx=25
pady=70
a=False
b=False
se=False
st=False
u=False
d=False
l=False
r=False
h=False
with open("Checkmark.sprt", "rb") as r:
    checkmark=FrameBuffer(bytearray(r.read()),16,16,RGB565)
mask=PicoGameBoy.color(31,17,9)
for i in range(24):
    i=24-i
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
    for g,f in enumerate(words[5]):
        pgb.create_text(f, -1, 15+(12*g), PicoGameBoy.color(255,255,255))
    circle(200,90,24,PicoGameBoy.color(100,100,100))
    circle(200,90,20,PicoGameBoy.color(220,0,0))
    pgb.create_text("A", 196, 86, PicoGameBoy.color(255,255,255))
    circle(160,140,24,PicoGameBoy.color(100,100,100))
    circle(160,140,20,PicoGameBoy.color(220,0,0))
    pgb.create_text("B", 157, 137, PicoGameBoy.color(255,255,255))
    pgb.fill_rect(96, 36, 48, 28, PicoGameBoy.color(100,100,100))
    pgb.fill_rect(100, 40, 40, 20, PicoGameBoy.color(200,200,200))
    pgb.create_text("Home", -1, 45, PicoGameBoy.color(255,255,255))
    pgb.fill_rect(41, 176, 68, 28, PicoGameBoy.color(100,100,100))
    pgb.fill_rect(45, 180, 60, 20, PicoGameBoy.color(200,200,200))
    pgb.create_text("Select", 51, 186, PicoGameBoy.color(255,255,255))
    pgb.fill_rect(131, 176, 68, 28, PicoGameBoy.color(100,100,100))
    pgb.fill_rect(135, 180, 60, 20, PicoGameBoy.color(200,200,200))
    pgb.create_text("Start", 144, 186, PicoGameBoy.color(255,255,255))
    for g,f in enumerate(words[6]):
        pgb.create_text(f, -1, 210+(g*12), PicoGameBoy.color(255,255,255))
    dpad(padx,pady,True)
    pgb.fill_rect(0,0,6*i,240,BLACK)
    pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
    pgb.show()
    
while True:
    if pgb.button_up() and not u:
        soundeffect()
        u=True
    if pgb.button_down()and not d:
        soundeffect()
        d=True
    if pgb.button_left()and not l:
        soundeffect()
        l=True
    if pgb.button_right()and not r:
        soundeffect()
        r=True
    
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
    for g,f in enumerate(words[5]):
        pgb.create_text(f, -1, 15+(12*g), PicoGameBoy.color(255,255,255))
    if pgb.button_A()and not a:
        soundeffect()
        a=True
    circle(200,90,24,PicoGameBoy.color(100,100,100))
    if not a:
        circle(200,90,20,PicoGameBoy.color(220,0,0))
        pgb.create_text("A", 196, 86, PicoGameBoy.color(255,255,255))
    else:
        pgb.blit(checkmark,192,82,mask)
    
    if pgb.button_B()and not b:
        soundeffect()
        b=True
    circle(160,140,24,PicoGameBoy.color(100,100,100))
    if not b:
        circle(160,140,20,PicoGameBoy.color(220,0,0))
        pgb.create_text("B", 157, 137, PicoGameBoy.color(255,255,255))
    else:
        pgb.blit(checkmark,152,132,mask)
    if pgb.button_Home()and not h:
        soundeffect()
        h=True
    pgb.fill_rect(96, 36, 48, 28, PicoGameBoy.color(100,100,100))
    if not h:
        pgb.fill_rect(100, 40, 40, 20, PicoGameBoy.color(200,200,200))
        pgb.create_text("Home", -1, 45, PicoGameBoy.color(255,255,255))
    else:
        pgb.blit(checkmark, 112, 42, mask)
    if pgb.button_select()and not se:
        soundeffect()
        se=True
    pgb.fill_rect(41, 176, 68, 28, PicoGameBoy.color(100,100,100))
    if not se:
        pgb.fill_rect(45, 180, 60, 20, PicoGameBoy.color(200,200,200))
        pgb.create_text("Select", 51, 186, PicoGameBoy.color(255,255,255))
    else:
        pgb.blit(checkmark, 67, 182, mask)
    if pgb.button_start()and not st:
        soundeffect()
        st=True
    pgb.fill_rect(131, 176, 68, 28, PicoGameBoy.color(100,100,100))
    if not st:
        pgb.fill_rect(135, 180, 60, 20, PicoGameBoy.color(200,200,200))
        pgb.create_text("Start", 144, 186, PicoGameBoy.color(255,255,255))
    else:
        pgb.blit(checkmark, 157, 182, mask)
    for g,f in enumerate(words[6]):
        pgb.create_text(f, -1, 210+(g*12), PicoGameBoy.color(255,255,255))
    dpad(padx,pady)
    if a and b and h and st and se and u and d and l and r:
        pgb.fill_rect(25, 105, 190, 14+(len(words[7])*12), BLACK)
        for g,f in enumerate(words[7]):
            pgb.create_text(f, -1, 116+(g*12), WHITE)
        pgb.show()
        sleep(0.5)
        pgb.sound(300)
        sleep(0.05)
        pgb.sound(0)
        pgb.sound(400)
        sleep(0.5)
        pgb.sound(0)
        sleep(2.5)
        for i in range(24):
            pgb.fill_rect(0,0,6*i,240,BLACK)
            pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
            pgb.show()
        break
        break
    pgb.show()
    pgb.sound(0)
    
    
#SOUND TEST
    
for i in range(24):
    i=24-i
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
    for g,f in enumerate(words[8]):
        pgb.create_text(f, -1, 15+(g*12), PicoGameBoy.color(255,255,255))
    for g,f in enumerate(words[9]):
        pgb.create_text(f, -1, 48+(g*12), PicoGameBoy.color(255,255,255))
    for g,f in enumerate(words[10]):
        pgb.create_text(f, -1, 116+(g*12), PicoGameBoy.color(255,255,255))
    for g,f in enumerate(words[11]):
        pgb.create_text(f, -1, 200+(g*12), PicoGameBoy.color(255,255,255))
    pgb.fill_rect(0,0,6*i,240,BLACK)
    pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
    pgb.show()
    
pgb.fill(PicoGameBoy.color(*bgcolors[8]))
for g,f in enumerate(words[8]):
    pgb.create_text(f, -1, 15+(g*12), PicoGameBoy.color(255,255,255))
for g,f in enumerate(words[9]):
    pgb.create_text(f, -1, 48+(g*12), PicoGameBoy.color(255,255,255))
for g,f in enumerate(words[10]):
    pgb.create_text(f, -1, 116+(g*12), PicoGameBoy.color(255,255,255))
for g,f in enumerate(words[11]):
    pgb.create_text(f, -1, 200+(g*12), PicoGameBoy.color(255,255,255))
pgb.show()

while True:
    if pgb.button_A():
        pgb.sound(200)
        sleep(0.1)
        pgb.sound(0)
        break
channels=[]
for i in range(4):
    loop=0
    pgb.fill_rect(0,100,240,140,PicoGameBoy.color(*bgcolors[8]))
    for g,f in enumerate(words[12]):
        pgb.create_text(f+str(i+1)+"", -1, 116+(12*g), WHITE)
    for g,f in enumerate(words[13]):
        pgb.create_text(f, -1, 200+(g*13), PicoGameBoy.color(255,255,255))
    pgb.show()
    sleep(1)
    pgb.sound(100*(i+1), i+1)
    cha=words[14][0]
    while True:
        loop+=1
        if loop==500:
            pgb.sound(0,i+1)
            soundeffectbad()
            pgb.create_text(cha+str(i+1)+words[15][0], -1, 130, WHITE)
            channels.append(False)
            break
        if pgb.button_A():
            pgb.sound(0,i+1)
            soundeffect()
            channels.append(True)
            pgb.create_text(cha+str(i+1)+words[16][0], -1, 130, WHITE)
            break
        sleep(0.005)
    pgb.show()
    sleep(2)

pgb.fill_rect(0,100,240,140,PicoGameBoy.color(*bgcolors[8]))
if all(channels):
    for g,f in enumerate(words[17]):
        pgb.create_text(f, -1, 116+(g*12), WHITE)
    pgb.show()
    sleep(0.5)
    pgb.sound(300)
    sleep(0.05)
    pgb.sound(0)
    pgb.sound(400)
    sleep(0.5)
    pgb.sound(0)
    sleep(2.5)
else:
    for g,f in enumerate(words[18]):
        pgb.create_text(f, -1, 116+(g*12), WHITE)
    for g,f in enumerate(words[19]):
        pgb.create_text(f, -1, 140+(g*12), WHITE)

    pgb.show()
    exit()
    
    
def readchunk_mask(filename,x2,y2,w,h,cmask=57351):
    with open(filename,"rb") as r:
            for x in range(h):
                tempfb=FrameBuffer(bytearray(r.read(2*w)),w,1,RGB565)
                pgb.blit(tempfb,x2,y2+x,cmask)
                del tempfb
    
# TESTS PASSED
t=0

pgb.sound(100)
while True:
    t+=1
    if t==1:
        pgb.sound(0)
        pgb.sound(200)
    if t==2:
        pgb.sound(0)
        pgb.sound(300)
    if t==3:
        pgb.sound(0)
        pgb.sound(100,1)
        pgb.sound(200,2)
        pgb.sound(300,3)
        pgb.sound(400,4)
    if t==6:
        pgb.sound(0,1)
        pgb.sound(0,2)
        pgb.sound(0,3)
        pgb.sound(0,4)
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
    for g,f in enumerate(words[20]):
        pgb.create_text(f, -1, 15+(g*12), PicoGameBoy.color(255,255,255))
    for g,f in enumerate(words[21]):
        pgb.create_text(f, -1, 33+(g*12), PicoGameBoy.color(255,255,255))
    px=70
    py=70
    readchunk_mask("Data Upload Mode.pbimg",px,py,100,100,cmask=PicoGameBoy.color(31,17,9))
    pgb.fill_rect(px,py,100,50,PicoGameBoy.color(*bgcolors[8]))
    pgb.fill_rect(px+39,py+62,22,23,BLACK)
    pgb.blit(checkmark, px+42, py+65, mask)
    for g,f in enumerate(words[22]):
        pgb.create_text(f, -1, 82+(g*12), PicoGameBoy.color(255,255,255))
    for g,f in enumerate(words[23]):
        pgb.create_text(f, -1, 200+(g*12), WHITE)
    if pgb.button_A():
        pgb.sound(0,1)
        pgb.sound(0,2)
        pgb.sound(0,3)
        pgb.sound(0,4)
        sleep(0.1)
        for i in range(24):
            pgb.fill_rect(0,0,6*i,240,BLACK)
            pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
            pgb.show()
        break
    pgb.show()
    
# CHOOSE BG
bgcolor565=PicoGameBoy.color(*bgcolors[8])
runcheck=True
bindex=8
for i in range(24):
    i=24-i
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
        
    pgb.fill(bgcolor565)
    for g,f in enumerate(words[24]):
        pgb.create_text(f,-1,113+(g*12),ttcolor)
    for g,f in enumerate(words[25]):
        pgb.create_text(f,-1,200+(g*12),ttcolor)
        
    pgb.fill_rect(0,0,6*i,240,BLACK)
    pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
    pgb.show()
while True:
    pgb.fill(bgcolor565)
    for g,f in enumerate(words[24]):
        pgb.create_text(f,-1,113+(g*12),ttcolor)
    for g,f in enumerate(words[25]):
        pgb.create_text(f,-1,200+(g*12),ttcolor)
    if runcheck:
        runcheck=False
    if pgb.button_A():
        pgb.sound(200)
        sleep(0.1)
        pgb.sound(0)
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
            ottcolor=WHITE
        else:
            ottcolor=BLACK
        selectcolor=PicoGameBoy.color(127,127,127)
        if tcolor==0:
            selectcolor=PicoGameBoy.color(200,200,200)
        pgb.fill(bgcolor565)
        for g,f in enumerate(words[24]):
            pgb.create_text(f,-1,113+(g*12),ttcolor)
        for g,f in enumerate(words[25]):
            pgb.create_text(f,-1,200+(g*12),ttcolor)
        sleep(0.1)
for i in range(24):
    pgb.fill_rect(0,0,6*i,240,BLACK)
    pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
    pgb.show()
    
# CHOOSE BRIGHTNESS
for i in range(24):
    i=24-i
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
        
    pgb.fill(bgcolor565)
    pgb.rect(20,110,200,20,ttcolor)
    brightness=pgb.bl.duty_u16()-10000
    width=int((brightness/55000)*198)
    percentage=int((brightness/55000)*100)
    pgb.fill_rect(21,111,width,18,ttcolor)
    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
    for g,f in enumerate(words[26]):
        pgb.create_text(f,-1,140+(g*12),ttcolor)
    for g,f in enumerate(words[27]):
        pgb.create_text(f,-1,200+(g*12),ttcolor)
        
    pgb.fill_rect(0,0,6*i,240,BLACK)
    pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
    pgb.show()
while True:
    pgb.fill(bgcolor565)
    pgb.rect(20,110,200,20,ttcolor)
    brightness=pgb.bl.duty_u16()-10000
    width=int((brightness/55000)*198)
    percentage=int((brightness/55000)*100)
    pgb.fill_rect(21,111,width,18,ttcolor)
    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
    for g,f in enumerate(words[26]):
        pgb.create_text(f,-1,140+(g*12),ttcolor)
    for g,f in enumerate(words[27]):
        pgb.create_text(f,-1,200+(g*12),ttcolor)
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
    if pgb.button_A():
        pgb.sound(200)
        sleep(0.1)
        pgb.sound(0)
        break
    pgb.show()
for i in range(24):
    pgb.fill_rect(0,0,6*i,240,BLACK)
    pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
    pgb.show()

# CHOOSE VOLUME
for i in range(24):
    i=24-i
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
        
    pgb.fill(bgcolor565)
    pgb.rect(20,110,200,20,ttcolor)
    volume=pgb.vol
    width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
    percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
    pgb.fill_rect(21,111,width,18,ttcolor)
    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
    for g,f in enumerate(words[28]):
        pgb.create_text(f,-1,140+(g*12),ttcolor)
    for g,f in enumerate(words[29]):
        pgb.create_text(f,-1,200+(g*12),ttcolor)
        
    pgb.fill_rect(0,0,6*i,240,BLACK)
    pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
    pgb.show()
while True:
    pgb.fill(bgcolor565)
    pgb.rect(20,110,200,20,ttcolor)
    volume=pgb.vol
    width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
    percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
    pgb.fill_rect(21,111,width,18,ttcolor)
    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
    for g,f in enumerate(words[28]):
        pgb.create_text(f,-1,140+(g*12),ttcolor)
    for g,f in enumerate(words[29]):
        pgb.create_text(f,-1,200+(g*12),ttcolor)
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
    if pgb.button_A():
        pgb.sound(200)
        sleep(0.1)
        pgb.sound(0)
        sleep(0.4)
        pgb.sound(0)
        break
    pgb.show()

# ALL DONE
t=0
pgb.sound(100)
while True:
    t+=1
    if t==1:
        pgb.sound(0)
        pgb.sound(200)
    if t==2:
        pgb.sound(0)
        pgb.sound(300)
    if t==3:
        pgb.sound(0)
        pgb.sound(100,1)
        pgb.sound(200,2)
        pgb.sound(300,3)
        pgb.sound(400,4)
    if t==6:
        pgb.sound(0,1)
        pgb.sound(0,2)
        pgb.sound(0,3)
        pgb.sound(0,4)
    pgb.fill(PicoGameBoy.color(*bgcolors[8]))
    for g,f in enumerate(words[30]):
        pgb.create_text(f, -1, 15+(12*g), PicoGameBoy.color(255,255,255))
    for g,f in enumerate(words[31]):
        pgb.create_text(f, -1, 45+(g*12), PicoGameBoy.color(255,255,255))
    px=70
    py=70
    readchunk_mask("Data Upload Mode.pbimg",px,py,100,100,cmask=PicoGameBoy.color(31,17,9))
    pgb.fill_rect(px,py,100,50,PicoGameBoy.color(*bgcolors[8]))
    pgb.fill_rect(px+39,py+62,22,23,BLACK)
    for g,f in enumerate(words[32]):
        pgb.create_text(f, -1, 200+(g*12), WHITE)
    if pgb.button_Home():
        pgb.sound(200)
        sleep(0.1)
        pgb.sound(0)
        for i in range(24):
            pgb.fill_rect(0,0,6*i,240,BLACK)
            pgb.fill_rect(240-(6*i),0,6*i,240,BLACK)
            pgb.show()
        remove("Intro Text.csv")
        remove("Checkmark.sprt")
        remove("main.py")
        rename("title.py", "main.py")
        reset()
    pgb.show()
