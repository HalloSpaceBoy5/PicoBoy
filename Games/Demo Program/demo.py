#Written by HalloSpaceBoy
from os import rename
rename("main.py", "demo.py")
rename("title.py", "main.py")
from time import sleep
import random
import math
from PicoGameBoy import PicoGameBoy
pgb=PicoGameBoy()

def check_collision(speed,detectionradius, posx, posy, width, height, posx2, posy2, width2, height2):
    bbox1 = [posx, posy, posx + width, posy + height]
    bbox2 = [posx2, posy2, posx2 + width2, posy2 + height2]

    if bbox1[0] < bbox2[2] and bbox1[2] > bbox2[0] and bbox1[1] < bbox2[3] and bbox1[3] > bbox2[1]:
        if posx + width + speed >= posx2 and posx - speed <= posx2 + width2 and posy + height + speed >= posy2 and posy - speed <= posy2 + height2:
            return True
    
    return False

pgb.fill(PicoGameBoy.color(255,0,0))
pgb.show()
sleep(0.5)
pgb.fill(PicoGameBoy.color(0,255,0))
pgb.show()
sleep(0.5)
pgb.fill(PicoGameBoy.color(0,0,255))
pgb.show()
sleep(0.5)
pgb.fill(PicoGameBoy.color(0,0,0))
pgb.create_text("Welcome to the",-1,100,PicoGameBoy.color(255,255,255))
pgb.create_text("Demo Program!",-1,115,PicoGameBoy.color(255,255,255))
pgb.create_text("Press A to begin",-1,150,PicoGameBoy.color(255,255,255))
pgb.show()
while True:
    if pgb.button_A():
        pgb.fill(PicoGameBoy.color(100,100,100))
        pgb.show()
        break

class dvd:
    def __init__(self):
        self.playerx=random.randint(10,210)
        self.playery=random.randint(10,210)
        self.color=(255,0,0)
        self.speedx=5
        self.speedy=5

    def update(self):
        if self.playerx<0:
            self.speedx=random.randint(3, 7)
            self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pgb.sound(random.randint(100, 500))
        if self.playerx>220:
            self.speedx=random.randint(-7, -3)
            self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pgb.sound(random.randint(100, 500))
        if self.playery<0:
            self.speedy=random.randint(3, 7)
            self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pgb.sound(random.randint(100, 500))
        if self.playery>220:
            self.speedy=random.randint(-7, -3)
            self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pgb.sound(random.randint(100, 500))
        self.playery+=self.speedy
        self.playerx+=self.speedx
        pgb.fill_rect(self.playerx,self.playery,20,20,PicoGameBoy.color(*self.color))

blocks=[]
blocks.append(dvd())
sleep(0.25)
tick=0
while True:
    pgb.fill(PicoGameBoy.color(0,0,0))
    if pgb.button_A():
        for i in blocks:
            del i
        del blocks
        break
    if tick%4==0 and len(blocks)<50:
        blocks.append(dvd())
    for i in blocks:
        i.update()
    pgb.create_text("Press A to continue", -1, 15, PicoGameBoy.color(255,255,255))
    pgb.show()
    sleep(0.025)
    tick+=1
    pgb.sound(0)

playery=10
playerx=10
def char(x,y):
    pgb.fill_rect(x,y,20,20,PicoGameBoy.color(255,255,255))
    pgb.fill_rect(x+2, y+16, 16, 2, PicoGameBoy.color(0,0,0))
    pgb.fill_rect(x+2, y+10, 2, 6, PicoGameBoy.color(0,0,0))
    pgb.fill_rect(x+16, y+10, 2, 6, PicoGameBoy.color(0,0,0))
    pgb.fill_rect(x+2, y+2, 5, 5, PicoGameBoy.color(0,0,0))
    pgb.fill_rect(x+13, y+2, 5, 5, PicoGameBoy.color(0,0,0))
def flag(x,y):
    pgb.fill_rect(x, y+16, 20, 4, PicoGameBoy.color(255,255,255))
    pgb.fill_rect(x+8, y, 4, 16, PicoGameBoy.color(200,200,200))
    pgb.fill_rect(x, y, 8, 6, PicoGameBoy.color(255,0,0))
pgb.sound(0)
flagposx=random.randint(0, 220)
flagposy=random.randint(0, 220)
tick=0
while True:
    pgb.fill(PicoGameBoy.color(0,0,0))
    if pgb.button_Home():
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()
    if tick%10==0:
        pgb.sound(random.randint(100, 500))
        flagposx=random.randint(0, 220)
        while abs(flagposx) < abs(playerx):
            flagposx=random.randint(0, 220)
        flagposy=random.randint(0, 220)
        while abs(flagposy) < abs(playery):
            flagposy=random.randint(0, 220)
    if pgb.button_up() and playery>0:
        playery-=10
    if pgb.button_down() and playery<220:
        playery+=10
    if pgb.button_left() and playerx>0:
        playerx-=10
    if pgb.button_right() and playerx<220:
        playerx+=10
    if check_collision(10, 30, playerx, playery, 20, 20, flagposx, flagposy, 20, 20):
        break
    flag(flagposx, flagposy)
    char(playerx, playery)
    pgb.create_text("Reach the goal", -1, 15, PicoGameBoy.color(255,255,255))
    pgb.show()
    tick+=1
    sleep(0.05)
    pgb.sound(0)

heart=["###############","###############","###@@@###@@@###","##@%%%@#@%%%@##","##@%#%%@%%%%@##","##@%##%%%%%%@##","##@%%%%%%%%%@##","##@%%%%%%%%%@##","##@%%%%%%%%%@##","###@%%%%%%%@###","####@%%%%%@####","#####@%%%@#####","######@%@######","#######@#######","###############","###############"]
pgb.fill(PicoGameBoy.color(100,100,100))
pgb.show()
pgb.sound(0)
sleep(1)
for line in range(len(heart)):
    for char in range(len(heart[line])):
        if heart[line][char]=="#":
            pgb.fill_rect(char*16, line*16, 16,16,PicoGameBoy.color(255,255,255))
        if heart[line][char]=="@":
            pgb.fill_rect(char*16, line*16, 16,16,PicoGameBoy.color(0,0,0))
        if heart[line][char]=="%":
            pgb.fill_rect(char*16, line*16, 16,16,PicoGameBoy.color(255,0,0))
        pgb.create_text("Heart!", -1, 15, PicoGameBoy.color(0,0,0))
        pgb.show()
pgb.sound(123)
sleep(0.2)
pgb.sound(0)
pgb.sound(155)
sleep(0.2)
pgb.sound(0)
pgb.sound(185)
sleep(0.2)
pgb.sound(0)
pgb.sound(246)
sleep(0.2)
pgb.sound(0)
sleep(1)

def dpad(x,y):
    pgb.fill_rect(x, y+25, 80, 30, PicoGameBoy.color(200,200,200))
    pgb.fill_rect(x+25, y, 30, 80, PicoGameBoy.color(200,200,200))
    pgb.line(x+28, y+16, x+40, y+4, PicoGameBoy.color(255,255,255))
    pgb.line(x+52, y+16, x+40, y+4, PicoGameBoy.color(255,255,255))
    pgb.line(x+28, y+16, x+52, y+16, PicoGameBoy.color(255,255,255))
    pgb.line(x+28, y+64, x+40, y+76, PicoGameBoy.color(255,255,255))
    pgb.line(x+52, y+64, x+40, y+76, PicoGameBoy.color(255,255,255))
    pgb.line(x+28, y+64, x+52, y+64, PicoGameBoy.color(255,255,255))
    pgb.line(x+16, y+28, x+4, y+40, PicoGameBoy.color(255,255,255))
    pgb.line(x+16, y+52, x+4, y+40, PicoGameBoy.color(255,255,255))
    pgb.line(x+16, y+28, x+16, y+52, PicoGameBoy.color(255,255,255))
    pgb.line(x+64, y+28, x+76, y+40, PicoGameBoy.color(255,255,255))
    pgb.line(x+64, y+52, x+76, y+40, PicoGameBoy.color(255,255,255))
    pgb.line(x+64, y+28, x+64, y+52, PicoGameBoy.color(255,255,255))

def circle(x,y,r,c):
  pgb.hline(x-r,y,r*2,c)
  for i in range(1,r):
    a = int(math.sqrt(r*r-i*i)) # Pythagoras!
    pgb.hline(x-a,y+i,a*2,c) # Lower half
    pgb.hline(x-a,y-i,a*2,c) # Upper half

while True:
    padx=25
    pady=80
    if pgb.button_up():
        pady-=10
        pgb.sound(174)
    if pgb.button_down():
        pady+=10
        pgb.sound(220)
    if pgb.button_left():
        padx-=10
        pgb.sound(261)
    if pgb.button_right():
        padx+=10
        pgb.sound(329)
    
    pgb.fill(PicoGameBoy.color(0,0,0))
    pgb.create_text("Test your buttons!", -1, 15, PicoGameBoy.color(255,255,255))
    if pgb.button_A():
        circle(200,100,20,PicoGameBoy.color(100,100,100))
    else:
        circle(200,100,20,PicoGameBoy.color(200,200,200))
    pgb.create_text("A", 197, 97, PicoGameBoy.color(255,255,255))
    if pgb.button_B():
        circle(160,150,20,PicoGameBoy.color(100,100,100))
    else:
        circle(160,150,20,PicoGameBoy.color(200,200,200))
    pgb.create_text("B", 157, 147, PicoGameBoy.color(255,255,255))
    if pgb.button_Home():
        pgb.fill_rect(100, 40, 40, 20, PicoGameBoy.color(100,100,100))
    else:
        pgb.fill_rect(100, 40, 40, 20, PicoGameBoy.color(200,200,200))
    pgb.create_text("Home", -1, 45, PicoGameBoy.color(255,255,255))
    if pgb.button_select():
        pgb.fill_rect(55, 180, 60, 20, PicoGameBoy.color(100,100,100))
    else:
        pgb.fill_rect(55, 180, 60, 20, PicoGameBoy.color(200,200,200))
    pgb.create_text("Select", 60, 185, PicoGameBoy.color(255,255,255))
    if pgb.button_start():
        pgb.fill_rect(125, 180, 60, 20, PicoGameBoy.color(100,100,100))
    else:
        pgb.fill_rect(125, 180, 60, 20, PicoGameBoy.color(200,200,200))
    pgb.create_text("Start", 130, 187, PicoGameBoy.color(255,255,255))
    pgb.create_text("Press all buttons on", -1, 210, PicoGameBoy.color(255,255,255))
    pgb.create_text("the D-PAD to continue", -1, 225, PicoGameBoy.color(255,255,255))
    if pgb.button_up() and pgb.button_down() and pgb.button_left() and pgb.button_right():
        break
    dpad(padx,pady)
    pgb.show()
    pgb.sound(0)


#end
pgb.fill(PicoGameBoy.color(0,0,0))
textpos=50
tpos=-1
pgb.create_text("See you later!", -1, 50, PicoGameBoy.color(255,255,255))
pgb.show()
pgb.sound(0)
sleep(1)
while True:
    textpos+=5
    if textpos>240:
        tpos+=1
    #pgb.create_text("See you later!", -1, 50, PicoGameBoy.color(255,255,255))
    pgb.hline(0, tpos, 240, PicoGameBoy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    pgb.show()
    if tpos>240:
        sleep(2)
        pgb.sound(246)
        sleep(0.2)
        pgb.sound(0)
        pgb.sound(185)
        sleep(0.2)
        pgb.sound(0)
        pgb.sound(155)
        sleep(0.2)
        pgb.sound(0)
        pgb.sound(123)
        sleep(0.2)
        pgb.sound(0)
        sleep(1)
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()

    

