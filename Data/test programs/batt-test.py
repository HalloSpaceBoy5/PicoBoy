import machine
import sys
from PicoGameBoy import PicoGameBoy
import time

pgb=PicoGameBoy()

black=PicoGameBoy.color(0,0,0)
white=PicoGameBoy.color(255,255,255)

print("sys.implementation:{}".format(sys.implementation))
print("sys.version:{}".format(sys.version))
pin = machine.ADC(29) 
while True: 
    adc_reading  = pin.read_u16()
    adc_voltage  = (adc_reading * 3.3) / 65535
    vsys_voltage = adc_voltage * 12
    if vsys_voltage>10:
        vsys_voltage = adc_voltage * 3
        percentage=int(int((round(vsys_voltage,3)/4.5)*100)/5)*5
    else:
        percentage=int(int((round(vsys_voltage,3)/3.3)*100)/5)*5
    pgb.fill(black) 
    pgb.create_text(f"Batt Voltage:",-1,-1,white)
    pgb.create_text(str(vsys_voltage),-1,130,white)
    #if pgb.button_A():
    #    pgb.create_text(str(adc_voltage),-1,145,white)
    
    
    
    

    if percentage>100 and percentage<150:
        percentage=100
    battx=25
    batty=100
    pgb.rect(battx,batty,20,40,white)
    pgb.fill_rect(battx+5,batty-4,10,5,white)
    if percentage>100:
        pgb.create_text("U",battx+6, batty+7,white)
        pgb.create_text("S",battx+6, batty+17,white)
        pgb.create_text("B",battx+6, batty+27,white)
        pgb.create_text("USB",battx+10-int(len(str(percentage))/2 * 8), batty+44, white)
    else:
        h=int(38*(percentage/100))
        print(h)
        pgb.fill_rect(battx+1,batty+1+(38-h),18,h,white)
        pgb.create_text(str(percentage)+"%",battx+10-int(len(str(percentage)+"%")/2 * 8), batty+44, white)
        
    #pgb.rect()
    if pgb.button_A():
        break
    #time.sleep(0.07)
    pgb.show()


