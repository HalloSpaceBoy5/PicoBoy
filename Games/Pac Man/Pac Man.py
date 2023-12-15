#Original game for the PicoBoy by HalloSpaceBoy
from PicoGameBoy import PicoGameBoy
from os import rename
rename("/main.py", "/Pac Man/Pac Man.py")
rename("/title.py", "/main.py")
del rename
pgb=PicoGameBoy()
WHITE=PicoGameBoy.color(255,255,255)
BLACK=PicoGameBoy.color(0,0,0)
def check_home():
    if pgb.button_Home():
        homebootstop=open("/noboot", "w")
        homebootstop.close()
        pgb.fill(BLACK)
        pgb.show()
        machine.reset()
try:
    pgb.sound(0,3,2000)
except:
    while True:
        check_home()
        pgb.fill(BLACK)
        pgb.create_text("Update your OS!",-1,25,WHITE)
        pgb.create_text("Update your PicoBoy",-1,140,WHITE)
        pgb.create_text("to play this game.",-1,150,WHITE)
        pgb.show()
reset=False
score=0
lscore=0
lives=3
with open("/Pac Man/sprite_pellet.bin","rb") as sprt:
    pgb.add_sprite(bytearray(sprt.read()), 5,5)
with open("/Pac Man/sprite_blinky.bin","rb") as sprt:
    pgb.add_sprite(bytearray(sprt.read()),16,16)
with open("/Pac Man/sprite_clyde.bin","rb") as sprt:
    pgb.add_sprite(bytearray(sprt.read()),16,16)
with open("/Pac Man/sprite_inky.bin","rb") as sprt:
    pgb.add_sprite(bytearray(sprt.read()),16,16)
with open("/Pac Man/sprite_pinky.bin","rb") as sprt:
    pgb.add_sprite(bytearray(sprt.read()),16,16)
with open("/Pac Man/sprite_panicked.bin","rb") as sprt:
    pgb.add_sprite(bytearray(sprt.read()),16,16)
from math import sqrt
from time import sleep,ticks_ms,ticks_diff
from random import randint

dotlocations=((25,25,1,True),(41,24,1),(57,24,1),(72,24,1),(87,24,2),(104,24,2),(137,24,2),(151,24,2),(167,24,3),(183,24,3),(199,24,3),(215,24,3,True),(25,41,1),(104,41,2),(137,41,2),(216,41,3),(25,57,1),(104,57,2),(137,57,2),(216,57,3),(25,73,1),(41,73,1),(57,73,1),(72,73,1),(87,73,2),(104,73,2),(137,73,2),(151,73,2),(167,73,3),(183,73,3),(199,73,3),(215,73,3),(25,89,4),(72,89,4),(167,89,5),(215,89,6),(25,105,4),(41,105,4),(57,105,4),(72,105,4),(87,105,5),(104,105,5),(137,105,5),(151,105,5),(167,105,6),(183,105,6),(199,105,6),(215,105,6),(8,105,4),(232,105,6),(25,119,4),(105,119,5),(137,119,5),(215,119,6),(25,135,4),(41,135,4),(57,135,4),(72,135,4),(87,135,5),(104,135,5),(120,135,5),(137,135,5),(151,135,5),(167,135,6),(183,135,6),(199,135,6),(215,135,6),(25,151,4),(72,151,4),(167,151,5),(215,151,6),(25,166,7),(72,166,7),(167,166,8),(215,166,9),(25,182,7),(72,182,7),(167,182,8),(215,182,9),(25,198,7,True),(41,198,7),(57,198,7),(72,198,7),(87,198,8),(104,198,8),(120,198,8),(137,198,8),(151,198,8),(167,198,9),(183,198,9),(199,198,9),(215,198,9,True))
def draw_pacman(x, y, d, m):
    pgb.hline(x-8,y,8*2,PicoGameBoy.color(255,255,0))
    for i in range(1,8):
        a = int(sqrt(8*8-i*i))
        pgb.hline(x-a,y+i,a*2,PicoGameBoy.color(255,255,0))
        pgb.hline(x-a,y-i,a*2,PicoGameBoy.color(255,255,0))
        if d==3:
            for i in range(m):
                pgb.line(x, y, x+8, y+(i+1), BLACK)
            for i in range(m):
                pgb.line(x, y, x+8, y-(i+1), BLACK)
            pgb.hline(x, y, 8, BLACK)
        elif d==2:
            for i in range(m):
                pgb.line(x, y, x-8, y+(i+1), BLACK)
            for i in range(m):
                pgb.line(x, y, x-8, y-(i+1), BLACK)
            pgb.hline(x-8, y, 8, BLACK)
        elif d==1:
            for i in range(m):
                pgb.line(x, y, x-(i+1), y+8, BLACK)
            for i in range(m):
                pgb.line(x, y, x+(i+1), y+8, BLACK)
            pgb.vline(x, y, 8, BLACK)
        elif d==0:
            for i in range(m):
                pgb.line(x, y, x-(i+1), y-8, BLACK)
            for i in range(m):
                pgb.line(x, y, x+(i+1), y-8, BLACK)
            pgb.vline(x, y-8, 8, BLACK)
        else:
            if d==3:
                pgb.hline(x, y, 8, BLACK)
            elif d==2:
                pgb.hline(x-8, y, 8, BLACK)
            elif d==1:
                pgb.vline(x, y, 8, BLACK)
            elif d==0:
                pgb.vline(x, y-8, 8, BLACK)

def bounding_box_collision(x, y, width=16, height=16, boxes=((0,0,240,16),(0,0,16,96),(0,112,16,240),(225,0,240,96),(225,113,240,240),(0,209,240,240),(33,33,96,64),(113,17,128,64),(145,33,208,64),(33,81,64,96),(81,81,160,96),(177,81,208,96),(113,97,128,128),(33,113,96,128),(145,113,208,128),(33,145,64,192),(81,145,112,160),(129,145,160,160),(81,161,96,176),(145,161,160,176),(81,177,160,192),(177,145,208,192),(225,113,260,129),(225,81,260,97),(-16,113,16,128),(-16,81,16,96)), boolean=False):
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
                    if not boolean:
                        x -= x_adjust
                    else:
                        return True
                else:
                    if not boolean:
                        x += x_adjust
                    else:
                        return True
            else:
                if y + height > box_y and y < box_y:
                    if not boolean:
                        y -= y_adjust
                    else:
                        return True
                else:
                    if not boolean:
                        y += y_adjust
                    else:
                        return True
    if not boolean:
        return x, y
    else:
        return False
def draw_dots(playerx, playery, dots=dotlocations):
    global currentdots
    global dt
    global grid
    global lscore
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
                dist=sqrt((cenpoint1[0]-cenpoint2[0])**2+(cenpoint1[1]-cenpoint2[1])**2)
                p+=1
                if dist<5:
                    mod[pos]=False
                    score+=10
                    lscore+=10
            if mod[pos]:
                pgb.sprite(0, x-2, y-2)
        else:
            global playerstate
            if mod[pos] and dot[2] in ind:
                cenpoint2=(x+4/2,y+4/2)
                dist=sqrt((cenpoint1[0]-cenpoint2[0])**2+(cenpoint1[1]-cenpoint2[1])**2)
                if dist<9:
                    mod[pos]=False
                    score+=50
                    lscore+=50
                    playerstate=True
                    dt=0
            if mod[pos]:
                pgb.hline(x-5,y,5*2,WHITE)
                for i in range(1,5):
                    a = int(sqrt(5*5-i*i)) # Pythagoras!
                    pgb.hline(x-a,y+i,a*2,WHITE) # Lower half
                    pgb.hline(x-a,y-i,a*2,WHITE)
    currentdots=tuple(mod)
    del mod



class ghost:
    def __init__(self, x, y, c, ai):
        #This is where you can tinker in the ghost's heads
        self.x=x
        self.y=y
        self.initx=x
        self.inity=y
        self.speed=4
        self.raycastdist=4
        self.branchdist=16
        self.c=c+1
        self.ai=ai
        self.scatter=False
        self.scattertimer=0
        self.deadtimer=0
        self.dead=False
        self.deadnot=False
        self.renew=True
        self.current_direction=""
    
    def update(self):
        global playerx
        global playery
        global playerstate
        global debug
        global direction
        global lscore
        global alive
        global reset
        global score
        if reset:
            self.x=self.initx
            self.y=self.inity
            self.renew=True
        if playerstate and not self.deadnot:
            self.playerstate=True
            self.deadnot=True
        if not playerstate:
            self.playerstate=False
            self.deadnot=False
        d=direction
        if self.dead:
            self.deadtimer+=1
            if self.deadtimer<20:
                pgb.create_text("100",self.x,self.y,WHITE)
            if self.deadtimer%20==0:
                self.dead=False
                self.playerstate=False
                self.x=self.initx
                self.y=self.inity
                self.renew=True
                self.deadtimer=0
            return
        if self.ai==1:
            self.playerx=playerx
            self.playery=playery
            self.renew=False
        elif self.ai==2:
            if d==0:
                self.playery=playery-32
                self.playerx=playerx-32
            elif d==1:
                self.playery=playery+48
                self.playerx=playerx
            elif d==2:
                self.playerx=playerx-32
                self.playery=playery
            elif d==3:
                self.playerx=playerx+48
                self.playery=playery
        elif self.ai==3:
            if d==0:
                self.playery=playery-64
                self.playerx=playerx-64
            elif d==1:
                self.playery=playery+70
                self.playerx=playerx+64
            elif d==2:
                self.playerx=playerx-64
                self.playery=playery-64
            elif d==3:
                self.playerx=playerx+70
                self.playery=playery+64
        elif self.ai==4:
            self.playerx=randint(0,240)
            self.playery=randint(0,240)
        if self.scatter:
            self.playerx=randint(0,240)
            self.playery=randint(0,240)
        if self.scattertimer%200==0 and self.scatter==False:
            self.scatter = True
            self.scattertimer=1
        if self.scattertimer%70==0 and self.scatter==True:
            self.scatter = False
            self.scattertimer=1
        if self.playerstate:
            self.playerx=randint(0,240)
            self.playery=randint(0,240)
        else:
            self.scattertimer+=1
        dtc=[]
        u=["UP",None]
        d=["DOWN",None]
        l=["LEFT",None]
        r=["RIGHT",None]
        decision=""
        if self.renew:
            self.y-=self.speed
        else:
            if (not bounding_box_collision(self.x,self.y-self.raycastdist,16,self.raycastdist,boolean=True) and not bounding_box_collision(self.x,self.y-self.raycastdist,16,self.raycastdist,boxes=((113,145,128,160),(225,97,240,112),(1,97,16,112)), boolean=True)) and not self.current_direction=="DOWN":
                dtc.append("UP")
            if (not bounding_box_collision(self.x,self.y+16,16,self.raycastdist, boolean=True) and not bounding_box_collision(self.x,self.y+16,16,self.raycastdist,boxes=((113,145,128,160),(225,97,240,112),(1,97,16,112)), boolean=True)) and not self.current_direction=="UP":
                dtc.append("DOWN")
            if (not bounding_box_collision(self.x-self.raycastdist,self.y,self.raycastdist,16, boolean=True) and not bounding_box_collision(self.x-self.raycastdist,self.y,self.raycastdist,16,boxes=((113,145,128,160),(225,97,240,112),(1,97,16,112)), boolean=True)) and not self.current_direction=="RIGHT":
                dtc.append("LEFT")
            if (not bounding_box_collision(self.x+16,self.y,self.raycastdist,16, boolean=True) and not bounding_box_collision(self.x+16,self.y,self.raycastdist,16,boxes=((113,145,128,160),(225,97,240,112),(1,97,16,112)), boolean=True)) and not self.current_direction=="LEFT":
                dtc.append("RIGHT")
            for dr in dtc:
                if dr=="UP":
                    u[1]=(sqrt((self.playerx+8-self.x+8)**2+(self.playery+8-self.y-self.branchdist)**2))
                if dr=="DOWN":
                    d[1]=(sqrt((self.playerx+8-self.x+8)**2+(self.playery+8-self.y+16+self.branchdist)**2))
                if dr=="LEFT":
                    l[1]=(sqrt((self.playerx+8-self.x-self.branchdist)**2+(self.playery+8-self.y+8)**2))
                if dr=="RIGHT":
                    r[1]=(sqrt((self.playerx+8-self.x+16+self.branchdist)**2+(self.playery+8-self.y+8)**2))
            i=0
            if not u[1] == None:
                decimal_places = len(str(u[1]).split('.')[1])
                factor = 10 ** decimal_places
                u[1] = int(u[1] * factor)
            if not d[1] == None:
                decimal_places = len(str(d[1]).split('.')[1])
                factor = 10 ** decimal_places
                d[1] = int(d[1] * factor)
            if not l[1] == None:
                decimal_places = len(str(l[1]).split('.')[1])
                factor = 10 ** decimal_places
                l[1] = int(l[1] * factor)
            if not r[1] == None:
                decimal_places = len(str(r[1]).split('.')[1])
                factor = 10 ** decimal_places
                r[1] = int(r[1] * factor)
            variables=[tuple(u),tuple(d),tuple(l),tuple(r)]
            sorted_priorities = ["UP", "LEFT", "DOWN", "RIGHT"]
            sorted_variables = sorted([var for var in variables if var[1] is not None], key=lambda x: (x[1], sorted_priorities.index(x[0]) if x[0] in sorted_priorities else len(sorted_priorities)))
            for idx, r in enumerate(sorted_variables):
                r = (r[0], int(r[1]))
                sorted_variables[idx] = r
            decision=sorted_variables[0][0]
            if decision=="UP":
                self.y-=self.speed
                self.current_direction="UP"
            if decision=="DOWN":
                self.y+=self.speed
                self.current_direction="DOWN"
            if decision=="LEFT":
                self.x-=self.speed
                self.current_direction="LEFT"
            if decision=="RIGHT":
                self.x+=self.speed
                self.current_direction="RIGHT"
        if self.y<=129:
            self.renew=False
        if self.playerstate:
            pgb.sprite(5,self.x,self.y)
            if bounding_box_collision(self.x,self.y,16,16,((playerx,playery,playerx+16,playery+16),(0,0,0,0)),boolean=True):
                self.dead=True
                score+=100
                lscore+=100
                pgb.sound(146,3)
                sleep(0.05)
                pgb.sound(0,3)
                pgb.sound(207,3)
                sleep(0.05)
                pgb.sound(0,3)
        else:
            if bounding_box_collision(self.x,self.y,16,16,((playerx,playery,playerx+16,playery+16),(0,0,0,0)),boolean=True):
                alive=False
            pgb.sprite(self.c,self.x,self.y)
        

def pacdeath(o,x,y):
    pgb.hline(x-8,y,8*2,PicoGameBoy.color(255,255,0))
    for i in range(1,8):
        a = int(sqrt(8*8-i*i))
        pgb.hline(x-a,y+i,a*2,PicoGameBoy.color(255,255,0))
        pgb.hline(x-a,y-i,a*2,PicoGameBoy.color(255,255,0))
    for i in range(o):
        pgb.line(x, y, x+8, y+(i+1), BLACK)
    for i in range(o):
        pgb.line(x, y, x+8, y-(i+1), BLACK)
    pgb.hline(x, y, 8, BLACK)
    for i in range(o):
        pgb.line(x, y, x-8, y+(i+1), BLACK)
    for i in range(o):
        pgb.line(x, y, x-8, y-(i+1), BLACK)
    pgb.hline(x-8, y, 8, BLACK)
    for i in range(o):
        pgb.line(x, y, x-(i+1), y+8, BLACK)
    for i in range(o):
        pgb.line(x, y, x+(i+1), y+8, BLACK)
    pgb.vline(x, y, 8, BLACK)
    for i in range(o):
        pgb.line(x, y, x-(i+1), y-8, BLACK)
    for i in range(o):
        pgb.line(x, y, x+(i+1), y-8, BLACK)
    pgb.vline(x, y-8, 8, BLACK)

def new_level():
    global grid
    global playerx
    global playery
    global lives
    global score
    global lscore
    global playerstate
    global direction
    global debug
    global alive
    global reset
    global currentdots
    global dotlocations
    global dt
    currentdots=[]
    for i in range(len(dotlocations)):
        currentdots.append(True)
    currentdots=tuple(currentdots)
    grid=(True,False,False,False,False,False,False,False,False)
    m=4
    d=True
    direction=0
    playerx=113
    playery=65
    playerspeed=4
    alive=True
    soundposextralife=0
    playerstate=False
    dt=0
    blinky=ghost(113,129,0,1)
    pinky=ghost(113,161,3,2)
    inky=ghost(113,161,2,3)
    clyde=ghost(113,161,1,4)
    while True:
        if pgb.button_start():
                pgb.sound(0,1)
                pgb.sound(0,2)
                pgb.sound(0,3)
                pgb.fill_rect(10,90,220,80,PicoGameBoy.color(50,50,50))
                pgb.center_text("Game Paused",WHITE)
                pgb.create_text("Press Start to resume", -1, 135, WHITE)
                pgb.show()
                sleep(0.5)
                while True:
                    pgb.show()
                    check_home()
                    if pgb.button_start():
                        sleep(0.5)
                        break
        check_home()
        if alive:
            if playerstate:
                playerspeed=6
                dt+=1
                if dt%70==0:
                    playerstate=False
                    dt=0
                    soundalt=True
                    playerspeed=4
            pgb.load_image("/Pac Man/pacmanbg.bin")
            pgb.create_text("Score: "+str(score)+"  Lives: "+str(lives), -1, 223, WHITE)
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
            f=bounding_box_collision(playerx,playery, boxes=((113,145,128,160),(0,0,0,0)))
            playerx=f[0]
            playery=f[1]
            del f
            c=bounding_box_collision(playerx,playery)
            playerx=c[0]
            playery=c[1]
            del c
            draw_dots(playerx, playery)
            if playerx<-17:
                playerx=240
            if playerx>250:
                playerx=-16
            blinky.update()
            inky.update()
            pinky.update()
            clyde.update()
            draw_pacman(playerx+7,playery+7,direction, m)
            if lscore>=5000:
                lives+=1
                lscore-=5000
            pgb.show()
            if lives<1:
                return False
            if not any(currentdots):
                pgb.sound(0)
                pgb.sound(0,2)
                pgb.sound(0,3)
                return True
            reset=False
        else:
            pgb.sound(0)
            pgb.sound(0,2)
            pgb.sound(0,3)
            for index, i in enumerate((185,145,165,125,145,105,233)):
                pgb.sound(i)
                sleep(0.15)
                pgb.sound(0)
                pacdeath(index*2,playerx+7,playery+7)
                pgb.show()
            sleep(0.005)
            pgb.sound(233)
            sleep(0.15)
            pgb.sound(0)
            sleep(1)
            playerx=113
            playery=65
            reset=True
            lives-=1
            alive=True

def view_scores():
    x=open("/Pac Man/highscoresPac Man.sc", "r")
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
            pgb.fill(BLACK)
            pgb.show()
            machine.reset()
            break
        pgb.fill(BLACK)
        for i in range(len(scores)):
            pgb.create_text("Score "+str(i+1)+": "+str(scores[i]), -1, 50+i*15, WHITE)
        pgb.create_text("Press B to exit", -1, 220, WHITE)
        pgb.show()
        
now = ticks_ms()
while True:
    if pgb.button_Home():
        homebootstop=open("/noboot", "w")
        homebootstop.close()
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()
        break
    pgb.load_image("/Pac Man/pacman_title.bin")
    pgb.show()
    
    if ticks_diff(ticks_ms(), now) > 200:
        now = ticks_ms()
        pgb.create_text("PRESS A TO PLAY",-1,150,WHITE)
        pgb.show()
        while ticks_diff(ticks_ms(), now) < 200:
            sleep(0.020)
        now = ticks_ms()
    if pgb.button_start():
        view_scores()
    elif pgb.button_A():
        break
sleep(0.25)
while True:
    if new_level():
        pgb.fill(BLACK)
        pgb.center_text("Level Clear!",WHITE)
        pgb.create_text("Press A to play",-1, 125, WHITE)
        pgb.create_text("the next level",-1, 140, WHITE)
        pgb.text("Press home to quit.", 40, 160, WHITE)
        pgb.create_text("Score: "+str(score),-1,80,WHITE)
        pgb.show()
        while True:
            check_home()
            if pgb.button_A():
                sleep(0.5)
                break
    else:
        with open("/Pac Man/highscoresPac Man.sc", "r") as s:
            scores=s.read().split("\n")
            for r in range(len(scores)):
                scores[r]=int(scores[r])
        newscores=scores
        newscores.append(int(score))
        newscores.sort(reverse=True)
        for i in range(len(newscores)): newscores[i]=str(newscores[i])
        with open("/Pac Man/highscoresPac Man.sc", "w+") as w:
            w.write("\n".join(newscores[:10]))
        while True:
            pgb.fill(BLACK)
            pgb.center_text("GAME OVER",WHITE)
            pgb.text("Press A to play again.", 35, 125, WHITE)
            pgb.text("Press home to quit.", 40, 140, WHITE)
            pgb.create_text("Press start", -1, 175, WHITE)
            pgb.create_text("to view scores.", -1, 190, WHITE)
            pgb.create_text("Score: "+str(score),-1,80,WHITE)
            pgb.show()
            check_home()
            if pgb.button_A():
                score=0
                lscore=0
                lives=3
                sleep(0.5)
                break
            if pgb.button_start():
                view_scores()
