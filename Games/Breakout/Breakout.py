# Original game for PicoBoy by HalloSpaceBoy
from PicoGameBoy import PicoGameBoy
from time import sleep, ticks_diff, ticks_ms
from random import randint
from math import sqrt
import os

try:
    os.rename("/main.py", "/Breakout/Breakout.py")
    os.rename("/title.py", "/main.py")
except:
    ""

pgb=PicoGameBoy()
pgb.free_mem()

pgb.add_rect_sprite(PicoGameBoy.color(255,255,255), 30,10)
ball=bytearray(b'\x00\x00\x00\x00\xceY\xceY\xceY\xceY\xceY\xceY\x00\x00\x00\x00\x00\x00\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\x00\x00\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\x00\x00\xceY\xceY\xceY\xceY\xceY\xceY\xceY\xceY\x00\x00\x00\x00\x00\x00\xceY\xceY\xceY\xceY\xceY\xceY\x00\x00\x00\x00')
pgb.add_sprite(ball,10,10)
del ball
paddle=pgb.sprite(0,100,220)
playerx=100
ballx=0
bally=0
score=0
changedirection=False
ballpos=[]
pgb.show()

#vars
speed=10
offset=40
defspeed=5
ballspeedx=ballspeedy=-5
lives=3

def pause_screen():
    pgb.fill_rect(10,90,220,80,PicoGameBoy.color(50,50,50))
    pgb.center_text("Game Paused",PicoGameBoy.color(255,255,255))
    pgb.create_text("Press Start to resume", -1, 135, PicoGameBoy.color(255,255,255))
    pgb.show()
    sleep(0.5)
    while True:
        pgb.show()
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        elif pgb.button_start():
            sleep(0.5)
            return
        
def append_to_board(score):
    with open("/Breakout/highscoresBreakout.sc", "r") as s:
        scores=s.read().split("\n")
        for r in range(len(scores)):
            scores[r]=int(scores[r])
    newscores=scores
    newscores.append(int(score))
    newscores.sort(reverse=True)
    for i in range(len(newscores)): newscores[i]=str(newscores[i])
    with open("/Breakout/highscoresBreakout.sc", "w+") as w:
        w.write("\n".join(newscores[:10]))

def view_scores():
    x=open("/Breakout/highscoresBreakout.sc", "r")
    scores=x.read()
    x.close()
    del x
    scores=scores.split("\n")
    while True:
        if pgb.button_B():
            sleep(0.1)
            return
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.create_text("High Scores:", -1, 15, PicoGameBoy.color(255,255,255))
        for i in range(len(scores)):
            pgb.create_text("Score "+str(i+1)+": "+str(scores[i]), -1, 50+i*15, PicoGameBoy.color(255,255,255))
        pgb.create_text("Press B to exit", -1, 220, PicoGameBoy.color(255,255,255))
        pgb.show()

def title_screen():
    # title screen
    now = ticks_ms()
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        if pgb.button_start():
            view_scores()
        elif pgb.any_button():
            break
        pgb.load_image("/Breakout/breakout_title.bin")
        pgb.show()
        
        if ticks_diff(ticks_ms(), now) > 200:
            now = ticks_ms()
            pgb.create_text("HOLD A TO PLAY",-1,175,PicoGameBoy.color(255,255,255))
            pgb.show()
            while ticks_diff(ticks_ms(), now) < 200:
                sleep(0.020)
            now = ticks_ms()
        
    sleep(0.25)

def game_over_screen():
    global score
    global lives
    global playerx
    global defspeed
    global speed
    defspeed=5
    speed=10
    append_to_board(score)
    playerx=100
    lives=3
    pgb.sound(0)
    while True:
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.center_text("GAME OVER",PicoGameBoy.color(255,255,255))
        pgb.text("Press A to play again.", 35, 125, PicoGameBoy.color(255,255,255))
        pgb.text("Press home to quit.", 40, 140, PicoGameBoy.color(255,255,255))
        pgb.create_text("Press start", -1, 175, PicoGameBoy.color(255,255,255))
        pgb.create_text("to view scores.", -1, 190, PicoGameBoy.color(255,255,255))
        pgb.create_text("Score: "+str(score),-1,80,PicoGameBoy.color(255,255,255))
        pgb.show()
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        if pgb.button_start():
            view_scores()
        elif pgb.button_A():
            score=0
            sleep(0.5)
            break

def win_screen():
    global score
    global lives
    global playerx
    global row1
    global row2
    global row3
    global row4
    global row5
    global ballx
    global bally
    global defspeed
    global speed
    speed+=1
    defspeed+=.5
    ballx=200
    bally=200
    row1=[1,1,1,1,1,1,1,1,1]
    row2=[1,1,1,1,1,1,1,1,1]
    row3=[1,1,1,1,1,1,1,1,1]
    row4=[1,1,1,1,1,1,1,1,1]
    row5=[1,1,1,1,1,1,1,1,1]
    playerx=100
    pgb.sound(0)
    pgb.fill(PicoGameBoy.color(0,0,0))
    pgb.center_text("Level Clear!",PicoGameBoy.color(255,255,255))
    pgb.create_text("Press A to play",-1, 125, PicoGameBoy.color(255,255,255))
    pgb.create_text("the next level",-1, 140, PicoGameBoy.color(255,255,255))
    pgb.text("Press home to quit.", 40, 160, PicoGameBoy.color(255,255,255))
    pgb.create_text("Score: "+str(score),-1,80,PicoGameBoy.color(255,255,255))
    pgb.show()
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        elif pgb.button_A():
            sleep(0.5)
            return
        
def Check_Collision(x,y,width,height,x2,y2,width2,height2,speed,mode):
    if x < x2 + width2 and x + width > x2 and y < y2 + height and y + height > y2:
        x_adjust = min(x + width - x2, x2 + width2 - x)
        y_adjust = min(y + height - y2, y2 + height - y)
        if x_adjust < y_adjust:
            if x + speed+width > x2 and x+speed < x2:
                if mode==2:
                    x=0
                    y=0
                if mode==0 or mode==2:
                    x -= x_adjust
                elif mode==1:
                    return True
            else:
                if mode==2:
                    x=0
                    y=0
                if mode==0 or mode==2:
                    x += x_adjust
                elif mode==1:
                    return True
        else:
            if y + height+speed > y2 and y+speed < y2:
                if mode==2:
                    y=0
                    x=0
                if mode==0 or mode==2:
                    y -= y_adjust
                elif mode==1:
                    return True
            else:
                if mode==2:
                    x=0
                    y=0
                if mode==0 or mode==2:
                    y += y_adjust
                elif mode==1:
                    return True
    else:
        if mode==2:
            x=0
            y=0
    if mode==0:
        return x, y
    elif mode==1:
        return False
    elif mode==2:
        return x,y




def draw_boxes():
    global row1
    global row2
    global row3
    global row4
    global row5
    global ballx
    global bally
    global speed
    global changedirection
    global ballspeedy
    global ballspeedx
    global offset
    global score
    alreadybroken=False
    for i in range(5):
            if i==0:
                for f in range(9):
                    colornum1=255#randint(50,255)
                    colornum2=0#randint(50,255)
                    colornum3=0#randint(50,255)
                    blo=25*f+10
                    if not row1[f]==0 and not alreadybroken:
                        cx,cy=Check_Collision(blo,0+offset,20,10,ballx,bally,10,10,5,2)
                        if not cx==0 or not cy==0:
                            ballx+=cx
                            bally+=cy
                            row1[f]=0
                            score=score+100
                            alreadybroken=True
                            pgb.sound(123)
                            #changedirection=True
                            if not cx==0:
                                ballspeedx=-ballspeedx
                            if not cy==0:
                                ballspeedy=-ballspeedy

                            
                            
                    if row1[f]==0:
                        pgb.fill_rect(blo,0+offset,20,10, PicoGameBoy.color(0,0,0))
                    else:
                        pgb.fill_rect(blo,0+offset,20,10, PicoGameBoy.color(colornum1,colornum2,colornum3))
            if i==1:
                for f in range(9):
                    colornum1=0#randint(50,255)
                    colornum2=255#randint(50,255)
                    colornum3=0#randint(50,255)
                    blo=25*f+10
                    if not row2[f]==0 and not alreadybroken:
                        cx,cy=Check_Collision(blo,25+offset,20,10,ballx,bally,10,10,5,2)
                        if not cx==0 or not cy==0:
                            ballx+=cx
                            bally+=cy
                            row2[f]=0
                            score=score+50
                            alreadybroken=True
                            pgb.sound(123)
                            #changedirection=True
                            if not cy==0:
                                ballspeedy=-ballspeedy
                            elif not cx==0:
                                ballspeedx=-ballspeedx
                            
                    if row2[f]==0:
                        pgb.fill_rect(blo,25+offset,20,10, PicoGameBoy.color(0,0,0))
                    else:
                        pgb.fill_rect(blo,25+offset,20,10, PicoGameBoy.color(colornum1,colornum2,colornum3))
            if i==2:
                for f in range(9):
                    colornum1=0#randint(50,255)
                    colornum2=0#randint(50,255)
                    colornum3=255#randint(50,255)
                    blo=25*f+10
                    if not row3[f]==0 and not alreadybroken:
                        cx,cy=Check_Collision(blo,50+offset,20,10,ballx,bally,10,10,5,2)
                        if not cx==0 or not cy==0:
                            ballx+=cx
                            bally+=cy
                            row3[f]=0
                            score=score+25
                            alreadybroken=True
                            pgb.sound(123)
                            #changedirection=True
                            if not cy==0:
                                ballspeedy=-ballspeedy
                            elif not cx==0:
                                ballspeedx=-ballspeedx
                            
                    if row3[f]==0:
                        pgb.fill_rect(blo,50+offset,20,10, PicoGameBoy.color(0,0,0))
                    else:
                        pgb.fill_rect(blo,50+offset,20,10, PicoGameBoy.color(colornum1,colornum2,colornum3))
            if i==3:
                for f in range(9):
                    colornum1=0#randint(50,255)
                    colornum2=255#randint(50,255)
                    colornum3=0#randint(50,255)
                    blo=25*f+10
                    if not row4[f]==0 and not alreadybroken:
                        cx,cy=Check_Collision(blo,75+offset,20,10,ballx,bally,10,10,5,2)
                        if not cx==0 or not cy==0:
                            ballx+=cx
                            bally+=cy
                            row4[f]=0
                            score=score+10
                            alreadybroken=True
                            pgb.sound(123)
                            #changedirection=True
                            if not cy==0:
                                ballspeedy=-ballspeedy
                            elif not cx==0:
                                ballspeedx=-ballspeedx
                            
                    if row4[f]==0:
                        pgb.fill_rect(blo,75+offset,20,10, PicoGameBoy.color(0,0,0))
                    else:
                        pgb.fill_rect(blo,75+offset,20,10, PicoGameBoy.color(colornum1,colornum2,colornum3))
            if i==4:
                for f in range(9):
                    colornum1=255#randint(50,255)
                    colornum2=0#randint(50,255)
                    colornum3=0#randint(50,255)
                    blo=25*f+10
                    if not row5[f]==0 and not alreadybroken:
                        cx,cy=Check_Collision(blo,100+offset,20,10,ballx,bally,10,10,5,2)
                        if not cx==0 or not cy==0:
                            ballx+=cx
                            bally+=cy
                            row5[f]=0
                            score=score+5
                            alreadybroken=True
                            pgb.sound(123)
                            #changedirection=True
                            if not cy==0:
                                ballspeedy=-ballspeedy
                            elif not cx==0:
                                ballspeedx=-ballspeedx
                            
                    if row5[f]==0:
                        pgb.fill_rect(blo,100+offset,20,10, PicoGameBoy.color(0,0,0))
                    else:
                        pgb.fill_rect(blo,100+offset,20,10, PicoGameBoy.color(colornum1,colornum2,colornum3))



def main_game():
    global row1
    global row2
    global row3
    global row4
    global row5
    global playerx
    global playery
    global ballx
    global bally
    global ballspeedy
    global ballspeedx
    global changedirection
    global lives
    global score
    global defspeed
    ballspeedx=ballspeedy=-abs(int(defspeed))
    row1=[1,1,1,1,1,1,1,1,1]
    row2=[1,1,1,1,1,1,1,1,1]
    row3=[1,1,1,1,1,1,1,1,1]
    row4=[1,1,1,1,1,1,1,1,1]
    row5=[1,1,1,1,1,1,1,1,1]
    stationary=True
    while True:
        
        going=True
        
        while going:
            if pgb.button_Home():
                homebootstop=open("/noboot", "w")
                homebootstop.close()
                pgb.fill(PicoGameBoy.color(0,0,0))
                pgb.show()
                machine.reset()
                break
            if pgb.button_start():
                pause_screen()
            pgb.fill(PicoGameBoy.color(0,0,0))
            #player movement
            if pgb.button_left() and playerx>15:
                playerx=playerx-speed
            if pgb.button_right() and playerx<210:
                playerx=playerx+speed
                
            #ball physics
            if stationary:
                draw_boxes()
                pgb.sprite(1,playerx+10,210)
                ballx=playerx+10
                bally=210
                if pgb.button_A():
                    stationary=False
                    bally=bally-5
            
            else:
                ballcoords=[[ballx,bally],[ballx,bally+10],[ballx+10,bally],[ballx+10,bally+10]]
                if ballcoords[2][0]<20:
                    ballx+=5
                    ballspeedx=-ballspeedx
                    pgb.sound(349)
                if ballcoords[2][0]>230:
                    ballx-=5
                    ballspeedx=-ballspeedx
                    pgb.sound(349)
                if ballcoords[0][1]<20:
                    ballspeedy=-ballspeedy
                    pgb.sound(349)
                if ballcoords[3][1]>240:
                    lives=lives-1
                    stationary=True
                    ballspeedx=ballspeedy=-abs(int(defspeed))
                    going=False
                    pgb.sound(349)
                    sleep(0.05)
                    pgb.sound(0)
                    sleep(0.1)
                    pgb.sound(349)
                    sleep(0.05)
                    pgb.sound(0)
                bally=bally+ballspeedy
                ballx=ballx+ballspeedx
                cx,cy=Check_Collision(ballx,bally,10,10,playerx,220,30,10,5,2)
                if not cx==0 or not cy==0:
                    bally+=cy
                    if ballx>playerx and ballx<playerx+6:
                        ballspeedx=-(int(defspeed)-3)
                    elif ballx>playerx+6 and ballx<playerx+12:
                        ballspeedx=-(int(defspeed)-2)
                    elif ballx>playerx+12 and ballx<playerx+18:
                        if ballspeedx<0:
                            ballspeedx=-int(defspeed)
                        else:
                            ballspeedx=int(defspeed)
                    elif ballx>playerx+18 and ballx<playerx+24:
                        ballspeedx=int(defspeed)-2
                    elif ballx>playerx+24 and ballx<playerx+30:
                        ballspeedx=int(defspeed)-3
                    if not cy==0:
                        ballspeedy=-ballspeedy
                    else:
                        ballspeedy=-abs(ballspeedy)
                    if cx==0:
                        bally=bally-5
                    pgb.sound(349)
                draw_boxes()
                pgb.sprite(1,ballx,bally)
                if lives<1:
                    return False
            if row1==[0,0,0,0,0,0,0,0,0] and row2==[0,0,0,0,0,0,0,0,0] and row3==[0,0,0,0,0,0,0,0,0] and row4==[0,0,0,0,0,0,0,0,0] and row5==[0,0,0,0,0,0,0,0,0]:
                return True
            #display drawing
            pgb.create_text("Score: "+str(score)+"       Lives: "+str(lives),-1,20)
            pgb.sprite(0,playerx,220)
            pgb.show()
            pgb.sound(0)
            sleep(0.015)


title_screen()
while True:
    if main_game():
        win_screen()
    else:
        game_over_screen()
