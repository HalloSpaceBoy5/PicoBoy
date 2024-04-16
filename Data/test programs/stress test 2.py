from PicoGameBoy import PicoGameBoy
from random import randint
import machine
pgb=PicoGameBoy()
machine.freq(270000000)
boxlist=[]

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

class box:
    def __init__(self):
        self.x=randint(0,220)
        self.y=randint(0,210)
        self.speed=randint(1,3)
        self.speedx=1
        self.speedy=1
        self.color=PicoGameBoy.color(randint(10,255),randint(10,255),randint(10,255))
        
    def update(self):
        global boxlist
        if self.x>=220:
            self.speedx=-self.speed
        if self.x<=0:
            self.speedx=self.speed
        if self.y>=210:
            self.speedy=-self.speed
        if self.y<=0:
            self.speedy=self.speed
        for b in boxlist:
            if not b==self:
                result=Check_Collision(self.x, self.y, 20, 20, b.x, b.y, 20, 20, self.speed, 2)
                if not result[0]==0:
                    if result[0]<0:
                        self.speedx=-self.speed
                        b.speedx=b.speed
                    else:
                        self.speedx=self.speed
                        b.speedx=-b.speed
                if not result[1]==0:
                    if result[1]<0:
                        self.speedy=-self.speed
                        b.speedy=b.speed
                    else:
                        self.speedy=self.speed
                        b.speedy=-b.speed
                self.x+=result[0]
                self.y+=result[1]
                if self.x<0:
                    self.x=0
                if self.x>220:
                    self.x=220
                if self.y<0:
                    self.y=0
                if self.y>210:
                    self.y=210
                #b.x+=b.speedx
                #b.y+=b.speedy
        self.x+=self.speedx
        self.y+=self.speedy
        pgb.fill_rect(self.x,self.y,20,20,self.color)
        
        
for i in range(2):
    boxlist.append(box())
pin = machine.ADC(29) 
while True:
    if pgb.button_A():
        boxlist.append(box())
    if pgb.button_B() and len(boxlist)>=5:
        boxlist.pop()
    adc_reading  = pin.read_u16()
    adc_voltage  = (adc_reading * 3.3) / 65535
    vsys_voltage = adc_voltage * 12
    pgb.fill(PicoGameBoy.color(0,0,0))
    for b in boxlist:
        b.update()
    pgb.fill_rect(0,230,240,10,PicoGameBoy.color(100,100,100))
    pgb.create_text(f"VSYS Voltage: {str(round(vsys_voltage, 3))}",-1,231,PicoGameBoy.color(255,255,255))
    pgb.show()

