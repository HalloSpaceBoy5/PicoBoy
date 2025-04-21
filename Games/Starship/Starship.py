from PicoBoySDK import PicoBoySDK, MusicBoxObject
from random import randint, choice
from math import ceil
from time import sleep, ticks_ms, ticks_diff
from array import array
from gc import mem_free


PicoBoy=PicoBoySDK("Starship",0.01)
print(mem_free())
try:
    PicoBoy.Line(0,0,1,1,(0,0,0))
except:
    PicoBoy.Fill_Screen((0,0,0))
    PicoBoy.Create_Text("This game requires",-1,20,(255,255,255))
    PicoBoy.Create_Text("at least PBOS V3.1",-1, 35,(255,255,255))
    PicoBoy.Create_Text("Press Home to quit.",-1,220,(255,255,255))
    while True:
        PicoBoy.Update(noclear=True)
    
MusicBox=MusicBoxObject(PicoBoy,1)
bulletsprite=PicoBoy.Load_Sprite("bullet.sprt",7,7)
playersprites=[PicoBoy.Load_Sprite("starship_up.sprt",17,17),PicoBoy.Load_Sprite("starship_down.sprt",17,17),PicoBoy.Load_Sprite("starship_left.sprt",17,17),PicoBoy.Load_Sprite("starship_right.sprt",17,17)]
enemysprites=[PicoBoy.Load_Sprite("enemy_left.sprt",17,17),PicoBoy.Load_Sprite("enemy_down.sprt",17,17)]
playerboundtop=27
playerboundright=27
playerboundbottom=23
score=0
level=1
musicchoice=-1
starcoords=[]
for i in range(100):
    starcoords.append((randint(0,240-playerboundright),randint(playerboundtop,240-playerboundbottom)))


class enemy:
    def __init__(self,x,y,typ,direction,speed,firerate):
        self.counter=-1
        self.firerate=firerate
        self.speed=Playerspeed-1
        self.firespeed=speed
        self.x=x
        self.y=y
        self.direction=direction
        self.type=typ
        if typ==1:
            if direction==0:
                self.x=240-17
                self.y=100
            else:
                self.x=100
                self.y=0
        else:
            if direction==0:
                self.x=240-17
            else:
                self.y=0
        
    def update(self):
        self.counter+=1
        if self.type==1:
            if self.direction==1:
                if self.x>Playerx:
                    self.x-=self.speed
                if self.x<Playerx:
                    self.x+=self.speed
                if self.counter%self.firerate==0:
                    bulletlist.append(bullet(self.x+5,self.y+17,self.firespeed,self.direction))
            if self.direction==0:
                if self.y>Playery:
                    self.y-=self.speed
                if self.y<Playery:
                    self.y+=self.speed
                if self.counter%self.firerate==0:
                    bulletlist.append(bullet(self.x-10,self.y+5,self.firespeed,self.direction))
        if self.type==0:
            if self.direction==1:
                if self.counter%self.firerate==0:
                    bulletlist.append(bullet(self.x+5,self.y+17,self.firespeed,self.direction))
            else:
                if self.counter%self.firerate==0:
                    bulletlist.append(bullet(self.x-10,self.y+5,self.firespeed,self.direction))
        PicoBoy.Render_Sprite(enemysprites[self.direction],self.x+frameshift,self.y)

class bullet:
    def __init__(self, x, y, speed, direction):
        self.x=x
        self.y=y
        self.speed=speed
        self.direction=direction
    
    def update(self):
        global bulletsprite,lives,frameshift,sfxcounter
        if self.direction==0:
            self.x-=self.speed
            if self.x<-17:
                bulletlist.remove(self)
                return
        if self.direction==1:
            self.y+=self.speed
            if self.y>240-playerboundbottom:
                bulletlist.remove(self)
                return
        if PicoBoy.Check_Collision(Playerx+frameshift,Playery+8,17,10,self.x+frameshift,self.y,7,7,0,1):
            lives-=1
            bulletlist.remove(self)
            frameshift=10
            for i in range(350):
                PicoBoy.Play_Sound(randint(5000,10000),4)
            PicoBoy.Stop_Sound(4)
            return
        PicoBoy.Render_Sprite(bulletsprite,self.x+frameshift,self.y)

class scoreboost:
    def __init__(self,x,y,amt):
        self.amt=amt
        self.x=x
        self.y=y
        self.gotten=False
        self.counter=0
        
    def update(self):
        global score
        if self.gotten:
            self.counter+=1
            PicoBoy.Create_Text("+"+str(self.amt),self.x-int(len("+"+str(self.amt))/2)*2+frameshift,self.y-4,(255,255,255))
            if self.counter<2:
                PicoBoy.Play_Sound(530,4)
            elif self.counter<5:
                PicoBoy.Play_Sound(650,4)
            if self.counter==6:
                PicoBoy.Stop_Sound(4)
            if self.counter%50==0:
                slist.remove(self)
                return
        else:
            if PicoBoy.Check_Collision(self.x-10+frameshift,self.y-10,20,20,Playerx,Playery,17,17,Playerspeed,1):
                score+=self.amt
                self.gotten=True
                PicoBoy.Play_Sound(130,4)
            PicoBoy.ellipse(self.x+frameshift,self.y,10,10,PicoBoy.color(0,180,0),True)
            PicoBoy.ellipse(self.x+frameshift,self.y,9,9,PicoBoy.color(100,100,100),True)
            PicoBoy.Create_Text(str(self.amt),(self.x)-(int(len(str(self.amt))/2)*8)+frameshift,self.y-3,(255,255,255))
        
class timer:
    def __init__(self):
        self.time=0
        self.counter=0
        
    def tick(self):
        self.counter+=1
        if self.counter%20==0:
            self.time+=1
        return self.time
        

def new_level():
    global Playerx,Playery,Playerspeed,Playerdirection,level,score,time,bulletlist,enemlist,lives,frameshift,slist,musicchoice
    Playerx,Playery=randint(playerboundtop,240-playerboundbottom-17),randint(0,240-playerboundright-17)
    Playerspeed=5
    Playerdirection=0 #0,1,2,3 = up,down,left,right
    bulletlist=[]
    enemlist=[]
    slist=[]
    frameshift=0
    lives=3+int(level/10)
    time=randint(15+int(level/2),20+int(level/2))
    while True:
        nmc=randint(0,2)
        if not nmc==musicchoice:
            break
    MusicBox.Stop_Song()
    MusicBox.Change_Mode(1)
    if nmc==0:
        currentsong="game_theme.pbs"
    elif nmc==1:
        currentsong="game_theme2.pbs"
    else:
        currentsong="game_theme3.pbs"
    MusicBox.Play_Song(currentsong)
    musicchoice=nmc


    scale=1
    if level>4:
        g=False
        if level<10 and not g:
            c=randint(int(1*ceil(scale/1)),int(2*ceil(scale/1)))
            g=True
        if level<20 and not g:
            c=randint(int(1*ceil(scale/1)),int(3*ceil(scale/1)))
            g=True
        if level<40 and not g:
            c=randint(int(1*ceil(scale/1)),int(4*ceil(scale/1)))
            g=True
        if level>=40:
            c=randint(int(2*ceil(scale/1)),int(4*ceil(scale/1)))
        w=randint(15+abs(5-int(level/10)),25+abs(10-int(level/10)))
        if w>100:
            w=randint(100,120)
        enemlist.append(enemy(223,100,1,0,c,w))
        w=randint(15+abs(5-int(level/10)),25+abs(10-int(level/10)))
        if w>100:
            w=randint(100,120)
        enemlist.append(enemy(100,0,1,1,c,w))
    else:
        w=randint(60+int(5*level),90+int(5*level))
        if w>100:
            w=randint(100,120)
        enemlist.append(enemy(223,100,1,randint(0,1),randint(int(1*scale),int(2*scale)),w))
    a=choice([True, False])
    pastx=[]
    pasty=[]
    right=0
    top=0
    num=randint(2+int(level/6),3+int(level/6))
    for i in range(num):
        if a:
            top+=1
            a=not a
        else:
            right+=1
            a=not a
    top=int(top)
    right=int(right)
    if level<10:
        cd=(1,2)
        g=True
    if level<20:
        cd=(2,3)
        g=True
    if level<40:
        cd=(2,4)
        g=True

    for i in range(top):
        g=False
        c=randint(*cd)
        count=0
        while True:
            if count==10000:
                break
            count+=1
            coo=randint(10,240-45)
            val=True
            for value in enemlist:
                if PicoBoy.Check_Collision(coo-8,0,34,17,value.x,value.y,17,17,1,1):# pygame.Rect(coo-16,0,64,32).colliderect(value.rect):
                    val=False
            if val:
                break
        w=randint(10+abs(5-int(level/10)),20+abs(10-int(level/10)))
        if w>100:
            w=randint(100,120)
        enemlist.append(enemy(coo,0,0,1,c,w))
        pastx.append(coo)
        if int((240-100)/32)-len(pastx)<0:
            break
    for i in range(right):
        g=False
        c=randint(*cd)
        count=0
        while True:
            if count==100000:
                break
            count+=1
            coo=randint(61,240-50)
            val=True
            for value in enemlist:
                if PicoBoy.Check_Collision(207,coo,17,17,value.x,value.y,17,17,1,1):# pygame.Rect(swidth-33,coo,32,32).colliderect(value.rect):
                    val=False
            if val:
                break
        w=randint(10+abs(5-int(level/10)),20+abs(10-int(level/10)))
        if w>100:
            w=randint(100,120)
        enemlist.append(enemy(223,coo,0,0,c,w))
        pasty.append(coo)
        if int((240-111)/32)-len(pasty)<0:
            break


    Timer=timer()
    while True:
        PicoBoy.Fill_Screen((48,48,48))
        timeg=Timer.tick()
        for s in starcoords:
            PicoBoy.vline(s[0]+frameshift,s[1],1,PicoBoy.color(255,255,255))
        PicoBoy.Fill_Rect(0+frameshift,19,240,8,(175,175,175))
        PicoBoy.Fill_Rect(214+frameshift,0,8,220,(175,175,175))
        if randint(0,25+abs(50-(level*10)))==0 and len(slist)<5:
            while True:
                while True:
                    xs=randint(20,150)
                    if not xs in range(Playerx-10,Playerx+10):
                        break
                while True:
                    ys=randint(100,150)
                    if not ys in range(Playerx-10,Playerx+10):
                        break
                go=True
                for p in slist:
                    if PicoBoy.Check_Collision(xs-10,ys-10,20,20,p.x-10,p.y-10,20,20,Playerspeed,1):
                        go=False
                if go:
                    break
            slist.append(scoreboost(xs,ys,choice((10,10,10,10,10,10,10,10,10,10,25,25,25,25,25,25,25,50,50,50,50,50,75,75,75,75,99,99))))
        global Playerx,Playery,Playerdirection
        if PicoBoy.Button("Up"):
            if Playery>playerboundtop:
                Playery-=Playerspeed
            Playerdirection=0
        elif PicoBoy.Button("Down"):
            if Playery<240-playerboundbottom-17:
                Playery+=Playerspeed
            Playerdirection=1
        elif PicoBoy.Button("Left"):
            if Playerx>0:
                Playerx-=Playerspeed
            Playerdirection=2
        elif PicoBoy.Button("Right"):
            if Playerx<240-playerboundright-17:
                Playerx+=Playerspeed
            Playerdirection=3
        if Playery<playerboundtop:
            Playery=playerboundtop
        if Playery>240-playerboundbottom-17:
            Playery=240-playerboundbottom-17
        if Playerx<0:
            Playerx=0
        if Playerx>240-playerboundright-17:
            Playerx=240-playerboundright-17
        PicoBoy.Render_Sprite(playersprites[Playerdirection],Playerx+frameshift,Playery)
        for s in slist:
            s.update()
        for e in enemlist:
            e.update()
        for b in bulletlist:
            b.update()
        PicoBoy.Fill_Rect(0+frameshift,217,240,8,(175,175,175))
        PicoBoy.Create_Text("Score: "+str(score),240-((len("Score: "+str(score))+1)*8)+frameshift,229,(255,255,255))
        PicoBoy.Create_Text("Time: "+str(time-timeg),8+frameshift,229,(255,255,255))
        PicoBoy.Create_Text(str(lives),231-int(((len(str(lives))*8)/2))+frameshift,6,(255,255,255))
        if PicoBoy.Button("Start"):
            MusicBox.Stop_Song()
            PicoBoy.Pause_Screen()
            MusicBox.Play_Song(currentsong)
        PicoBoy.Update()
        if time-timeg<0:
            return True
        if lives<=0:
            return False
        if frameshift>0:
            frameshift-=1
      
      
blocsl=[]
blocsr=[]
for i in range(randint(6,8)):
    while True:
        c=(randint(5,48),randint(55,188))
        cont=True
        for f in blocsl:
            if PicoBoy.Check_Collision(c[0],c[1],17,17,f[0],f[1],17,17,1,1):
                cont=False
        if cont:
            break
    blocsl.append(c)
for i in range(randint(6,8)):
    while True:
        c=(randint(168,221),randint(55,188))
        cont=True
        for f in blocsr:
            if PicoBoy.Check_Collision(c[0],c[1],17,17,f[0],f[1],17,17,1,1):
                cont=False
        if cont:
            break
    blocsr.append(c)
MusicBox.Play_Song("main_title.pbs")
now = ticks_ms()
while True:
    PicoBoy.Fill_Screen((48,48,48))
    for s in starcoords:
        PicoBoy.vline(int(s[0]*1.2),int(s[1]*1.2-20),1,PicoBoy.color(255,255,255))
    for c in blocsl:
        PicoBoy.Render_Sprite(bulletsprite,c[0],c[1])
    for c in blocsr:
        PicoBoy.Render_Sprite(bulletsprite,c[0],c[1])
    PicoBoy.Load_Small_Image("title.pbimg",23,20,194,25)
    PicoBoy.Load_Small_Image("Big Starship.pbimg",80,55,83,78)
    PicoBoy.Fill_Rect(80, 140, 5, 65, (255,255,255))
    PicoBoy.Fill_Rect(158, 140, 5, 65, (255,255,255))
    PicoBoy.Fill_Rect(100, 140, 5, 45, (255,255,255))
    PicoBoy.Fill_Rect(138, 140, 5, 45, (255,255,255))
    PicoBoy.Fill_Rect(119, 140, 5, 35, (255,255,255))
    PicoBoy.Fill_Rect(20,215,200,20,(0,255,0))
    PicoBoy.Fill_Rect(22,218,194,14,(0,0,0))
    if ticks_diff(ticks_ms(), now) > 200:
        now = ticks_ms()
        PicoBoy.Create_Text("HOLD A TO PLAY",-1,221,(255,255,255))
        PicoBoy.Update(noclear=True)
        while ticks_diff(ticks_ms(), now) < 200:
            sleep(0.020)
        now = ticks_ms()
    PicoBoy.Update(noclear=True)
    if PicoBoy.Button("Start"):
        PicoBoy.Show_Scores()
    elif PicoBoy.Button("A"):
        break
sleep(0.25)
while True:
    if new_level():
            score+=100
            MusicBox.Change_Mode(0)
            MusicBox.Stop_Song()
            MusicBox.Play_Song("level_clear.pbs")
            PicoBoy.fill(PicoBoy.color(48,48,48))
            for s in starcoords:
                PicoBoy.vline(int(s[0]*1.2),int(s[1]*1.2-20),1,PicoBoy.color(255,255,255))
            PicoBoy.Create_Text("Level Clear!",-1,20,(255,255,255))
            PicoBoy.Load_Small_Image("Big Starship.pbimg",80,45,83,78)
            PicoBoy.Create_Text("Press A to play",-1, 145, (255,255,255))
            PicoBoy.Create_Text("the next level",-1, 160, (255,255,255))
            PicoBoy.Create_Text("Press home to quit.", -1, 180, (255,255,255))
            PicoBoy.Create_Text("Level: "+str(level),-1,200,(255,255,255))
            PicoBoy.Create_Text("Score: "+str(score), -1, 217, (255,255,255))
            PicoBoy.Update(score,noclear=True)
            while True:
                PicoBoy.Update(score, noclear=True)
                if PicoBoy.Button("A"):
                    level+=1
                    break
    else:
        PicoBoy.Save_Score(score)
        MusicBox.Change_Mode(0)
        MusicBox.Stop_Song()
        MusicBox.Play_Song("game_over.pbs")
        PicoBoy.fill(PicoBoy.color(48,48,48))
        for s in starcoords:
            PicoBoy.vline(int(s[0]*1.2),int(s[1]*1.2-20),1,PicoBoy.color(255,255,255))
        PicoBoy.Create_Text("Game Over",-1,20,(255,255,255))
        PicoBoy.Load_Small_Image("Big Starship.pbimg",80,45,83,78)
        for i in range(5):
            PicoBoy.Line(70,40-i,173,128-i,(255,0,0))
        for i in range(5):
            PicoBoy.Line(173,40-i,70,128-i,(255,0,0))
        PicoBoy.Create_Text("Press A to play again.", -1, 145, (255,255,255))
        PicoBoy.Create_Text("Press home to quit.", -1, 160, (255,255,255))
        PicoBoy.Create_Text("Press start", -1, 175, (255,255,255))
        PicoBoy.Create_Text("to view scores.", -1, 190, (255,255,255))
        PicoBoy.Create_Text("Level: "+str(level), -1, 205, (255,255,255))
        PicoBoy.Create_Text("Score: "+str(score), -1, 217, (255,255,255))
        PicoBoy.Update(noclear=True)
        while True:
            PicoBoy.Update(noclear=True)
            if PicoBoy.Button("Start"):
                PicoBoy.Show_Scores()
            elif PicoBoy.Button("A"):
                score=0
                level=1
                break
 