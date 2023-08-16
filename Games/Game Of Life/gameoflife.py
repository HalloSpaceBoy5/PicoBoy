# Original source files for GameOfLife.py by Matthieu Mistler
# Modified By HalloSpaceBoy for the PicoBoy
from PicoGameBoy import PicoGameBoy
import random
import os
import time
pgb = PicoGameBoy()
pgb.free_mem()
os.rename("./main.py", "./GameOfLife.py")
os.rename("./title.py", "./main.py")
# Predefined colors
BLACK = PicoGameBoy.color(0,0,0)
WHITE = PicoGameBoy.color(255,255,255)
RED = PicoGameBoy.color(255,0,0)
GREEN = PicoGameBoy.color(0,255,0)
BLUE = PicoGameBoy.color(0,0,255)

def title_screen():
    # title screen
    now = time.ticks_ms()
    while pgb.any_button()==False:
        if pgb.button_Home():
            x=open("/noboot", "w")
            x.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.load_image("gameoflife_title.bin")
        pgb.show()
        
        if time.ticks_diff(time.ticks_ms(), now) > 200:
            now = time.ticks_ms()
            pgb.create_text("PRESS ANY BUTTON",-1,150,WHITE)
            pgb.show()
            while time.ticks_diff(time.ticks_ms(), now) < 200:
                time.sleep(0.020)
            now = time.ticks_ms()
def game_over_screen():
    pgb.fill_rect(10,90,220,80,BLACK)
    pgb.center_text("GAME OVER",WHITE)
    pgb.text("Press A to play again.", 35, 125, WHITE)
    pgb.text("Press home to quit.", 40, 140, WHITE)
    pgb.show()
    while True:
        if pgb.button_Home():
            x=open("/noboot", "w")
            x.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        elif pgb.button_A():
            return
cursor=bytearray(b'\x08>\x08>\x08>\x08>\x08>\xff\xff\xff\xff\x08>\x08>\xff\xff\xff\xff\x08>\x08>\x08>\x08>\x08>')
# run the animation
title_screen()
def main_game():
    global cursor
    lastboard=[]
    divtime=1
    # Game parameters
    WIDTH = pgb.width        # screen width in pixels
    HEIGHT = pgb.height      # screen height in pixels
    CELL_SIZE = 8            # width and height of cells in pixels
    POPULATION_PERCENT = 12  # Initial population size as function of total surface in %
    BACKGROUND_COLOR = BLACK
    CELL_COLOR = GREEN

    # Board initialisation
    BOARD_SIZE_X = int(WIDTH/CELL_SIZE)
    BOARD_SIZE_Y = int(HEIGHT/CELL_SIZE)
    BOARD_SURFACE = BOARD_SIZE_X * BOARD_SIZE_Y

    board=[]
    for i in range(0,BOARD_SIZE_Y):
        line = []
        for j in range(0,BOARD_SIZE_X):
            line.append(0)
        board.append(line)


    # Initial number of cells 
    NUMBER_OF_CELLS = int((POPULATION_PERCENT)/100 * BOARD_SURFACE);
    editing=True
    posx=120
    posy=120
    pgb.fill(BLACK)
    pgb.show()
    pgb.add_sprite(cursor, 4,4)
    time.sleep(0.5)
    while editing:
        if pgb.button_Home():
            x=open("/noboot", "w")
            x.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        if pgb.button_left() and posx>0:
            posx=posx-8
        if pgb.button_right() and posx<BOARD_SIZE_X*8-8:
            posx=posx+8
        if pgb.button_down() and posy<BOARD_SIZE_Y*8-8:
            posy=posy+8
        if pgb.button_up() and posy>0:
            posy=posy-8
        if pgb.button_A():
            board[int(posy/8)][int(posx/8)]=CELL_COLOR
        if pgb.button_B():
            board[int(posy/8)][int(posx/8)]=BACKGROUND_COLOR
        if pgb.button_select():
            for i in range(0,NUMBER_OF_CELLS):
                board[random.randint(0,BOARD_SIZE_Y-1)][random.randint(0,BOARD_SIZE_X-1)] = CELL_COLOR
        if pgb.button_start():
            time.sleep(0.25)
            editing=False
        pgb.fill(BACKGROUND_COLOR)
        pgb.create_text("Use the cursor to", -1, 10, WHITE)
        pgb.create_text("draw a design", -1, 20, WHITE)
        for i in range(0,BOARD_SIZE_Y):
            for j in range(0,BOARD_SIZE_X):
                if board[i][j]!=0:
                    pgb.fill_rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE,CELL_SIZE,board[i][j])
        
        pgb.sprite(0, posx+2,posy+2)
        pgb.show()
        time.sleep(0.08)
        ng=False
    while True:
        lboard=[]
        if pgb.button_Home():
                x=open("/noboot", "w")
                x.close()
                pgb.fill(PicoGameBoy.color(0,0,0))
                pgb.show()
                machine.reset()
                break
        if pgb.button_start():
            return True
            ng=True
        # Update the screen
        pgb.fill(BACKGROUND_COLOR)
        for i in range(0,BOARD_SIZE_Y):
            for j in range(0,BOARD_SIZE_X):
                if board[i][j]!=0:
                    pgb.fill_rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE,CELL_SIZE,board[i][j])
        pgb.show()
        
        # count number of neighbors for each position
        for i in range(0,BOARD_SIZE_Y):
            for j in range(0,BOARD_SIZE_X):
                number_neighbors = 0
                
                if i>1 and j>1 and board[i-1][j-1]!=0:
                    number_neighbors+=1
                if i>1 and board[i-1][j]!=0:
                    number_neighbors+=1
                if i>1 and j<BOARD_SIZE_X-1 and board[i-1][j+1]!=0:
                    number_neighbors+=1
                if i<BOARD_SIZE_Y-1 and j>1 and board[i+1][j-1]!=0:
                    number_neighbors+=1
                if i<BOARD_SIZE_Y-1 and board[i+1][j]!=0:
                    number_neighbors+=1
                if i<BOARD_SIZE_Y-1 and j<BOARD_SIZE_Y-1 and board[i+1][j+1]!=0:
                    number_neighbors+=1
                if j>1 and board[i][j-1]!=0:
                    number_neighbors+=1
                if j<BOARD_SIZE_X-1 and board[i][j+1]!=0:
                    number_neighbors+=1
                    
                
                # The game's rules
                if board[i][j]!=BLACK:
                    # There is a living cell at row #i col #j
                    # It survives only if it surrounded by 2 or 3 neighbors
                    if number_neighbors<2 or number_neighbors>3:
                        board[i][j] = 0
                        lboard.append(0)
                else:
                    # row #i col #j is empty
                    # Create a new cell at (i,j) if it is surrounded by exactly 3 neighbors
                    if number_neighbors==3:
                        board[i][j] = CELL_COLOR
                        lboard.append(1)
        divtime=divtime+1
        if lastboard==lboard and ng==False:
            return False
        lastboard=lboard
while True:
    if not main_game():
        game_over_screen()
