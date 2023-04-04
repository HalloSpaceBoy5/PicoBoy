from PicoGameBoy import PicoGameBoy
import time
import math
pgb=PicoGameBoy()
movx=200
movy=200
rectx=100
recty=100
pgb.add_rect_sprite(PicoGameBoy.color(255,0,0),10,10)

def check_collision(speed,detectionradius, posx,posy,width,height, posx2,posy2,width2,height2):
    global movx
    global movy
    cenpoint1=[posx+width/2,posy+height/2]
    cenpoint2=[posx2+width2/2,posy2+height2/2]
    dist=sqrt((cenpoint1[0]-cenpoint2[0])**2+(cenpoint1[1]-cenpoint2[1])**2)
    if not dist<detectionradius:
        playerpos=[[posx,posy],[posx+width,posy],[posx,posy+height],[posx+width,posy+height]]
        colliderpos=[[posx2,posy2],[posx2+width2, posy2],[posx2,posy2+height2],[posx2+width2,posy2+height2]]
        if (playerpos[0][0]>colliderpos[0][0] or playerpos[1][0]>colliderpos[0][0]) and (playerpos[0][0]<colliderpos[1][0] or playerpos[1][0]<colliderpos[1][0]) and posy<colliderpos[0][1] and posy>colliderpos[0][1]-(speed*2):
            movy=movy-5
        elif (playerpos[0][0]>colliderpos[0][0] or playerpos[1][0]>colliderpos[0][0]) and (playerpos[0][0]<colliderpos[1][0] or playerpos[1][0]<colliderpos[1][0]) and posy>colliderpos[0][1] and posy<colliderpos[0][1]+(speed*2):
            movy=movy+5
        elif (playerpos[1][1]>colliderpos[1][1] or playerpos[2][1]>colliderpos[1][1]) and (playerpos[1][1]<colliderpos[2][1] or playerpos[2][1]<colliderpos[2][1]) and posx>colliderpos[2][0] and posx<colliderpos[2][0]+(speed*2):
                movx=movx+5
        elif (playerpos[1][1]>colliderpos[1][1] or playerpos[2][1]>colliderpos[1][1]) and (playerpos[1][1]<colliderpos[2][1] or playerpos[2][1]<colliderpos[2][1]) and posx<colliderpos[2][0] and posx>colliderpos[2][0]-(speed*2):
                movx=movx-5


while True:
    pgb.fill(PicoGameBoy.color(0,0,0))
    pgb.fill_rect(rectx,recty,10,10,PicoGameBoy.color(255,255,255))
    if pgb.button_up():
        movy=movy-5
    if pgb.button_down():
        movy=movy+5
    if pgb.button_left():
        movx=movx-5
    if pgb.button_right():
        movx=movx+5
    check_collision(5,movx,movy,10,10,rectx,recty,10,10)
        
            
        
    pgb.sprite(0,movx,movy)
    pgb.show()
    time.sleep(0.05)