try:
    from PicoBoySDK import PicoBoySDK, PlayerObject
    PicoBoy=PicoBoySDK("Space Invaders",0)
    Player=PlayerObject(PicoBoy,112,224,16,16,PicoBoy.Load_Sprite("player.sprt",16,16),4)
    test=Player.initx
except:
    try:
        del PicoBoy
        del Player
    except:
        "none"
    from os import chdir, rename
    chdir("/")
    try:
        try:
            from PicoBoySDK import PicoBoySDK
        except:
            rename("/main.py", "/Space Invaders/Space Invaders.py")
            rename("/title.py", "/main.py")
    except:
        rename("/main.py", "/Space Invaders.py")
        rename("/title.py", "/main.py")
    from PicoGameBoy import PicoGameBoy
    pgb=PicoGameBoy()
    pgb.fill(PicoGameBoy.color(0,0,0))
    pgb.create_text("Your OS is not",-1,20,PicoGameBoy.color(255,255,255))
    pgb.create_text("up to date!",-1, 35,PicoGameBoy.color(255,255,255))
    pgb.create_text("This game requires",-1,120,PicoGameBoy.color(255,255,255))
    pgb.create_text("at least PBOS V2.2",-1, 135,PicoGameBoy.color(255,255,255))
    pgb.create_text("to play this game.",-1,150,PicoGameBoy.color(255,255,255))
    pgb.create_text("Press Home to quit.",-1,220,PicoGameBoy.color(255,255,255))
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.show_screen()
from random import randint
import time
from gc import mem_free


Player.direction="X"
hit_taken=False
enemysprite=PicoBoy.Load_Sprite("invader.sprt",16,16)
deathsprite=PicoBoy.Load_Sprite("death.sprt",16,16)
greencornerL=PicoBoy.Load_Sprite("green_cornerL.sprt",16,16)
greencornerR=PicoBoy.Load_Sprite("green_cornerR.sprt",16,16)

starpattern=[]
for i in range(50):
    starpattern.append((randint(5,235),randint(22,235)))
class Bullet:
    def __init__(self, initx, inity, speed, direction, typ):
        self.x=initx
        self.y=inity
        self.speed=speed
        self.typ=typ
        self.direction=direction
        
    def update(self):
        global Player
        global bull
        global hit_taken
        global playerbullets
        if self.x+16>Player.x and self.x-16<Player.x:
            if PicoBoy.Check_Collision(Player.x,Player.y,16,16,self.x,self.y,8,8,Player.speed,1) and not self.typ:
                hit_taken=True
                del bull
                return
        if self.y>240 or self.y<20:
            if self.typ:
                try:
                    playerbullets.remove(self)
                except:
                    del self
            else:
                del self
            return
        if self.direction==0:
            self.y+=self.speed
        else:
            self.y-=self.speed
        if self.typ==False:
            PicoBoy.Fill_Rect(self.x+7,self.y,2,8,(255,0,0))
        else:
            PicoBoy.Fill_Rect(self.x+7,self.y,2,8,(255,255,255))
            
            
class enemy:
    def __init__(self, colum,row):
        self.colum=colum
        self.row=row
        self.x=colum*16
        self.y=row*16
        self.position=0
        self.offsetx=48
        self.offsety=0
        self.counter=0
        self.skip=False
        self.waitamnt=1
        self.active=True
        self.ex=0
        self.dactive=True
        self.phase=1
        self.phasecounter=0
        self.sound=False
        self.speed=0
    
    def update(self):
        global PicoBoy
        global enemysprite
        global enemylist
        global bull
        global erasedindicies
        global deathsprite
        global all1false
        global all2false
        global lives
        self.x=self.colum*16+4*self.colum+self.offsetx
        self.y=self.row*16+8*self.row+self.offsety+32
        if self.active:
            self.phasecounter+=1
            self.counter+=1
            if all1false:
                self.ex=3
            elif all2false:
                self.ex=1
            if (int(self.offsety/16))==9+self.ex:
                lives=0
                return
            if self.phasecounter%5==0 and self.sound:
                self.phasecounter=0
                PicoBoy.Stop_Sound(4)
                self.phase+=1
                if self.phase>4:
                    self.phase=1
                self.sound=False
            
            if int(self.counter)%self.speed==0:
                if not self.sound:
                    if self.phase==1:
                        PicoBoy.Play_Sound(200,4)
                    if self.phase==2:
                        PicoBoy.Play_Sound(150,4)
                    if self.phase==3:
                        PicoBoy.Play_Sound(100,4)
                    if self.phase==4:
                        PicoBoy.Play_Sound(50,4)
                    self.phasecounter=0
                    self.sound=True
                if self.offsetx==80+right_count*16 and self.offsety%32==0:
                    self.offsety+=16
                    self.skip=True
                elif self.offsetx==0-left_count*16 and not self.offsety%32==0:
                    self.offsety+=16
                    self.skip=True
                if not self.skip:
                    if self.offsety%32==0:
                        self.offsetx+=16
                    else:
                        self.offsetx-=16
                else:
                    self.skip=False
                self.counter=0
            PicoBoy.Render_Sprite(enemysprite,self.x,self.y)
        elif self.dactive:
            self.counter+=1
            if self.counter%5==0:
                self.dactive=False
            PicoBoy.Render_Sprite(deathsprite,self.x,self.y)
            
            
class brick:
    def __init__(self, x,y,block):
        self.x=16+x*16+block*32+48*block
        self.y=y*16+176
        self.posx=x
        self.posy=y
        self.active=True
        self.block=block
        
    def update(self):
        global PicoBoy
        global greencornerL
        global greencornerR
        if self.active:
            if self.posx==0 and self.posy==0:
                PicoBoy.Render_Sprite(greencornerL,self.x,self.y)
            elif self.posx==2 and self.posy==0:
                PicoBoy.Render_Sprite(greencornerR,self.x,self.y)
            elif self.posx==0 and self.posy==2:
                PicoBoy.Render_Sprite(greencornerL,self.x,self.y)
            elif self.posx==2 and self.posy==2:
                PicoBoy.Render_Sprite(greencornerR,self.x,self.y)
            else:
                PicoBoy.Fill_Rect(self.x,self.y,16,16,(0,255,0))
            
            
def main_game():
    global lives
    global enemylist
    global score
    global level
    global all1false
    global all2false
    global left_count
    global right_count
    playerbullets=[]
    erasedindicies=[]
    fired=False
    e_speed=30
    f_cooldown=0
    fb_cooldown=0
    a_cooldown=0
    enemylist=[]
    global blockers
    blockers=[]
    for i in range(3):
        temp=[]
        for f in range(2):
            temp1=[]
            for g in range(3):
                temp1.append(brick(g,f,i))
            temp.append(temp1)
        blockers.append(temp)
    global hit_taken
    global bull
    hit_taken=False
    alldead=False
    for i in range(8):
        temp=[]
        for f in range(3):
            temp.append(enemy(i,f))
        enemylist.append(temp)
    while True:
        PicoBoy.Stop_Sound(2)
        PicoBoy.Fill_Screen((0,0,0))
        for i in starpattern:
            PicoBoy.hline(i[0],i[1],1,PicoBoy.color(255,255,255))
        PicoBoy.Create_Text("Score: "+str(score),4,4,(255,255,255))
        PicoBoy.Create_Text("LV"+str(level),125,4,(255,255,255))
        PicoBoy.Create_Text("Lives: "+str(lives),165,4,(255,255,255))
        PicoBoy.hline(0,17,240,PicoBoy.color(255,255,255))
        Player.Update()
        if PicoBoy.Button("A") and a_cooldown==0:
            playerbullets.append(Bullet(Player.x, Player.y, 8, 1, True))
            f_cooldown=4
            a_cooldown=5
        if a_cooldown>0:
            a_cooldown-=1
        if f_cooldown>0:
            PicoBoy.Play_Sound(1000,1)
            f_cooldown-=1
        else:
            PicoBoy.Stop_Sound(1)
        if fb_cooldown==6:
            PicoBoy.Play_Sound(200,2)
            fb_cooldown-=1
        elif fb_cooldown==4:
            PicoBoy.Play_Sound(300,2)
            fb_cooldown-=1
        elif fb_cooldown==2:
            PicoBoy.Play_Sound(400,2)
            fb_cooldown-=1
        elif fb_cooldown>0:
            fb_cooldown-=1
        killableenemies=[]
        killableenemiescoords=[]
        ch=[]
        for i in enemylist:
            a=0
            for f in i:
                if f.active:
                    a+=1
            ch.append(a)
        t=0
        for i in ch:
            t+=i
        new_e=round(e_speed*(t/(24+(level-1))))
        if new_e<5:
            new_e=5
        for x,i in enumerate(enemylist):
            highest=0
            newy=0
            newx=0
            for f in i:
                f.speed=new_e
                if f.active==True and f.row>=highest:
                    highest=f.row
                    newy=f.y
                    newx=f.x
            killableenemies.append((x,highest))
            killableenemiescoords.append((newx,newy))
        for bullet in playerbullets:
            bullet.update()
            if bullet.y<20:
                playerbullets.remove(bullet)
            for x,enem in enumerate(killableenemiescoords):
                if bullet.x+16>enem[0] and bullet.x-16<enem[0]:
                    if PicoBoy.Check_Collision(enem[0],enem[1],16,16,bullet.x,bullet.y,16,16,bullet.speed,1):
                        setr=killableenemies[x]
                        enemylist[setr[0]][setr[1]].active=False
                        enemylist[setr[0]][setr[1]].counter=0
                        if setr[1]==2:
                            score+=10
                        if setr[1]==1:
                            score+=20
                        if setr[1]==0:
                            score+=30
                        fb_cooldown=6
                        playerbullets.remove(bullet)
                        break
        check=True
        all1false=True
        all2false=True
        left_count = 0
        right_count = 0
        for x,i in enumerate(enemylist):
            c=False
            for f in i:
                if f.active:
                    c=True
            if not c:
                left_count+=1
            else:
                break
        for x,i in enumerate(reversed(enemylist)):
            c=False
            for f in i:
                if f.active:
                    c=True
            if not c:
                right_count+=1
            else:
                break
        for x,lis in enumerate(enemylist):
            if lis[1].active:
                all1false=False
            if lis[2].active:
                all2false=False
            for e in lis:
                e.update()
                if e.active:
                    check=False
        if check:
            return True
        good2fire=False
        try:
            if bull.y>240:
                good2fire=True
        except:
            good2fire=True
        if good2fire:
            firablecoords=[]
            for x,i in enumerate(enemylist):
                highest=0
                newy=0
                newx=0
                for f in i:
                    if f.active==True and f.row>=highest:
                        highest=f.row
                        newy=f.y
                        newx=f.x
                if not newy==0:
                    firablecoords.append((newx,newy))
            choice=firablecoords[randint(0,len(firablecoords)-1)]
            bull=Bullet(choice[0],choice[1]+16,4,0,False)
        try:
            bull.update()
        except:
            "object doesnt exist"
        for block in blockers:
            for row in block:
                for obj in row:
                        obj.update()
                        if obj.active:
                            for bullet in playerbullets:
                                if bullet.x+16>obj.x and bullet.x-16<obj.x:
                                    if PicoBoy.Check_Collision(obj.x,obj.y,16,16,bullet.x,bullet.y,8,16,bullet.speed,1):
                                        obj.active=False
                                        playerbullets.remove(bullet)
                                        break
                            try:
                                if bull.x+16>obj.x and bull.x-16<obj.x:
                                    if PicoBoy.Check_Collision(obj.x,obj.y,16,16,bull.x,bull.y,8,16,bull.speed,1):
                                        obj.active=False
                                        del bull
                            except:
                                ""
                                    
        if hit_taken:
            lives-=1
            hit_taken=False
            try:
                del bull
            except:
                ""
            PicoBoy.Render_Sprite(deathsprite, Player.x, Player.y)
            PicoBoy.show_screen()
            for i in range(2500):
                PicoBoy.Play_Sound(randint(1000,2000),3)
                PicoBoy.Stop_Sound(3)
            Player.x=Player.initx
            playerbullets=[]
        if lives==0:
            return False
        if PicoBoy.Button("Start"):
            PicoBoy.Pause_Screen()
        PicoBoy.Update()


lives=3
score=0
level=1
t=True
while True:
    PicoBoy.Load_Image("Space Invaders Title.pbimg")
    if t:
        PicoBoy.Create_Text("HOLD A TO PLAY",-1, 202,(255,255,255))
        t=False
    elif not t:
        PicoBoy.Create_Text("HOLD A TO PLAY",-1, 202,(0,0,0))
        t=True
    PicoBoy.Update()
    if PicoBoy.Button("Start"):
        PicoBoy.Show_Scores()
    elif PicoBoy.Button("A"):
        time.sleep(0.5)
        break
    time.sleep(0.2)
while True:
    if main_game():
        PicoBoy.Stop_Sound(1)
        PicoBoy.Stop_Sound(2)
        PicoBoy.Stop_Sound(3)
        PicoBoy.Stop_Sound(4)
        PicoBoy.Fill_Screen((0,0,0))
        PicoBoy.Create_Text("YOU PASSED LEVEL "+str(level),-1,75,(255,0,0))
        PicoBoy.Create_Text("YOU PASSED LEVEL "+str(level),-1,77,(255,255,0))
        PicoBoy.Create_Text("Your score is: "+str(score),-1,100,(255,255,255))
        PicoBoy.Create_Text("Press A to continue",-1,120,(255,255,255))
        PicoBoy.Create_Text("to the next level.",-1,135,(255,255,255))
        PicoBoy.Update()
        time.sleep(0.5)
        while True:
            PicoBoy.Create_Text("YOU PASSED LEVEL "+str(level),-1,75,(255,0,0))
            PicoBoy.Create_Text("YOU PASSED LEVEL "+str(level),-1,77,(255,255,0))
            PicoBoy.Create_Text("Your score is: "+str(score),-1,100,(255,255,255))
            PicoBoy.Create_Text("Press A to continue",-1,120,(255,255,255))
            PicoBoy.Create_Text("to the next level.",-1,135,(255,255,255))
            PicoBoy.Update()
            if PicoBoy.Button("A"):
                time.sleep(0.5)
                level+=1
                break
        try:
            del bull
        except:
            ""
    else:
        PicoBoy.Save_Score(score)
        PicoBoy.Stop_Sound(1)
        PicoBoy.Stop_Sound(2)
        PicoBoy.Stop_Sound(3)
        PicoBoy.Stop_Sound(4)
        PicoBoy.Fill_Screen((0,0,0))
        PicoBoy.Create_Text("GAME OVER",-1,75,(255,0,0))
        PicoBoy.Create_Text("GAME OVER",-1,77,(255,255,0))
        PicoBoy.Create_Text("Your score is: "+str(score),-1,100,(255,255,255))
        PicoBoy.Create_Text("Press A to play again.",-1,120,(255,255,255))
        PicoBoy.Create_Text("Press Start to",-1,140,(255,255,255))
        PicoBoy.Create_Text("view high scores.",-1,155,(255,255,255))
        PicoBoy.Update()
        time.sleep(0.5)
        while True:
            PicoBoy.Create_Text("GAME OVER",-1,75,(255,0,0))
            PicoBoy.Create_Text("GAME OVER",-1,77,(255,255,0))
            PicoBoy.Create_Text("Your score is: "+str(score),-1,100,(255,255,255))
            PicoBoy.Create_Text("Press A to play again.",-1,120,(255,255,255))
            PicoBoy.Create_Text("Press Start to",-1,140,(255,255,255))
            PicoBoy.Create_Text("view high scores.",-1,155,(255,255,255))
            PicoBoy.Update()
            if PicoBoy.Button("A"):
                time.sleep(0.5)
                lives=3
                score=0
                level=1
                break
            if PicoBoy.Button("Start"):
                PicoBoy.Show_Scores()
