from PicoBoySDK import PicoBoySDK
from os import listdir, remove, mkdir
from math import sqrt
from time import sleep
from random import randint
from framebuf import FrameBuffer, RGB565

PicoBoy=PicoBoySDK(namespace="Puzzle Slide", tick_time=0)

def split_chunks(path,size):
    # takes ascii-based pbd image and converts to binary rgb565 chunks using framebuffer as temp storage
    data=[]
    # open and parse pbd data
    with open(path, "r") as f:
        for i in range(30):
            comp=[]
            for x in f.readline().split(":"):
                comp.append(int(x))
            data.append(comp)
    # init vars based off of chunk size (180 screen size)
    pixelsize=6
    bigsize=int(sqrt(size))
    chunksize=int(180/bigsize)
    sprites=[]
    # plot pbd data onto framebuffer, generating rgb565 data
    ps=int(180/len(data))
    y=-1
    for i in data:
        y+=1
        x=-1
        for f in i:
            x+=1
            PicoBoy.fill_rect(x*ps,y*ps,ps,ps,f)
    # check for placeholder, delete it
    try:
        remove("/Puzzle Slide/placeholder.pbimg")
    except:
        "already gone"
    # check for temp, if not made make it
    try:
        mkdir("/Puzzle Slide/Temp")
    except:
        ""
    # list all files in temp and delete
    fs=listdir("/Puzzle Slide/Temp")
    for file in fs:
        remove("/Puzzle Slide/Temp/"+file)
        
    #parse rgb565 data in framebuffer and read chunks into bin files
    PicoBoy.show_screen()
    # iterate through the y positions
    for f in range(bigsize):
        #iterate through the x positions
        for i in range(bigsize):
            #calculate starting position within buffer
            startingpos=(i*(480*chunksize))+(f*(chunksize*2))
            #iterate through pixels in buffer, line by line, and append them to a file
            with open("/Puzzle Slide/Temp/"+str(i)+"-"+str(f)+".bin", "ab") as w:
                for h in range(chunksize):
                    print(startingpos+(h*480),startingpos+(h*480)+(chunksize*2),startingpos, i, f)
                    # seek starting position with refrence to the large chunks, then within refrence to the working chunk
                    # iterate through lines, wrapping around each time.
                    w.write(bytes(PicoBoy.buffer[startingpos+(h*480):startingpos+(h*480)+(chunksize*2)]))

def mainloop(puzzle,mode, size):
    if type(puzzle[1])== int:
        numbers=True
    else:
        if mode==0:
            split_chunks(f"/Puzzle Slide/{puzzle}.pbd", size)
    
                
    PicoBoy.Fill_Screen((100,100,100))
    sizeroot=int(sqrt(size))
    sizechunk=int(180/sizeroot)
    while True:
        for y in range(sizeroot):
            for x in range(sizeroot):
                PicoBoy.Load_Small_Image("Temp/"+str(y)+"-"+str(x)+".bin",int(sizechunk*1.4)*x,int(sizechunk*1.4)*y,sizechunk,sizechunk)
        PicoBoy.Update()
        # render puzzle

                
                
                
            
    

def game(puzzles, mode):
    difficulty=randint(1,3) #1=9 tiles, 2=16 tiles, 3=25 tiles
    if puzzles==0:
        lop=["Sunny Day", "Tree", "PB Logo", "Face"]
    if puzzles==1:
        try:
            directory=listdir("/Puzzle Slide/")
        except:
            return 0
        files=[]
        for item in directory:
            if ".pbd" in item:
                files.append(item)
        for i,file in enumerate(files):
            files[i]=file.replace(".pbd","")
        lop=files[:]
        if len(lop)==0:
            return 1
    if puzzles==2:
        lop=[1]
    # insert choose drawing here (unless numbers)
    puzzle=lop[randint(0,len(lop)-1)]
    if difficulty==1:
        size=9
    elif difficulty==2:
        size=16
    else:
        size=25
    mainloop(puzzle, mode, size)


puzzles=0 #1 for regular, 0 for custom from paint, 2 for numbers
mode=0 #0 for free play, 1 for timed
puzzles=1
game(puzzles, mode)
while True:
    if PicoBoy.Button("A"):
        puzzles=1
    if PicoBoy.Button("B"):
        puzzles=0
    if PicoBoy.Button("Select"):
        puzzles=2
    if PicoBoy.Button("Start"):
        value=game(puzzles, mode)
        if value==0:
            print("Err: Paint not installed")
        if value==1:
            print("Err: No Drawings")