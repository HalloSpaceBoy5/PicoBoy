# FLEXIBLE LINK EXCHANGE PROTOCOL
# Designed by HalloSpaceBoy for the PicoBoy

"""
TODO:
- Modify the transfer process to use one clock signal
- Add timeouts to everything
- Make more detailed errors (raised at the micropy level)
- Document
- Test thouroughly
"""
"""
INTRODUCTION:

NOTICE: This library is still in beta, use it at your own risk

The FLEX (Flexible Link Exchange Protocol) is a communication protocol designed for efficient, bi-directional
data exchange between devices using a minimal 5-pin connection. It utilizes negotiable TX/RX roles (MX0 and MX1)
and synchronized clock signals (CL0 and CL1) to facilitate reliable communication between devices, even with varying
processing speeds. The protocol is interrupt-driven and asynchronous, allowing for efficient, low-latency data
transfer with minimal wiring. FLEX is designed to simplify connections while ensuring stability and flexibility in
communication, making it ideal for devices like the PicoBoy that require robust and scalable data exchange.

"""

"""
DEVICE CONNECTION:

    +------------------------+           +------------------------+
    |   Device A (PicoBoy 1) |           |   Device B (PicoBoy 2) |
    |------------------------|           |------------------------|
    |           GND          |-----------|            GND         |
    |           MX0          |-----------|            MX0         |
    |           MX1          |-----------|            MX1         |
    |           CL0          |-----------|            CL0         |
    |           CL1          |-----------|            CL1         |
    +------------------------+           +------------------------+

MX0=GPIO0
MX1=GPIO1
CL0=GPIO26
CL1=GPIO27

You can use the GPIO breakout on your PicoBoy to use this.


"""


from machine import Pin
from random import randint
from time import sleep
import micropython
micropython.alloc_emergency_exception_buf(100)


class Flex:
    def __init__(self):
        #user variables
        self.mx1=0
        self.mx2=1
        self.clk1=26
        self.clk2=27
        
        # variable inits
        self.state=0
        self.status=False
        self.tx=None
        self.rx=None
        self.clkin=None
        self.clkout=None
        self.ready=False
        
        #init pins
        Pin(self.clk1, Pin.OUT).value(0)
        Pin(self.clk2, Pin.OUT).value(0)
        Pin(self.mx1, Pin.OUT).value(0)
        Pin(self.mx2, Pin.OUT).value(0)
        
    
    def Port_Handshake(self):
        #init detect pin
        send_pin=Pin(self.mx2,Pin.OUT)
        send_pin.value(0)
        send_pin=Pin(self.mx2,Pin.IN,Pin.PULL_DOWN)
        
        #init check pin
        check_pin=Pin(self.mx1, Pin.OUT)
        check_pin.value(0)
        state=0
        ret=False
        while True:
            #set high for random interval
            delay=randint(0,10)
            check_pin=Pin(self.mx1, Pin.OUT)
            check_pin.value(1)
            sleep(delay/1000)
            delay=randint(0,10)
            #set low and read for random interval
            check_pin.value(0)
            check_pin=Pin(self.mx1, Pin.IN ,Pin.PULL_DOWN)
            for i in range(delay):
                #if the check pin is on, handshake complete
                if check_pin.value()==1:
                    send_pin=Pin(self.mx2,Pin.OUT)
                    send_pin.value(1)
                    ret=True
                    while not check_pin.value()==0:
                        sleep(0.005)
                        pass
                    break
                #if the send pin is on, other console completed handshake
                if send_pin.value()==1:
                    state=1
                    ret=True
                    break
                sleep(i/1000)
            #break out of loop cause connected
            if ret:
                break
            
        #return states and correct variables
        if state==0:
            a=(self.mx1,self.mx2)
            b=(self.clk1, self.clk2)
        else:
            a=(self.mx2,self.mx1)
            b=(self.clk2, self.clk1)
        return (a, state, b)
            

    def callback(self, v):
        #use this func for IRQ cause micropy does not handle interrupts well enough
        self.ready=True
        
    def false_callback(self, v):
        # nothing to see here
        return
             
        
        
    def Recieve(self):
        self.rx.irq(trigger=Pin.IRQ_FALLING, handler=self.false_callback)
        self.clkout.value(1) # let T know im ready
        while self.clkin.value()==0: #wait for first clock pulse
            pass
        self.clkout.value(0) # let T know I am synced
        while self.clkin.value()==1: #wait for T's CLK to be 0
            pass
        self.clkout.value(1) # let T know I am synced to clock
        sleep(0.005)
        self.clkout.value(0) # reset for communication
        
        #begin recieve of amount of bytes
        rbyte=0b000000000000000000
        for i in range(16):
            while self.clkin.value()==0: #wait for T's CLK
                pass
            self.clkout.value(0) # let T know CLK recieved, and to wait for me
            z=self.rx.value()
            rbyte |= (z & 1) << (15 - i)
            self.clkout.value(1) # let T know ready for CLK low
            while self.clkin.value()==1: # wait for T to set CLK low
                pass
            self.clkout.value(0)
        
        bytesout=[]
        
        #recieve actual bytes
        for f in range(rbyte):
            nbyte=0b00000000
            for i in range(8):
                while self.clkin.value()==0: #wait for T's CLK
                    pass
                self.clkout.value(0) # let T know CLK recieved, and to wait for me
                z=self.rx.value()
                nbyte |= (z & 1) << (7 - i)
                self.clkout.value(1) # let T know ready for CLK low
                while self.clkin.value()==1: # wait for T to set CLK low
                    pass
                #send ready signal
                self.clkout.value(0)
            #append recieved byte to list
            bytesout.append(nbyte)
        
        #Reset values
        self.clkout.value(0)
        self.tx.value(1)
        self.ready=False
        self.rx.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)
        o=bytes(bytesout)
        try:
            if o.decode()=="£¾ãØãä4|":
                self.Disconnect(False)
                return
        except:
            "Could not decode to string"
        return bytes(bytesout)
        
        
        
        
    def Send(self, byts):
        #get amount of bytes
        amount = len(byts)
     
        #Handshake
        self.tx.value(0) #send interrupt to r
        while self.clkin.value()==0: # wait for r
            pass
        self.clkout.value(1) # tell R to sync
        while self.clkin.value()==1: # wait for r to confirm sync
            pass
        self.clkout.value(0) #initialize clock
        while self.clkin.value()==0: # wait for r to confirm clock sync
            pass
        
        
        #send number of bytes
        for i in range(15, -1, -1): 
            bit = (amount >> i) & 1 # get bit to send
            self.clkout.value(1) # tell R to enter read mode read
            self.tx.value(bit) # send data to R
            while self.clkin.value()==1:# wait for R to confirm entrance
                pass
            while self.clkin.value()==0: # wait for confirmation of recipt
                pass
            self.clkout.value(0) # tell R to stop reading
            while self.clkin.value()==1: # wait for R to confirm ready for next pulse
                pass
            
        #send each byte
        for byte in byts:
            for i in range(7, -1, -1): 
                bit = (byte >> i) & 1 # get bit to send
                self.clkout.value(1) # tell R to enter read mode read
                self.tx.value(bit) # send data to R
                while self.clkin.value()==1:# wait for R to confirm entrance
                    pass
                while self.clkin.value()==0: # wait for confirmation of recipt
                    pass
                self.clkout.value(0) # tell R to stop reading
                while self.clkin.value()==1: # wait for R to confirm ready for next pulse
                    pass
            
        
        #Reset pins
        self.tx.value(1)
        self.clkout.value(0)
            
    def Check_Read(self):
        # check for a read by polling even though there is an irq
        if self.ready==True:
            return self.Recieve()
        
    
    def Connect(self):
        Pins=self.Port_Handshake()
        self.state=Pins[1]
        self.clkout=Pin(Pins[2][0], Pin.OUT)
        self.clkin=Pin(Pins[2][1], Pin.IN, Pin.PULL_DOWN)
        self.tx=Pin(Pins[0][0], Pin.OUT)
        self.tx.value(1)
        self.rx=Pin(Pins[0][1], Pin.IN, Pin.PULL_DOWN)
        self.rx.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)
        
    def Disconnect(self, d=True):
        if d:
            # using random string that is very uncommon for sending disconnect signal
            # 1 in ~3 quintillion chance of accidentally sending
            self.Send('£¾ãØãä4|'.encode())
        self.rx.irq(trigger=Pin.IRQ_FALLING, handler=self.false_callback)
        self.state=0
        self.tx=None
        self.rx=None
        self.clkin=None
        self.clkout=None
        self.ready=False
        Pin(self.clk1, Pin.OUT).value(0)
        Pin(self.clk2, Pin.OUT).value(0)
        Pin(self.mx1, Pin.OUT).value(0)
        Pin(self.mx2, Pin.OUT).value(0)
        
   





# Demo use: Sending text from one picoboy to another (Using the Thonny shell)
# uncomment to run as a file
"""
comm=Flex()
input("Press enter to connect...")
comm.Connect()
from PicoGameBoy import PicoGameBoy
from sys import exit
pgb=PicoGameBoy()


if comm.state==0:
    while True:
        l=input("Send: ")
        if l=="disconnect":
            comm.Disconnect()
            exit()
        l=l.encode()
        comm.Send(l)
else:
    while True:
        l=comm.Check_Read()
        if not l==None:
            last=l
            print(last.decode())
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.create_text(last.decode(),-1,-1,PicoGameBoy.color(255,255,255))
            pgb.show_screen()
"""
            






