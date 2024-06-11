# Original source files for PicoGameBoy.py by Vincent Mistler for YouMakeTech
# Modified By HalloSpaceBoy for the PicoBoy
from machine import Pin, PWM, ADC
from framebuf import FrameBuffer, RGB565
from st7789 import ST7789
from time import sleep
from random import randint
import struct
import sys


class PicoGameBoy(ST7789):
    def __init__(self):
        self.__up = Pin(2, Pin.IN, Pin.PULL_UP)
        self.__down = Pin(3, Pin.IN, Pin.PULL_UP)
        self.__left = Pin(4, Pin.IN, Pin.PULL_UP)
        self.__right = Pin(5, Pin.IN, Pin.PULL_UP)
        self.__button_A = Pin(6, Pin.IN, Pin.PULL_UP)
        self.__button_B = Pin(7, Pin.IN, Pin.PULL_UP)
        self.__button_home = Pin(8, Pin.IN, Pin.PULL_UP)
        self.__button_select = Pin(9, Pin.IN, Pin.PULL_UP)
        self.__button_start = Pin(10, Pin.IN, Pin.PULL_UP)
        self.__buzzer = PWM(Pin(12))
        self.__buzzer2 = PWM(Pin(13))
        self.__buzzer3 = PWM(Pin(14))
        self.__buzzer4 = PWM(Pin(15))
        super().__init__(width=240, height=240, id_=0, sck=18, mosi=19,
                         dc=20, rst=21, cs=17, bl=22, baudrate=62500000)
        
        self.__fb=[] # Array of FrameBuffer objects for sprites
        self.__w=[]
        self.__h=[]
        self.vpin=ADC(29)
        self.audio_pwm_wrap=5000
        self.curve=1.8
        self.vol_max=100000#30000
        self.vol_min=2500
        try:
            with open("/volume.conf", "r") as r:
                self.vol=int(r.read())
        except:
            self.vol=self.vol_max
    # center_text(s,color) displays a text in the middle of 
    # the screen with the specified color
    def free_mem(self):
        import gc, sys
        for key in sys.modules:
            del sys.modules[key]
        gc.collect()
    
    def show(self):
        self.show_screen()
        if self.button_up() and self.button_select():
            self.increase_brightness()
        if self.button_down() and self.button_select():
            self.decrease_brightness()
        if self.button_right() and self.button_select():
            self.increase_vol()
        if self.button_left() and self.button_select():
            self.decrease_vol()
        adc_reading  = self.vpin.read_u16()
        adc_voltage  = (adc_reading * 3.3) / 65535
        vsys_voltage = adc_voltage * 12
        if vsys_voltage>10:
            vsys_voltage = adc_voltage * 3
        if vsys_voltage<1.9:
            try:
                with open("langauge.conf") as r:
                    self.langauge=int(r.read())
                if self.langauge>4:
                    raise
            except:
                self.langauge=0
            self.fill(PicoGameBoy.color(0,0,0))
            if self.langauge==0:
                self.create_text("BATTERY CRITICALLY LOW!",-1,30,PicoGameBoy.color(255,255,255))
                self.create_text("Please replace the", -1, 130, PicoGameBoy.color(255,255,255))
                self.create_text("batteries in your PicoBoy.", -1, 145, PicoGameBoy.color(255,255,255))
                self.create_text("Please switch your", -1, 200, PicoGameBoy.color(255,255,255))
                self.create_text("PicoBoy off.", -1, 215, PicoGameBoy.color(255,255,255))
            if self.langauge==1:
                self.create_text("BATERIA CRITICAMENTE BAJA!",-1,30,PicoGameBoy.color(255,255,255))
                self.create_text("Por favor reemplace el", -1, 130, PicoGameBoy.color(255,255,255))
                self.create_text("baterias en su PicoBoy.", -1, 145, PicoGameBoy.color(255,255,255))
                self.create_text("Por favor cambia tu", -1, 200, PicoGameBoy.color(255,255,255))
                self.create_text("PicoBoy fuera.", -1, 215, PicoGameBoy.color(255,255,255))
            if self.langauge==2:
                self.create_text("BATTERIE CRITIQUEMENT FAIBLE!",-1,30,PicoGameBoy.color(255,255,255))
                self.create_text("Veuillez remplacer le", -1, 130, PicoGameBoy.color(255,255,255))
                self.create_text("piles dans votre PicoBoy.", -1, 145, PicoGameBoy.color(255,255,255))
                self.create_text("Veuillez changer votre", -1, 200, PicoGameBoy.color(255,255,255))
                self.create_text("PicoBoy s'en va.", -1, 215, PicoGameBoy.color(255,255,255))
            if self.langauge==3:
                self.create_text("BATTERIE KRITISCH NIEDRIG!",-1,30,PicoGameBoy.color(255,255,255))
                self.create_text("Bitte ersetzen Sie die", -1, 130, PicoGameBoy.color(255,255,255))
                self.create_text("Batterien in Ihrem PicoBoy.", -1, 145, PicoGameBoy.color(255,255,255))
                self.create_text("Bitte wechseln Sie Ihr", -1, 200, PicoGameBoy.color(255,255,255))
                self.create_text("PicoBoy aus.", -1, 215, PicoGameBoy.color(255,255,255))
            if self.langauge==4:
                self.create_text("BATTERIA CRITICAMENTE SCARICA!",-1,30,PicoGameBoy.color(255,255,255))
                self.create_text("Si prega di sostituire il", -1, 130, PicoGameBoy.color(255,255,255))
                self.create_text("batterie del tuo PicoBoy.", -1, 145, PicoGameBoy.color(255,255,255))
                self.create_text("Per favore, cambia il tuo", -1, 200, PicoGameBoy.color(255,255,255))
                self.create_text("PicoBoy spento.", -1, 215, PicoGameBoy.color(255,255,255))
            self.rect(75,60,80,40,PicoGameBoy.color(255,0,0))
            self.fill_rect(155,70,10,20,PicoGameBoy.color(255,0,0))
            self.line(75,60,155,99,PicoGameBoy.color(255,0,0))
            self.sound(0)
            self.sound(0,2)
            self.sound(0,3)
            self.sound(0,4)
            self.show_screen()
            sys.exit()
    
    def center_text(self, s, color = 1):
        x = int(self.width/2)- int(len(s)/2 * 8)
        y = int(self.height/2) - 8
        self.text(s, x, y, color)
        
    def create_text(self, s,x=-1,y=-1, color = ST7789.color(255,255,255)):
        if x==-1:
            x = int(self.width/2)- int(len(s)/2 * 8)
        if y==-1:
            y = int(self.height/2) - 8
        self.text(s, x, y, color)
        

    
    # center_text(s,color) displays a text in the right corner of 
    # the screen with the specified color
    def top_right_corner_text(self, s, color = 1):
        x = self.width - int(len(s) * 8)
        y = 0
        self.text(s, x, y, color)
        
        
    # add_sprite(buffer,w,h) creates a new sprite from framebuffer
    # with a width of w and a height of h
    # The first sprite is #0 and can be displayed by sprite(0,x,y)
    def add_sprite(self, buffer, w, h, r=1):
        if r==1:
            rotated_fb = FrameBuffer(buffer, w, h, RGB565)
        elif r==2:
            fb = FrameBuffer(buffer, w, h, RGB565)
            rotated_fb = FrameBuffer(bytearray(w*h*2), w, h, RGB565)
            for x in range(w):
                for y in range(h):
                    p=fb.pixel(x,y)
                    rotated_fb.pixel(-y+h,-x+w,p)
        elif r==3:
            fb = FrameBuffer(buffer, w, h, RGB565)
            rotated_fb = FrameBuffer(bytearray(w*h*2), w, h, RGB565)
            for x in range(w):
                for y in range(h):
                    p=fb.pixel(x,y)
                    rotated_fb.pixel(-x+w,-y+h,p)
        else:
            fb = FrameBuffer(buffer, w, h, RGB565)
            rotated_fb = FrameBuffer(bytearray(w*h*2), w, h, RGB565)
            for x in range(w):
                for y in range(h):
                    p=fb.pixel(x,y)
                    rotated_fb.pixel(y,x,p)
        self.__fb.append(rotated_fb)
        self.__w.append(w)
        self.__h.append(h)
        
        
    def replace_sprite_colors(self,sprite,color1,color2):
        width=self.__w[sprite]
        height=self.__h[sprite]
        for x in range(width):
            for y in range(height):
                if self.__fb[sprite].pixel(x,y)==color1:
                    self.__fb[sprite].pixel(x,y,color2)
                else:
                    self.__fb[sprite].pixel(x,y,self.__fb[sprite].pixel(x,y))
                
        
    # add_rect_sprite(color,w,h) creates a new rectangular sprite
    # with the specified color, width and height
    def add_rect_sprite(self, color, w, h):
        buffer = bytearray(w * h * 2) # 2 bytes per pixel
        # fill the buffer with the specified color
        lsb = (color & 0b0000000011111111)
        msb = (color & 0b1111111100000000) >> 8
        for i in range(0,w*h*2,2):
            buffer[i] = lsb
            buffer[i+1] = msb
        fb = FrameBuffer(buffer, w, h, RGB565)
        self.__fb.append(fb)
        self.__w.append(w)
        self.__h.append(h)
       
    # sprite(n,x,y) displays the nth sprite at coordinates (x,y)
    # the sprite must be created first by method add_sprite
    def sprite(self, n, x, y):
        self.blit(self.__fb[n], x, y)
        
    def load_binary_image(self, path, x, y,w,h):
        chunk_size = 16384
        start_index=20
        with open(path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break  
                for i, byte in enumerate(chunk):
                    self.buffer[start_index + i] = byte

        
    # sprite_width(n) returns the width of the nth sprite in pixels
    def sprite_width(self,n):
        return self.__w[n]
    
    # sprite_height(n) returns the height of the nth sprite in pixels
    def sprite_height(self,n):
        return self.__h[n]
        
    # button_up() returns True when the player presses the up button
    def button_up(self):
        return self.__up.value()==0
    
    # button_down() returns True when the player presses the down button
    def button_down(self):
        return self.__down.value()==0
    
    # button_left() returns True when the player presses the left button
    def button_left(self):
        return self.__left.value()==0
    
    # button_right() returns True when the player presses the right button
    def button_right(self):
        return self.__right.value()==0
    
    # button_A() returns True when the player presses the A button
    def button_A(self):
        return self.__button_A.value()==0
    
    # button_B() returns True when the player presses the B button
    def button_B(self):
        return self.__button_B.value()==0

    # button_Home() returns True when the player presses the home button
    def button_Home(self):
        return self.__button_home.value()==0

    # button_Home() returns True when the player presses the home button
    def button_start(self):
        return self.__button_start.value()==0

    # button_Home() returns True when the player presses the home button
    def button_select(self):
        return self.__button_select.value()==0

    # any_button() returns True if any button is pressed
    def any_button(self):
        button_pressed=False
        if self.button_up():
            button_pressed = True
        if self.button_down():
            button_pressed = True
        if self.button_left():
            button_pressed = True
        if self.button_right():
            button_pressed = True
        if self.button_A():
            button_pressed = True
        if self.button_B():
            button_pressed = True
        if self.button_select():
            button_pressed = True
        if self.button_start():
            button_pressed = True
        return button_pressed
    
    # sound(freq) makes a sound at the selected frequency in Hz
    # call sound(0) to stop playing the sound
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
    
    def sound(self, freq, channel=1, j=0):
        pwm_divider = 133000000 / self.audio_pwm_wrap / (freq+1)
        max_count = (freq * self.audio_pwm_wrap) / 10000
        level = (self.vol / 100.0**self.curve) * max_count
        if channel==1:
            if freq>0:
                self.__buzzer.freq(freq)
                self.__buzzer.duty_u16(int(level))
            else:
                self.__buzzer.duty_u16(0)
        if channel==2:
            if freq>0:
                self.__buzzer2.freq(freq)
                self.__buzzer2.duty_u16(int(level))
            else:
                self.__buzzer2.duty_u16(0)
        if channel==3:
            if freq>0:
                self.__buzzer3.freq(freq)
                self.__buzzer3.duty_u16(int(level))
            else:
                self.__buzzer3.duty_u16(0)
        if channel==4:
            if freq>0:
                self.__buzzer4.freq(freq)
                self.__buzzer4.duty_u16(int(level))
            else:
                self.__buzzer4.duty_u16(0)
            
if __name__ == "__main__":
    pgb=PicoGameBoy()
    
    # Colors (RGB)
    # Note that color is a static method and can be called
    # without creating an object (PicoGameBoy.color instead of pgb.color)
    BLACK=PicoGameBoy.color(0,0,0)
    WHITE=PicoGameBoy.color(255,255,255)
    RED=PicoGameBoy.color(255,0,0)
    GREEN=PicoGameBoy.color(0,255,0)
    BLUE=PicoGameBoy.color(0,0,255)
    
    # PicoGameBoy inherits all methods from the FrameBuffer class
    # see https://docs.micropython.org/en/latest/library/framebuf.html
    
    pgb.fill(BLACK)
    
    # The Raspberry Pi Pico GameBoy uses a framebuffer
    # The framebuffer is only transfered to the actual screen and become visible
    # when calling show()
    pgb.show()

    # Drawing primitive shapes
    # The screen resolution is 240x240 pixels but Python like many programming 
    # languages starts counting from zero, not one.
    # The top left corner is (0,0) and bottom right is (239,239)
    pgb.pixel(0,0,WHITE)
    pgb.pixel(239,239,BLUE)
    pgb.show()
    sleep(1)
    
    pgb.line(0,239,239,0,RED)
    pgb.show()
    sleep(1)
    
    pgb.rect(10,10,220,220,WHITE)
    pgb.show()
    sleep(1)
    
    pgb.fill_rect(10,10,220,220,WHITE)
    pgb.show()
    sleep(1)
    
    # text
    pgb.fill(BLACK)
    pgb.text('Hello from Pi Pico GameBoy!',0,0,GREEN)
    pgb.show()
    sleep(1)
    
    pgb.center_text('GAME OVER',WHITE)
    pgb.show()
    sleep(1)
            
    # sprites
    x = 120
    y = 120 
    pgb.fill(BLACK)
    pgb.add_rect_sprite(GREEN,12,12) # Create sprite #0
    while True:
        pgb.sprite(0,x,y)
        pgb.show()
        while not pgb.any_button():
            sleep(0.020)
        if pgb.button_right():
            x=x+1
        elif pgb.button_left():
            x=x-1
        elif pgb.button_up():
            y=y-1
        elif pgb.button_down():
            y=y+1
   