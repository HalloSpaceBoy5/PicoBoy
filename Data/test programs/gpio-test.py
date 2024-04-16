import machine
import sys
from PicoGameBoy import PicoGameBoy
import time
import utime
pgb=PicoGameBoy()
xAxis = machine.ADC(machine.Pin(26))
yAxis = machine.ADC(machine.Pin(27))


while True:
    pgb.fill(PicoGameBoy.color(0,0,0))
    #pgb.create_text(str(xAxis.read_u16()),-1,-1,PicoGameBoy.color(255,255,255))
    #pgb.create_text(str(yAxis.read_u16()),-1,130,PicoGameBoy.color(255,255,255))
    percentx=int((xAxis.read_u16()/65535)*100)
    percenty=int((yAxis.read_u16()/65535)*100)
    finx=120+(int(70*((percentx-50)/100))*2)
    finy=120+(int(70*((percenty-50)/100))*2)
    pgb.rect(40,40,160,160,PicoGameBoy.color(255,255,255))
    pgb.rect(finx-10,finy-10,20,20,PicoGameBoy.color(255,255,255))
    pgb.show()
    #time.sleep(1)