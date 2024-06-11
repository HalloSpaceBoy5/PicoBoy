# Original source files for st7789.py by Vincent Mistler for YouMakeTech
# Modified for PicoBoy by HalloSpaceBoy
# MicroPython ST7789 OLED driver, SPI interfaces for the PicoGameBoy/PicoBoy
from micropython import const
from machine import Pin, PWM, SPI
import framebuf
from utime import sleep_ms
from time import sleep




# register definitions
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

# Subclassing FrameBuffer provides support for graphics primitives
# http://docs.micropython.org/en/latest/pyboard/library/framebuf.html
class ST7789(framebuf.FrameBuffer):
    def __init__(self, width=240, height=240, id_=0, sck=18, mosi=19,
                 dc=20, rst=21, cs=17, bl=22, baudrate=62500000):
        self.width = width
        self.height = height
        self.dc = Pin(dc, Pin.OUT)
        self.rst = Pin(rst, Pin.OUT)
        self.cs = Pin(cs, Pin.OUT)
        try:
            self.bl = PWM(Pin(bl, Pin.OUT),freq=1000,duty_u16=10000)
        except:
            self.bl = PWM(Pin(bl, Pin.OUT))
        self.spi = SPI(id_, sck=Pin(sck), mosi=Pin(mosi), baudrate=baudrate, polarity=0, phase=0)
        self.PWM_FREQUENCY = 1000  
        self.DUTY_CYCLE_MIN = 10000 #Minimum Brightness
        self.DUTY_CYCLE=45000 #Brightness
        self.DUTY_CYCLE_MAX = 65000 #Maximum Brightness
        
        ### Enable for screenshots
        #self.sbuffer=bytearray(self.height * self.width * 2)
        #self.buffer = memoryview(self.sbuffer)
        ##### Otherwise:
        self.buffer = memoryview(bytearray(self.height * self.width * 2))
        
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        
        self.init_display()
        
    def write_cmd(self, cmd=None, data=None):
        self.cs(0)
        if cmd:
            self.dc(0) # command mode
            self.spi.write(cmd)
        if data:
            self.dc(1) # data mode
            self.spi.write(data)
        self.cs(1)

    def init_display(self):
        
        # Hardware reset
        self.rst.value(1)
        sleep(0.150)
        self.rst.value(0)
        sleep(0.150)
        self.rst.value(1)
        sleep(0.150)
        
        self.bl.duty_u16(0)#self.bl.value(0) # Turn backlight off initially to avoid nasty surprises

        self.write_cmd(SWRESET)
        sleep(0.150)
        self.write_cmd(TEON) # enable frame sync signal if used
        self.write_cmd(COLMOD, b'\x05') # 16 bits per pixel
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
        
        self.write_cmd(INVON)   # set inversion mode
        self.write_cmd(SLPOUT)  # leave sleep mode
        self.write_cmd(DISPON)  # turn display on
        
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
    
    def color(r, g, b):
        """
        color(r, g, b) returns a 16 bits integer color code for the ST7789 display


        where:
            r (int): Red value between 0 and 255
            g (int): Green value between 0 and 255
            b (int): Blue value between 0 and 255
        """
        # rgb (24 bits) -> rgb565 conversion (16 bits)
        # rgb = r(8 bits) + g(8 bits) + b(8 bits) = 24 bits
        # rgb565 = r(5 bits) + g(6 bits) + b(5 bits) = 16 bits
        r5 = (r & 0b11111000) >> 3
        g6 = (g & 0b11111100) >> 2
        b5 = (b & 0b11111000) >> 3
        rgb565 = (r5 << 11) | (g6 << 5) | b5
        
        # swap LSB and MSB bytes before sending to the screen
        lsb = (rgb565 & 0b0000000011111111)
        msb = (rgb565 & 0b1111111100000000) >> 8
        
        return ((lsb << 8) | msb)
    
    def load_image(self,filename):
        open(filename, "rb").readinto(self.buffer)
        

        
    def get_pixel(self, x, y):
        byte1=self.buffer[2*(y*self.width+x)];
        byte2=self.buffer[2*(y*self.width+x)+1];
        return byte2*256+byte1
