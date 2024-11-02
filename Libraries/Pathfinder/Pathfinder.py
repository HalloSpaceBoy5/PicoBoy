

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

    
class Pathfinder:

        
    def Pathfind(locationz, startt, endd):
        global locations, start, end, coveredpositions, totalobjs
        locations=locationz
        start=startt
        end=endd

        totalobjs=[]
        coveredpositions=[]
        check1=False
        pathfinder=finder(start,5).update()
        while True:

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
                    print("Found Solution!")
                    return finalpath
            if len(totalobjs)==0 and not check1:
                check1=True
            elif len(totalobjs)==0 and check1:
                print("No Solution!")
                del pathfinder
                for obj in totalobjs:
                    totalobjs.remove(obj)
                return
            else:
                check1=False

    