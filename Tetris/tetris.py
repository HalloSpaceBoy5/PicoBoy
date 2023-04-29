# Original source code for tetris.py by Vincent Mistler for YouMakeTech
# Modified By HalloSpaceBoy for the PicoBoy
from micropython import const
from PicoGameBoy import PicoGameBoy
import time
import os
from random import randint
import machine
import _thread
import gc

from rpmidi import RPMidi

os.rename("./main.py", "./tetris.py")
os.rename("./title.py", "./main.py")

BLOCK_SIZE = 12 # Size of a single tetromino block in pixels
GRID_OFFSET = 2
GRID_ROWS  = 20
GRID_COLS  = 10
currentmusic=[0xF0]
pgb = PicoGameBoy()
midi=RPMidi()
# image definitions 12x12 pixels
theme=[0x90,76, 1,9, 0x91,64, 0,245, 0x92,71, 0x80, 0,16, 0x81, 0,218, 0x82, 0,16, 0x90,72, 0x91,64, 0,234, 0x80, 
0,11, 0x90,74, 0,15, 0x81, 0,235, 0x91,64, 0,250, 0x92,72, 0x80, 0,10, 0x81, 0,219, 0x82, 0,15, 0x90,71, 
0x91,64, 0,235, 0x80, 0,15, 0x90,69, 0,11, 0x81, 0,255, 0x91,57, 0,245, 0x90,69, 0,16, 0x81, 0,218, 0x80, 
0,16, 0x90,72, 0x91,57, 0,234, 0x80, 0,11, 0x90,76, 0,15, 0x81, 0,235, 0x91,57, 0,250, 0x92,74, 0x80, 0,10, 
0x81, 0,219, 0x82, 0,15, 0x90,72, 0x91,57, 0,235, 0x80, 0,15, 0x90,71, 0,11, 0x81, 0,255, 0x91,56, 0,245, 
0x90,71, 0,16, 0x81, 0,218, 0x80, 0,16, 0x90,72, 0x91,56, 0,234, 0x80, 0,11, 0x90,74, 0,15, 0x81, 0,235, 
0x91,56, 0,250, 0x90,76, 0,10, 0x81, 0,234, 0x91,56, 0,245, 0x80, 0,5, 0x90,72, 0,11, 0x81, 0,255, 0x91,57, 
0,245, 0x92,69, 0x80, 0,16, 0x81, 0,234, 0x90,57, 0,245, 0x91,69, 0x82, 0,15, 0x80, 0,235, 0x90,57, 0,250, 
0x91,59, 0,10, 0x80, 0,203, 0x81, 0,31, 0x90,60, 0,219, 0x80, 1,36, 0x90,74, 0,5, 0x91,62, 1,5, 0x81, 
0,229, 0x90,77, 0,5, 0x91,62, 0,229, 0x80, 0,16, 0x90,81, 0,15, 0x81, 0,235, 0x91,62, 0,229, 0x80, 0,15, 
0x90,79, 0,16, 0x81, 0,234, 0x90,62, 0,16, 0x91,77, 0,229, 0x81, 0,16, 0x91,76, 0x80, 0,250, 0x90,60, 1,4, 
0x80, 0,235, 0x90,72, 0x91,60, 0,229, 0x80, 0,15, 0x90,76, 0,16, 0x81, 0,234, 0x91,60, 0,219, 0x80, 0,21, 
0x81, 0,10, 0x90,74, 0,235, 0x80, 0,10, 0x90,72, 0,21, 0x91,60, 0,214, 0x80, 0,15, 0x90,71, 0,32, 0x81, 
0,229, 0x91,56, 1,4, 0x81, 0,219, 0x90,72, 0,15, 0x91,56, 0,219, 0x80, 0,16, 0x90,74, 0,26, 0x81, 0,255, 
0x91,56, 0,219, 0x80, 0,15, 0x90,76, 0,27, 0x81, 0,234, 0x91,56, 0,234, 0x92,72, 0x80, 0,26, 0x81, 0,235, 
0x90,57, 0,234, 0x91,69, 0x82, 0,26, 0x80, 0,234, 0x90,57, 0,235, 0x91,69, 0,26, 0x80, 0,255, 0x90,57, 0,229, 
0x81, 0,32, 0x80, 0,234, 0x90,57, 0,239, 0x91,76, 0,21, 0x80, 0,250, 0x90,57, 1,10, 0x80, 0,229, 0x90,57, 
0,208, 0x81, 0,32, 0x91,72, 0,26, 0x80, 0,234, 0x90,57, 1,5, 0x80, 0,234, 0x90,57, 0,208, 0x81, 0,31, 
0x91,74, 0,21, 0x80, 0,250, 0x90,56, 1,10, 0x80, 0,229, 0x90,56, 0,203, 0x81, 0,37, 0x91,71, 0,26, 0x80, 
0,234, 0x90,56, 1,5, 0x80, 0,234, 0x90,56, 0,203, 0x81, 0,36, 0x91,72, 0,21, 0x80, 0,250, 0x90,57, 1,10, 
0x80, 0,229, 0x90,57, 0,208, 0x81, 0,32, 0x91,69, 0,26, 0x80, 0,234, 0x90,57, 1,5, 0x80, 0,234, 0x90,57, 
0,203, 0x81, 0,36, 0x91,68, 0,21, 0x80, 0,250, 0x90,56, 1,10, 0x80, 0,229, 0x90,56, 0,172, 0x81, 0,68, 
0x91,71, 0,26, 0x80, 0,234, 0x90,56, 1,5, 0x80, 0,234, 0x90,56, 0,208, 0x81, 0,31, 0x91,76, 0,21, 0x80, 
0,250, 0x90,57, 1,10, 0x80, 0,229, 0x90,57, 0,208, 0x81, 0,32, 0x91,72, 0,26, 0x80, 0,234, 0x90,57, 1,5, 
0x80, 0,234, 0x90,57, 0,182, 0x81, 0,57, 0x91,74, 0,73, 0x80, 0,198, 0x90,56, 1,10, 0x80, 0,229, 0x90,56, 
0,203, 0x81, 0,37, 0x91,71, 0,26, 0x80, 0,234, 0x90,56, 1,4, 0x80, 0,235, 0x90,56, 0,135, 0x80, 0,42, 
0x81, 0,62, 0x90,72, 1,213, 0x80, 0,42, 0x90,76, 1,239, 0x90,81, 3,221, 0x80, 0,5, 0x90,80, 7,203, 0x80, 
0xF0]
tetris_wall=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00mXmXmX3\x91\x00\x00\x00\x00mXmXmX3\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00mX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9emX\x00\x00\x00\x00\xf7\x9e\xf7\x9e\xf7\x9e3\x91\x00\x00\x00\x00mXmXmX3\x91\x00\x00\x00\x00mXmXmX3\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x913\x91\x00\x00\x00\x00mX3\x913\x91')
bottom_border=bytearray(b'\xeeP\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xf6\x90\xeeP\xf6p\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xf6p\xdd\x0f\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xe5P\xdd\x0fI\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84I\x84@\xc3H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4H\xc4@\xc3\xd3\r\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xdb.\xd3\r\xe4\xef\xed0\xed0\xed0\xed0\xed0\xed0\xed0\xed0\xed0\xed0\xe4\xef\xe5P\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xe5P\xf6p\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xfe\xb1\xf6p\xe5P\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xf5p\xe5P\xdc\xef\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xe5\x0f\xdc\xefI\x84I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\xa4I\x84')
corner=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00mX\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffmX\x00\x00\x00\x00mXmX\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffmXmX\x00\x00\x00\x00mXmXmX\xff\xff\xff\xff\xff\xff\xff\xffmXmXmX\x00\x00\x00\x00mXmXmXmX\xff\xff\xff\xffmXmXmXmX\x00\x00\x00\x00mXmXmXmX3\x913\x91mXmXmXmX\x00\x00\x00\x00mXmXmX3\x913\x913\x913\x91mXmXmX\x00\x00\x00\x00mXmX3\x913\x913\x913\x913\x913\x91mXmX\x00\x00\x00\x00mX3\x913\x913\x913\x913\x913\x913\x913\x91mX\x00\x00\x00\x003\x913\x913\x913\x913\x913\x913\x913\x913\x913\x91\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
left_border=bytearray(b'\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\xe3\x0e\x00\x00\x00\x00\xedP\xedP\xedP\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xedP\xedP\xfe\xd1\xedP\xedP\xe3\x0e\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1')
right_border=bytearray(b'\xedP\xedP\xedP\x00\x00\x00\x00\xe3\x0e\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xe3\x0e\xedP\xedP\xfe\xd1\xedP\xedP\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\x00\x00\xe3\x0e\xe3\x0e\xedP\xe3\x0e\xe3\x0e\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\x00\x00\xfe\xd1\xfe\xd1\xedP\x00\x00\x00\x00\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\x00\x00')
top_border=bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\xe3\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xedP\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1\xfe\xd1')



pgb.add_sprite(tetris_wall,12,12) #0
pgb.add_sprite(bottom_border,12,12) #1
pgb.add_sprite(corner,12,12) #2
pgb.add_sprite(left_border,12,12) #3
pgb.add_sprite(right_border,12,12) #4
pgb.add_sprite(top_border,12,12) #5


field = [[-1 for col in range(GRID_COLS)] for row in range(GRID_ROWS)]

# shape of the 7 tetrominos
# [0][1]
# [2][3]
# [4][5]
# [6][7]
# e.g. [3,4,5,7] is:
#    [ ]
# [ ][ ]
#    [ ]
tetrominos = [[1,3,5,7],
              [2,4,5,7],
              [3,5,4,6],
              [3,5,4,7],
              [2,3,5,7],
              [3,5,7,6],
              [2,3,4,5]]

# Game Boy Color Tetrominos colors
tetrominos_colors =[PicoGameBoy.color(239,146,132),
             PicoGameBoy.color(222,146,239),
             PicoGameBoy.color(239,170,132),
             PicoGameBoy.color(165,211,132),
             PicoGameBoy.color(99,219,222),
             PicoGameBoy.color(231,97,115),
             PicoGameBoy.color(0,0,0)]

# Color scheme
BLACK = PicoGameBoy.color(0,0,0)
WHITE = PicoGameBoy.color(255,255,255)
GRID_BACKGROUND_COLOR = PicoGameBoy.color(255,211,132)
BACKGROUND_COLOR = PicoGameBoy.color(99,154,132)
BACKGROUND_COLOR2 = PicoGameBoy.color(57,89,41)
TEXT_COLOR = BLACK
TEXT_BACKGROUND_COLOR = WHITE

lines = 0
level = 0
score = 0
music=True
last_button="NONE"
has_rotated=False
now = time.ticks_ms()
n =randint(0, 6)
next_n = randint(0, 6)
x=[0,0,0,0]
y=[0,0,0,0]
prev_x=[0,0,0,0]
prev_y=[0,0,0,0]
for i in range(0,4):
    x[i]=(tetrominos[n][i]) % 2;
    y[i]=int(tetrominos[n][i] / 2);
    
    x[i]+=int(GRID_COLS/2)
currentmusic=[0xF0]

def play_music():
    global midi
    global currentmusic
    while True:
        #if not currentmusic==[0xF0]:
            #while not currentmusic==[0xF0]:
     midi.play_song(currentmusic)
            

def no_music():
    global currentmusic
    global rept
    rept=False
    currentmusic=[0xF0]
    midi.stop_all_music()
    midi.stop_all()

def append_to_board(score):
    with open("highscorestetris.sc", "r") as s:
        scores=s.read().split("\n")
        for r in range(len(scores)):
            scores[r]=int(scores[r])
    newscores=scores
    newscores.append(int(score))
    newscores.sort(reverse=True)
    for i in range(len(newscores)): newscores[i]=str(newscores[i])
    with open("highscorestetris.sc", "w+") as w:
        w.write("\n".join(newscores[:10]))

def view_scores():
    x=open("highscorestetris.sc", "r")
    scores=x.read()
    x.close()
    del x
    scores=scores.split("\n")
    while True:
        if pgb.button_B():
            time.sleep(0.1)
            return
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.create_text("High Scores:", -1, 15, PicoGameBoy.color(255,255,255))
        for i in range(len(scores)):
            pgb.create_text("Score "+str(i+1)+": "+str(scores[i]), -1, 50+i*15, PicoGameBoy.color(255,255,255))
        pgb.create_text("Press B to exit", -1, 220, PicoGameBoy.color(255,255,255))
        pgb.show()

def pause_screen():
    global currentmusic
    no_music()
    currentmusic=[0xF0]
    pgb.fill_rect(10,90,220,80,PicoGameBoy.color(0,0,0))
    pgb.center_text("Game Paused",PicoGameBoy.color(255,255,255))
    pgb.create_text("Press Start or Select", -1, 135, PicoGameBoy.color(255,255,255))
    pgb.create_text("to resume.", -1, 147, PicoGameBoy.color(255,255,255))
    pgb.show()
    time.sleep(0.5)
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        elif pgb.button_select() or pgb.button_start():
            time.sleep(0.5)
            return

def collision(x,y):
    for i in range(4):
        # check collision against the border
        if x[i]<0 or x[i]>=GRID_COLS or y[i]>=GRID_ROWS:
            return True
        # check collision against another triomino
        if field[y[i]][x[i]]>=0:
            return True
            
    return False

def title_screen():
    # title screen
    now = time.ticks_ms()
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.load_image("tetris_title.bin")
        pgb.show()
        
        if time.ticks_diff(time.ticks_ms(), now) > 200:
            now = time.ticks_ms()
            pgb.center_text("PRESS ANY BUTTON",WHITE)
            pgb.show()
            while time.ticks_diff(time.ticks_ms(), now) < 200:
                time.sleep(0.020)
            now = time.ticks_ms()
        if pgb.button_select() or pgb.button_start():
            view_scores()
        elif pgb.button_A():
            break
            
def game_over_screen():
    global midi
    global music
    global musicthread
    global score
    global lines
    global level
    global currentmusic
    no_music()
    currentmusic=[0xF0]
    pgb.fill(BLACK)
    pgb.create_text("GAME OVER",-1,85,WHITE)
    pgb.text("Press A to play again.", 35, 105, WHITE)
    pgb.text("Press home to quit.", 40, 120, WHITE)
    pgb.create_text("Press select/start", -1, 135, PicoGameBoy.color(255,255,255))
    pgb.create_text("to view scores.", -1, 150, PicoGameBoy.color(255,255,255))
    pgb.create_text("Score: "+str(score), -1, 165, WHITE)
    pgb.show()
    append_to_board(score)
    while True:
        pgb.fill(BLACK)
        pgb.create_text("GAME OVER",-1,85,WHITE)
        pgb.text("Press A to play again.", 35, 105, WHITE)
        pgb.text("Press home to quit.", 40, 120, WHITE)
        pgb.create_text("Press select/start", -1, 135, PicoGameBoy.color(255,255,255))
        pgb.create_text("to view scores.", -1, 150, PicoGameBoy.color(255,255,255))
        pgb.create_text("Score: "+str(score), -1, 165, WHITE)
        pgb.show()
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        if pgb.button_select() or pgb.button_start():
            view_scores()
        elif pgb.button_A():
            lines=0
            level=0
            score=0
            clear_lines()
            break
def draw_background():
    pgb.fill(BACKGROUND_COLOR)
    
    for i in range(0,int(240/BLOCK_SIZE),2):
        for j in range(0,int(240/BLOCK_SIZE),2):
            pgb.fill_rect(j*BLOCK_SIZE,i*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE,BACKGROUND_COLOR2)
            pgb.fill_rect((j+1)*BLOCK_SIZE,(i+1)*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE,BACKGROUND_COLOR2)
            
    pgb.fill_rect(GRID_OFFSET*BLOCK_SIZE,0,
                  GRID_COLS*BLOCK_SIZE,GRID_ROWS*BLOCK_SIZE,
                  GRID_BACKGROUND_COLOR)
    
    # add walls
    for i in range(GRID_ROWS):
        pgb.sprite(0,(GRID_OFFSET-1)*BLOCK_SIZE,i*BLOCK_SIZE)
        pgb.sprite(0,(GRID_OFFSET+GRID_COLS)*BLOCK_SIZE,i*BLOCK_SIZE)
    
    # draw text (LINES)
    pgb.fill_rect((GRID_OFFSET+GRID_COLS+1)*BLOCK_SIZE+1,16*BLOCK_SIZE,
                  BLOCK_SIZE*7,BLOCK_SIZE*2,
                  TEXT_BACKGROUND_COLOR)
    pgb.text("LINES",(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,16*BLOCK_SIZE+1,TEXT_COLOR)
    pgb.text("%8s" % lines,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,17*BLOCK_SIZE+1,TEXT_COLOR)
    
    # draw text (LEVEL)
    pgb.fill_rect((GRID_OFFSET+GRID_COLS+1)*BLOCK_SIZE+1,13*BLOCK_SIZE,
                  BLOCK_SIZE*7,BLOCK_SIZE*2,
                  TEXT_BACKGROUND_COLOR)
    pgb.text("LEVEL",(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,13*BLOCK_SIZE+1,TEXT_COLOR)
    pgb.text("%8s" % level,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,14*BLOCK_SIZE+1,TEXT_COLOR)
    
    # draw text (SCORE)
    pgb.fill_rect((GRID_OFFSET+GRID_COLS+1)*BLOCK_SIZE+1,10*BLOCK_SIZE,
                  BLOCK_SIZE*7,BLOCK_SIZE*2,
                  TEXT_BACKGROUND_COLOR)
    pgb.text("SCORE",(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,10*BLOCK_SIZE+1,TEXT_COLOR)
    pgb.text("%8s" % score,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE+1,11*BLOCK_SIZE+1,TEXT_COLOR)
    
    # next tetromino box
    pgb.fill_rect((GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE,2*BLOCK_SIZE,
                  BLOCK_SIZE*6 ,BLOCK_SIZE*7,TEXT_BACKGROUND_COLOR)
    
    pgb.sprite(2,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE,2*BLOCK_SIZE) #upper left corner
    pgb.sprite(5,(GRID_OFFSET+GRID_COLS+3)*BLOCK_SIZE,2*BLOCK_SIZE) #top border
    pgb.sprite(5,(GRID_OFFSET+GRID_COLS+4)*BLOCK_SIZE,2*BLOCK_SIZE) #
    pgb.sprite(5,(GRID_OFFSET+GRID_COLS+5)*BLOCK_SIZE,2*BLOCK_SIZE) #
    pgb.sprite(5,(GRID_OFFSET+GRID_COLS+6)*BLOCK_SIZE,2*BLOCK_SIZE) #
    pgb.sprite(2,(GRID_OFFSET+GRID_COLS+7)*BLOCK_SIZE,2*BLOCK_SIZE) #upper right corner
    
    pgb.sprite(2,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE,8*BLOCK_SIZE) #lower left corner
    pgb.sprite(1,(GRID_OFFSET+GRID_COLS+3)*BLOCK_SIZE,8*BLOCK_SIZE) #lower border
    pgb.sprite(1,(GRID_OFFSET+GRID_COLS+4)*BLOCK_SIZE,8*BLOCK_SIZE) #
    pgb.sprite(1,(GRID_OFFSET+GRID_COLS+5)*BLOCK_SIZE,8*BLOCK_SIZE) #
    pgb.sprite(1,(GRID_OFFSET+GRID_COLS+6)*BLOCK_SIZE,8*BLOCK_SIZE) #
    pgb.sprite(2,(GRID_OFFSET+GRID_COLS+7)*BLOCK_SIZE,8*BLOCK_SIZE) #lower right corner
    
    for k in range(3,8):
        pgb.sprite(3,(GRID_OFFSET+GRID_COLS+2)*BLOCK_SIZE,k*BLOCK_SIZE) #left border
        pgb.sprite(4,(GRID_OFFSET+GRID_COLS+7)*BLOCK_SIZE,k*BLOCK_SIZE) #right border
    
    for i in range(4):
        draw_block((GRID_OFFSET+GRID_COLS+2)+tetrominos[next_n][i] % 2,
                   3+int(tetrominos[next_n][i] / 2), next_n)

def draw_block(j,i,n):
    # draw a tetris block of type n at the ith row and jth column
    # of the grid

    x = (GRID_OFFSET+j)*BLOCK_SIZE
    y = i*BLOCK_SIZE
    
    pgb.fill_rect(x,y,BLOCK_SIZE,BLOCK_SIZE,tetrominos_colors[n]) # main color
    pgb.rect(x,y,BLOCK_SIZE,BLOCK_SIZE,BLACK) # black border
    pgb.line(x+3,y+3,x+5,y+3,WHITE)
    pgb.line(x+3,y+3,x+3,y+5,WHITE)


    #####################################################################
 
 # show title screen and wait for a button

def clear_lines():
    for i in range(20):
        try:
            k=GRID_ROWS-i
            for i in range(GRID_ROWS-1,0,-1):
                count=0
                for j in range(GRID_COLS):
                    if field[i][j]>=0:
                        count+=1
                    field[k][j]=field[i][j]
        except:
            print("out of range")

def main_game():
    global last_button
    global delay
    global now
    global n
    global next_n
    global has_rotated
    global musicthread
    global score
    global lines
    global BLOCK_SIZE
    global GRID_OFFSET
    global GRID_ROWS
    global GRID_COLS
    global currentmusic
    global theme
    no_music()
    currentmusic=theme
    draw_background()
    pgb.show()
    # game loop
    while True:
        currentmusic=[0x90,76, 1,9, 0x91,64, 0,245, 0x92,71, 0x80, 0,16, 0x81, 0,218, 0x82, 0,16, 0x90,72, 0x91,64, 0,234, 0x80, 
0,11, 0x90,74, 0,15, 0x81, 0,235, 0x91,64, 0,250, 0x92,72, 0x80, 0,10, 0x81, 0,219, 0x82, 0,15, 0x90,71, 
0x91,64, 0,235, 0x80, 0,15, 0x90,69, 0,11, 0x81, 0,255, 0x91,57, 0,245, 0x90,69, 0,16, 0x81, 0,218, 0x80, 
0,16, 0x90,72, 0x91,57, 0,234, 0x80, 0,11, 0x90,76, 0,15, 0x81, 0,235, 0x91,57, 0,250, 0x92,74, 0x80, 0,10, 
0x81, 0,219, 0x82, 0,15, 0x90,72, 0x91,57, 0,235, 0x80, 0,15, 0x90,71, 0,11, 0x81, 0,255, 0x91,56, 0,245, 
0x90,71, 0,16, 0x81, 0,218, 0x80, 0,16, 0x90,72, 0x91,56, 0,234, 0x80, 0,11, 0x90,74, 0,15, 0x81, 0,235, 
0x91,56, 0,250, 0x90,76, 0,10, 0x81, 0,234, 0x91,56, 0,245, 0x80, 0,5, 0x90,72, 0,11, 0x81, 0,255, 0x91,57, 
0,245, 0x92,69, 0x80, 0,16, 0x81, 0,234, 0x90,57, 0,245, 0x91,69, 0x82, 0,15, 0x80, 0,235, 0x90,57, 0,250, 
0x91,59, 0,10, 0x80, 0,203, 0x81, 0,31, 0x90,60, 0,219, 0x80, 1,36, 0x90,74, 0,5, 0x91,62, 1,5, 0x81, 
0,229, 0x90,77, 0,5, 0x91,62, 0,229, 0x80, 0,16, 0x90,81, 0,15, 0x81, 0,235, 0x91,62, 0,229, 0x80, 0,15, 
0x90,79, 0,16, 0x81, 0,234, 0x90,62, 0,16, 0x91,77, 0,229, 0x81, 0,16, 0x91,76, 0x80, 0,250, 0x90,60, 1,4, 
0x80, 0,235, 0x90,72, 0x91,60, 0,229, 0x80, 0,15, 0x90,76, 0,16, 0x81, 0,234, 0x91,60, 0,219, 0x80, 0,21, 
0x81, 0,10, 0x90,74, 0,235, 0x80, 0,10, 0x90,72, 0,21, 0x91,60, 0,214, 0x80, 0,15, 0x90,71, 0,32, 0x81, 
0,229, 0x91,56, 1,4, 0x81, 0,219, 0x90,72, 0,15, 0x91,56, 0,219, 0x80, 0,16, 0x90,74, 0,26, 0x81, 0,255, 
0x91,56, 0,219, 0x80, 0,15, 0x90,76, 0,27, 0x81, 0,234, 0x91,56, 0,234, 0x92,72, 0x80, 0,26, 0x81, 0,235, 
0x90,57, 0,234, 0x91,69, 0x82, 0,26, 0x80, 0,234, 0x90,57, 0,235, 0x91,69, 0,26, 0x80, 0,255, 0x90,57, 0,229, 
0x81, 0,32, 0x80, 0,234, 0x90,57, 0,239, 0x91,76, 0,21, 0x80, 0,250, 0x90,57, 1,10, 0x80, 0,229, 0x90,57, 
0,208, 0x81, 0,32, 0x91,72, 0,26, 0x80, 0,234, 0x90,57, 1,5, 0x80, 0,234, 0x90,57, 0,208, 0x81, 0,31, 
0x91,74, 0,21, 0x80, 0,250, 0x90,56, 1,10, 0x80, 0,229, 0x90,56, 0,203, 0x81, 0,37, 0x91,71, 0,26, 0x80, 
0,234, 0x90,56, 1,5, 0x80, 0,234, 0x90,56, 0,203, 0x81, 0,36, 0x91,72, 0,21, 0x80, 0,250, 0x90,57, 1,10, 
0x80, 0,229, 0x90,57, 0,208, 0x81, 0,32, 0x91,69, 0,26, 0x80, 0,234, 0x90,57, 1,5, 0x80, 0,234, 0x90,57, 
0,203, 0x81, 0,36, 0x91,68, 0,21, 0x80, 0,250, 0x90,56, 1,10, 0x80, 0,229, 0x90,56, 0,172, 0x81, 0,68, 
0x91,71, 0,26, 0x80, 0,234, 0x90,56, 1,5, 0x80, 0,234, 0x90,56, 0,208, 0x81, 0,31, 0x91,76, 0,21, 0x80, 
0,250, 0x90,57, 1,10, 0x80, 0,229, 0x90,57, 0,208, 0x81, 0,32, 0x91,72, 0,26, 0x80, 0,234, 0x90,57, 1,5, 
0x80, 0,234, 0x90,57, 0,182, 0x81, 0,57, 0x91,74, 0,73, 0x80, 0,198, 0x90,56, 1,10, 0x80, 0,229, 0x90,56, 
0,203, 0x81, 0,37, 0x91,71, 0,26, 0x80, 0,234, 0x90,56, 1,4, 0x80, 0,235, 0x90,56, 0,135, 0x80, 0,42, 
0x81, 0,62, 0x90,72, 1,213, 0x80, 0,42, 0x90,76, 1,239, 0x90,81, 3,221, 0x80, 0,5, 0x90,80, 7,203, 0x80, 
0xF0]
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        if pgb.button_select() or pgb.button_start():
            pause_screen()
        dx=0
        dy=1
        rotate=False

        if pgb.button_A() and not n==6:
            if last_button!="UP":
                rotate=True
            last_button="UP"
        elif pgb.button_left():
                last_button="RIGHT"
                dx=-1
        elif pgb.button_right():
                last_button="RIGHT"
                dx=1
        elif pgb.button_down():
            last_button="DOWN"
            delay=0
        else:
            last_button="NONE"
        if pgb.button_B() or pgb.button_down():
            delay=50
        else:
            delay=500

        # save current position to restore it
        # in case the requested move generates a collision
        for i in range(4):
            prev_x[i] = x[i]
            prev_y[i] = y[i]
        
        # move left & right
        for i in range(4):
            x[i]+=dx
            
        if collision(x, y):
            # collision detected => impossible move
            # => restore previous position
            for i in range(4):
                x[i] = prev_x[i]
                y[i] = prev_y[i]
            
        # rotate
        if rotate:
            # center of rotation
            x0 = x[1]
            y0 = y[1]
            for i in range(4):
                x_=y[i]-y0
                y_=x[i]-x0
                x[i]=x0-x_
                y[i]=y0+y_
            
            if collision(x, y):
                # collision detected => impossible move
                # => restore previous position
                for i in range(4):
                    x[i] = prev_x[i]
                    y[i] = prev_y[i]
            else:
                has_rotated=True

        # move down
        ticks_ms = time.ticks_ms()
        if time.ticks_diff(ticks_ms, now) > delay:
            now = ticks_ms
            
            if has_rotated:
                freq=180
            elif delay>0:
                freq=140
            else:
                freq=0
            has_rotated = False
            
            for i in range(4):
                prev_x[i]=x[i]
                prev_y[i]=y[i]
                y[i]+=dy
               
            if collision(x,y):
                # collision detected
                
                # collision at the top of the screen?
                # => game over
                for i in range(4):
                    if prev_y[i]<=1:
                        return
                
                # => Store the last good position in the field
                for i in range(4):
                    field[prev_y[i]][prev_x[i]]=n
                
                # => choose randomly the next trinomino
                n = next_n
                next_n = randint(0, 6)
                for i in range(4):
                    x[i]=(tetrominos[n][i]) % 2;
                    y[i]=int(tetrominos[n][i] / 2);
                    
                    x[i]+=int(GRID_COLS/2)
            
        # check lines
        k=GRID_ROWS-1
        for i in range(GRID_ROWS-1,0,-1):
            count=0
            for j in range(GRID_COLS):
                if field[i][j]>=0:
                    count+=1
                field[k][j]=field[i][j]
            if count<GRID_COLS:
                k-=1
            else:
                # ith line complete
                lines+=1
                score+=40
                
                # make the line blink white <-> black
                
                for l in range(3):
                    pgb.fill_rect(GRID_OFFSET*BLOCK_SIZE,i*BLOCK_SIZE,
                                  GRID_COLS*BLOCK_SIZE,BLOCK_SIZE,WHITE)
                    pgb.show()
                    time.sleep(0.050)
                    pgb.fill_rect(GRID_OFFSET*BLOCK_SIZE,i*BLOCK_SIZE,
                                  GRID_COLS*BLOCK_SIZE,BLOCK_SIZE,BLACK)
                    pgb.show()
                    time.sleep(0.050)
                
        
        #####################################################################
        # update screen 
        
        # background
        draw_background()

        # draw all the previous blocks
        for i in range(GRID_ROWS):
            for j in range(GRID_COLS):
                if field[i][j]>=0:
                    # non empty
                    draw_block(j,i,field[i][j])
        
        # draw the current block
        for i in range(4):
            draw_block(x[i],y[i],n)
        
        # transfer the frame buffer to the actual screen over the SPI bus
        pgb.show()

        
title_screen()   
musicthread= _thread.start_new_thread(play_music, ())
while True:
    main_game()
    game_over_screen()