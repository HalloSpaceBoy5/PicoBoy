from PicoBoySDK import PicoBoySDK
from random import choice, randint
from gc import mem_free
from time import sleep
from heapq import heappop, heappush
from math import sqrt, floor


PicoBoy=PicoBoySDK("Pac Man", tick_time=0.01)
WHITE=PicoBoy.color(255,255,255)
BLACK=PicoBoy.color(0,0,0)


    




class Ghost:
    def __init__(self, ai, sprite):
        self.ai=ai
        self.sprite=sprite
        self.relx=7
        self.rely=10
        self.x=112
        self.y=160
        self.panicked=False
        self.scatter=True
        self.speed=4
        self.dead=False
        self.currentpath=[]
        self.moved=0
        self.nextposition=[7,10]
        self.direction=-1
        self.amnttomove=0
        self.lastdirection=-1
        self.counter=0
        self.respawn=True
        if ai==0:
            self.badcoords=((1,1),(1,2),(1,3),(1,4),(2,1),(2,4),(3,1),(3,4),(4,1),(4,4),(5,1),(5,4),(6,1),(6,2),(6,3),(6,4))
        if ai==1:
            self.badcoords=((8,1),(8,2),(8,3),(8,4),(9,1),(9,4),(10,1),(10,4),(11,1),(11,4),(12,1),(12,4),(13,1),(13,2),(13,3),(13,4))
        if ai==2:
            self.badcoords=((1,8),(2,8),(3,8),(4,8),(1,9),(4,9),(1,10),(4,10),(1,11),(4,11),(1,12),(2,12),(3,12),(4,12))
        if ai==3:
            self.badcoords=((10,8),(11,8),(12,8),(13,8),(10,9),(13,9),(10,10),(13,10),(10,11),(13,11),(10,12),(11,12),(12,12),(13,12))
        
    def update(self):
        nogo=False
        self.counter+=1
        if self.counter%150==0 and not self.scatter:
            self.scatter=True
            self.counter=0
        elif self.counter%100==0 and self.scatter:
            self.scatter=False
            self.counter=0
        if self.currentpath==[]:
            if (self.panicked) or (self.scatter):
                target=choice(self.badcoords)
            elif not [self.relx, self.rely]==player.pos:
                if self.ai==0:
                    #Blinky
                    target=player.pos[:]
                    while target[0]<0:
                        target[0]+=1
                    while target[0]>14:
                        target[0]-=1
                    target=tuple(target)
                elif self.ai==1:
                    #Pinky
                    if player.direction==0 or player.direction==-1:
                            target=(player.pos[0], player.pos[1]-2)
                    elif player.direction==1:
                            target=(player.pos[0], player.pos[1]+2)
                    elif player.direction==2:
                            target=(player.pos[0]-2, player.pos[1])
                    elif player.direction==3:
                            target=(player.pos[0]+2, player.pos[1])
                    if not target in positions:
                        target=tuple(player.pos)
                elif self.ai==2:
                    # Clyde
                    loc=[]
                    for f in range(player.pos[0]-4, player.pos[0]+4):
                        for i in range(player.pos[1]-4, player.pos[1]+4):
                            if (f,i) in positions:
                                loc.append((f,i))
                    target=choice(loc)
                elif self.ai==3:
                    if player.direction==0 or player.direction==-1:
                            target=(player.pos[0]-3, player.pos[1]+3)
                    elif player.direction==1:
                            target=(player.pos[0]+3, player.pos[1]-3)
                    elif player.direction==2:
                            target=(player.pos[0]-3, player.pos[1]-3)
                    elif player.direction==3:
                            target=(player.pos[0]+3, player.pos[1]+3)
                    if not target in positions:
                        target=tuple(player.pos)
            else:
                nogo=True
            
            if not nogo:
                if self.respawn:
                    self.relx=7
                    self.rely=10
                    self.x=112
                    self.y=160
                    temppositions=list(positions[:])+[(7,9),(7,8)]
                    for i in ((0,6),(14,6),(-1,6),(15,6)):
                        temppositions.remove(i)
                    self.respawn=False
                else:
                    temppositions=list(positions[:])
                    for i in ((0,6),(14,6),(-1,6),(15,6)):
                        temppositions.remove(i)
                if self.lastdirection==0 and (self.relx, self.rely+1) in positions:
                    temppositions.remove((self.relx, self.rely+1))
                if self.lastdirection==1 and (self.relx, self.rely-1) in positions:
                    temppositions.remove((self.relx, self.rely-1))
                if self.lastdirection==2 and (self.relx+1, self.rely) in positions:
                    temppositions.remove((self.relx+1, self.rely))
                if self.lastdirection==3 and (self.relx-1, self.rely) in positions:
                    temppositions.remove((self.relx-1, self.rely))
                print(self.scatter)
                self.currentpath=self.Find_Path(temppositions, (self.relx, self.rely), target)
                del temppositions
                try:
                    self.nextposition=self.currentpath.pop(0)
                    self.amnttomove=int(16/self.speed)
                    if self.rely>self.nextposition[1]:
                        self.direction=0
                    if self.rely<self.nextposition[1]:
                        self.direction=1
                    if self.relx>self.nextposition[0]:
                        self.direction=2
                    if self.relx<self.nextposition[0]:
                        self.direction=3
                except:
                    ""        
        if (self.relx, self.rely) == self.nextposition:
            if len(self.currentpath) > 0:
                self.nextposition = self.currentpath.pop(0)
            self.lastdirection=self.direction
            if self.rely>self.nextposition[1]:
                self.direction=0
            if self.rely<self.nextposition[1]:
                self.direction=1
            if self.relx>self.nextposition[0]:
                self.direction=2
            if self.relx<self.nextposition[0]:
                self.direction=3
            self.amnttomove=int(16/self.speed)
        if not (self.relx, self.rely) == self.nextposition:
            if not self.moved==self.amnttomove:
                if self.direction==0:
                    self.y-=self.speed
                elif self.direction==1:
                    self.y+=self.speed
                elif self.direction==2:
                    self.x-=self.speed
                elif self.direction==3:
                    self.x+=self.speed
                self.moved+=1
            if self.moved==self.amnttomove:
                self.moved=0
                if self.direction==0:
                    self.rely-=1
                elif self.direction==1:
                    self.rely+=1
                elif self.direction==2:
                    self.relx-=1
                elif self.direction==3:
                    self.relx+=1
        if self.moved==0 and not (self.relx, self.rely) == (self.x, self.y):
            self.x=self.relx*16
            self.y=self.rely*16
        """
        for l in self.currentpath:
            if self.ai==0:
                PicoBoy.Fill_Rect(l[0]*16+6,l[1]*16+6,4,4,(255,0,0))
            elif self.ai==1:
                PicoBoy.Fill_Rect(l[0]*16+6,l[1]*16+6,4,4,(255,0,200))
            elif self.ai==2:
                PicoBoy.Fill_Rect(l[0]*16+6,l[1]*16+6,4,4,(255,200,0))
            elif self.ai==3:
                PicoBoy.Fill_Rect(l[0]*16+6,l[1]*16+6,4,4,(0,0,255))
        """
        if not self.panicked:
            PicoBoy.Render_Sprite(self.sprite, self.x, self.y)
        else:
            PicoBoy.Render_Sprite(panickedsprite, self.x, self.y)
        
        
        

        
    def Find_Path(self, moveablelocs, start, end):
        def heuristic(a, b):
            # Manhattan distance
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        open_set = []
        heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, end)}
        
        while open_set:
            _, current = heappop(open_set)
            
            if current == end:
                return self.reconstruct_path(came_from, current)
            
            neighbors = [((current[0] - 1, current[1]), 0),
                         ((current[0] + 1, current[1]), 1),
                         ((current[0], current[1] - 1), 2),
                         ((current[0], current[1] + 1), 3)]
            
            for neighbor, direction in neighbors:
                if neighbor in moveablelocs:
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                        heappush(open_set, (f_score[neighbor], neighbor))
        
        return []

    def reconstruct_path(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path
        
def draw_pacman(x, y, d, m):
    PicoBoy.hline(x-8,y,8*2,PicoBoy.color(255,255,0))
    for i in range(1,8):
        a = int(sqrt(8*8-i*i))
        PicoBoy.hline(x-a,y+i,a*2,PicoBoy.color(255,255,0))
        PicoBoy.hline(x-a,y-i,a*2,PicoBoy.color(255,255,0))
        if d==3:
            for i in range(m):
                PicoBoy.line(x, y, x+8, y+(i+1), BLACK)
            for i in range(m):
                PicoBoy.line(x, y, x+8, y-(i+1), BLACK)
            PicoBoy.hline(x, y, 8, BLACK)
        elif d==2:
            for i in range(m):
                PicoBoy.line(x, y, x-8, y+(i+1), BLACK)
            for i in range(m):
                PicoBoy.line(x, y, x-8, y-(i+1), BLACK)
            PicoBoy.hline(x-8, y, 8, BLACK)
        elif d==1:
            for i in range(m):
                PicoBoy.line(x, y, x-(i+1), y+8, BLACK)
            for i in range(m):
                PicoBoy.line(x, y, x+(i+1), y+8, BLACK)
            PicoBoy.vline(x, y, 8, BLACK)
        elif d==0:
            for i in range(m):
                PicoBoy.line(x, y, x-(i+1), y-8, BLACK)
            for i in range(m):
                PicoBoy.line(x, y, x+(i+1), y-8, BLACK)
            PicoBoy.vline(x, y-8, 8, BLACK)
        else:
            if d==3:
                PicoBoy.hline(x, y, 8, BLACK)
            elif d==2:
                PicoBoy.hline(x-8, y, 8, BLACK)
            elif d==1:
                PicoBoy.vline(x, y, 8, BLACK)
            elif d==0:
                PicoBoy.vline(x, y-8, 8, BLACK)

class Player:
    def __init__(self):
        self.speed=4
        self.frames=16/self.speed
        self.d=False
        self.mouth=0
        self.nextpoint=[7,4]
        self.pos=[7,4]
        self.frac_pos=[112,64]
        self.direction=-1
        self.go=False
        
    def update(self):
        if self.go:
            if self.d:
                if self.mouth<=0:
                    self.d=not self.d
                    PicoBoy.Play_Sound(200)
                else:
                    self.mouth-=4
            else:
                if self.mouth>=4:
                    self.d=not self.d
                    PicoBoy.Play_Sound(100)
                else:
                    self.mouth+=4
        else:
            PicoBoy.Stop_Sound()
        justdeclared=False
        if [(self.frac_pos[0]/16),(self.frac_pos[1]/16)]==[int(self.frac_pos[0]/16),int(self.frac_pos[1]/16)]:
            if PicoBoy.Button("Up") and (self.pos[0],self.pos[1]-1) in positions:
                self.direction=0
                self.nextpoint=[self.pos[0],self.pos[1]-1]
                justdeclared=True
            elif PicoBoy.Button("Down") and (self.pos[0],self.pos[1]+1) in positions:
                self.direction=1
                self.nextpoint=[self.pos[0],self.pos[1]+1]
                justdeclared=True
            elif PicoBoy.Button("Left") and (self.pos[0]-1,self.pos[1]) in positions:
                self.direction=2
                self.nextpoint=[self.pos[0]-1,self.pos[1]]
                justdeclared=True
            elif PicoBoy.Button("Right") and (self.pos[0]+1,self.pos[1]) in positions:
                self.direction=3
                self.nextpoint=[self.pos[0]+1,self.pos[1]]
                justdeclared=True
        if not self.nextpoint==self.pos:
            self.go=True
            if self.direction==0:
                self.frac_pos[1]-=self.speed
            if self.direction==1:
                self.frac_pos[1]+=self.speed
            if self.direction==2:
                self.frac_pos[0]-=self.speed
            if self.direction==3:
                self.frac_pos[0]+=self.speed
        else:
            self.go=False
        if [(self.frac_pos[0]/16),(self.frac_pos[1]/16)]==self.nextpoint:
            self.pos=self.nextpoint[:]
            if not justdeclared:
                if self.direction==0 and (self.pos[0],self.pos[1]-1) in positions:
                    self.nextpoint=[self.pos[0],self.pos[1]-1]
                elif self.direction==1 and (self.pos[0],self.pos[1]+1) in positions:
                    self.nextpoint=[self.pos[0],self.pos[1]+1]
                elif self.direction==2 and (self.pos[0]-1,self.pos[1]) in positions:
                    self.nextpoint=[self.pos[0]-1,self.pos[1]]
                elif self.direction==3 and (self.pos[0]+1,self.pos[1]) in positions:
                    self.nextpoint=[self.pos[0]+1,self.pos[1]]
                elif self.direction==2 and self.pos[0]-1<0:
                    self.frac_pos[0]=240
                    self.pos[0]=15
                    self.nextpoint=[self.pos[0], self.pos[1]]
                elif self.direction==3 and self.pos[0]>14:
                    self.frac_pos[0]=-16
                    self.pos[0]=-1
                    self.nextpoint=[self.pos[0], self.pos[1]]
                else:
                    self.direction=-1
        draw_pacman(self.frac_pos[0]+7,self.frac_pos[1]+7,self.direction, self.mouth)

#find moveable areas
positions=[]
for i in range(13):
    for f in range(12):
        positions.append((i+1,f+1))
positions.append((0,6))
positions.append((14,6))
positions.append((-1,6))
positions.append((15,6))
nogo=((2,2),(2,3),(3,2),(3,3),(4,2),(4,3),(5,2),(5,3),(7,1),(7,2),(7,3),(9,2),(9,3),(10,2),(10,3),(11,2),(11,3),(12,2),(12,3),(2,5),(3,5),(5,5),(6,5),(7,5),(8,5),(9,5),(11,5),(12,5),(7,6),(2,7),(3,7),(4,7),(5,7),(7,7),(9,7),(10,7),(11,7),(12,7),(2,9),(3,9),(5,9),(6,9),(8,9),(9,9),(11,9),(12,9),(2,10),(3,10),(5,10),(9,10),(11,10),(12,10),(2,11),(3,11),(5,11),(6,11),(7,11),(8,11),(9,11),(11,11),(12,11),(7,9),(6,10),(7,10),(8,10))
for i in nogo:
    positions.remove(i)
positions=tuple(positions)

#init player
panickedsprite=PicoBoy.Load_Sprite("sprite_panicked.sprt",16,16)
player=Player()
clyde=Ghost(2, PicoBoy.Load_Sprite("sprite_clyde.sprt",16,16))
inky=Ghost(3, PicoBoy.Load_Sprite("sprite_inky.sprt",16,16))
blinky=Ghost(0, PicoBoy.Load_Sprite("sprite_blinky.sprt",16,16))
pinky=Ghost(1, PicoBoy.Load_Sprite("sprite_pinky.sprt",16,16))
while True:
    #print(mem_free())
    PicoBoy.Load_Image("pacmanbg.pbimg")
    #Player Stuff
    player.update()
    blinky.update()
    pinky.update()
    inky.update()
    clyde.update()
    PicoBoy.Update()
    
    
