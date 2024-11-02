from PicoBoySDK import PicoBoySDK
from random import randint
from time import sleep
from math import sqrt

PicoBoy=PicoBoySDK(namespace="Pathfinder Demo", tick_time=0)
score=0
level=1



class finder:
    def __init__(self, currentposition, direction, parent=None, path=None):
        self.listofobjs=[]
        self.currentposition=currentposition
        self.direction=direction
        self.parent=parent
        if not path==None:
            self.path=path
        else:
            self.path=[]
        
    def update(self):
        global positions, totalobjs, coveredpositions, goalloc, finalpath, playerloc
        self.path.append(self.currentposition)
        if self.currentposition==goalloc:
            finalpath=self.path[:]
            return -1
        PicoBoy.Fill_Rect(self.currentposition[0]*16,self.currentposition[1]*16,16,16,(0,255,255))
        PicoBoy.Update(noclear=True)
        coveredpositions.append(self.currentposition)
        if not (self.currentposition[0]-1,self.currentposition[1]) in positions and not (self.currentposition[0])-1 < 0:
            if not self.direction == 1 and not ((self.currentposition[0])-1,self.currentposition[1]) in coveredpositions:
                self.listofobjs.append(finder(((self.currentposition[0]-1),self.currentposition[1]),0, self, self.path[:]))
                
        if not (self.currentposition[0]+1,self.currentposition[1]) in positions and not (self.currentposition[0])+1 > 14:
            if not self.direction == 0 and not (self.currentposition[0]+1,self.currentposition[1]) in coveredpositions:
                self.listofobjs.append(finder(((self.currentposition[0]+1),self.currentposition[1]),1, self, self.path[:]))
                
        if not (self.currentposition[0],self.currentposition[1]-1) in positions and not (self.currentposition[1])-1 < 0:
            if not self.direction == 3 and not (self.currentposition[0],self.currentposition[1]-1) in coveredpositions:
                self.listofobjs.append(finder((self.currentposition[0],(self.currentposition[1]-1)), 2, self, self.path[:]))
                
        if not (self.currentposition[0],self.currentposition[1]+1) in positions and not (self.currentposition[1]+1) > 14:
            if not self.direction == 2 and not (self.currentposition[0],self.currentposition[1]+1) in coveredpositions:
                self.listofobjs.append(finder((self.currentposition[0],(self.currentposition[1]+1)),3, self, self.path[:]))
        if self.listofobjs==[]:
            try:
                totalobjs.remove(self)
            except:
                ""
            del self
            return 0
        for obj in self.listofobjs:
            totalobjs.append(obj)
        try:
            totalobjs.remove(self)
        except:
            ""
        del self
        return 1
        

def minefield():
    global positions, totalobjs, coveredpositions, goalloc, finalpath, playerloc
    positions=[]
    totalobjs=[]
    coveredpositions=[]
    finalpath=[]
    playerloc=(randint(0,14),randint(0,14))
    badsprt=PicoBoy.Load_Sprite("mine.sprt",16,16)
    goodsprite=PicoBoy.Load_Sprite("flag.sprt",16,16)
    psprite=PicoBoy.Load_Sprite("detector.sprt",16,16)
    while True:
        goalloc=(randint(0,14),randint(0,14))
        if sqrt((goalloc[0]-playerloc[0])**2 + (goalloc[1]-playerloc[1])**2) > 3:
            break
    lastdirection=0
    for i in range(112+(2*level)):
        while True:
            pos=(randint(0,14),randint(0,14))
            if not pos==playerloc and not pos==goalloc:
                positions.append(pos)
                break
    check1=False
    PicoBoy.Fill_Screen((0,0,0))
    for pos in positions:
        PicoBoy.Render_Sprite(badsprt,pos[0]*16,pos[1]*16)
    PicoBoy.Render_Sprite(psprite,playerloc[0]*16,playerloc[1]*16)
    PicoBoy.Render_Sprite(goodsprite,goalloc[0]*16,goalloc[1]*16)
    PicoBoy.Update(noclear=True)
    pathfinder=finder(playerloc[:],5).update()
    while True:
        PicoBoy.Fill_Screen((0,0,0))
        for pos in positions:
            PicoBoy.Render_Sprite(badsprt,pos[0]*16,pos[1]*16)
        PicoBoy.Render_Sprite(psprite,playerloc[0]*16,playerloc[1]*16)
        PicoBoy.Render_Sprite(goodsprite,goalloc[0]*16,goalloc[1]*16)

        for obj in totalobjs:
            state=obj.update()
            if state==0:
                try:
                    totalobjs.remove(obj)
                except:
                    ""
            elif state==-1:
                for obj in totalobjs:
                    totalobjs.remove(obj)
                try:
                    del pathfinder
                except:
                    ""
                PicoBoy.Fill_Screen((0,0,0))
                for pos in positions:
                    PicoBoy.Render_Sprite(badsprt,pos[0]*16,pos[1]*16)
                PicoBoy.Render_Sprite(psprite,playerloc[0]*16,playerloc[1]*16)
                PicoBoy.Render_Sprite(goodsprite,goalloc[0]*16,goalloc[1]*16)
                for pos in coveredpositions:
                    PicoBoy.Fill_Rect(pos[0]*16,pos[1]*16,16,16,(0,255,0))
                PicoBoy.Update(noclear=True)
                for p in finalpath:
                    PicoBoy.Fill_Rect(p[0]*16,p[1]*16,16,16,(0,0,255))
                    PicoBoy.Update(noclear=True)
                for pos in positions:
                    PicoBoy.Render_Sprite(badsprt,pos[0]*16,pos[1]*16)
                PicoBoy.Render_Sprite(psprite,playerloc[0]*16,playerloc[1]*16)
                PicoBoy.Render_Sprite(goodsprite,goalloc[0]*16,goalloc[1]*16)
                PicoBoy.Update(noclear=True)
                print("Found Solution!")
                return

        if len(totalobjs)==0 and not check1:
            check1=True
        elif len(totalobjs)==0 and check1:
            print("No Solution!")
            for pos in coveredpositions:
                PicoBoy.Fill_Rect(pos[0]*16,pos[1]*16,16,16,(255,0,0))
            PicoBoy.Update(noclear=True)
            del pathfinder
            for obj in totalobjs:
                totalobjs.remove(obj)
            return
        else:
            check1=False
        #PicoBoy.Update(noclear=True)


        

PicoBoy.Fill_Screen((0,0,0))
PicoBoy.Create_Text("Press A to begin.", -1, -1, (255,255,255))
while True:

    if PicoBoy.Button("A"):
        minefield()
    PicoBoy.Update(noclear=True)

