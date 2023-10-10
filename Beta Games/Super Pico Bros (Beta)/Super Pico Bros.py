from PicoGameBoy import PicoGameBoy
from time import sleep
from random import randint
from math import sqrt
from os import rename
rename("/main.py", "/Super Pico Bros/Super Pico Bros.py")
rename("/title.py", "/main.py")
pgb=PicoGameBoy()

def bounding_box_collision(x, y, width, height,box_x,box_y,box_width,box_height,direction):
    player_box = (x, y, width, height)
    nx=0
    ny=0
    if x < box_x + box_width and x + width > box_x and y < box_y + box_height and y + height > box_y:
        x_adjust = min(x + width - box_x, box_x + box_width - x)
        y_adjust = min(y + height - box_y, box_y + box_height - y)
        if x_adjust < y_adjust and (direction=="left" or direction=="right"):
            if x + width > box_x and x < box_x and direction=="left":
                    nx -= x_adjust
            elif direction=="right":
                    nx += x_adjust
        else:
            if y + height > box_y and y < box_y and direction=="up":
                    ny -= y_adjust
            elif direction=="down":
                    ny += y_adjust
    return nx, ny
def loadlevel(filename):
    with open(filename, "r") as r:
        todraw=r.read().split("\n")
        for x,i in enumerate(todraw):
            o=[]
            for g in range(len(i)):
                o.append(0)
            for z,f in enumerate(i):
                if f==" ":
                    o[z]=0
                if f=="G":
                    o[z]=1
                if f=="B":
                    o[z]=2
                if f=="S":
                    o[z]=3
                if f=="M":
                    o[z]=4
            todraw[x]=tuple(o)
    return tuple(todraw)

def drawmap(frame, scene):
    for line in range(15):
        for pos in range(15+int(scene/16)):
            if frame[line][pos]==1 and pos*16-scene > -15 and pos*16-scene<300:
                pgb.fill_rect(pos*16-scene,line*16,16,16,PicoGameBoy.color(0,255,0))
            if frame[line][pos]==2 and pos*16-scene > -15 and pos*16-scene<300:
                pgb.fill_rect(pos*16-scene,line*16,16,16,PicoGameBoy.color(255,255,255))
            if frame[line][pos]==3 and pos*16-scene > -15 and pos*16-scene<300:
                pgb.fill_rect(pos*16-scene,line*16,16,16,PicoGameBoy.color(255,255,0))
            if frame[line][pos]==4 and pos*16-scene > -15 and pos*16-scene<300:
                pgb.fill_rect(pos*16-scene,line*16,16,16,PicoGameBoy.color(255,0,0))

lev=loadlevel("/Super Pico Bros/demolevel.lv")
playerx=0
playery=0
velocity=0
x_velocity=0
x_maxvelocity=4
maxvelocity=12
powerupstate=1
grounded=False
jumped=False
window=0
playerspeed=6
a_frames=0
a_held=False
jumping=False
cancel_vel=False
stop_a=False
while True:
    if pgb.button_Home():
        homebootstop=open("/noboot", "w")
        homebootstop.close()
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()
        break
    pgb.fill(PicoGameBoy.color(50,50,50))
    drawmap(lev, window)
    if pgb.button_A() and grounded:
        velocity=-24
        jumping=True
        jumped=True
        grounded=False
    if pgb.button_A() and not jumped:
        a_held=True
    else:
        a_held=False
    if pgb.button_B():
        if x_velocity<x_maxvelocity:
            x_velocity+=2
    else:
        if x_velocity>0:
            x_velocity-=2
    if pgb.button_left():
        if window<=0:
            window=0
            if playerx>0:
                playerx-=playerspeed+x_velocity
            if playerx<=0:
                playerx=0
        else:
            playerx-=playerspeed+x_velocity
            if playerx<112:
                window-=playerspeed+x_velocity
                playerx=112
    if pgb.button_right():
        playerx+=playerspeed+x_velocity
    if playerx>128 and window<(len(lev[0])-16)*16:
        playerx=128
        window+=playerspeed+x_velocity
    if window>(len(lev[0])-16)*16:
        window=(len(lev[0])-16)*16
    if powerupstate==0:
        h_c=16
    else:
        h_c=32
    if velocity<0 and not jumped:
        for boxy in range(15):
            for boxx in range(15+int(window/16)):
                if not lev[boxy][boxx] == 0 and boxx*16-window > playerx-48 and boxx*16-window<playerx+64:
                    col_check=bounding_box_collision(playerx,playery,16,h_c,boxx*16-window,boxy*16,16,16,"down")
                    if not col_check[1] ==0 or col_check[1]==1 or col_check[1]==-1:
                        playery=playery+(boxy*16+16)-playery
                        velocity=0
                        jumped=True
                        cancel_vel=True
                        break
    pgb.fill_rect(playerx,playery,16,h_c,PicoGameBoy.color(150,150,150))
    if grounded==False:
        if not jumped and velocity>0:
            for boxy in range(15):
                for boxx in range(15+int(window/16)):
                    if not lev[boxy][boxx] == 0 and boxx*16-window > playerx-48 and boxx*16-window<playerx+64:
                        col_check=bounding_box_collision(playerx,playery+velocity,16,h_c+velocity,boxx*16-window,boxy*16,16,16,"up")
                        if not col_check[1] ==0 or col_check[1]==1 or col_check[1]==-1:
                            playery=playery-(playery+h_c-boxy*16)
                            grounded=True
                            jumping=False
                            velocity=0
                            break
        if not grounded:
            if not cancel_vel:
                if velocity<maxvelocity:
                    if jumping and a_held:
                        velocity+=2
                    else:
                        velocity+=4
                playery+=velocity
            else:
                cancel_vel=False
        if jumped:
            jumped=False
    if grounded and not jumped and velocity>=0:
        offset=[0,0]
        for boxy in range(15):
            for boxx in range(15+int(window/16)):
                if not lev[boxy][boxx] == 0 and boxx*16-window > playerx-48 and boxx*16-window<playerx+64:
                    if jumping:
                        col_check=bounding_box_collision(playerx,playery+4,16,h_c,boxx*16-window,boxy*16,16,16,"up")
                    else:
                        col_check=bounding_box_collision(playerx,playery+4,16,h_c,boxx*16-window,boxy*16,16,16,"up")
                    offset[0]+=col_check[0]
                    offset[1]+=col_check[1]
        if offset[1] == 0:
            grounded=False
    if playery>260:
        playery=0
        playerx=0
        window=0
    pgb.show()
    #sleep(0.025)