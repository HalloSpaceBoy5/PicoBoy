# Original game designed for the PicoBoy by HalloSpaceBoy
from os import rename
from PicoGameBoy import PicoGameBoy
rename("main.py","/Starship/Starship.py")
rename("title.py","main.py")
del rename
pgb=PicoGameBoy()
starship=bytearray(b'1\x861\x861\x86\x00\x001\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x86\x00\x001\x861\x861\x861\x861\x861\x86\x00\x001\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x86\x00\x001\x861\x861\x861\x861\x86\x00\x00\xff\xff\x00\x001\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x86\x00\x00\xff\xff\x00\x001\x861\x861\x861\x86\x00\x00\xff\xff\x00\x001\x861\x861\x861\x861\x861\x861\x86\x00\x001\x861\x861\x861\x861\x861\x861\x86\x00\x00\xff\xff\x00\x001\x861\x861\x86\x00\x00\xff\xff\xff\xff\xff\xff\x00\x001\x861\x861\x861\x861\x86\x00\x00\x05^\x00\x001\x861\x861\x861\x861\x86\x00\x00\xff\xff\xff\xff\xff\xff\x00\x001\x861\x86\x00\x00\xff\xff\xff\xff\xff\xff\x00\x001\x861\x861\x861\x861\x86\x00\x00\x05^\x00\x001\x861\x861\x861\x861\x86\x00\x00\xff\xff\xff\xff\xff\xff\x00\x001\x861\x86\x00\x00\xff\xff\xff\xff\xff\xff\x00\x001\x861\x861\x861\x86\x00\x00\x05^\x05^\x05^\x00\x001\x861\x861\x861\x86\x00\x00\xff\xff\xff\xff\xff\xff\x00\x001\x86\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x001\x861\x861\x86\x00\x00\x05^\x00\x00\x05^\x00\x001\x861\x861\x86\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x9c\xf3\x00\x001\x861\x86\x00\x00\x05\xdf\x00\x00\x05^\x00\x00\x05\xdf\x00\x001\x861\x86\x00\x00\x9c\xf3\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x9c\xf3\x9c\xf3\x00\x001\x86\x00\x00\x00\x00\x05^\x05^\x05^\x00\x00\x00\x001\x86\x00\x00\x9c\xf3\x9c\xf3\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x9c\xf3\x9c\xf3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\x00\x00\x00\x00\x00\x00\x9c\xf3\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\x9c\xf3\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x00\x00\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\x00\x00\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x00\x00\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\x00\x00\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\x00\x001\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x86\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x9c\xf3\x9c\xf3\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x00\x00\x00\x001\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x86\x00\x00\x00\x00\x9c\xf3\x9c\xf3\x00\x00\x00\x00\x00\x00\x00\x001\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x86\x00\x00\x00\x00\x00\x00')
#OS Version detection
try:
    pgb.add_sprite(starship, 25,25,1)
except:
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.create_text("Update your OS!",-1,25,PicoGameBoy.color(255,255,255))
        pgb.create_text("Update your PicoBoy",-1,140,PicoGameBoy.color(255,255,255))
        pgb.create_text("to play this game.",-1,150,PicoGameBoy.color(255,255,255))
        pgb.show()
pgb.add_sprite(starship,25,25,3)
pgb.add_sprite(starship,25,25,4)
pgb.add_sprite(starship,25,25,2)
del starship
enemy=bytearray(b'1\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x86\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x001\x861\x861\x861\x86\x00\x00{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf\x00\x00\xa5\x14\xa5\x14\x00\x00\x00\x001\x861\x861\x861\x86\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa5\x14\xa5\x14\xa5\x14\x00\x00\x00\x001\x861\x861\x861\x86\x00\x00{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf\x00\x00\xa5\x14\xa5\x14\xa5\x14\x00\x00{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa5\x14\xa5\x14\xa5\x14\xa5\x14\x00\x00{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00{\xcf{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\xa5\x14\xa5\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81\xa6\x81\xa6\x81\xa6\x81\xa6\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x86\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd9$\xd9$\xd9$\x00\x00\x81\xa6\x81\xa6\x81\xa6\x81\xa6\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x86\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\xd9$\xd9$\xd9$\x00\x00\x81\xa6\x81\xa6\x81\xa6\x81\xa6\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x86\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\xd9$\xd9$\xd9$\x00\x00\x81\xa6\x81\xa6\x81\xa6\x81\xa6\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x86\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\xd9$\xd9$\xd9$\x00\x00\x81\xa6\x81\xa6\x81\xa6\x81\xa6\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x86\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd9$\xd9$\xd9$\x00\x00\x81\xa6\x81\xa6\x81\xa6\x81\xa6\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\xa5\x14\xa5\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81\xa6\x81\xa6\x81\xa6\x81\xa6\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00R\xaaR\xaaR\xaaR\xaa\x00\x00{\xcf{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\xa5\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00{\xcf{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa5\x14\xa5\x14\xa5\x14\xa5\x14\x00\x00{\xcf\x00\x001\x861\x861\x861\x86\x00\x00{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf\x00\x00\xa5\x14\xa5\x14\xa5\x14\x00\x00{\xcf\x00\x001\x861\x861\x861\x86\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa5\x14\xa5\x14\xa5\x14\x00\x00\x00\x001\x861\x861\x861\x86\x00\x00{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf{\xcf\x00\x00\xa5\x14\xa5\x14\x00\x00\x00\x001\x861\x861\x861\x86\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x001\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x861\x86')
pgb.add_sprite(enemy,25,25)
pgb.add_sprite(enemy,25,25,2)
del enemy
bullet=bytearray(b'1\x861\x861\x861\x861\x86\xd9$\xd9$\xd9$\xd9$\xd9$1\x861\x861\x861\x861\x861\x861\x861\x86\xd9$\xd9$\xd9$\xd9$\xd9$\xd9$\xd9$\xd9$\xd9$1\x861\x861\x861\x861\x86\xd9$\xd9$\xd9$\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xd9$\xd9$\xd9$1\x861\x861\x86\xd9$\xd9$\xd9$\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xd9$\xd9$\xd9$1\x861\x86\xd9$\xd9$\xa9\xa6\xa9\xa6\xa9\xa6\xf8\x00\xf8\x00\xf8\x00\xa9\xa6\xa9\xa6\xa9\xa6\xd9$\xd9$1\x86\xd9$\xd9$\xa9\xa6\xa9\xa6\xa9\xa6\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xa9\xa6\xa9\xa6\xa9\xa6\xd9$\xd9$\xd9$\xd9$\xa9\xa6\xa9\xa6\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xa9\xa6\xa9\xa6\xd9$\xd9$\xd9$\xd9$\xa9\xa6\xa9\xa6\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xa9\xa6\xa9\xa6\xd9$\xd9$\xd9$\xd9$\xa9\xa6\xa9\xa6\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xa9\xa6\xa9\xa6\xd9$\xd9$\xd9$\xd9$\xa9\xa6\xa9\xa6\xa9\xa6\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xa9\xa6\xa9\xa6\xa9\xa6\xd9$\xd9$1\x86\xd9$\xd9$\xa9\xa6\xa9\xa6\xa9\xa6\xf8\x00\xf8\x00\xf8\x00\xa9\xa6\xa9\xa6\xa9\xa6\xd9$\xd9$1\x861\x86\xd9$\xd9$\xd9$\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xd9$\xd9$\xd9$1\x861\x861\x86\xd9$\xd9$\xd9$\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xa9\xa6\xd9$\xd9$\xd9$1\x861\x861\x861\x861\x86\xd9$\xd9$\xd9$\xd9$\xd9$\xd9$\xd9$\xd9$\xd9$1\x861\x861\x861\x861\x861\x861\x861\x86\xd9$\xd9$\xd9$\xd9$\xd9$1\x861\x861\x861\x861\x86')
pgb.add_sprite(bullet,15,15)
del bullet
from time import sleep, ticks_diff, ticks_ms
from random import randint, choice as randomchoice
from math import sqrt
import _thread
from gc import collect
from rpmidi import RPMidi
currentmusic=[0000]
rept=True
starcoords=[]
for i in range(75):
    x=randint(10,200)
    y=randint(35,210)
    starcoords.append([x,y])
bullets=[]
static=[]
followers=[]
lives=3
playerx=100
playery=100
playerwidth=25
playerheight=25
exitthread=False
playerspeed=5
bulletspeed=3
followspeed=5
tick=0.0001
direction=0 #0=up, 1=down, 2=left, 3=right
level=0
class new_bullet:
    def __init__(self,posx,posy,direction,pos_in_list):
        self.posx=posx
        self.posy=posy
        self.direction=direction
        self.width=10
        self.height=10
        self.pil=pos_in_list
    def check_collision(self):
        global playerx
        global playery
        global playerwidth
        global playerheight
        global playerspeed
        cenpoint1=[self.posx+self.width/2,self.posy+self.height/2]
        cenpoint2=[playerx+playerwidth/2,playery+playerheight/2]
        dist=sqrt((cenpoint1[0]-cenpoint2[0])**2+(cenpoint1[1]-cenpoint2[1])**2)
        if dist<30:
            playerpos=[[self.posx,self.posy],[self.posx+self.width,self.posy],[self.posx,self.posy+self.height],[self.posx+self.width,self.posy+self.height]]
            colliderpos=[[playerx,playery],[playerx+playerwidth, playery],[playerx,playery+playerheight],[playerx+playerwidth,playery+playerheight]]
            if (playerpos[0][0]>colliderpos[0][0] or playerpos[1][0]>colliderpos[0][0]) and (playerpos[0][0]<colliderpos[1][0] or playerpos[1][0]<colliderpos[1][0]) and self.posy<colliderpos[0][1] and self.posy>colliderpos[0][1]-(playerspeed*2):
                return True
            elif (playerpos[0][0]>colliderpos[0][0] or playerpos[1][0]>colliderpos[0][0]) and (playerpos[0][0]<colliderpos[1][0] or playerpos[1][0]<colliderpos[1][0]) and self.posy>colliderpos[0][1] and self.posy<colliderpos[0][1]+(playerspeed*2):
                return True
            elif (playerpos[1][1]>colliderpos[1][1] or playerpos[2][1]>colliderpos[1][1]) and (playerpos[1][1]<colliderpos[2][1] or playerpos[2][1]<colliderpos[2][1]) and self.posx>colliderpos[2][0] and self.posx<colliderpos[2][0]+(playerspeed*2):
                    return True
            elif (playerpos[1][1]>colliderpos[1][1] or playerpos[2][1]>colliderpos[1][1]) and (playerpos[1][1]<colliderpos[2][1] or playerpos[2][1]<colliderpos[2][1]) and self.posx<colliderpos[2][0] and self.posx>colliderpos[2][0]-(playerspeed*2):
                    return True
    def update(self):
        global pgb
        global bulletspeed
        global bullets
        global lives
        if self.direction=="left":
            if self.posx<0:
                bullets.remove(self)
                del self
                return
            self.posx=self.posx-int(bulletspeed)
        elif (self.direction=="down"):
            if self.posy>=210-self.height:
                bullets.remove(self)
                del self
                return
            self.posy=self.posy+int(bulletspeed)
        pgb.sprite(6,self.posx,self.posy)
        if self.check_collision():
            try:
                bullets.remove(self)
            except:
                "no bullet"
            lives=lives-1
            lfreq=-100
            for i in range(2500):
                pgb.sound(500)
                pgb.sound(1500)
            pgb.sound(0)
            for i in bullets:
                del i
            bullets=[]
class enemy:
    def __init__(self, posx, posy, axis, delay,idd):
        self.posx=posx
        self.posy=posy
        self.axis=axis
        self.delay=delay
        self.counter=0
        self.idd=idd
    def update(self):
        global bullets
        global playerx
        global playery
        global followspeed
        if self.idd==0:
            if self.axis==0:
                pgb.sprite(5, self.posx, self.posy)
                if self.counter % self.delay == 0:
                    if len(bullets)-1<=0:
                        tlen=0
                    else:
                        tlen=len(bullets)-1
                    newB=new_bullet(self.posx+5, self.posy+35, "down", tlen)
                    bullets.append(newB)
            if self.axis==1:
                pgb.sprite(4, self.posx, self.posy)
                if self.counter % self.delay == 0:
                    if len(bullets)-1<=0:
                        tlen=0
                    else:
                        tlen=len(bullets)-1
                    newB = new_bullet(self.posx-25, self.posy+5, "left", tlen)
                    bullets.append( newB )
            self.counter=self.counter+1
        if self.idd==1:
            if self.axis==0:
                if self.posx<playerx:
                    self.posx=self.posx+followspeed
                if self.posx>playerx:
                    self.posx=self.posx-followspeed
                pgb.sprite(5, self.posx, self.posy)
                if self.counter % self.delay == 0:
                    if len(bullets)-1<=0:
                        tlen=0
                    else:
                        tlen=len(bullets)-1
                    newB=new_bullet(self.posx+5, self.posy+35, "down", tlen)
                    bullets.append(newB)
            if self.axis==1:
                if self.posy<playery:
                    self.posy=self.posy+followspeed
                if self.posy>playery:
                    self.posy=self.posy-followspeed
                pgb.sprite(4, self.posx, self.posy)
                if self.counter % self.delay == 0:
                    if len(bullets)-1<=0:
                        tlen=0
                    else:
                        tlen=len(bullets)-1
                    newB = new_bullet(self.posx-25, self.posy+5, "left", tlen)
                    bullets.append( newB )
            self.counter=self.counter+1
def play_music():
    global midi
    global rept
    global currentmusic
    global exitthread
    midi=RPMidi()
    while True:
        if exitthread:
            exitthread=False
            _thread.exit()
        if not currentmusic==[0000]:
            if rept and not currentmusic==[0000]:
                while rept and not currentmusic==[0000]:
                    midi.play_song(currentmusic)
            else:
                midi.play_song(currentmusic)
                currentmusic=[0000]
        sleep(tick)
def no_music():
    global currentmusic
    global rept
    global midi
    rept=False
    currentmusic=[0000]
    midi.stop_all_music()
    midi.stop_all()
def new_level():
    global direction
    global playerx
    global playery
    global level
    global tick
    global musicthread
    global currentmusic
    global rept
    global ls
    global starcoords
    global followers
    global exitthread
    global static
    global bullets
    playerx=100
    playery=100
    no_music()
    tps=1/tick
    aot=randint(15,20)
    counter=1
    level=level+1
    for i in followers:
        del i
    for i in static:
        del i
    for i in bullets:
        del i
    followers=[]
    static=[]
    bullets=[]
    lastaxs=-1
    axis=-2
    if level<=10:
        s=4
    elif level<=20:
        s=5
    else:
        s=6
    for i in range(s):
        while axis==lastaxs:
            axis=randint(0,1)
        lastaxs=axis
        if axis==0:
            x=randint(10,180)
            y=0
            static.append(enemy(x,y,axis,randint(40,80),0))
        elif axis==1:
            x=215
            y=randint(45,180)
            static.append(enemy(x,y,axis,randint(40,80),0))
    for i in range(2):
        while axis==lastaxs:
            axis=randint(0,1)
        lastaxs=axis
        if axis==0:
            x=randint(10,160)
            y=0
            followers.append(enemy(x,y,axis,randint(40,80),1))
        elif axis==1:
            x=215
            y=randint(45,205)
            followers.append(enemy(x,y,axis,randint(40,80),1))
    while True:
        musicchoice=randint(0,2)
        if not musicchoice==ls:
            ls=musicchoice
            break
    while True:
        rept=True
        if musicchoice==0:
            currentmusic=[0x90,48, 0x91,72, 1,228, 0x81, 0,5, 0x80, 0,10, 0x90,47, 1,234, 0x80, 0,10, 0x90,46, 0x91,75, 1,234, 0x80, 
0x81, 0,16, 0x90,45, 0,234, 0x80, 0,10, 0x90,47, 0,235, 0x80, 0,15, 0x90,48, 0x91,72, 1,234, 0x80, 0x81, 0,10, 
0x90,47, 1,229, 0x80, 0,15, 0x90,46, 0x91,70, 1,234, 0x80, 0x81, 0,16, 0x90,45, 0x91,70, 0,229, 0x80, 0,5, 
0x81, 0,10, 0x90,47, 0x91,71, 0,250, 0x80, 0x81, 0xF0]
        elif musicchoice==1:
            currentmusic=[0x90,72, 0x91,48, 1,238, 0x80, 0x81, 0,5, 0x90,49, 0x91,73, 1,234, 0x80, 0x81, 0,10, 0x90,47, 0x91,76, 0,245, 
0x81, 0,5, 0x91,75, 0,245, 0x80, 0x81, 0,5, 0x90,46, 1,234, 0x80, 0,10, 0x90,48, 0x91,72, 1,234, 0x81, 0,5, 
0x80, 0,5, 0x90,49, 0x91,73, 1,234, 0x80, 0x81, 0,10, 0x90,47, 0x91,76, 0,245, 0x81, 0,11, 0x91,75, 0,234, 
0x80, 0,5, 0x81, 0,5, 0x90,46, 0,6, 0x91,74, 0,239, 0x81, 0,5, 0x91,73, 0,250, 0x80, 0x81, 0xF0]
        else:
            currentmusic=[0x90,60, 0x91,72, 0,114, 0x81, 0,135, 0x91,72, 0,115, 0x81, 0,10, 0x91,72, 0,115, 0x80, 0x81, 0,10, 0x90,65, 
0x91,77, 1,234, 0x80, 0x81, 0,10, 0x90,60, 0,250, 0x91,72, 0,115, 0x81, 0,10, 0x91,72, 0,115, 0x80, 0x81, 0,10, 
0x90,63, 0x91,77, 1,234, 0x80, 0x81, 0,10, 0x90,60, 0x91,72, 0,115, 0x81, 0,135, 0x91,72, 0,115, 0x81, 0,10, 
0x91,72, 0,115, 0x80, 0x81, 0,10, 0x90,65, 0x91,77, 1,234, 0x80, 0x81, 0,10, 0x90,65, 1,5, 0x91,77, 0,229, 
0x80, 0x81, 0,16, 0x90,72, 0,5, 0x91,67, 0,104, 0x80, 0,10, 0x90,72, 0,115, 0x80, 0,10, 0x90,79, 0,250, 
0x80, 0x81, 0xF0]
        try:
            collect()
            _thread.start_new_thread(play_music, ())
        except:
            "Already running"
        if lives==0:
            return False
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.fill(PicoGameBoy.color(48,48,48))
        pgb.create_text(str(lives),225,10,PicoGameBoy.color(255,255,255))
        pgb.fill_rect(0,25,240,10,PicoGameBoy.color(175,175,175))
        pgb.fill_rect(0,215,240,10,PicoGameBoy.color(175,175,175))
        pgb.fill_rect(205,0,10,215,PicoGameBoy.color(175,175,175))
        for star in starcoords:
            pgb.fill_rect(star[0],star[1],1,1,PicoGameBoy.color(255,255,255))
        pgb.create_text("Level: "+str(level),150,228,PicoGameBoy.color(255,255,255))
        counter=counter+1
        if counter%(15)==0:
            aot=aot-1
        if aot<10:
            aotstr="0"+ str(aot)
        else:
            aotstr=str(aot)
        pgb.create_text("Time: "+aotstr,25,228,PicoGameBoy.color(255,255,255))
        if aot==0:
            return True
        for e in static:
            e.update()
        for e in followers:
            e.update()
        for bullet in bullets:
            bullet.update()
        if pgb.button_up() and playery>35:
            playery=playery-playerspeed
            direction=0
        elif pgb.button_down() and playery<215-playerheight:
            playery=playery+playerspeed
            direction=1
        elif pgb.button_left() and playerx>0:
            playerx=playerx-playerspeed
            direction=2
        elif pgb.button_right() and playerx<205-playerwidth:
            playerx=playerx+playerspeed
            direction=3
        pgb.sprite(direction,playerx,playery)
        if pgb.button_start():
                no_music()
                currentmusic=[0000]
                exitthread=True
                pgb.fill_rect(10,90,220,80,PicoGameBoy.color(0,0,0))
                pgb.center_text("Game Paused",PicoGameBoy.color(255,255,255))
                pgb.create_text("Press Start to resume", -1, 135, PicoGameBoy.color(255,255,255))
                pgb.show()
                sleep(0.5)
                while True:
                    pgb.fill_rect(10,90,220,80,PicoGameBoy.color(0,0,0))
                    pgb.center_text("Game Paused",PicoGameBoy.color(255,255,255))
                    pgb.create_text("Press Start to resume", -1, 135, PicoGameBoy.color(255,255,255))
                    pgb.show()
                    if pgb.button_Home():
                        homebootstop=open("/noboot", "w")
                        homebootstop.close()
                        pgb.fill(PicoGameBoy.color(0,0,0))
                        pgb.show()
                        machine.reset()
                        break
                    if pgb.button_start():
                        sleep(0.5)
                        break
                    sleep(tick)
                    print(randint(0,1000))
        pgb.show()
        sleep(tick)

rept=True
currentmusic=[0x90,48, 0x91,72, 1,244, 0x90,48, 0x91,74, 0,250, 0x90,51, 0,250, 0x92,72, 0x81, 0,250, 0x90,70, 0x82, 0,250, 
0x80, 1,244, 0x90,51, 0x91,72, 1,244, 0x90,51, 0x91,74, 0,250, 0x92,48, 0x80, 0,250, 0x90,73, 0x81, 0,250, 0x91,72, 
0x80, 0x82, 0,250, 0x90,71, 0x81, 0,250, 0x91,70, 0x80, 0,250, 0x81, 0xF0]
now = ticks_ms()
try:
    collect()
    _thread.start_new_thread(play_music, ())
except:
    "Already running"
while True:
    collect()
    if pgb.button_Home():
        homebootstop=open("/noboot", "w")
        homebootstop.close()
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()
        break
    pgb.load_image("/Starship/starship_title.bin")
    pgb.show()
    if ticks_diff(ticks_ms(), now) > 200:
        now = ticks_ms()
        pgb.create_text("HOLD A TO PLAY",-1,160,PicoGameBoy.color(255,255,255))
        pgb.show()
        while ticks_diff(ticks_ms(), now) < 200:
            sleep(0.020)
        now = ticks_ms()
    if pgb.button_start():
            x=open("Starship/highscoresStarship.sc", "r")
            scores=x.read()
            x.close()
            del x
            scores=scores.split("\n")
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.create_text("High Scores:", -1, 15, PicoGameBoy.color(255,255,255))
            for i in range(len(scores)):
                pgb.create_text("Score "+str(i+1)+": Level "+str(scores[i]), -1, 50+i*15, PicoGameBoy.color(255,255,255))
            pgb.create_text("Press B to exit", -1, 220, PicoGameBoy.color(255,255,255))
            while True:
                if pgb.button_B():
                    break
                if pgb.button_Home():
                    homebootstop=open("/noboot", "w")
                    homebootstop.close()
                    pgb.fill(PicoGameBoy.color(0,0,0))
                    pgb.show()
                    machine.reset()
                    break
                pgb.show()
    elif pgb.button_A():
        break
sleep(0.25)
ls=4

while True:
    if new_level():
            no_music()
            collect()
            try:
                _thread.start_new_thread(play_music, ())
            except:
                "Already running"
            currentmusic=[0x90,51, 0x91,63, 0,187, 0x92,50, 0x90,62, 0x81, 0,188, 0x91,51, 0x90,63, 0x82, 0,187, 0x91,52, 0x90,64, 0,188, 
0x92,51, 0x91,63, 0x80, 0,187, 0x90,52, 0x91,64, 0x82, 0,188, 0x90,53, 0x91,65, 0,62, 0x90,53, 0x91,65, 0,63, 
0x90,53, 0x91,65, 0,62, 0x90,53, 0x91,65, 0,63, 0x90,53, 0x91,65, 0,62, 0x90,53, 0x91,65, 0,63, 0x80, 0x81, 
0xF0]
            lives=3
            bulletspeed+=.25
            for i in followers:
                del i
            for i in static:
                del i
            for i in bullets:
                del i
            followers=[]
            static=[]
            bullets=[]
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.rect(70,20,100,80,PicoGameBoy.color(255,255,255))
            pgb.fill_rect(90, 30,10,10,PicoGameBoy.color(255,255,255))
            pgb.fill_rect(140, 30,10,10,PicoGameBoy.color(255,255,255))
            pgb.rect(90,60,60,20,PicoGameBoy.color(255,255,255))
            pgb.line(90,60,150,60,PicoGameBoy.color(0,0,0))
            pgb.create_text("Level Clear!",-1,125,PicoGameBoy.color(255,255,255))
            pgb.create_text("Press A to play",-1, 145, PicoGameBoy.color(255,255,255))
            pgb.create_text("the next level",-1, 160, PicoGameBoy.color(255,255,255))
            pgb.create_text("Press home to quit.", -1, 180, PicoGameBoy.color(255,255,255))
            pgb.create_text("Level: "+str(level),-1,200,PicoGameBoy.color(255,255,255))
            pgb.show()
            while True:
                if pgb.button_Home():
                    with open("Starship/highscoresStarship.sc", "r") as s:
                        scores=s.read().split("\n")
                        for r in range(len(scores)):
                            scores[r]=int(scores[r])
                    newscores=scores
                    newscores.append(int(level))
                    newscores.sort(reverse=True)
                    for i in range(len(newscores)): newscores[i]=str(newscores[i])
                    with open("Starship/highscoresStarship.sc", "w+") as w:
                        w.write("\n".join(newscores[:10]))
                    del newscores
                    del scores
                    homebootstop=open("/noboot", "w")
                    homebootstop.close()
                    pgb.fill(PicoGameBoy.color(0,0,0))
                    pgb.show()
                    machine.reset()
                    break
                elif pgb.button_A():
                    no_music()
                    break
    else:
        no_music()
        collect()
        try:
            _thread.start_new_thread(play_music, ())
        except:
            "Already running"
        currentmusic=[0x90,45, 0x91,48, 1,119, 0x80, 0x81, 0,250, 0x90,44, 0x91,47, 1,119, 0x80, 0x81, 0,250, 0x90,43, 0x91,46, 1,119, 
0x80, 0x81, 1,119, 0x90,41, 0x91,44, 0,62, 0x90,41, 0x91,44, 0,63, 0x90,41, 0x91,44, 0,62, 0x90,41, 0x91,44, 
0,63, 0x90,41, 0x91,44, 0,62, 0x90,41, 0x91,44, 0,63, 0x90,41, 0x91,44, 0,62, 0x90,41, 0x91,44, 0,63, 
0x90,41, 0x91,44, 0,62, 0x90,41, 0x91,44, 0,63, 0x90,41, 0x91,44, 0,62, 0x90,41, 0x91,44, 0,63, 0x90,41, 
0x91,44, 0,62, 0x90,41, 0x91,44, 0,63, 0x90,41, 0x91,44, 0,62, 0x90,41, 0x91,44, 0,63, 0x80, 0x81, 0xF0]
        for i in followers:
            del i
        for i in static:
            del i
        for i in bullets:
            del i
        bulletspeed=3
        followers=[]
        static=[]
        bullets=[]
        lives=3
        with open("Starship/highscoresStarship.sc", "r") as s:
            scores=s.read().split("\n")
            for r in range(len(scores)):
                scores[r]=int(scores[r])
        newscores=scores
        newscores.append(int(level))
        newscores.sort(reverse=True)
        for i in range(len(newscores)): newscores[i]=str(newscores[i])
        with open("Starship/highscoresStarship.sc", "w+") as w:
            w.write("\n".join(newscores[:10]))
        del newscores
        del scores
        pgb.sound(0)
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.rect(70,20,100,80,PicoGameBoy.color(255,255,255))
        pgb.fill_rect(90, 30,10,10,PicoGameBoy.color(255,255,255))
        pgb.fill_rect(140, 30,10,10,PicoGameBoy.color(255,255,255))
        pgb.rect(90,60,60,20,PicoGameBoy.color(255,255,255))
        pgb.line(90,79,150,79,PicoGameBoy.color(0,0,0))
        pgb.create_text("Game Over",-1,125,PicoGameBoy.color(255,255,255))
        pgb.create_text("Press A to play again.", -1, 145, PicoGameBoy.color(255,255,255))
        pgb.create_text("Press home to quit.", -1, 160, PicoGameBoy.color(255,255,255))
        pgb.create_text("Level: "+str(level), -1, 180, PicoGameBoy.color(255,255,255))
        pgb.show()
        while True:
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.rect(70,20,100,80,PicoGameBoy.color(255,255,255))
            pgb.fill_rect(90, 30,10,10,PicoGameBoy.color(255,255,255))
            pgb.fill_rect(140, 30,10,10,PicoGameBoy.color(255,255,255))
            pgb.rect(90,60,60,20,PicoGameBoy.color(255,255,255))
            pgb.line(90,79,150,79,PicoGameBoy.color(0,0,0))
            pgb.create_text("Game Over",-1,125,PicoGameBoy.color(255,255,255))
            pgb.create_text("Press A to play again.", -1, 145, PicoGameBoy.color(255,255,255))
            pgb.create_text("Press home to quit.", -1, 160, PicoGameBoy.color(255,255,255))
            pgb.create_text("Press start", -1, 175, PicoGameBoy.color(255,255,255))
            pgb.create_text("to view scores.", -1, 190, PicoGameBoy.color(255,255,255))
            pgb.create_text("Level: "+str(level), -1, 205, PicoGameBoy.color(255,255,255))
            pgb.show()
            if pgb.button_Home():
                homebootstop=open("/noboot", "w")
                homebootstop.close()
                pgb.fill(PicoGameBoy.color(0,0,0))
                pgb.show()
                machine.reset()
                break
            if pgb.button_start():
                    x=open("Starship/highscoresStarship.sc", "r")
                    scores=x.read()
                    x.close()
                    del x
                    scores=scores.split("\n")
                    pgb.fill(PicoGameBoy.color(0,0,0))
                    pgb.create_text("High Scores:", -1, 15, PicoGameBoy.color(255,255,255))
                    for i in range(len(scores)):
                        pgb.create_text("Score "+str(i+1)+": Level "+str(scores[i]), -1, 50+i*15, PicoGameBoy.color(255,255,255))
                    pgb.create_text("Press B to exit", -1, 220, PicoGameBoy.color(255,255,255))
                    while True:
                        if pgb.button_B():
                            break
                        if pgb.button_Home():
                            homebootstop=open("/noboot", "w")
                            homebootstop.close()
                            pgb.fill(PicoGameBoy.color(0,0,0))
                            pgb.show()
                            machine.reset()
                            break
                        pgb.show()
            elif pgb.button_A():
                level=0
                no_music()
                break
