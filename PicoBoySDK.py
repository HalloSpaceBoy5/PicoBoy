# Original Software Development Kit by HalloSpaceBoy
# Code used from MikeDev and Vincient Mistler
from machine import Pin, PWM, SPI, reset, ADC
import framebuf
from framebuf import FrameBuffer, RGB565
from time import sleep
from utime import sleep_ms, ticks_ms, ticks_diff
from sys import implementation
from os import rename, chdir, listdir
from _thread import start_new_thread
from gc import collect
from array import array
from random import randint

mpyversion=implementation[1]
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
def colorc(rgb565):
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


class ST7789(framebuf.FrameBuffer):
    def __init__(self, width=240, height=240, id_=0, sck=18, mosi=19,
                 dc=20, rst=21, cs=17, bl=22, baudrate=62500000):
        self.width = width
        self.height = height
        self.spi = SPI(id_, sck=Pin(sck), mosi=Pin(mosi), baudrate=baudrate, polarity=0, phase=0)
        self.dc = Pin(dc, Pin.OUT)
        self.rst = Pin(rst, Pin.OUT)
        self.cs = Pin(cs, Pin.OUT)
        try:
            self.bl = PWM(Pin(bl, Pin.OUT),freq=1000,duty_u16=10000)
        except:
            self.bl = PWM(Pin(bl, Pin.OUT))
        self.PWM_FREQUENCY = 1000  
        self.DUTY_CYCLE_MIN = 10000
        self.DUTY_CYCLE=45000
        self.DUTY_CYCLE_MAX = 65000
        self.last_frame_time = ticks_ms()
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
            self.DUTY_CYCLE -= int((self.DUTY_CYCLE_MAX-self.DUTY_CYCLE_MIN)/20)
        if self.DUTY_CYCLE<self.DUTY_CYCLE_MIN:
            self.DUTY_CYCLE=self.DUTY_CYCLE_MIN
        self.bl.duty_u16(self.DUTY_CYCLE)
        try:
            with open("/brghtness.conf", "w") as w:
                w.write(str(self.DUTY_CYCLE))
        except:
            ""

    def increase_brightness(self):
        if self.DUTY_CYCLE < self.DUTY_CYCLE_MAX:
            self.DUTY_CYCLE += int((self.DUTY_CYCLE_MAX-self.DUTY_CYCLE_MIN)/20)
        if self.DUTY_CYCLE>self.DUTY_CYCLE_MAX:
            self.DUTY_CYCLE=self.DUTY_CYCLE_MAX
        self.bl.duty_u16(self.DUTY_CYCLE)
        try:
            with open("/brghtness.conf", "w") as w:
                w.write(str(self.DUTY_CYCLE))
        except:
            ""


    def show_screen(self):
        frame_time = 1000 // 60  # 16.67 ms per frame
        now = ticks_ms()
        elapsed = ticks_diff(now, self.last_frame_time)
        if elapsed < frame_time:
            sleep_ms(frame_time - elapsed)
        self.last_frame_time = ticks_ms()   
        self.write_cmd(RAMWR, self.buffer)

    
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
        return colorc(byte2*256+byte1)

class PicoBoySDK(ST7789):
    def __init__(self,namespace=None,tick_time=0.025):
        error=""
        if not namespace:
            error="PicoBoySDK Error: Namespace missing"
        if len(namespace)>18:
            error="PicoBoySDK Error: Namespace too long. The length should be at most 18 characters"
        try:
            if not error=="":
                raise
            try:
                chdir("/"+namespace)
            except:
                error="PicoBoySDK Error: Namespace invalid or Game not Installed"
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
                raise TypeError(error)
        try:
            with open("/langauge.conf") as r:
                self.langauge=int(r.read())
            if self.langauge>4:
                raise
        except:
            self.langauge=0
        self.maskcolor=self.color(31,17,9)
        self.namespace=namespace
        self.tick=tick_time
        self.cycle=1
        self.up = Pin(2, Pin.IN, Pin.PULL_UP)
        self.down = Pin(3, Pin.IN, Pin.PULL_UP)
        self.left = Pin(4, Pin.IN, Pin.PULL_UP)
        self.right = Pin(5, Pin.IN, Pin.PULL_UP)
        self.A = Pin(6, Pin.IN, Pin.PULL_UP)
        self.B = Pin(7, Pin.IN, Pin.PULL_UP)
        self.home = Pin(8, Pin.IN, Pin.PULL_UP)
        self.select = Pin(9, Pin.IN, Pin.PULL_UP)
        self.start = Pin(10, Pin.IN, Pin.PULL_UP)
        self.channels={
            "spk_channel1" : PWM(Pin(12)),
            "spk_channel2" : PWM(Pin(13)),
            "spk_channel3" : PWM(Pin(14)),
            "spk_channel4" : PWM(Pin(15))
            }

        collect()        
        super().__init__(width=240, height=240, id_=0, sck=18, mosi=19,
                         dc=20, rst=21, cs=17, bl=22, baudrate=62500000)
        self.sprites=[]
        self.vpin=ADC(29)
        self.audio_pwm_wrap=5000
        self.curve=1.8
        self.vol_max=100000
        self.vol_min=2500
        try:
            with open("/volume.conf", "r") as r:
                self.vol=int(r.read())
        except:
            self.vol=self.vol_max
        
    def Load_Library(self, libname, objects):
        try:
            rename("/libs/"+libname+"/"+libname+".py", "/"+libname+".py")
        except:
                try:
                    rename("/"+libname+".py","/libs/"+libname+"/"+libname+".py")
                except:
                    ""
                raise TypeError("PicoBoySDK Error: Library \""+libname+"\" nonexistent in filesystem at path \"/libs/"+libname+"/"+libname+".py\".")
                exit()
        chdir("/")
        try:
            exec("from "+libname+" import "+str(", ".join(objects)))
        except:
            try:
                rename("/"+libname+".py","/libs/"+libname+"/"+libname+".py")
            except:
                ""
            raise TypeError("PicoBoySDK Error: Could not import \""+str(", ".join(objects))+"\" from library \""+libname+"\".")
            exit()
        chdir("/"+self.namespace)
        rename("/"+libname+".py","/libs/"+libname+"/"+libname+".py")
        
    def Load_Sprite(self,filename,width,height):
        with open(filename,"rb") as read:
            sprite = FrameBuffer(bytearray(read.read()), width, height, RGB565)
        return sprite
    
    def Render_Sprite(self, sprite, x, y):
        self.blit(sprite, x, y, self.maskcolor)
    
 
                    
    def Load_Small_Image(self, filename, x2, y2, w, h):
        # Early exit if the image is out of bounds
        if x2 > 240 or x2 + w < 0 or y2 > 240 or y2 + h < 0:
            sleep(0.005)
            return
        # Figure out if clipping, if so, then on which sides of the screen
        wx, wy = 0, 0
        if 240-x2-w<0:
            wx = 1
        elif x2 < 0:
            wx = 2
        else:
            wx=0
        if y2 + h > 240:
            wy = 1
        elif y2 < 0:
            wy = 2
        else:
            wy=0
        #Find X clipping overlap
        p = 0  
        if x2 + w > 240:  
            p =  240-x2-w
        elif x2 < 0:  
            p = x2
            x2=0
        p=abs(p)
        #Find x buffer size according to the width minus the overlap
        buffersize = (w-p) * 2
        #Create a temp buffer to store the overlap from the .readinto function
        x = bytearray(p * 2)
        #Calculate y clip 
        ydiff = 0
        if wy == 2:
            ydiff = h - (h + y2)
        elif wy == 1:
            ydiff = (h + y2) - 240
        with open(filename, "rb") as image_file:
            #If the image is clipping on the left side, create a read offset of p*2
            if wx==2:
                image_file.readinto(x[0:p*2])
            for y in range(h):
                #Check if there is y clipping, if so then read that into the null buffer
                if (wy == 2 and y < ydiff) or (wy == 1 and y > h - ydiff):
                    image_file.readinto(bytearray(w * 2))
                    continue
                #Find the starting index
                existing_line_start = ((y + y2) * 240 + x2) * 2
                #Read the image file line into that index
                image_file.readinto(self.buffer[existing_line_start:existing_line_start + buffersize])
                #Discard any x overlap
                image_file.readinto(x[0:p*2])

                sleep(0.0005)






    def Update(self, savescore=None, noclear=False):
        if self.home.value()==0:
            if not savescore==None:
                self.Save_Score(savescore)
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
        if self.Button("Right") and self.Button("Select"):
            self.increase_vol()
        if self.Button("Left") and self.Button("Select"):
            self.decrease_vol()
        if self.cycle%50==0:
            self.cycle=0
            collect()
        self.cycle+=1
        sleep(self.tick)
        if not noclear:
            self.Fill_Screen((0,0,0))
        adc_reading  = self.vpin.read_u16()
        adc_voltage  = (adc_reading * 3.3) / 65535
        vsys_voltage = adc_voltage * 3 if mpyversion[1]>=24 else adc_voltage * 12
        if vsys_voltage<1.9:
            self.fill(self.color(0,0,0))
            language_texts = {
                0: ("BATTERY CRITICALLY LOW!", "Please replace the","batteries in your PicoBoy.","Please switch your", "PicoBoy off."),
                1: ("BATERIA CRITICAMENTE BAJA!", "Por favor reemplace las","baterias en su PicoBoy.","Por favor cambia tu","PicoBoy fuera."),
                2: ("BATTERIE CRITIQUEMENT FAIBLE!", "Veuillez remplacer les","piles dans votre PicoBoy.","Veuillez changer votre","PicoBoy s'en va."),
                3: ("BATTERIE KRITISCH NIEDRIG!", "Bitte ersetzen Sie die","Batterien in Ihrem PicoBoy.","Bitte wechseln Sie Ihr","PicoBoy aus."),
                4: ("BATTERIA CRITICAMENTE SCARICA!", "Si prega di sostituire le","batterie del tuo PicoBoy.","Per favore, cambia il tuo","PicoBoy spento.")
            }
            message = language_texts.get(self.langauge, language_texts[0])  # Default to English
            self.Create_Text(message[0],-1,30,(255,255,255))
            self.Create_Text(message[1], -1, 130, (255,255,255))
            self.Create_Text(message[2], -1, 145, (255,255,255))
            self.Create_Text(message[3], -1, 200, (255,255,255))
            self.Create_Text(message[4], -1, 215, (255,255,255))
            self.rect(75,60,80,40,self.color(255,0,0))
            self.fill_rect(155,70,10,20,self.color(255,0,0))
            self.line(75,60,155,99,self.color(255,0,0))
            self.Play_Sound(0)
            self.Play_Sound(0,2)
            self.Play_Sound(0,3)
            self.Play_Sound(0,4)
            self.show_screen()
            exit()
            
    def increase_vol(self):
        if self.vol<=self.vol_max-5500:
            self.vol+=4875
        else:
            self.vol=self.vol_max
        try:
            with open("volume.conf", "w") as w:
                w.write(str(self.vol))
        except:
            ""
                
    def decrease_vol(self):
        if self.vol>=self.vol_min+5500:
            self.vol-=4875
        else:
            self.vol=self.vol_min
        try:
            with open("volume.conf", "w") as w:
                w.write(str(self.vol))
        except:
            ""
            
    def Button(self, button):
        buttons = {
            "Up": self.up, "Down": self.down, "Left": self.left,
            "Right": self.right, "A": self.A, "B": self.B,
            "Select": self.select, "Start": self.start
        }
        if button == "Any":
            return any(btn.value() == 0 for btn in buttons.values())
        elif button in buttons:
            return buttons[button].value() == 0
        return False

    def Outline_Rect(self, x, y, width, height, color):
        self.rect(x,y,width,height,self.color(*color))
        
    def Fill_Rect(self, x, y, width, height, color):
        self.fill_rect(x,y,width,height,self.color(*color))
        
    def Line(self,x1,y1,x2,y2,c):
        self.line(x1,y1,x2,y2,self.color(*c))
        
    def Hline(self,x1,y1,h,c):
        self.hline(x1,y1,h,self.color(*c))

    def Vline(self,x1,y1,w,c):

        self.vline(x1,y1,w,self.color(*c))
            
    def Fill_Screen(self,color):
        self.fill(self.color(*color))


    def Play_Sound(self, freq, channel=1, duty_u16=2000):
        if freq==0:
            self.Stop_Sound(channel)
            return
        if channel in [1, 2, 3, 4]:
            spk_channel = self.channels[f"spk_channel{channel}"]
            max_count = (freq * self.audio_pwm_wrap) / 10000
            level = (self.vol / 100.0**self.curve) * max_count
            spk_channel.freq(freq if freq > 0 else 0)
            spk_channel.duty_u16(0 if freq == 0 else int(level))

    def Stop_Sound(self, channel=1):
        spk_channel = self.channels[f"spk_channel{channel}"]
        spk_channel.duty_u16(0)

    def Create_Text(self, s, x, y, c=(255, 255, 255), wid=None):
        if not s:
            return
        
        words = s.split(" ")
        if wid:
            longest = max(words, key=len)
            wid = max(wid, (len(longest) * 8) + 30)

            currentlines, line, temp = [], [], 0
            lengths = [(len(word) * 8) + 8 for word in words]

            for word, length in zip(words, lengths):
                if temp + length > wid - 20:
                    currentlines.append(" ".join(line))
                    line, temp = [], 0
                line.append(word)
                temp += length

            if line:
                currentlines.append(" ".join(line))

            y = y if y != -1 else (self.height // 2) - 8
            for line in currentlines:
                nx = x if x != -1 else (self.width // 2) - (len(line) * 8 // 2)
                self.text(line, nx, y, self.color(*c))
                y += 12
        else:
            x = x if x != -1 else (self.width // 2) - (len(s) * 8 // 2)
            y = y if y != -1 else (self.height // 2) - 8
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

    def Pause_Screen(self):
        self.fill_rect(18,90,206,81,self.color(50,50,50))
        self.fill_rect(10,98,221,66,self.color(50,50,50))
        self.poly(10,90,array('h',[8,0,0,8,8,8]),self.color(50,50,50),True)
        self.poly(230,90,array('h',[0,8,-8,0,-8,8]),self.color(50,50,50),True)
        self.poly(10,170,array('h',[8,0,0,-8,8,-8]),self.color(50,50,50),True)
        self.poly(230,170,array('h',[0,-8,-8,0,-8,-8]),self.color(50,50,50),True)
        self.Create_Text("Game Paused", -1,-1,(255,255,255))
        self.Create_Text("Press start to resume.", -1, 135, (255,255,255))
        self.Update(noclear=True)
        sleep(0.25)
        while True:
            self.Update(True, True)
            if self.Button("Start"):
                sleep(0.25)
                return
            
    def Render_Popup(self, bgcolor, textcolor, x, y, width, title, description):
        error=""
        if type(bgcolor)==tuple:
            if not len(bgcolor)==3:
                error="Background color is incorrectly formatted (Use RGB888)"
        else:
            error="Background color is not a tuple"
        if type(textcolor)==tuple:
            if not len(textcolor)==3:
                error="Text color is incorrectly formatted (Use RGB888)"
        else:
            error="Text color is not a tuple"
        if not type(x) == int:
            error="The X value must be an integer"
        if not type(y) == int:
            error="The Y value must be an integer"
        if not type(width) == int:
            error="The width value must be an integer"
        if not type(title)==str:
            error="The title must be a string"
        if not type(description)==list:
            error="The description must be a list of strings"
        else:
            if not all(isinstance(item, str) for item in description):
                error="The description must be a list of strings"
        if not error=='':
            raise TypeError(f"PicoBoySDK Error: {error}!")
            exit()
        height=15
        
        words=[]
        if not title=="":
            l=title.split(" ")
            for f in l:
                words.append(f)
        for l in description:
            l=l.split(" ")
            for f in l:
                words.append(f)
        longest=""
        for w in words:
            if len(w)>len(longest):
                longest=w
        newwidth=(len(longest)*8)+30
        #if newwidth>width:
        #    width=newwidth
        
        lines=[]
        if not title=="":
            line=title.split(" ")
            currentlines=[]
            lengths=[]
            for string in line:
                lengths.append((len(string)*8)+8)
            repeated=False
            while len(line)>0:
                currentline=[]
                temp=0
                while True:
                    if len(line)==0:
                        break
                    if lengths[0]+temp>width-20 and not width<newwidth:
                        break
                    try:
                        temp+=lengths.pop(0)
                        currentline.append(line.pop(0))
                    except:
                        break
                if not currentline==[]:
                    currentlines.append(" ".join(currentline))
            lines.append(currentlines)
        for line in description:
            line=line.split(" ")
            lengths=[]
            currentlines=[]
            for string in line:
                lengths.append((len(string)*8)+8)
            repeated=False
            while len(line)>0:
                
                currentline=[]
                temp=0
                while True:
                    if len(line)==0 and not repeated:
                        repeated=True
                        break
                    else:
                        repeated=False
                    if lengths[0]+temp>width-20 and not width<newwidth:
                        break
                    try:
                        temp+=lengths.pop(0)
                        currentline.append(line.pop(0))
                    except:
                        break
                if not currentline==[]:
                    currentlines.append(" ".join(currentline))
            lines.append(currentlines)
        for line in lines:
            height+=8
            height+=len(line)*12
            

        if x<0:
            x=int(120-(width/2))
        if y<0:
            y=int(120-(height/2))
        self.fill_rect(x+8,y,width-16,height,self.color(*bgcolor))
        self.fill_rect(x,y+8,width,height-17,self.color(*bgcolor))
        self.poly(x,y,array('h',[8,0,0,8,8,8]),self.color(*bgcolor),True)
        self.poly(x+width-1,y,array('h',[0,8,-8,0,-8,8]),self.color(*bgcolor),True)
        self.poly(x,y+height-1,array('h',[8,0,0,-8,8,-8]),self.color(*bgcolor),True)
        self.poly(x+width-1,y+height-1,array('h',[0,-8,-8,0,-8,-8]),self.color(*bgcolor),True)
        currenty=y+10
        tcolor=self.color(*textcolor)
        for i,l in enumerate(lines):
            for line in l:
                self.text(line, x+int((width/2)-((len(line)*8)/2)), currenty, tcolor)
                currenty+=12
            if not i==0:
                currenty+=8
            else:
                currenty+=13
            
    def Save_Score(self, score):
        if not type(score) == int:
            raise TypeError("PicoBoySDK Error: given score must be an integer.")
        directory=listdir()
        if not "highscores"+self.namespace+".sc" in directory:
            with open("highscores"+self.namespace+".sc", "w") as w:
                w.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
                with open("/games/"+self.namespace, "a") as a:
                    a.write("---PICOBOYFILELIST---"+"highscores"+self.namespace+".sc")
        with open("highscores"+self.namespace+".sc", "r") as s:
            scores=s.read().split("\n")
            for r in range(len(scores)):
                scores[r]=int(scores[r])
        newscores=scores
        newscores.append(int(score))
        newscores.sort(reverse=True)
        for i in range(len(newscores)): newscores[i]=str(newscores[i])
        with open("highscores"+self.namespace+".sc", "w+") as w:
            w.write("\n".join(newscores[:10]))
            
    def Show_Scores(self):
        directory=listdir()
        if not "highscores"+self.namespace+".sc" in directory:
            with open("highscores"+self.namespace+".sc", "w") as w:
                w.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0")
                with open("/games/"+self.namespace, "a") as a:
                    a.write("---PICOBOYFILELIST---"+"highscores"+self.namespace+".sc")
        x=open("highscores"+self.namespace+".sc", "r")
        scores=x.read()
        x.close()
        del x
        scores=scores.split("\n")
        while True:
            if self.Button("B"):
                sleep(0.1)
                return
            self.fill(self.color(0,0,0))
            self.Create_Text("High Scores:", -1, 15, (255,255,255))
            for i in range(len(scores)):
                self.Create_Text("Score "+str(i+1)+": "+str(scores[i]), -1, 50+i*15, (255,255,255))
            self.Create_Text("Press B to exit", -1, 220, (255,255,255))
            self.Update()
        
        
class PlayerObject:
    def __init__(self,parent,initx,inity,width,height,sprite,speed):
        if not "PicoBoySDK" in str(type(parent)):
            raise TypeError("PicoBoySDK Error: The PicoBoySDK object is missing or invalid in "+str(self))
            exit()
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
        
    def Goto(self, x, y):
        self.x=x
        self.y=y
    
    def Change_Axis(self, x, y):
        self.direction="XY"
        if x and y:
            return
        if x:
            self.direction="X"
        if y:
            self.direction="Y"

class MusicBoxObject:
    def __init__(self,parent,mode):
        if not "PicoBoySDK" in str(type(parent)):
            raise TypeError("PicoBoySDK Error: The PicoBoySDK object is missing or invalid in "+str(self))
            exit()
        self.parent=parent
        self.song=[]
        self.ch_a_0 = self.parent.channels["spk_channel1"]
        self.ch_a_1 = self.parent.channels["spk_channel2"]
        self.ch_b_0 = self.parent.channels["spk_channel3"]
        self.ch_b_1 = self.parent.channels["spk_channel4"]
        self.opcode=0x00
        self.mode=mode
        self.savedindex=0
        self.tmp=[]
        self.isReading=False
        self.savedsong=[]
        self.index=0
        self.audio_pwm_wrap=5000
        self.curve=1.8
        self.vol=self.parent.vol/18
        self.thread=start_new_thread(self.Play,())
            
    def _pitch(self, freq):
        return (2**((freq-69)/12))*440

    def _duty_cycle(self, percent):
        return round((percent/100)*65535)
    
    def play_note(self, note, channel, duty):
        self.vol=self.parent.vol/18
        pwm_divider = 133000000 / self.audio_pwm_wrap / (note+1)
        max_count = (note * self.audio_pwm_wrap) / 10000
        level = (self.vol / 100.0**self.curve) * max_count
        if channel == "a0":
            self.ch_a_0.freq(round(self._pitch(note)))
            self.ch_a_0.duty_u16(self._duty_cycle(int(level)))
        elif channel == "a1":
            self.ch_a_1.freq(round(self._pitch(note)))
            self.ch_a_1.duty_u16(self._duty_cycle(int(level)))
        elif channel == "b0":
            self.ch_b_0.freq(round(self._pitch(note)))
            self.ch_b_0.duty_u16(self._duty_cycle(int(level)))
        elif channel == "b1":
            self.ch_b_1.freq(round(self._pitch(note)))
            self.ch_b_1.duty_u16(self._duty_cycle(int(level)))

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
        with open(song, "r") as r:
            song=r.read()
        song=song.split(", ")
        nsong=[]
        for item in song:
            if "x" in item:
                nsong.append(item)
            else:
                nsong.append(int(item))
        self.tmp=[]
        self.isReading=False
        self.opcode=0x00
        self.index=0
        self.song=nsong
        
    def Change_Mode(self, mode):
        self.mode=mode
    
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
                if self.song[self.index] in ("0x90", "0x91", "0x92", "0x93", "0x80", "0x81", "0x82", "0x83", "0xf0", "0xe0"):
                    self.opcode = self.song[self.index]
                    self.isReading = True
                    self.tmp = []
                    self.tmp_index = 1
                    while self.isReading: 
                        if (self.index + self.tmp_index) >= len(self.song):
                            break
                        else:
                            if not self.song[self.index + self.tmp_index] in ("0x90", "0x91", "0x92", "0x93", "0x80", "0x81", "0x82", "0x83", "0xf0", "0xe0"):
                                self.tmp.append(self.song[self.index + self.tmp_index])
                                self.tmp_index += 1
                            else:
                                self.isReading = False
                    if self.opcode in ("0x90", "0x91", "0x92", "0x93"):
                        if len(self.tmp) > 0:
                            if self.opcode == "0x90":
                                self.play_note(self.tmp[0], "a0", 50)
                            elif self.opcode == "0x91":
                                self.play_note(self.tmp[0], "b0", 50)
                            elif self.opcode == "0x92":
                                self.play_note(self.tmp[0], "a1", 50)
                            elif self.opcode == "0x93":
                                self.play_note(self.tmp[0], "b1", 50)
                            if len(self.tmp) == 3:
                                delay = ((self.tmp[1]*256)+(self.tmp[2]))
                                sleep_ms(delay)
                        self.index += 1
                        
                    elif self.opcode in ("0x80", "0x81", "0x82", "0x83"):
                        if self.opcode == "0x80":
                            self.stop_channel("a0")
                        elif self.opcode == "0x81":
                            self.stop_channel("b0")
                        elif self.opcode == "0x82":
                            self.stop_channel("a1")
                        elif self.opcode == "0x83":
                            self.stop_channel("b1")
                            
                        if len(self.tmp) >= 2:
                            delay = ((self.tmp[0]*256)+(self.tmp[1]))
                            sleep_ms(delay)
                        self.index += 1
                        
                    elif self.opcode in ("0xf0", "0xe0"):
                        if self.mode: 
                            self.index = 0
                else:
                    self.index += 1
            except:
                self.ch_a_0.duty_u16(0)
                self.ch_a_1.duty_u16(0)
                self.ch_b_0.duty_u16(0)
                self.ch_b_1.duty_u16(0)


    



