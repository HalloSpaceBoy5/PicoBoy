# Original source files for PicoGameBoy.py by Vincent Mistler for YouMakeTech
# Modified By HalloSpaceBoy for the PicoBoy
from machine import Pin, PWM
from framebuf import FrameBuffer, RGB565
from st7789 import ST7789
from time import sleep
from random import randint
import struct


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
    def sound(self, freq, channel=1, duty_u16 = 2000):
        if channel==1:
            if freq>0:
                self.__buzzer.freq(freq)
                self.__buzzer.duty_u16(duty_u16)
            else:
                self.__buzzer.duty_u16(0)
        if channel==2:
            if freq>0:
                self.__buzzer2.freq(freq)
                self.__buzzer2.duty_u16(duty_u16)
            else:
                self.__buzzer2.duty_u16(0)
        if channel==3:
            if freq>0:
                self.__buzzer3.freq(freq)
                self.__buzzer3.duty_u16(duty_u16)
            else:
                self.__buzzer3.duty_u16(0)
        if channel==4:
            if freq>0:
                self.__buzzer4.freq(freq)
                self.__buzzer4.duty_u16(duty_u16)
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
   