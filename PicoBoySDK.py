# Original Software Development Kit by HalloSpaceBoy
# Code used from MikeDev and Vincient Mistler
from machine import Pin, PWM, SPI, reset
import framebuf
from framebuf import FrameBuffer, RGB565
from time import sleep
from utime import sleep_ms
import sys
from os import rename, chdir, listdir
from _thread import start_new_thread

collided=False

SWRESET   = b'\x01'
TEOFF     = b'\x34'
TEON      = b'\x35'
MADCTL    = b'\x36'
COLMOD    = b'\x3A'
GCTRL     = b'\xB7'
VCOMS     = b'\xBB'
LCMCTRL   = b'\xC0'
VDVVRHEN  = b'\xC2'
VRHS      = b'\xC3'
VDVS      = b'\xC4'
FRCTRL2   = b'\xC6'
PWCTRL1   = b'\xD0'
PORCTRL   = b'\xB2'
GMCTRP1   = b'\xE0'
GMCTRN1   = b'\xE1'
INVOFF    = b'\x20'
SLPOUT    = b'\x11'
DISPON    = b'\x29'
GAMSET    = b'\x26'
DISPOFF   = b'\x28'
RAMWR     = b'\x2C'
INVON     = b'\x21'
CASET     = b'\x2A'
RASET     = b'\x2B'
PWMFRSEL  = b'\xCC'


class ST7789(framebuf.FrameBuffer):
    def __init__(self, width=240, height=240, id_=0, sck=18, mosi=19,
                 dc=20, rst=21, cs=17, bl=22, baudrate=62500000):
        self.width = width
        self.height = height
        self.spi = SPI(id_, sck=Pin(sck), mosi=Pin(mosi), baudrate=baudrate, polarity=0, phase=0)
        self.dc = Pin(dc, Pin.OUT)
        self.rst = Pin(rst, Pin.OUT)
        self.cs = Pin(cs, Pin.OUT)
        self.bl = PWM(Pin(bl, Pin.OUT))
        self.PWM_FREQUENCY = 1000  
        self.DUTY_CYCLE_MIN = 10000
        self.DUTY_CYCLE=45000
        self.DUTY_CYCLE_MAX = 65000
        self.buffer = memoryview(bytearray(self.height * self.width * 2))
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()
    def write_cmd(self, cmd=None, data=None):
        self.cs(0)
        if cmd:
            self.dc(0) 
            self.spi.write(cmd)
        if data:
            self.dc(1)
            self.spi.write(data)
        self.cs(1)

    def init_display(self):
        self.rst.value(1)
        sleep(0.150)
        self.rst.value(0)
        sleep(0.150)
        self.rst.value(1)
        sleep(0.150)
        self.bl.duty_u16(0)
        self.write_cmd(SWRESET)
        sleep(0.150)
        self.write_cmd(TEON) 
        self.write_cmd(COLMOD, b'\x05')
        self.write_cmd(PORCTRL, b'\x0c\x0c\x00\x33\x33')
        self.write_cmd(GCTRL, b'\x14')
        self.write_cmd(VCOMS, b'\x37')
        self.write_cmd(LCMCTRL, b'\x2c')
        self.write_cmd(VDVVRHEN, b'\x01')
        self.write_cmd(VRHS, b'\x12')
        self.write_cmd(VDVS, b'\x20')
        self.write_cmd(PWCTRL1, b'\xa4\xa1')
        self.write_cmd(FRCTRL2, b'\x0f')
        self.write_cmd(GMCTRP1, b'\xD0\x04\x0D\x11\x13\x2B\x3F\x54\x4C\x18\x0D\x0B\x1F\x23')
        self.write_cmd(GMCTRN1, b'\xD0\x04\x0C\x11\x13\x2C\x3F\x44\x51\x2F\x1F\x1F\x20\x23')
        self.write_cmd(INVON) 
        self.write_cmd(SLPOUT) 
        self.write_cmd(DISPON)  
        sleep(0.1)
        self.write_cmd(CASET, b'\x00\x00\x00\xF0')
        self.write_cmd(RASET, b'\x00\x00\x00\xF0')
        self.write_cmd(MADCTL, b'\x04')
        
        self.fill(0)
        self.show_screen()
        sleep(0.050)
        try:
            with open("/brghtness.conf", "r") as r:
                self.DUTY_CYCLE=int(r.read())
        except:
            "no brightness config file"
        self.bl.duty_u16(self.DUTY_CYCLE)
    
    def decrease_brightness(self):
        if self.DUTY_CYCLE > self.DUTY_CYCLE_MIN:
            self.DUTY_CYCLE -= 5000
        self.bl.duty_u16(self.DUTY_CYCLE)
        with open("/brghtness.conf", "w") as w:
            w.write(str(self.DUTY_CYCLE))

    def increase_brightness(self):
        if self.DUTY_CYCLE < self.DUTY_CYCLE_MAX:
            self.DUTY_CYCLE += 5000
        self.bl.duty_u16(self.DUTY_CYCLE)
        with open("/brghtness.conf", "w") as w:
            w.write(str(self.DUTY_CYCLE))
    
    def power_off(self):
        pass

    def power_on(self):
        pass

    def contrast(self, contrast):
        pass

    def invert(self, invert):
        pass

    def rotate(self, rotate):
        pass

    def show_screen(self):
        self.write_cmd(RAMWR, self.buffer)
        
    def colorc(self,rgb565):
        lsb = (rgb565 & 0b0000000011111111)<<8
        msb = (rgb565 & 0b1111111100000000)>>8
        rgb565=(lsb | msb)
        red5 = rgb565 >> 11
        green6 = (rgb565 >> 5) & 0b111111
        blue5 = rgb565 & 0b11111
        red8 = round(red5 / 31 * 255)
        green8 = round(green6 / 63 * 255)
        blue8 = round(blue5 / 31 * 255)
        return (red8, green8, blue8)
    
    def color(self,r, g, b):
        r5 = (r & 0b11111000) >> 3
        g6 = (g & 0b11111100) >> 2
        b5 = (b & 0b11111000) >> 3
        rgb565 = (r5 << 11) | (g6 << 5) | b5
        lsb = (rgb565 & 0b0000000011111111)
        msb = (rgb565 & 0b1111111100000000) >> 8
        
        return ((lsb << 8) | msb)
    
    def Load_Image(self,filename):
        open(filename, "rb").readinto(self.buffer)
        
    def Get_Pixel_Color(self, x, y):
        x-=1
        y-=1
        byte1=self.buffer[2*(y*self.width+x)];
        byte2=self.buffer[2*(y*self.width+x)+1];
        return self.colorc(byte2*256+byte1)

class PicoBoySDK(ST7789):
    def __init__(self,namespace=None,tick_time=0.025):
        error=""
        if not namespace:
            error="PicoBoySDK Error: Namespace missing"
        try:
            if not error=="":
                raise
            try:
                chdir("/"+namespace)
            except:
                error="PicoBoySDK Error: Namespace invalid"
            if not error=="":
                raise
            if not "title.py" in listdir("/"):
                raise
            rename("/main.py","/"+namespace+"/"+namespace+".py")
            rename("/title.py","/main.py")
            self.mode=True
        except:
            if error=="":
                print("Starting in developer mode.")
                self.mode=False
            else:
                print(error)
                sys.exit()
        
        self.namespace=namespace
        self.tick=tick_time
        self.up = Pin(2, Pin.IN, Pin.PULL_UP)
        self.down = Pin(3, Pin.IN, Pin.PULL_UP)
        self.left = Pin(4, Pin.IN, Pin.PULL_UP)
        self.right = Pin(5, Pin.IN, Pin.PULL_UP)
        self.A = Pin(6, Pin.IN, Pin.PULL_UP)
        self.B = Pin(7, Pin.IN, Pin.PULL_UP)
        self.home = Pin(8, Pin.IN, Pin.PULL_UP)
        self.select = Pin(9, Pin.IN, Pin.PULL_UP)
        self.start = Pin(10, Pin.IN, Pin.PULL_UP)
        self.spk_channel1 = PWM(Pin(12))
        self.spk_channel2 = PWM(Pin(13))
        self.spk_channel3 = PWM(Pin(14))
        self.spk_channel4 = PWM(Pin(15))
        super().__init__(width=240, height=240, id_=0, sck=18, mosi=19,
                         dc=20, rst=21, cs=17, bl=22, baudrate=62500000)
        self.sprites=[] 
        
    def Load_Sprite(self,filename,width,height):
        with open(filename,"rb") as read:
            sprite = FrameBuffer(bytearray(read.read()), width, height, RGB565)
        return sprite
    
    def Render_Sprite(self, sprite, x, y):
        self.blit(sprite, x, y)
    
    def Update(self):
        if self.home.value()==0:
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            self.fill(self.color(0,0,0))
            self.show_screen()
            reset()
        self.show_screen()
        if self.Button("Up") and self.Button("Select"):
            self.increase_brightness()
        if self.Button("Down") and self.Button("Select"):
            self.decrease_brightness()
        sleep(self.tick)
            
    def Button(self, button):
        if button=="Any":
            if self.up.value()==0:
                return True
            elif self.down.value()==0:
                return True
            elif self.left.value()==0:
                return True
            elif self.right.value()==0:
                return True
            elif self.A.value()==0:
                return True
            elif self.B.value()==0:
                return True
            elif self.select.value()==0:
                return True
            elif self.start.value()==0:
                return True
            else:
                return False
        else:
            if button=="Up" and self.up.value()==0:
                return True
            elif button=="Down" and self.down.value()==0:
                return True
            elif button=="Left" and self.left.value()==0:
                return True
            elif button=="Right" and self.right.value()==0:
                return True
            elif button=="A" and self.A.value()==0:
                return True
            elif button=="B" and self.B.value()==0:
                return True
            elif button=="Select" and self.select.value()==0:
                return True
            elif button=="Start" and self.start.value()==0:
                return True
            else:
                return False
        
    def Outline_Rect(self, x, y, width, height, color):
        if not 'tuple' in str(type(color)):
            print("Outline_Rect() color must be a tuple!")
            sys.exit()
        self.rect(x,y,width,height,self.color(*color))
        
    def Fill_Rect(self, x, y, width, height, color):
        if not 'tuple' in str(type(color)):
            print("Fill_Rect() color must be a tuple!")
            sys.exit()
        self.fill_rect(x,y,width,height,self.color(*color))

    def Fill_Screen(self,color):
        self.fill(self.color(*color))

    def Play_Sound(self, freq, channel=1, duty_u16 = 2000):
        if channel==1:
            if freq>0:
                self.spk_channel1.freq(freq)
                self.spk_channel1.duty_u16(duty_u16)
            else:
                self.spk_channel1.duty_u16(0)
        if channel==2:
            if freq>0:
                self.spk_channel2.freq(freq)
                self.spk_channel2.duty_u16(duty_u16)
            else:
                self.spk_channel2.duty_u16(0)
        if channel==3:
            if freq>0:
                self.spk_channel3.freq(freq)
                self.spk_channel3.duty_u16(duty_u16)
            else:
                self.spk_channel3.duty_u16(0)
        if channel==4:
            if freq>0:
                self.spk_channel4.freq(freq)
                self.spk_channel4.duty_u16(duty_u16)
            else:
                self.spk_channel4.duty_u16(0)

    def Create_Text(self, s,x=-1,y=-1, c = (255,255,255)):
        if x==-1:
            x = int(self.width/2)- int(len(s)/2 * 8)
        if y==-1:
            y = int(self.height/2) - 8
        self.text(s, x, y, self.color(*c))
        
    def Check_Collision(self,x,y,width,height,x2,y2,width2,height2,speed,mode):
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

class PlayerObject:
    def __init__(self,parent,initx,inity,width,height,sprite,speed):
        if not "PicoBoySDK" in str(type(parent)):
            print("PicoBoySDK Error: The PicoBoySDK object is missing or invalid in "+str(self))
            sys.exit()
        self.initx=initx
        self.inity=inity
        self.x=initx
        self.y=inity
        self.width=width
        self.height=height
        self.sprite=sprite
        self.speed=speed
        self.parent=parent
        self.direction="XY"
        
    def Update(self):
        if self.parent.Button("Up") and self.y>0 and "Y" in self.direction:
            self.y-=self.speed
        if self.parent.Button("Down") and self.y<240-self.width and "Y" in self.direction:
            self.y+=self.speed
        if self.parent.Button("Left") and self.x>0 and "X" in self.direction:
            self.x-=self.speed
        if self.parent.Button("Right") and self.x<240-self.width and "X" in self.direction:
            self.x+=self.speed
        self.parent.Render_Sprite(self.sprite,self.x,self.y)
        
        
    def MoveTo(self, x, y):
        self.x=x
        self.y=y
        
class MusicBoxObject:
    def __init__(self,parent,mode):
        if not "PicoBoySDK" in str(type(parent)):
            print("PicoBoySDK Error: The PicoBoySDK object is missing or invalid in "+str(self))
            exit()
        self.parent=parent
        self.song=[]
        self.ch_a_0 = self.parent.spk_channel1
        self.ch_a_1 = self.parent.spk_channel2
        self.ch_b_0 = self.parent.spk_channel3
        self.ch_b_1 = self.parent.spk_channel4
        self.opcode=0x00
        self.mode=mode
        self.savedindex=0
        self.tmp=[]
        self.isReading=False
        self.savedsong=[]
        self.index=0
        
    def Initialize(self):
        self.thread=start_new_thread(self.Play,())
            
    def _pitch(self, freq):
        return (2**((freq-69)/12))*440

    def _duty_cycle(self, percent):
        return round((percent/100)*65535)
    
    def play_note(self, note, channel, duty):
        if channel == "a0":
            self.ch_a_0.freq(round(self._pitch(note)))
            self.ch_a_0.duty_u16(self._duty_cycle(duty))
        elif channel == "a1":
            self.ch_a_1.freq(round(self._pitch(note)))
            self.ch_a_1.duty_u16(self._duty_cycle(duty))
        elif channel == "b0":
            self.ch_b_0.freq(round(self._pitch(note)))
            self.ch_b_0.duty_u16(self._duty_cycle(duty))
        elif channel == "b1":
            self.ch_b_1.freq(round(self._pitch(note)))
            self.ch_b_1.duty_u16(self._duty_cycle(duty))

    def stop_channel(self, channel):
        if channel == "a0":
            self.ch_a_0.duty_u16(0)
        elif channel == "a1":
            self.ch_a_1.duty_u16(0)
        elif channel == "b0":
            self.ch_b_0.duty_u16(0)
        elif channel == "b1":
            self.ch_b_1.duty_u16(0)

    def Play_Song(self, song):
        if not type(song)==list:
            print("PicoBoySDK Error: The song provided is improperly formatted")
            sys.exit()
        self.tmp=[]
        self.isReading=False
        self.opcode=0x00
        self.index=0
        self.song=song
        
    def Stop_Song(self):
        self.song=[]
        self.tmp=[]
        self.isReading=False
        self.opcode=0x00
        self.index=0
        
    
    def Play(self):
        self.tmp = []
        self.index = 0
        self.isReading = False
        self.opcode = 0x00
        while True:
            if self.index >= len(self.song):
                if self.mode==True:
                    self.index=0
                    sleep(0.01)
                else:
                    sleep(0.01)
            try:
                if self.song[self.index] in (0x90, 0x91, 0x92, 0x93, 0x80, 0x81, 0x82, 0x83, 0xf0, 0xe0):
                    self.opcode = self.song[self.index]
                    self.isReading = True
                    self.tmp = []
                    self.tmp_index = 1
                    while self.isReading: 
                        if (self.index + self.tmp_index) >= len(self.song):
                            break
                        else:
                            if not self.song[self.index + self.tmp_index] in (0x90, 0x91, 0x92, 0x93, 0x80, 0x81, 0x82, 0x83, 0xf0, 0xe0):
                                self.tmp.append(self.song[self.index + self.tmp_index])
                                self.tmp_index += 1
                            else:
                                self.isReading = False
                    if self.opcode in (0x90, 0x91, 0x92, 0x93):
                        if len(self.tmp) > 0:
                            if self.opcode == 0x90:
                                self.play_note(self.tmp[0], "a0", 50)
                            elif self.opcode == 0x91:
                                self.play_note(self.tmp[0], "b0", 50)
                            elif self.opcode == 0x92:
                                self.play_note(self.tmp[0], "a1", 50)
                            elif self.opcode == 0x93:
                                self.play_note(self.tmp[0], "b1", 50)
                            if len(self.tmp) == 3:
                                delay = ((self.tmp[1]*256)+(self.tmp[2]))
                                sleep_ms(delay)
                        self.index += 1
                        
                    elif self.opcode in (0x80, 0x81, 0x82, 0x83):
                        if self.opcode == 0x80:
                            self.stop_channel("a0")
                        elif self.opcode == 0x81:
                            self.stop_channel("b0")
                        elif self.opcode == 0x82:
                            self.stop_channel("a1")
                        elif self.opcode == 0x83:
                            self.stop_channel("b1")
                            
                        if len(self.tmp) >= 2:
                            delay = ((self.tmp[0]*256)+(self.tmp[1]))
                            sleep_ms(delay)
                        self.index += 1
                        
                    elif self.opcode in (0xf0, 0xe0):
                        if self.mode: 
                            self.index = 0
                else:
                    self.index += 1
            except:
                self.ch_a_0.duty_u16(0)
                self.ch_a_1.duty_u16(0)
                self.ch_b_0.duty_u16(0)
                self.ch_b_1.duty_u16(0)


    

