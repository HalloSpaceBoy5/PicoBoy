from PicoGameBoy import PicoGameBoy
import math
import random
from time import sleep
from random import randint, choice
from os import rename
import machine
import _thread
rename("./main.py", "./pacman.py")
rename("./title.py", "./main.py")
machine.freq(250000000)
pgb=PicoGameBoy()

pellet=bytearray(b'\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00')
pgb.add_sprite(pellet, 5,5)
del pellet
l_pellet=bytearray(b'\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00')
pgb.add_sprite(l_pellet, 9, 9)
del l_pellet
pinky=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xecz\xecz\xecz\xecz\xecz\xecz\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\x00\x00\x00\x00\x00\x00\xecz\xecz\xecz\xff\xff\xff\xff\xecz\xecz\xecz\xecz\xff\xff\xff\xff\xecz\xecz\xecz\x00\x00\x00\x00\xecz\xecz\xff\xff\x08>\x08>\xff\xff\xecz\xecz\xff\xff\x08>\x08>\xff\xff\xecz\xecz\x00\x00\xecz\xecz\xecz\xff\xff\x08>\x08>\xff\xff\xecz\xecz\xff\xff\x08>\x08>\xff\xff\xecz\xecz\xecz\xecz\xecz\xecz\xff\xff\x08>\x08>\xff\xff\xecz\xecz\xff\xff\x08>\x08>\xff\xff\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xff\xff\xff\xff\xecz\xecz\xecz\xecz\xff\xff\xff\xff\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\xecz\x00\x00\xecz\xecz\xecz\xecz\xecz\xecz\x00\x00\xecz\xecz\xecz\xecz\xecz\xecz\xecz\x00\x00\x00\x00\x00\x00\xecz\xecz\xecz\xecz\x00\x00\x00\x00\x00\x00\xecz\xecz\xecz\x00\x00\xecz\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xecz\xecz\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xecz\x00\x00')
pgb.add_sprite(pinky,16,16)
del pinky
inky=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x00\x00\x00\x00\x00\x00\x02\x1f\x02\x1f\x02\x1f\xff\xff\xff\xff\x02\x1f\x02\x1f\x02\x1f\x02\x1f\xff\xff\xff\xff\x02\x1f\x02\x1f\x02\x1f\x00\x00\x00\x00\x02\x1f\x02\x1f\xff\xff\x08>\x08>\xff\xff\x02\x1f\x02\x1f\xff\xff\x08>\x08>\xff\xff\x02\x1f\x02\x1f\x00\x00\x02\x1f\x02\x1f\x02\x1f\xff\xff\x08>\x08>\xff\xff\x02\x1f\x02\x1f\xff\xff\x08>\x08>\xff\xff\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\xff\xff\x08>\x08>\xff\xff\x02\x1f\x02\x1f\xff\xff\x08>\x08>\xff\xff\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\xff\xff\xff\xff\x02\x1f\x02\x1f\x02\x1f\x02\x1f\xff\xff\xff\xff\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x00\x00\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x00\x00\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x00\x00\x00\x00\x00\x00\x02\x1f\x02\x1f\x02\x1f\x02\x1f\x00\x00\x00\x00\x00\x00\x02\x1f\x02\x1f\x02\x1f\x00\x00\x02\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x1f\x02\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x1f\x00\x00')
pgb.add_sprite(inky,16,16)
del inky
blinky=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\xff\xff\xff\xff\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xff\xff\xff\xff\xf8\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xff\xff\x08>\x08>\xff\xff\xf8\x00\xf8\x00\xff\xff\x08>\x08>\xff\xff\xf8\x00\xf8\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\xff\xff\x08>\x08>\xff\xff\xf8\x00\xf8\x00\xff\xff\x08>\x08>\xff\xff\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xff\xff\x08>\x08>\xff\xff\xf8\x00\xf8\x00\xff\xff\x08>\x08>\xff\xff\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xff\xff\xff\xff\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xff\xff\xff\xff\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\xf8\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00')
pgb.add_sprite(blinky,16,16)
del blinky
clyde=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc \xfc \xfc \xfc \xfc \xfc \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \x00\x00\x00\x00\x00\x00\xfc \xfc \xfc \xff\xff\xff\xff\xfc \xfc \xfc \xfc \xff\xff\xff\xff\xfc \xfc \xfc \x00\x00\x00\x00\xfc \xfc \xff\xff\x08>\x08>\xff\xff\xfc \xfc \xff\xff\x08>\x08>\xff\xff\xfc \xfc \x00\x00\xfc \xfc \xfc \xff\xff\x08>\x08>\xff\xff\xfc \xfc \xff\xff\x08>\x08>\xff\xff\xfc \xfc \xfc \xfc \xfc \xfc \xff\xff\x08>\x08>\xff\xff\xfc \xfc \xff\xff\x08>\x08>\xff\xff\xfc \xfc \xfc \xfc \xfc \xfc \xfc \xff\xff\xff\xff\xfc \xfc \xfc \xfc \xff\xff\xff\xff\xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \xfc \x00\x00\xfc \xfc \xfc \xfc \xfc \xfc \x00\x00\xfc \xfc \xfc \xfc \xfc \xfc \xfc \x00\x00\x00\x00\x00\x00\xfc \xfc \xfc \xfc \x00\x00\x00\x00\x00\x00\xfc \xfc \xfc \x00\x00\xfc \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc \xfc \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc \x00\x00')
pgb.add_sprite(clyde,16,16)
del clyde
nogocoords=((0,214,240,240), (0,0,240,6), (0,0,6,240), (234,0,240,240), (23,23,70,38), (87,23,154,38), (105,7,136,22), (171,23,218,38), (7,55,46,70), (63,55,112,70), (97,71,112,102), (111,87,130,102), (129,71,144,102), (129,55,178,70), (195,55,234,70), (23,87,80,102), (49,103,64,134), (161,87,218,102), (177,103,192,134), (209,119,234,134), (23,151,64,166), (23,167,38,182), (177,151,218,166), (203,167,218,182), (54,183,112,198), (129,183, 186,198), (23,199,38,22), (203,199,218,214), (23,199,38,214), (7,119,32,134), (81,119,112,134), (81,135,96,150), (81,151,160,166), (145,135,160,150), (129,119,160,134))
dotlocations=((30,14,1), (46,14,1), (62,14,1), (78,14,1), (94,14,2,True), (147,14,2,True), (163,14,2), (179,14,3), (195,14,3), (211,14,3), (227,14,3), (14,30,1), (78,30,1), (163,30,2), (227,30,3), (14,46,1), (30,46,1), (46,46,1), (62,46,1), (78,46,1), (94,46,2), (112,46,2), (130,46,2), (147,46,2), (163,46,2), (179,46,3), (195,46,3), (211,46,3), (227,46,3), (54, 61, 1), (120, 61, 2), (186, 61, 3), (13,77,1), (29,77,1), (45,77,1), (61,77,1), (75,77,1), (89,77,1), (152,77,2), (167,77,3), (182,77,3), (197,77,3), (212,77,3), (227,77,3), (120,77,2), (13,93,4), (89,93,5), (152,93,5), (228,93,6), (13,109,4), (27,109,4), (40,109,4), (201,109,6), (214,109,6), (228,109,6), (73,109,4), (89,109,5), (105,109,5), (120,109,5,True), (137,109,5), (153,109,5), (168,109,6), (41,125,4), (73,125,4), (168,125,5), (201,125,6), (14,141,4), (28,141,4), (42,141,4), (57,141,4), (73,141,4), (168,141,6), (182,141,6), (196,141,6), (211,141,6), (226,141,6), (14,157,4), (73,157,4), (168,157,6), (226,157,6), (14,173,7), (45,173,7), (59,173,7), (73,173,7), (89,173,8), (104,173,8), (120,173,8), (136,173,8), (153,173,8), (168,173,9), (181,173,9), (194,173,9), (226,173,9), (14,189,7), (30,189,7), (45,189,7), (121,189,8), (194,189,9), (210,189,9), (225,189,9), (14,205,7,True), (45,205,7), (59,205,7), (73,205,7), (89,205,8), (104,205,8), (120,205,8), (136,205,8), (153,205,8), (168,205,9), (181,205,9), (194,205,9), (226,205,9,True))
m_spaces=((6,6),(22,6),(38,6),(54,6),(70,6),(86,6),(138,6),(154,6),(170,6),(186,6),(202,6),(218,6),(6,22),(70,22),(154,22),(218,22),(6,38),(22,38),(38,38),(54,38),(70,38),(86,38),(102,38),(118,38),(134,38),(150,38),(166,38),(182,38),(198,38),(214,38))
currentdots=[]
for i in range(len(dotlocations)):
    currentdots.append(True)
currentdots=tuple(currentdots)
def draw_pacman(x, y, d, m):
    pgb.hline(x-8,y,8*2,PicoGameBoy.color(255,255,0))
    for i in range(1,8):
        a = int(math.sqrt(8*8-i*i))
        pgb.hline(x-a,y+i,a*2,PicoGameBoy.color(255,255,0))
        pgb.hline(x-a,y-i,a*2,PicoGameBoy.color(255,255,0))
        if d==3:
            for i in range(m):
                pgb.line(x, y, x+8, y+(i+1), PicoGameBoy.color(0,0,0))
            for i in range(m):
                pgb.line(x, y, x+8, y-(i+1), PicoGameBoy.color(0,0,0))
            pgb.hline(x, y, 8, PicoGameBoy.color(0,0,0))
        elif d==2:
            for i in range(m):
                pgb.line(x, y, x-8, y+(i+1), PicoGameBoy.color(0,0,0))
            for i in range(m):
                pgb.line(x, y, x-8, y-(i+1), PicoGameBoy.color(0,0,0))
            pgb.hline(x-8, y, 8, PicoGameBoy.color(0,0,0))
        elif d==1:
            for i in range(m):
                pgb.line(x, y, x-(i+1), y+8, PicoGameBoy.color(0,0,0))
            for i in range(m):
                pgb.line(x, y, x+(i+1), y+8, PicoGameBoy.color(0,0,0))
            pgb.vline(x, y, 8, PicoGameBoy.color(0,0,0))
        elif d==0:
            for i in range(m):
                pgb.line(x, y, x-(i+1), y-8, PicoGameBoy.color(0,0,0))
            for i in range(m):
                pgb.line(x, y, x+(i+1), y-8, PicoGameBoy.color(0,0,0))
            pgb.vline(x, y-8, 8, PicoGameBoy.color(0,0,0))
        else:
            if d==3:
                pgb.hline(x, y, 8, PicoGameBoy.color(0,0,0))
            elif d==2:
                pgb.hline(x-8, y, 8, PicoGameBoy.color(0,0,0))
            elif d==1:
                pgb.vline(x, y, 8, PicoGameBoy.color(0,0,0))
            elif d==0:
                pgb.vline(x, y-8, 8, PicoGameBoy.color(0,0,0))
                
def bounding_box_collision(x, y, width=16, height=16, boxes=nogocoords):
    player_box = (x, y, width, height)
    for box in boxes:
        box_x, box_y, box_x2, box_y2 = box
        box_width = box_x2 - box_x
        box_height = box_y2 - box_y
        box_box = (box_x, box_y, box_width, box_height)
        if x < box_x + box_width and x + width > box_x and y < box_y + box_height and y + height > box_y:
            x_adjust = min(x + width - box_x, box_x + box_width - x)
            y_adjust = min(y + height - box_y, box_y + box_height - y)
            if x_adjust < y_adjust:
                if x + width > box_x and x < box_x:
                    x -= x_adjust
                else:
                    x += x_adjust
            else:
                if y + height > box_y and y < box_y:
                    y -= y_adjust
                else:
                    y += y_adjust
    return x, y

def draw_spaces():
    global m_spaces
    for space in m_spaces:
        pgb.fill_rect(space[0], space[1], 16, 16, PicoGameBoy.color(randint(0,255),randint(0,255),randint(0,255)))

def draw_dots(playerx, playery, dots=dotlocations):
    global currentdots
    global grid
    global score
    mod=list(currentdots)
    ind=[]
    for i in range(len(grid)):
        if grid[i]:
            ind.append(int(i)+1)
    cenpoint1=(playerx+16/2,playery+16/2)
    p=0
    for pos, dot in enumerate(dots):
        try:
            x=dot[3]
            del x
            big=True
        except:
            big=False
        x=dot[0]
        y=dot[1]
        if not big:
            
            if mod[pos] and dot[2] in ind:
                cenpoint2=(x+2/2,y+2/2)
                dist=math.sqrt((cenpoint1[0]-cenpoint2[0])**2+(cenpoint1[1]-cenpoint2[1])**2)
                p+=1
                if dist<5:#abs(cenpoint1[0]-cenpoint2[0]) < 4 and abs(cenpoint1[1]-cenpoint2[1])<4:
                    mod[pos]=False
                    score+=10
            if mod[pos]:
                pgb.sprite(0, x-2, y-2)
        else:
            global playerstate
            if mod[pos] and dot[2] in ind:
                cenpoint2=(x+4/2,y+4/2)
                dist=math.sqrt((cenpoint1[0]-cenpoint2[0])**2+(cenpoint1[1]-cenpoint2[1])**2)
                if dist<9:#abs(cenpoint1[0]-cenpoint2[0]) < 8 and abs(cenpoint1[1]-cenpoint2[1])<8:
                    mod[pos]=False
                    score+=500
                    playerstate=True
            if mod[pos]:
                pgb.sprite(1, x-4, y-4)
    currentdots=tuple(mod)
    del mod
    
class ghost:
    def __init__(self, x, y, c, speed, ai):
        self.x=x
        self.y=y
        self.speed=speed
        self.c=c+2
        self.ai=ai
        self.state=True #false=dead, true=alive
        self.renew=True
        self.direction=0
        self.current_direction=""
        self.streak_counter=0
        self.streak_length=0
        self.lastmove=0 #0=up, 1=down, 2=left, 3=right
    
    def update(self):
        global playerx
        global playery
        global playerstate
        if self.renew:
            self.y-=self.speed
        else:
            if self.ai=="smart":
                if self.x < playerx:
                    self.x += self.speed
                elif self.x > playerx:
                    self.x -= self.speed
                if self.y < playery:
                    self.y += self.speed
                elif self.y > playery:
                    self.y -= self.speed
            if self.ai=="dumb":
                if 'current_direction' not in self.__dict__:
                    self.current_direction = random.choice(['left', 'right', 'up', 'down'])
                    self.streak_counter = 5

                if self.streak_counter > 0:
                    self.streak_counter -= 1
                else:
                    self.current_direction = random.choice(['left', 'right', 'up', 'down'])
                    self.streak_counter = 5

                if self.current_direction == 'left':
                    self.x -= self.speed
                elif self.current_direction == 'right':
                    self.x += self.speed
                elif self.current_direction == 'up':
                    self.y -= self.speed
                elif self.current_direction == 'down':
                    self.y += self.speed
            oback=bounding_box_collision(self.x,self.y,boxes=((113,119,128,134),(0,0,0,0)))
            self.x=oback[0]
            self.y=oback[1]
            del oback
        back=bounding_box_collision(self.x,self.y)
        if back[0]<playerx:
            self.lastcoll=3
        if back[0]>playerx:
            self.lastcoll=2
        if back[1]<playery:
            self.lastcoll=1
        if back[1]>playery:
            self.lastcoll=0
        if self.renew and not back[1]==self.y:
            self.renew=False
        self.x=back[0]
        self.y=back[1]
        del back
        pgb.sprite(self.c,self.x,self.y)
        

#NOTE: The max score per level is 3580
grid=(True,False,False,False,False,False,False,False,False)
m=4
d=True
direction=0
playerx=7
playery=7
playerspeed=4
score=0
playerstate=False #false=killable true=able to kill
dt=0 #playerstate timer
blinky=ghost(113,134,2,3,"dumb")
while True:
    if pgb.button_Home():
        x=open("/noboot", "w")
        x.close()
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()
        break
    if playerstate:
        playerspeed=6
        dt+=1
        if dt%50==0:
            playerstate=False
            dt=0
            playerspeed=4
    pgb.load_image("/pacmanbg.bin")
    pgb.create_text("Score: "+str(score), -1, 223, PicoGameBoy.color(255,255,255))
    if pgb.button_up() or pgb.button_down() or pgb.button_left() or pgb.button_right():
        if d:
            if m<=0:
                d=not d
                pgb.sound(200)
            else:
                m-=4
        else:
            if m>=4:
                d=not d
                pgb.sound(100)
            else:
                m+=4
        grid=list(grid)
        if (playerx <=90 and playerx >=0) and (playery<=90 and playery>=0):
            grid[0]=True
        else:
            grid[0]=False
        if (playerx <=170 and playerx >=70) and (playery<=90 and playery>=0):
            grid[1]=True
        else:
            grid[1]=False
        if (playerx <=240 and playerx >=150) and (playery<=90 and playery>=0):
            grid[2]=True
        else:
            grid[2]=False
        if (playerx <=90 and playerx >=0) and (playery<=170 and playery>=70):
            grid[3]=True
        else:
            grid[3]=False
        if (playerx <=170 and playerx >=70) and (playery<=170 and playery>=70):
            grid[4]=True
        else:
            grid[4]=False
        if (playerx <=240 and playerx >=150) and (playery<=170 and playery>=70):
            grid[5]=True
        else:
            grid[5]=False
        if (playerx <=90 and playerx >=0) and (playery<=240 and playery>=150):
            grid[6]=True
        else:
            grid[6]=False
        if (playerx <=170 and playerx >=70) and (playery<=240 and playery>=150):
            grid[7]=True
        else:
            grid[7]=False
        if (playerx <=240 and playerx >=150) and (playery<=240 and playery>=150):
            grid[8]=True
        else:
            grid[8]=False
        grid=tuple(grid)
    else:
        m=0
        pgb.sound(0)
        
    if pgb.button_up():
        direction=0
        playery-=playerspeed
    elif pgb.button_down():
        direction=1
        playery+=playerspeed
    elif pgb.button_left():
        direction=2
        playerx-=playerspeed
    elif pgb.button_right():
        direction=3
        playerx+=playerspeed
    f=bounding_box_collision(playerx,playery, boxes=((113,119,128,134),(0,0,0,0)))
    playerx=f[0]
    playery=f[1]
    del f
    c=bounding_box_collision(playerx,playery)
    playerx=c[0]
    playery=c[1]
    del c
    draw_dots(playerx, playery)
    blinky.update()
    draw_pacman(playerx+7,playery+7,direction, m)
    #draw_spaces()
    pgb.show()
    sleep(0.025)