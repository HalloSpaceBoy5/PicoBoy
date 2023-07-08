from PicoGameBoy import PicoGameBoy
from random import randint

pgb=PicoGameBoy()

lfreq=0
while True:
    going=True
    while going:
        freq=randint(50,3000)
        if freq<lfreq-1000 or freq>lfreq+1000:
            going=False
            lfreq=freq
    pgb.sound(freq)
    pgb.sound(0)
