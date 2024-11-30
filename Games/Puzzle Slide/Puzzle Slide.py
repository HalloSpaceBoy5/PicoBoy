# Written by HalloSpaceBoy
from PicoBoySDK import PicoBoySDK
from os import listdir, remove, mkdir
from time import sleep
from random import randint, choice
from framebuf import FrameBuffer, RGB565
from machine import RTC
from array import array

rtc = machine.RTC()
PicoBoy=PicoBoySDK(namespace="Puzzle Slide", tick_time=0.01)

def readchunk_mask(filename,x2,y2,w,h,cmask=57351):
    with open(filename,"rb") as r:
            for x in range(h):
                tempfb=FrameBuffer(bytearray(r.read(2*w)),w,1,RGB565)
                PicoBoy.blit(tempfb,x2,y2+x,PicoBoy.color(31,17,9))
                del tempfb


bgcolor=(69,69,69)


def split_chunks(path,size,bigsize):
    data=[]
    with open(path, "r") as f:
        for i in range(30):
            comp=[]
            for x in f.readline().split(":"):
                comp.append(int(x))
            data.append(comp)
    pixelsize=6
    chunksize=int(180/bigsize)
    sprites=[]
    PicoBoy.Load_Image("background.pbimg")
    PicoBoy.Fill_Rect(48, 100, 144, 50, bgcolor)
    PicoBoy.Fill_Rect(40, 108, 160, 34, bgcolor)
    PicoBoy.poly(40,100,array('h',[8,0,0,8,8,8]),PicoBoy.color(*bgcolor),True)
    PicoBoy.poly(199,100,array('h',[0,8,-8,0,-8,8]),PicoBoy.color(*bgcolor),True)
    PicoBoy.poly(40,150,array('h',[8,0,0,-8,8,-8]),PicoBoy.color(*bgcolor),True)
    PicoBoy.poly(197,150,array('h',[0,-8,-8,0,-8,-8]),PicoBoy.color(*bgcolor),True)
    PicoBoy.Create_Text("Loading Puzzle...",-1,112,(255,255,255))
    PicoBoy.Create_Text("Please Wait",-1,132,(255,255,255))
    PicoBoy.show_screen()
    ps=int(180/len(data))
    y=-1
    for i in data:
        y+=1
        x=-1
        for f in i:
            x+=1
            PicoBoy.fill_rect(x*ps,y*ps,ps,ps,f)
    try:
        remove("/Puzzle Slide/placeholder.pbimg")
    except:
        "already gone"
    try:
        mkdir("/Puzzle Slide/Temp")
    except:
        ""
    fs=listdir("/Puzzle Slide/Temp")
    for file in fs:
        remove("/Puzzle Slide/Temp/"+file)
    for f in range(bigsize):
        for i in range(bigsize):
            startingpos=(i*(480*chunksize))+(f*(chunksize*2))
            with open("/Puzzle Slide/Temp/"+str(i)+"-"+str(f)+".bin", "ab") as w:
                for h in range(chunksize):
                    w.write(bytes(PicoBoy.buffer[startingpos+(h*480):startingpos+(h*480)+(chunksize*2)]))
                    
    
def hue_to_rgb888(hue_multiplier, brightness=0.92):
    H = hue_multiplier * 360
    S = 1
    V = brightness
    C = V * S
    X = C * (1 - abs((H / 60) % 2 - 1))
    m = V - C

    if 0 <= H < 60:
        R1, G1, B1 = C, X, 0
    elif 60 <= H < 120:
        R1, G1, B1 = X, C, 0
    elif 120 <= H < 180:
        R1, G1, B1 = 0, C, X
    elif 180 <= H < 240:
        R1, G1, B1 = 0, X, C
    elif 240 <= H < 300:
        R1, G1, B1 = X, 0, C
    elif 300 <= H < 360:
        R1, G1, B1 = C, 0, X
    R = int((R1 + m) * 255)
    G = int((G1 + m) * 255)
    B = int((B1 + m) * 255)

    return (R, G, B)



def mainloop(puzzle,mode, size,typ,time,bigsize, shownumbers):
    if type(puzzle)== int:
        numbers=True
        shownumbersasa=True
    else:
        numbers=False
        if typ==0:
            split_chunks(f"/Puzzle Slide/{puzzle}.pbd", size,bigsize)
        if typ==1:
            split_chunks(f"/Paint/{puzzle}.pbd", size,bigsize)
    if time==-1:
        timed=False
    else:
        timed=True
    
                
    PicoBoy.Fill_Screen(bgcolor)
    sizeroot=bigsize
    sizechunk=int(180/sizeroot)
    ogrid=[]
    grid=[]
    for y in range(sizeroot):
        for x in range(sizeroot):
            ogrid.append(str(y)+"-"+str(x))
    for g in range(sizeroot):
        subg=[]
        for h in range(sizeroot):
            ch=choice(ogrid)
            subg.append(ch)
            ogrid.remove(ch)
        grid.append(subg)
    del ogrid
    cpos=[0,0]
    selected=[]
    offset=int(((sizeroot-1)*3)/2)
    update=True
    seconds=0
    minutes=0
    hours=0
    
    dt=rtc.datetime()
    inittime=(dt[4],dt[5],dt[6])
    elapsed_seconds = 0
    paused = False
    pause_start_time = None
    total_pause_duration = 0
    while True:
        dt = rtc.datetime()
        elapsed_seconds = (dt[4] - inittime[0]) * 3600 + (dt[5] - inittime[1]) * 60 + (dt[6] - inittime[2])
        elapsed_seconds -= total_pause_duration
        if timed:
            elapsed_seconds=time-elapsed_seconds
        if elapsed_seconds<1 and timed:
            PicoBoy.Update(noclear=True)
            sleep(0.25)
            while True:
                PicoBoy.fill_rect(18,70,204,120,PicoBoy.color(50,50,50))
                PicoBoy.fill_rect(10,78,220,104,PicoBoy.color(50,50,50))
                PicoBoy.poly(10,70,array('h',[8,0,0,8,8,8]),PicoBoy.color(50,50,50),True)
                PicoBoy.poly(229,70,array('h',[0,8,-8,0,-8,8]),PicoBoy.color(50,50,50),True)
                PicoBoy.poly(10,190,array('h',[8,0,0,-8,8,-8]),PicoBoy.color(50,50,50),True)
                PicoBoy.poly(229,190,array('h',[0,-8,-8,0,-8,-8]),PicoBoy.color(50,50,50),True)
                PicoBoy.Create_Text("Puzzle Failed!",-1,80,(255,255,255))
                PicoBoy.Create_Text("Press The A Button", -1, 115, (255,255,255))
                PicoBoy.Create_Text("to try again.", -1, 129, (255,255,255))
                PicoBoy.Create_Text("Press the B Button", -1, 150, (255,255,255))
                PicoBoy.Create_Text("to go to the Main Menu", -1, 165, (255,255,255))
                PicoBoy.Update(noclear=True)
                if PicoBoy.Button("A"):
                    sleep(0.25)
                    return True
                if PicoBoy.Button("B"):
                    sleep(0.25)
                    return False
        check=True
        for g,i in enumerate(grid):
            for h,f in enumerate(i):
                if not f == str(g)+"-"+str(h):
                    check=False
                    
        if not check or not timed:
            hours = elapsed_seconds // 3600
            minutes = (elapsed_seconds % 3600) // 60
            seconds = elapsed_seconds % 60
        elif timed:
            hours = (time-elapsed_seconds) // 3600
            minutes = ((time-elapsed_seconds) % 3600) // 60
            seconds = (time-elapsed_seconds) % 60
        if seconds<0:
            seconds=60+(seconds-1)
            minutes-=1
        if seconds<10:
            secondsstr="0"+str(seconds)
        else:
            secondsstr=str(seconds)
        if minutes<0:
            minutes=60+minutes
            hours-=1
        if minutes<10:
            minutesstr="0"+str(minutes)
        else:
            minutesstr=str(minutes)
        if hours<0:
            hours=24+hours
        if hours<10:
            hoursstr="0"+str(hours)
        else:
            hoursstr=str(hours)
        if check:
            PicoBoy.Update(noclear=True)
            sleep(0.25)
            while True:
                PicoBoy.fill_rect(18,70,204,120,PicoBoy.color(50,50,50))
                PicoBoy.fill_rect(10,78,220,104,PicoBoy.color(50,50,50))
                PicoBoy.poly(10,70,array('h',[8,0,0,8,8,8]),PicoBoy.color(50,50,50),True)
                PicoBoy.poly(229,70,array('h',[0,8,-8,0,-8,8]),PicoBoy.color(50,50,50),True)
                PicoBoy.poly(10,190,array('h',[8,0,0,-8,8,-8]),PicoBoy.color(50,50,50),True)
                PicoBoy.poly(229,190,array('h',[0,-8,-8,0,-8,-8]),PicoBoy.color(50,50,50),True)
                PicoBoy.Create_Text("Puzzle Complete!",-1,80,(255,255,255))
                PicoBoy.Create_Text(f"Time: {hoursstr}:{minutesstr}:{secondsstr}", -1, 95, (255,255,255))
                PicoBoy.Create_Text("Press The A Button", -1, 115, (255,255,255))
                PicoBoy.Create_Text("to view the puzzle.", -1, 129, (255,255,255))
                PicoBoy.Create_Text("Press the B Button", -1, 150, (255,255,255))
                PicoBoy.Create_Text("to go to the Main Menu", -1, 165, (255,255,255))
                if PicoBoy.Button("A"):
                    sleep(0.1)
                    while True:
                        PicoBoy.Fill_Screen(bgcolor)
                        PicoBoy.Create_Text(f"Time: {hoursstr}:{minutesstr}:{secondsstr}", -1, 10, (255,255,255))
                        for y,subgrid in enumerate(grid):
                            for x,item in enumerate(subgrid):
                                if not numbers:
                                    PicoBoy.Load_Small_Image("/Puzzle Slide/Temp/"+item.replace("*","")+".bin", 30-offset+x*(sizechunk), 30-offset+y*(sizechunk), sizechunk, sizechunk)
                                else:
                                    lpos=item.split("-")
                                    index=(int(lpos[0])*sizeroot)+int(lpos[1])
                                    PicoBoy.Fill_Rect(32-offset+x*(sizechunk), 32-offset+y*(sizechunk), sizechunk, sizechunk,hue_to_rgb888(index/(sizeroot**2)))
                        PicoBoy.Outline_Rect(30-offset,30-offset,180+((sizeroot-1)),180+((sizeroot-1)),(255,255,255))
                        PicoBoy.Create_Text("Press B to return", -1, 220, (255,255,255))
                        PicoBoy.Update(noclear=True)
                        if PicoBoy.Button("B"):
                            sleep(0.25)
                            break
                if PicoBoy.Button("B"):
                    sleep(0.25)
                    return False
                PicoBoy.Update(noclear=True)
        PicoBoy.Fill_Rect(0,0,240,20,bgcolor)
        PicoBoy.Create_Text(f"Time: {hoursstr}:{minutesstr}:{secondsstr}", -1, 10, (255,255,255))
        if PicoBoy.Button("Left") and cpos[1]>0:
            if not selected==[]:
                old=grid[cpos[0]][cpos[1]]
                cpos[1]-=1
                grid[cpos[0]][cpos[1]+1]=grid[cpos[0]][cpos[1]]
                grid[cpos[0]][cpos[1]]=old
                update=True
            else:
                cpos[1]-=1
                update=True
            if numbers:
                sleep(0.07)
        elif PicoBoy.Button("Right") and cpos[1]<sizeroot-1:
            if not selected==[]:
                old=grid[cpos[0]][cpos[1]]
                cpos[1]+=1
                grid[cpos[0]][cpos[1]-1]=grid[cpos[0]][cpos[1]]
                grid[cpos[0]][cpos[1]]=old
                update=True
            else:
                cpos[1]+=1
                update=True
            if numbers:
                sleep(0.07)
        elif PicoBoy.Button("Up") and cpos[0]>0:
            if not selected==[]:
                old=grid[cpos[0]][cpos[1]]
                cpos[0]-=1
                grid[cpos[0]+1][cpos[1]]=grid[cpos[0]][cpos[1]]
                grid[cpos[0]][cpos[1]]=old
                update=True
            else:
                cpos[0]-=1
                update=True
            if numbers:
                sleep(0.07)
        elif PicoBoy.Button("Down") and cpos[0]<sizeroot-1:
            if not selected==[]:
                old=grid[cpos[0]][cpos[1]]
                cpos[0]+=1
                grid[cpos[0]-1][cpos[1]]=grid[cpos[0]][cpos[1]]
                grid[cpos[0]][cpos[1]]=old
                update=True
            else:
                cpos[0]+=1
                update=True
            if numbers:
                sleep(0.07)
        if PicoBoy.Button("A"):
            selected=cpos[:]
            update=True
            if numbers:
                sleep(0.07)
        elif PicoBoy.Button("B"):
            selected=[]
            update=True
            if numbers:
                sleep(0.07)
        if update:
            PicoBoy.Fill_Screen(bgcolor)
            PicoBoy.Create_Text(f"Time: {hoursstr}:{minutesstr}:{secondsstr}", -1, 10, (255,255,255))
            PicoBoy.Outline_Rect(28-offset,28-offset,184+(3*(sizeroot-1)),184+(3*(sizeroot-1)),(255,255,255))
            for y,subgrid in enumerate(grid):
                for x,item in enumerate(subgrid):
                    if not numbers:
                        PicoBoy.Load_Small_Image("/Puzzle Slide/Temp/"+item.replace("*","")+".bin", 30-offset+x*(sizechunk+3), 30-offset+y*(sizechunk+3), sizechunk, sizechunk)
                    else:
                        lpos=item.split("-")
                        index=(int(lpos[0])*sizeroot)+int(lpos[1])
                        PicoBoy.Fill_Rect(30-offset+x*(sizechunk+3), 30-offset+y*(sizechunk+3), sizechunk, sizechunk,hue_to_rgb888(index/(sizeroot**2)))
                    lpos=item.split("-")
                    pcolor=PicoBoy.Get_Pixel_Color(30-offset+x*(sizechunk+3)+6, 30-offset+y*(sizechunk+3)+6)
                    if (pcolor[0]/255)+(pcolor[1]/255)+(pcolor[2]/255)>1.5:
                        color=(0,0,0)
                    else:
                        color=(255,255,255)
                    if shownumbers:
                        PicoBoy.Create_Text(str((int(lpos[1])+1)+((int(lpos[0]))*sizeroot)), 30-offset+(x*(sizechunk+3))+1, 30-offset+(y*(sizechunk+3))+1, color)
            for i in range(sizeroot-1):
                i+=1
                PicoBoy.Vline(30-offset+i*(sizechunk+3)-2, 30-offset,180+(3*(sizeroot-1)), (255,255,255))
            for i in range(sizeroot-1):
                i+=1
                PicoBoy.Hline(30-offset,30-offset+i*(sizechunk+3)-2,180+(3*(sizeroot-1)), (255,255,255))
            PicoBoy.Outline_Rect(30-offset+cpos[1]*(sizechunk+3),30-offset+cpos[0]*(sizechunk+3),sizechunk,sizechunk,(255,0,0))
            PicoBoy.Outline_Rect(31-offset+cpos[1]*(sizechunk+3),31-offset+cpos[0]*(sizechunk+3),sizechunk-2,sizechunk-2,(0,0,255))
            if not selected==[]:
                PicoBoy.Outline_Rect(32-offset+cpos[1]*(sizechunk+3),32-offset+cpos[0]*(sizechunk+3),sizechunk-4,sizechunk-4,(0,255,0))
                PicoBoy.Outline_Rect(33-offset+cpos[1]*(sizechunk+3),33-offset+cpos[0]*(sizechunk+3),sizechunk-6,sizechunk-6,(0,255,0))
            update=False
        if PicoBoy.Button("Start"):
            paused=True
            pause_start_time = rtc.datetime()  
            while True:
                    PicoBoy.fill_rect(18,70,204,120,PicoBoy.color(50,50,50))
                    PicoBoy.fill_rect(10,78,220,104,PicoBoy.color(50,50,50))
                    PicoBoy.poly(10,70,array('h',[8,0,0,8,8,8]),PicoBoy.color(50,50,50),True)
                    PicoBoy.poly(229,70,array('h',[0,8,-8,0,-8,8]),PicoBoy.color(50,50,50),True)
                    PicoBoy.poly(10,190,array('h',[8,0,0,-8,8,-8]),PicoBoy.color(50,50,50),True)
                    PicoBoy.poly(229,190,array('h',[0,-8,-8,0,-8,-8]),PicoBoy.color(50,50,50),True)
                    PicoBoy.Create_Text("Game Paused",-1,80,(255,255,255))
                    PicoBoy.Create_Text("Press The A Button", -1, 115, (255,255,255))
                    PicoBoy.Create_Text("to continue the puzzle.", -1, 129, (255,255,255))
                    PicoBoy.Create_Text("Press the B Button", -1, 150, (255,255,255))
                    PicoBoy.Create_Text("to go to the Main Menu", -1, 165, (255,255,255))
                    if PicoBoy.Button("A"):
                        sleep(0.25)
                        update=True
                        paused=False
                        resume_time = rtc.datetime()
                        total_pause_duration += (resume_time[4] - pause_start_time[4]) * 3600
                        total_pause_duration += (resume_time[5] - pause_start_time[5]) * 60
                        total_pause_duration += (resume_time[6] - pause_start_time[6])
                        break
                    if PicoBoy.Button("B"):
                        sleep(0.25)
                        return False
                    PicoBoy.Update(noclear=True)
        PicoBoy.Update(noclear=True)

                
                
                
            
    

def game(puzzles, mode, difficulty,sn):
    difficulty+=1
    typ=puzzles
    if mode==0:
        strmode="Free Play"
    else:
        strmode="Timed"
    if difficulty==1:
        strdiff="Easy"
    elif difficulty==2:
        strdiff="Regular"
    else:
        strdiff="Hard"
    if puzzles==0:
        lop=["Doge", "Dragon", "Gemstone", "Griffin", "Mountian", "Planet", "Rainbow","Skull","Sunset","Tree"]
    if puzzles==1:
        try:
            directory=listdir("/Paint/")
        except:
            PicoBoy.Fill_Screen(bgcolor)
            readchunk_mask("logo.pbimg",9, 10, 221,21)
            while True:
                PicoBoy.Fill_Rect(0,31,240,209,bgcolor)
                PicoBoy.Create_Text("Error!", -1, 80,(255,255,255))
                PicoBoy.Create_Text("The Paint app is not", -1, 120,(255,255,255))
                PicoBoy.Create_Text("installed or is corrupted.", -1, 132,(255,255,255))
                PicoBoy.Create_Text("Press any button to return", -1, 210,(255,255,255))
                PicoBoy.Create_Text("to the main menu.", -1, 222,(255,255,255))
                if PicoBoy.Button("Any"):
                    sleep(0.1)
                    return
                PicoBoy.Update(noclear=True)
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
        puzzle=1
    if not puzzles==2:
        opt=0
        optlength=len(lop)-1
        offset=0
        sleep(.2)
        PicoBoy.Fill_Screen(bgcolor)
        readchunk_mask("logo.pbimg",9, 10, 221,21)
        while True:
            PicoBoy.Fill_Rect(0,31,240,209,bgcolor)
            PicoBoy.Create_Text("Mode: "+strmode,-1,50,(255,255,255))
            PicoBoy.Create_Text("Difficulty: "+strdiff,-1,65,(255,255,255))
            PicoBoy.Create_Text("Please Choose a Puzzle:",-1,90,(255,255,255))
            if PicoBoy.Button("Up"):
                if opt>0:
                    opt-=1
                    sleep(0.07)
                elif opt==0 and offset>0:
                        offset-=1
                        sleep(0.07)
            if PicoBoy.Button("Down"):
                if optlength<=5:
                    if opt<optlength:
                        opt+=1
                        sleep(0.07)
                else:
                    if opt<4:
                        opt+=1
                        sleep(0.07)
                    elif opt+offset<optlength:
                        offset+=1
                        sleep(0.07)
            if PicoBoy.Button("A"):
                puzzle=lop[opt+offset]
                break
            if optlength>5:
                PicoBoy.Fill_Rect(180, 105, 15, 98, (120,120,120))
                PicoBoy.Fill_Rect(182, 107+int((offset / (optlength - 4)) * (94 - int(94*(5/optlength)))), 11, int(94*(5/optlength)), (200, 200, 200))
                boffset=-15
            else:
                boffset=0
            for i in range(optlength+1):
                if i==5:
                    break
                PicoBoy.Create_Text(lop[i+offset], 120- int(len(lop[i+offset])/2 * 8)+boffset, 110+i*20,(255,255,255))
            PicoBoy.Outline_Rect(55+boffset, 106+opt*20, 130, 15, (255,255,255))
            PicoBoy.Create_Text("Press B to return", -1, 210,(255,255,255))
            PicoBoy.Create_Text("to the main menu.", -1, 222,(255,255,255))
            if PicoBoy.Button("B"):
                sleep(0.25)
                return
            PicoBoy.Update(noclear=True)
    if difficulty==1:
        size=9
        bs=3
        time=100
    elif difficulty==2:
        size=16
        bs=4
        time=200
    else:
        size=25
        bs=5
        time=300
    if mode==0:
        time=-1
    while True:
        if not mainloop(puzzle, mode, size, typ, time,bs,sn):
            return


puzzles=0 #0 for regular, 1 for custom from paint, 2 for numbers
mode=0 #0 for free play, 1 for timed
difficulty=0
opt=0
skip=False
ns=False

wait=False
PicoBoy.Load_Image("background.pbimg")
readchunk_mask("logo.pbimg",9, 5, 221,21)
while True:
    PicoBoy.Fill_Rect(40, 38, 160,192,bgcolor)
    PicoBoy.Fill_Rect(48, 30, 144,205,bgcolor)
    PicoBoy.poly(40,30,array('h',[8,0,0,8,8,8]),PicoBoy.color(*bgcolor),True)
    PicoBoy.poly(199,30,array('h',[0,8,-8,0,-8,8]),PicoBoy.color(*bgcolor),True)
    PicoBoy.poly(40,235,array('h',[8,0,0,-8,8,-8]),PicoBoy.color(*bgcolor),True)
    PicoBoy.poly(197,235,array('h',[0,-8,-8,0,-8,-8]),PicoBoy.color(*bgcolor),True)
    
    PicoBoy.Create_Text("Puzzle Type:",-1,42,(255,255,255))
    strpuzzles=""
    if puzzles==1:
        strpuzzles="Paint"
    elif puzzles==0:
        strpuzzles="Built In"
    else:
        strpuzzles="Colors"
    PicoBoy.Create_Text(strpuzzles,-1,56,(255,255,255))
    PicoBoy.Create_Text("Game Mode:",-1,82,(255,255,255))
    strmode=""
    if mode==0:
        strmode="Free Play"
    else:
        strmode="Timed"
    PicoBoy.Create_Text(strmode,-1,96,(255,255,255))
    PicoBoy.Create_Text("Difficulty:",-1,122,(255,255,255))
    strdiff=""
    if difficulty==0:
        strdiff="Easy"
    elif difficulty==1:
        strdiff="Regular"
    else:
        strdiff="Hard"
    PicoBoy.Create_Text(strdiff,-1,136,(255,255,255))
    PicoBoy.Create_Text("Show Numbers:",-1,162,(255,255,255))
    PicoBoy.Create_Text(str(ns),-1,176,(255,255,255))
    PicoBoy.Load_Small_Image("playbutton.pbimg",67, 198,105,30)
    if opt<4:
        PicoBoy.Outline_Rect(65,37+(40*opt),107,32,(255,255,255))
        PicoBoy.poly(180,49+(40*opt),array('h',[0,8,8,4,0,0]),PicoBoy.color(255,255,255),True)
        PicoBoy.poly(57,49+(40*opt),array('h',[0,8,-8,4,0,0]),PicoBoy.color(255,255,255),True)
    else:
        PicoBoy.Outline_Rect(67,197,107,32,(255,255,255))
    if PicoBoy.Button("Down"):
        if opt<4:
            opt+=1
        wait=True
    if PicoBoy.Button("Up"):
        if opt>0:
            opt-=1
        wait=True
    if PicoBoy.Button("Left"):
        if opt==0:
            puzzles-=1
            if puzzles<0:
                puzzles=2
        elif opt==1:
            mode-=1
            if mode<0:
                mode=1
        elif opt==2:
            difficulty-=1
            if difficulty<0:
                difficulty=2
        elif opt==3:
            ns=not ns
        wait=True
    if PicoBoy.Button("Right"):
        if opt==0:
            puzzles+=1
            if puzzles>2:
                puzzles=0
        elif opt==1:
            mode+=1
            if mode>1:
                mode=0
        elif opt==2:
            difficulty+=1
            if difficulty>2:
                difficulty=0
        elif opt==3:
            ns=not ns
        wait=True
    if (opt==4 and PicoBoy.Button("A")) or PicoBoy.Button("Start"):
        sleep(0.1)
        game(puzzles, mode, difficulty,ns)
        PicoBoy.Load_Image("background.pbimg")
        readchunk_mask("logo.pbimg",9, 10, 221,21)
        skip=True
        wait=False
        opt=0
    elif PicoBoy.Button("A") and opt<4:
        opt+=1
        wait=True
    if not skip:
        PicoBoy.Update(noclear=True)
    else:
        skip=False
    if wait:
        sleep(0.05)