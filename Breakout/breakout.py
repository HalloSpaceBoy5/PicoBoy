# Original game for PicoBoy by HalloSpaceBoy
from PicoGameBoy import PicoGameBoy
from time import sleep, ticks_diff, ticks_ms
from random import randint
from math import sqrt
import os

os.rename("./main.py", "./breakout.py")
os.rename("./title.py", "./main.py")

pgb=PicoGameBoy()
pgb.free_mem()

pgb.add_rect_sprite(PicoGameBoy.color(255,255,255), 30,10)
pgb.add_rect_sprite(PicoGameBoy.color(200,200,200),10,10)
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
ballspeedx=ballspeedy=-5
lives=3

def pause_screen():
    pgb.fill_rect(10,90,220,80,PicoGameBoy.color(50,50,50))
    pgb.center_text("Game Paused",PicoGameBoy.color(255,255,255))
    pgb.create_text("Press Start or Select", -1, 135, PicoGameBoy.color(255,255,255))
    pgb.create_text("to resume.", -1, 147, PicoGameBoy.color(255,255,255))
    pgb.show()
    sleep(0.5)
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        elif pgb.button_select() or pgb.button_start():
            sleep(0.5)
            return
        
def append_to_board(score):
    with open("highscoresbreakout.sc", "r") as s:
        scores=s.read().split("\n")
        for r in range(len(scores)):
            scores[r]=int(scores[r])
    newscores=scores
    newscores.append(int(score))
    newscores.sort(reverse=True)
    for i in range(len(newscores)): newscores[i]=str(newscores[i])
    with open("highscoresbreakout.sc", "w+") as w:
        w.write("\n".join(newscores[:10]))

def view_scores():
    x=open("highscoresbreakout.sc", "r")
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
        if pgb.button_select() or pgb.button_start():
            view_scores()
        elif pgb.any_button():
            break
        pgb.load_image("breakout_title.bin")
        pgb.show()
        
        if ticks_diff(ticks_ms(), now) > 200:
            now = ticks_ms()
            pgb.create_text("PRESS ANY BUTTON",-1,175,PicoGameBoy.color(255,255,255))
            pgb.show()
            while ticks_diff(ticks_ms(), now) < 200:
                sleep(0.020)
            now = ticks_ms()
        
    sleep(0.25)

def game_over_screen():
    global score
    global lives
    global playerx
    append_to_board(score)
    playerx=100
    lives=3
    pgb.sound(0)
    while True:
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.center_text("GAME OVER",PicoGameBoy.color(255,255,255))
        pgb.text("Press A to play again.", 35, 125, PicoGameBoy.color(255,255,255))
        pgb.text("Press home to quit.", 40, 140, PicoGameBoy.color(255,255,255))
        pgb.create_text("Press select/start", -1, 175, PicoGameBoy.color(255,255,255))
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
        if pgb.button_select() or pgb.button_start():
            view_scores()
        elif pgb.button_A():
            score=0
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
            return


def check_collision(speed,detectionradius, posx, posy, width, height, posx2, posy2, width2, height2):
    bbox1 = [posx, posy, posx + width, posy + height]
    bbox2 = [posx2, posy2, posx2 + width2, posy2 + height2]

    if bbox1[0] < bbox2[2] and bbox1[2] > bbox2[0] and bbox1[1] < bbox2[3] and bbox1[3] > bbox2[1]:
        if posx + width + speed >= posx2 and posx - speed <= posx2 + width2 and posy + height + speed >= posy2 and posy - speed <= posy2 + height2:
            return True
    
    return False

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
                        if check_collision(abs(ballspeedy),35,blo,0+offset,20,10,ballx,bally,10,10):
                            row1[f]=0
                            score=score+100
                            alreadybroken=True
                            pgb.sound(123)
                            changedirection=True

                            
                            
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
                        if check_collision(abs(ballspeedy),35,blo,25+offset,20,10,ballx,bally,10,10):
                            row2[f]=0
                            score=score+50
                            alreadybroken=True
                            pgb.sound(123)
                            changedirection=True
                            
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
                        if check_collision(abs(ballspeedy),30,blo,50+offset,20,10,ballx,bally,10,10):
                            row3[f]=0
                            score=score+25
                            alreadybroken=True
                            pgb.sound(123)
                            changedirection=True
                            
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
                        if check_collision(abs(ballspeedy),45,blo,75+offset,20,10,ballx,bally,10,10):
                            row4[f]=0
                            score=score+10
                            alreadybroken=True
                            pgb.sound(123)
                            changedirection=True
                            
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
                        if check_collision(abs(ballspeedy),35,blo,100+offset,20,10,ballx,bally,10,10):
                            row5[f]=0
                            score=score+5
                            alreadybroken=True
                            pgb.sound(123)
                            changedirection=True
                            
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
            if pgb.button_select() or pgb.button_start():
                pause_screen()
            pgb.fill(PicoGameBoy.color(0,0,0))
            draw_boxes()
            #player movement
            if pgb.button_left() and playerx>15:
                playerx=playerx-speed
            if pgb.button_right() and playerx<210:
                playerx=playerx+speed
                
            #ball physics
            if stationary:
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
                    ballspeedx=ballspeedy=-5
                    going=False
                    pgb.sound(349)
                    sleep(0.05)
                    pgb.sound(0)
                    sleep(0.1)
                    pgb.sound(349)
                    sleep(0.05)
                    pgb.sound(0)
                if changedirection:
                    cchoice=randint(0,5)
                    if ballspeedx==0:
                        res=randint(0,1)
                        res=5 if res==1 else -5
                        ballspeedx=res
                        if ballspeedy<0:
                            ballspeedy+=2
                        else:
                            ballspeedy-=2
                    elif cchoice==5:
                        ballspeedx=0
                        if ballspeedy<0:
                            ballspeedy-=2
                        else:
                            ballspeedy+=2
                    else:
                        rchoice=randint(0,2)
                        if rchoice==0:
                            ballspeedx=-ballspeedx
                        else:
                            ballspeedx=ballspeedx
                    ballspeedy=-ballspeedy
                    changedirection=False
                if check_collision(abs(ballspeedy),30,ballx,bally,10,10,playerx,220,30,20):
                    if ballspeedx==0:
                        res=randint(0,1)
                        res=5 if res==1 else -5
                        ballspeedx=res
                        if ballspeedy<0:
                            ballspeedy+=2
                        else:
                            ballspeedy-=2
                        ballspeedy=-abs(ballspeedy)
                    else:
                        ballspeedy=-abs(ballspeedy)
                    bally=bally-5
                    pgb.sound(349)
                bally=bally+ballspeedy
                ballx=ballx+ballspeedx
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
