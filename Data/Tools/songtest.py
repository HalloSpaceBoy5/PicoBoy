from rpmidi import RPMidi
from PicoGameBoy import PicoGameBoy
import time
from random import randint
import _thread

pgb=PicoGameBoy()
x=[0x90,48, 0x91,72, 1,244, 0x92,47, 0x80, 0x81, 1,244, 0x90,46, 0x91,75, 0x82, 1,244, 0x92,45, 0x80, 0x81, 0,250, 0x90,47, 
0x82, 0,250, 0x90,48, 0x91,72, 1,244, 0x92,47, 0x80, 0x81, 1,244, 0x90,46, 0x91,70, 0x82, 1,244, 0x92,45, 0x90,70, 
0x81, 0,250, 0x91,47, 0x90,71, 0x82, 0,250, 0x80, 0x81, 0xF0]
midi=RPMidi()
def grandma():
    time.sleep(15)
    midi.stop_all_music()
nt=_thread.start_new_thread(grandma,())
while True:
    midi.play_song(x)
