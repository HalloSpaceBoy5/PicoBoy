from framebuf import FrameBuffer,RGB565
from time import sleep
class Functions:
    def __init__(self, pgb, ttcolor, ottcolor, ic):
        self.pgb=pgb
        self.ttcolor=ttcolor
        self.ic=ic
        self.ottcolor=ottcolor
        
    
    def readchunk(self, filename, x2, y2, w, h, q=True):
        if x2>240:
            sleep(0.015)
            return
        buffersize=w*2
        p=240-w-x2
        if p<0:
            e=abs(240-x2)
            buffersize=e*2
        if p<0:
            p=abs(p)
        else:
            p=0
        x=bytearray(p*2)
        total_line_size = buffersize + p*2
        size = h * total_line_size
        with open(filename, "rb") as image_file:
            for y in range(h):
                existing_line_start = ((y + y2) * 240 + x2) * 2
                image_file.readinto(self.pgb.buffer[existing_line_start:existing_line_start + buffersize])
                image_file.readinto(x[0:p*2])

        if not size==28800 and q:
            self.pgb.fill_rect(x2,y2,w,h,self.ttcolor)
            unit=int((len(self.ic)/2)*12)
            for i,j in enumerate(self.ic):
                j=j.replace("\r","")
                self.pgb.create_text(j,x2+(60-(len(j)*4)),y2+(60-unit)+(i*12),self.ottcolor)
            sleep(0.01)
            return


    def readchunk_mask(self, filename,x2,y2,w,h,cmask=57351):
        with open(filename,"rb") as r:
                for x in range(h):
                    tempfb=FrameBuffer(bytearray(r.read(2*w)),w,1,RGB565)
                    self.pgb.blit(tempfb,x2,y2+x,cmask)
                    del tempfb

    def draw_image(self, imagedata,ts=-1):
        ps=int(240/len(imagedata))
        y=-1
        for i in imagedata:
            y+=1
            x=-1
            if not ts==-1:
                if ts==0:
                    skip=True
                elif y in range(0,ts):
                    skip=True
                else:
                    skip=False
            else:
                skip=False
            if not skip:
                for f in i:
                    x+=1
                    self.pgb.fill_rect(x*ps,y*ps,ps,ps,f)
        sleep(0.1)

    def getimagedata(self, bgimagefile):
        imagedata=[]
        with open(bgimagefile) as f:
            for i in range(30):
                comp=[]
                for x in f.readline().split(":"):
                    comp.append(int(x))
                imagedata.append(comp)
        del comp
        del f
        return imagedata
    


