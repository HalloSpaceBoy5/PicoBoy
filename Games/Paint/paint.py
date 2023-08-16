#Original program for PicoBoy by HalloSpaceBoy
from PicoGameBoy import PicoGameBoy
from os import rename, remove, listdir
rename("./main.py", "./paint.py")
rename("./title.py", "./main.py")
del rename
from time import sleep
from gc import collect
pgb=PicoGameBoy()
pixelsize=8

COLORWHITE=PicoGameBoy.color(255,255,255)
COLORBLACK=PicoGameBoy.color(0,0,0)

def draw_cursor(x, y, p):
    global COLORWHITE
    pgb.fill_rect(x,y,p,1, COLORBLACK)
    pgb.fill_rect(x,y+p,p+1,1, COLORBLACK)
    pgb.fill_rect(x,y,1,p, COLORBLACK)
    pgb.fill_rect(x+p,y,1,p, COLORBLACK)
    pgb.fill_rect(x+1,y+1,p-2,1, COLORWHITE)
    pgb.fill_rect(x+1,y+p-1,p-1,1, COLORWHITE)
    pgb.fill_rect(x+1,y+1,1,p-2, COLORWHITE)
    pgb.fill_rect(x+p-1,y+1,1,p-2, COLORWHITE)

def check_home():
    if pgb.button_Home():
        homebootstop=open("/noboot", "w")
        homebootstop.close()
        pgb.fill(COLORBLACK)
        pgb.show()
        machine.reset()
        

def draw_grid(p):
    for i in range(int(240/p)):
        pgb.hline(0, i*p, 240, PicoGameBoy.color(225,225,225))
    for i in range(int(240/p)):
        pgb.vline(i*p, 0, 240, PicoGameBoy.color(225,225,225))
        
def display_drawing(lis):
    ps=int(240/len(lis))
    y=-1
    for i in lis:
        y+=1
        x=-1
        for f in i:
            x+=1
            pgb.fill_rect(x*ps,y*ps,ps,ps,PicoGameBoy.color(*f))
            
    
def menu():
    global COLORWHITE
    global drawing
    sleep(0.25)
    options=["Tools", "Save", "Load", "Delete Save"]
    option=0
    while True:
        collect()
        check_home()
        pgb.fill(COLORWHITE)
        display_drawing(drawing)
        draw_grid(pixelsize)
        pgb.fill_rect(10,10,150,5+15*len(options)-1, PicoGameBoy.color(150,150,150))
        for i in range(len(options)):
            pgb.create_text(options[i], 15, 15+i*15, COLORWHITE)
        if pgb.button_up() and option>0:
            option-=1
            sleep(0.1)
        if pgb.button_down() and option<len(options)-1:
            option+=1
            sleep(0.1)
        pgb.rect(13, 12+option*15, 146, 13, COLORWHITE)
        if pgb.button_A():
            opt=options[option]
            if opt=="Save":
                sleep(0.25)
                po=listdir("/")
                files=[]
                for i in po:
                    r=i.split('.')
                    if r[len(r)-1]=="pbd":
                        files.append(i.replace(".pbd", ""))
                options=["Drawing 1", "Drawing 2", "Drawing 3", "Drawing 4", "Drawing 5", "Drawing 6", "Drawing 7", "Drawing 8", "Drawing 9", "Drawing 10"]
                pos=-1
                for opt in options:
                    pos+=1
                    if opt in files:
                        options[pos]=options[pos]+" (Used)"
                option=0
                go=True
                while go:
                    check_home()
                    pgb.fill(COLORWHITE)
                    display_drawing(drawing)
                    draw_grid(pixelsize)
                    pgb.fill_rect(10,10,150,5+15*len(options)-1, PicoGameBoy.color(150,150,150))
                    for i in range(len(options)):
                        pgb.create_text(options[i], 15, 15+i*15, COLORWHITE)
                    if pgb.button_up() and option>0:
                        option-=1
                        sleep(0.1)
                    if pgb.button_down() and option<len(options)-1:
                        option+=1
                        sleep(0.1)
                    pgb.rect(13, 12+option*15, 146, 13, COLORWHITE)
                    if pgb.button_A():
                        file=options[option]
                        if "Used" in file:
                            pgb.fill_rect(10,90,220,100,COLORBLACK)
                            pgb.center_text("Are You Sure?",COLORWHITE)
                            pgb.create_text("Are you sure you want", -1, 135, COLORWHITE)
                            pgb.create_text("to replace this drawing?.", -1, 147, COLORWHITE)
                            pgb.create_text("A for yes, B for no.", -1, 157, COLORWHITE)
                            pgb.show()
                            sleep(0.5)
                            while True:
                                if pgb.button_A():
                                    break
                                    os.remove(file)
                                if pgb.button_B():
                                    del options
                                    return
                        pgb.fill_rect(10,90,220,80,COLORBLACK)
                        pgb.center_text("Saving",COLORWHITE)
                        pgb.create_text("Saving Drawing...", -1, 135, COLORWHITE)
                        pgb.create_text("Do not turn off console.", -1, 147, COLORWHITE)
                        pgb.show()
                        del options
                        collect()
                        with open("/games/paint", "a") as w:
                            w.write("---PICOBOYFILELIST---"+file.replace(" (Used)","")+".pbd")
                        del w
                        with open(file.replace(" (Used)","")+".pbd", "a") as f:
                            for row in drawing:
                                for g,x in enumerate(row):
                                    r=[]
                                    for y in x:
                                        r.append(str(y))
                                    if not g == len(row)-1:
                                        f.write(",".join(r)+":")
                                    else:
                                        f.write(",".join(r))
                                f.write("\n")
                        del g
                        del r                
                        del f
                        del files
                        del po
                        po=listdir("/")
                        files=[]
                        for i in po:
                            r=i.split('.')
                            if r[len(r)-1]=="pbd":
                                files.append(i.replace(".pbd", ""))
                        options=["Drawing 1", "Drawing 2", "Drawing 3", "Drawing 4", "Drawing 5", "Drawing 6", "Drawing 7", "Drawing 8", "Drawing 9", "Drawing 10"]
                        pos=-1
                        for opt in options:
                            pos+=1
                            if opt in files:
                                options[pos]=options[pos]+" (Used)"
                        option=0
                        sleep(0.25)
                    if pgb.button_B() or pgb.button_select():
                        options=["Tools", "Save", "Load", "Delete Save"]
                        option=0
                        go=False
                    pgb.show()
            if opt=="Load":
                sleep(0.25)
                po=listdir("/")
                files=[]
                for i in po:
                    r=i.split('.')
                    if r[len(r)-1]=="pbd":
                        files.append(i.replace(".pbd", ""))
                options=[]
                del po
                pos=-1
                if not files==[]:
                    for opt in files:
                        pos+=1
                        options.append(opt)
                option=0
                while True:
                    if files==[]:
                        options=["Tools", "Save", "Load", "Delete Save"]
                        option=0
                        break
                    check_home()
                    pgb.fill(COLORWHITE)
                    display_drawing(drawing)
                    draw_grid(pixelsize)
                    pgb.fill_rect(10,10,150,5+15*len(options)-1, PicoGameBoy.color(150,150,150))
                    for i in range(len(options)):
                        pgb.create_text(options[i], 15, 15+i*15, COLORWHITE)
                    if pgb.button_up() and option>0:
                        option-=1
                        sleep(0.1)
                    if pgb.button_down() and option<len(options)-1:
                        option+=1
                        sleep(0.1)
                    pgb.rect(13, 12+option*15, 146, 13, COLORWHITE)
                    if pgb.button_A():
                        collect()
                        file=options[option]
                        if not "(Used)" in file:
                            pgb.fill_rect(10,90,220,80,COLORBLACK)
                            pgb.center_text("Loading",COLORWHITE)
                            pgb.create_text("Loading Drawing...", -1, 135, COLORWHITE)
                            pgb.create_text("Do not turn off console.", -1, 147, COLORWHITE)
                            pgb.show()
                            rept=-1
                            del drawing
                            drawing=[]
                            with open(file+".pbd") as f:
                                for i in range(30):
                                    comp=[]
                                    for x in f.readline().split(":"):
                                        ocomp=[]
                                        for y in x.split(","):
                                            ocomp.append(int(y))
                                        comp.append(tuple(ocomp))
                                    drawing.append(comp)
                            del comp
                            del ocomp
                            del f
                    if pgb.button_B() or pgb.button_select():
                        options=["Tools", "Save", "Load", "Delete Save"]
                        option=0
                        break
                    pgb.show()
            if opt=="Delete Save":
                sleep(0.25)
                po=listdir("/")
                files=[]
                for i in po:
                    r=i.split('.')
                    if r[len(r)-1]=="pbd":
                        files.append(i.replace(".pbd", ""))
                del po
                del r
                del i
                options=[]
                pos=-1
                if not files==[]:
                    for opt in files:
                        pos+=1
                        options.append(opt)
                option=0
                del pos
                while True:
                    if files==[]:
                        options=["Tools", "Save", "Load", "Delete Save"]
                        option=0
                        break
                    check_home()
                    pgb.fill(COLORWHITE)
                    display_drawing(drawing)
                    draw_grid(pixelsize)
                    pgb.fill_rect(10,10,150,5+15*len(options)-1, PicoGameBoy.color(150,150,150))
                    for i in range(len(options)):
                        pgb.create_text(options[i], 15, 15+i*15, COLORWHITE)
                    if pgb.button_up() and option>0:
                        option-=1
                        sleep(0.1)
                    if pgb.button_down() and option<len(options)-1:
                        option+=1
                        sleep(0.1)
                    pgb.rect(13, 12+option*15, 146, 13, COLORWHITE)
                    if pgb.button_A():
                        pgb.fill_rect(10,90,220,100,COLORBLACK)
                        pgb.center_text("Are You Sure?",COLORWHITE)
                        pgb.create_text("Are you sure you want", -1, 135, COLORWHITE)
                        pgb.create_text("to delete this drawing?.", -1, 147, COLORWHITE)
                        pgb.create_text("A for yes, B for no.", -1, 157, COLORWHITE)
                        pgb.show()
                        sleep(0.5)
                        while True:
                            if pgb.button_A():
                                break
                            if pgb.button_B():
                                del options
                                return
                        collect()
                        file=options[option]
                        if not "(Used)" in file:
                            pgb.fill_rect(10,90,220,80,COLORBLACK)
                            pgb.center_text("Deleting",COLORWHITE)
                            pgb.create_text("Deleting Drawing...", -1, 135, COLORWHITE)
                            pgb.create_text("Do not turn off console.", -1, 147, COLORWHITE)
                            pgb.show()
                            with open("/games/paint", "r") as f:
                                lines = f.readlines()
                            del f
                            with open("/games/paint", "w") as f:
                                for line in lines:
                                    new_line = line.replace("---PICOBOYFILELIST---"+file+".pbd", "")
                                    f.write(new_line)
                            
                            remove("/"+file+".pbd")
                            del file
                        del files
                        del options
                        po=listdir("/")
                        files=[]
                        for i in po:
                            r=i.split('.')
                            if r[len(r)-1]=="pbd":
                                files.append(i.replace(".pbd", ""))
                        options=[]
                        pos=-1
                        if files==[]:
                            options=["Tools", "Save", "Load", "Delete Save"]
                            option=0
                            break
                        else:
                            for opt in files:
                                pos+=1
                                options.append(opt)
                        option=0
                    if pgb.button_B() or pgb.button_select():
                        options=["Tools", "Save", "Load", "Delete Save"]
                        option=0
                        break
                    pgb.show()
            if opt=="Tools":
                if tools():
                    return
            sleep(0.25)
        if pgb.button_B() or pgb.button_select():
            return
        pgb.show()
        



def tools():
    global drawing
    global activecolor
    global COLORWHITE
    sleep(0.25)
    options=("Pick Color", "Customise Color", "Replace Color", "Fill Screen", "Show Drawing")
    option=0
    while True:
        collect()
        check_home()
        pgb.fill(COLORWHITE)
        display_drawing(drawing)
        draw_grid(pixelsize)
        pgb.fill_rect(10,10,160,5+15*len(options)-1, PicoGameBoy.color(150,150,150))
        for i in range(len(options)):
            pgb.create_text(options[i], 15, 15+i*15, COLORWHITE)
        if pgb.button_up() and option>0:
            option-=1
            sleep(0.1)
        if pgb.button_down() and option<len(options)-1:
            option+=1
            sleep(0.1)
        pgb.rect(13, 12+option*15, 146, 13, COLORWHITE)
        if pgb.button_A():
            if options[option]=="Pick Color":
                cursorx=0
                cursory=0
                sleep(0.25)    
                while True:
                    check_home()
                    pgb.fill(COLORWHITE)
                    display_drawing(drawing)
                    draw_grid(pixelsize)
                    pgb.create_text("Choose a color and", -1, 5, PicoGameBoy.color(200, 200, 200))
                    pgb.create_text("press A to select it.", -1, 15, PicoGameBoy.color(200, 200, 200))
                    if pgb.button_up() and not cursory<=0:
                        cursory-=pixelsize
                        sleep(0.025)
                    if pgb.button_down() and not cursory>=240-pixelsize:
                        cursory+=pixelsize
                        sleep(0.025)
                    if pgb.button_left() and not cursorx<=0:
                        cursorx-=pixelsize
                        sleep(0.025)
                    if pgb.button_right() and not cursorx>=240-pixelsize:
                        cursorx+=pixelsize
                        sleep(0.025)
                    draw_cursor(cursorx, cursory, pixelsize)
                    if pgb.button_A():
                        activecolor=drawing[int(cursory/pixelsize)][int(cursorx/pixelsize)]
                        return True
                    if pgb.button_B():
                        return False
                    pgb.show()
            if options[option]=="Customise Color":
                color=list(activecolor)
                opt=0
                sleep(0.25)
                while True:
                    check_home()
                    pgb.fill(COLORBLACK)
                    pgb.create_text("Press A to confirm your color", -1, 230, COLORWHITE)
                    pgb.create_text("Use select and start to", -1, 205, COLORWHITE)
                    pgb.create_text("raise/lower all colors", -1, 215, COLORWHITE)
                    pgb.fill_rect(25, 10, 50, 50, PicoGameBoy.color(color[0],0,0))
                    pgb.fill_rect(95, 10, 50, 50, PicoGameBoy.color(0,color[1],0))
                    pgb.fill_rect(165, 10, 50, 50, PicoGameBoy.color(0,0,color[2]))
                    if opt==0:
                        pgb.rect(25, 10, 50, 50, COLORWHITE)
                    elif opt==1:
                        pgb.rect(95, 10, 50, 50, COLORWHITE)
                    else:
                        pgb.rect(165, 10, 50, 50, COLORWHITE)
                    pgb.create_text("Red:", 37, 67, COLORWHITE)
                    pgb.create_text("Green:", 98, 67, COLORWHITE)
                    pgb.create_text("Blue:", 170, 67, COLORWHITE)
                    pgb.create_text(str(color[0]), 37, 77, COLORWHITE)
                    pgb.create_text(str(color[1]), 98, 77, COLORWHITE)
                    pgb.create_text(str(color[2]), 170, 77, COLORWHITE)
                    pgb.create_text("Color:", -1, 95, COLORWHITE)
                    pgb.fill_rect(82,110,75,75,PicoGameBoy.color(*color))
                    pgb.rect(82,110,75,75,COLORWHITE)
                    
                    if pgb.button_up() and color[opt]<255:
                        color[opt]+=1
                    elif pgb.button_down() and color[opt]>0:
                        color[opt]-=1
                    elif pgb.button_select():
                        if color[0]>0:
                            color[0]-=1
                        if color[1]>0:
                            color[1]-=1
                        if color[2]>0:
                            color[2]-=1
                    elif pgb.button_start():
                        if color[0]<255:
                            color[0]+=1
                        if color[1]<255:
                            color[1]+=1
                        if color[2]<255:
                            color[2]+=1
                    elif pgb.button_left() and opt>0:
                        opt-=1
                        sleep(0.1)
                    elif pgb.button_right() and opt<2:
                        opt+=1
                        sleep(0.1)
                    elif pgb.button_A():
                        activecolor=tuple(color)
                        del color
                        return  True
                    elif pgb.button_start() or pgb.button_B():
                        break
                    pgb.show()
            if options[option]=="Replace Color":
                cursorx=0
                cursory=0
                sleep(0.25)    
                while True:
                        check_home()
                        pgb.fill(COLORWHITE)
                        display_drawing(drawing)
                        draw_grid(pixelsize)
                        pgb.create_text("Choose a color and", -1, 5, PicoGameBoy.color(200, 200, 200))
                        pgb.create_text("press A to select it.", -1, 15, PicoGameBoy.color(200, 200, 200))
                        if pgb.button_up() and not cursory<=0:
                            cursory-=pixelsize
                            sleep(0.025)
                        if pgb.button_down() and not cursory>=240-pixelsize:
                            cursory+=pixelsize
                            sleep(0.025)
                        if pgb.button_left() and not cursorx<=0:
                            cursorx-=pixelsize
                            sleep(0.025)
                        if pgb.button_right() and not cursorx>=240-pixelsize:
                            cursorx+=pixelsize
                            sleep(0.025)
                        draw_cursor(cursorx, cursory, pixelsize)
                        if pgb.button_A():
                            pgb.fill_rect(10,90,220,100,COLORBLACK)
                            pgb.center_text("Are You Sure?",COLORWHITE)
                            pgb.create_text("Are you sure you want", -1, 135, COLORWHITE)
                            pgb.create_text("to replace this color?.", -1, 147, COLORWHITE)
                            pgb.create_text("A for yes, B for no.", -1, 162, COLORWHITE)
                            pgb.show()
                            sleep(0.5)
                            while True:
                                if pgb.button_A():
                                    break
                                if pgb.button_B():
                                    return
                            c=drawing[int(cursory/pixelsize)][int(cursorx/pixelsize)]
                            for line in range(len(drawing)):
                                for value in range(len(drawing[line])):
                                    if drawing[line][value]==c:
                                        row = list(drawing[line])
                                        row[value] = activecolor
                                        drawing[line] = row
                                        del row
                            return True
                        if pgb.button_B():
                            break
                        pgb.show()
            if options[option]=="Fill Screen":
                color=activecolor
                pgb.fill_rect(10,90,220,100,COLORBLACK)
                pgb.center_text("Are You Sure?",COLORWHITE)
                pgb.create_text("Are you sure you want", -1, 135, COLORWHITE)
                pgb.create_text("to fill the screen?.", -1, 147, COLORWHITE)
                pgb.create_text("A for yes, B for no.", -1, 162, COLORWHITE)
                pgb.show()
                sleep(0.5)
                while True:
                    check_home()
                    if pgb.button_A():
                        break
                    if pgb.button_B():
                        return
                for line in range(len(drawing)):
                    for value in range(len(drawing[line])):
                        row = list(drawing[line])
                        row[value] = color
                        drawing[line] = row
                        del row
                return True
            if options[option]=="Show Drawing":
                while True:
                    display_drawing(drawing)
                    if pgb.button_B() or pgb.button_select():
                        return True
                    pgb.show()
        if pgb.button_B() or pgb.button_select():
            return
        pgb.show()

            
   

cursorx=0
cursory=0
activecolor=(0,0,0)
drawing=[]
for i in range(int(240/pixelsize)):
    z=[]
    for f in range(int(240/pixelsize)):
        z.append((255,255,255))
    drawing.append(z)
while True:
    check_home()
    pgb.fill(COLORWHITE)
    display_drawing(drawing)
    draw_grid(pixelsize)
    if pgb.button_up() and not cursory<=0:
        cursory-=pixelsize
        sleep(0.025)
    if pgb.button_down() and not cursory>=240-pixelsize:
        cursory+=pixelsize
        sleep(0.025)
    if pgb.button_left() and not cursorx<=0:
        cursorx-=pixelsize
        sleep(0.025)
    if pgb.button_right() and not cursorx>=240-pixelsize:
        cursorx+=pixelsize
        sleep(0.025)
    if pgb.button_A():
        row = list(drawing[int(cursory/pixelsize)])
        row[int(cursorx/pixelsize)] = activecolor
        drawing[int(cursory/pixelsize)] = row
        del row
    if pgb.button_B():
        sleep(1)
        drawing[int(cursory/pixelsize)][int(cursorx/pixelsize)]=(255,255,255)
    if pgb.button_start():
        colors=[(255,255,255),(225,0,0),(255,135,0),(225,225,0),(0,225,0),(0,0,225),(178,0,178),(255,20,147),(0,0,0),(175,175,175),(139,69,19),(255,222,179),(0,191,255),(0,150,0),(0,0,0),(0,0,0)]
        sleep(0.25)
        option=0
        optpos=0
        while True:
            check_home()
            pgb.fill(PicoGameBoy.color(100,100,100))
            pgb.create_text("Choose a color to use:", -1, 5, COLORWHITE)
            for f in range(4):
                for i in range(4):
                    pgb.fill_rect(i*45+35, f*45+30, 30, 30, PicoGameBoy.color(*colors[i+(f*4)]))
            if pgb.button_up() and optpos>0:
                optpos-=1
                sleep(0.1)
            if pgb.button_down() and optpos<3:
                optpos+=1
                sleep(0.1)
            if pgb.button_left() and option>0:
                option-=1
                sleep(0.1)
            if pgb.button_right() and option<3:
                option+=1
                sleep(0.1)
            if pgb.button_A():
                activecolor= colors[4*optpos+option]
                break
            if pgb.button_B():
                activecolor=activecolor
                break
            pgb.rect(option*45+35, optpos*45+30, 30,30, COLORWHITE)
            pgb.rect(option*45+36, optpos*45+31, 28,28, COLORBLACK)
            pgb.show()
            sleep(0.1)
    if pgb.button_select():
        menu()
        sleep(0.25)
    draw_cursor(cursorx, cursory, pixelsize)
    pgb.show()
        
