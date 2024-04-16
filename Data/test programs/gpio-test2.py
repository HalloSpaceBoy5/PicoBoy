import machine
import sys
from PicoGameBoy import PicoGameBoy
import time
import utime
pgb=PicoGameBoy()
x = machine.ADC(machine.Pin(26))


while True:
    pgb.fill(PicoGameBoy.color(0,0,0))
    pgb.create_text("Potentionmeter value:",-1,-1,PicoGameBoy.color(255,255,255))
    percent=int((x.read_u16()/65535)*100)
    pgb.bl.duty_u16(int(55000*(percent/100)))
    pgb.create_text(str(percent),-1,130,PicoGameBoy.color(255,255,255))
    pgb.show()
    #time.sleep(1)