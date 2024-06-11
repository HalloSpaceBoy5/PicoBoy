from micropython import const
from framebuf import FrameBuffer,RGB565
from PicoGameBoy import PicoGameBoy
from time import sleep
from random import randint
import array
import os
import sys
from random import randint
import machine

try:
    os.rename("/main.py", "/settings.py")
    os.rename("/title.py", "/main.py")
except:
    ""



pgb = PicoGameBoy()
runcheck=False
black=PicoGameBoy.color(0,0,0)
white=PicoGameBoy.color(255,255,255)
opt=0
sleep(0.2)
try:
    with open("background.conf","r") as r:
        bindex=int(r.read())
except:
    bindex=8
bgcolors=(
    (215, 0, 0),
    (227, 160, 5),
    (220, 213, 0),
    (0, 205, 0),
    (0, 0, 205),
    (141, 2, 171),
    (227, 52, 189),
    (161, 161, 161),
    (69, 69, 69),
    (0,0,0),
    (255,255,255))
bgcolor=bgcolors[bindex]
bgcolor565=PicoGameBoy.color(*bgcolor)
if sum(bgcolor)<765:
    tcolor=1
else:
    tcolor=0
if tcolor==0:
    ottcolor=PicoGameBoy.color(255,255,255)
else:
    ottcolor=PicoGameBoy.color(0,0,0)
ttcolor=PicoGameBoy.color(255,255,255)
if tcolor==0:
    ttcolor=PicoGameBoy.color(0,0,0)
try:
    with open("animated.conf") as r:
        if r.read()=="True":
            animated=True
        else:
            animated=False
except:
    animated=True
    
try:
    with open("VERSION") as r:
        version=r.read()
except:
    version="NULL"

selectcolor=PicoGameBoy.color(127,127,127)
if tcolor==0:
    selectcolor=PicoGameBoy.color(200,200,200)


try:
    with open("language.conf") as r:
        language=int(r.read())
    if language>4:
        raise
except:
    language=0

with open("Main Text.csv") as w:
    data=w.read().split("\n")[language]
    data=data.split(", ")
    dum=data[3].split("/")
    del data

def readchunk_mask( filename,x2,y2,w,h,cmask=57351):
    with open(filename,"rb") as r:
            for x in range(h):
                tempfb=FrameBuffer(bytearray(r.read(2*w)),w,1,RGB565)
                pgb.blit(tempfb,x2,y2+x,cmask)
                del tempfb

def languages():
    global language
    opti=language
    sleep(.1)
    while True:
        pgb.fill(bgcolor565)
        if language==0:
            pgb.create_text("Settings",-1,10,ttcolor)
        elif language==1:
            pgb.create_text("Ajustes",-1,10,ttcolor)
        elif language==2:
            pgb.create_text("Parametres",-1,10,ttcolor)
        elif language==3:
            pgb.create_text("Einstellungen",-1,10,ttcolor)
        elif language==4:
            pgb.create_text("Impostazioni",-1,10,ttcolor) 
        pgb.create_text("PicoBoy            "+version,10,225,ttcolor)
        options=["English", "Espanol", "Francais", "Deutsch", "Italiano"]
        for i,option in enumerate(options):
            pgb.rect(10,25+i*30,220,20,white)
            pgb.rect(11,26+i*30,218,18,black)
            if i==opti:
                pgb.fill_rect(12,27+i*30,216,16,selectcolor)
            pgb.create_text(option,-1,32+i*30,ttcolor)
        if pgb.button_up() and opti>0:
            opti-=1
            pgb.show()
            sleep(0.1)
        if pgb.button_down() and opti<len(options)-1:
            opti+=1
            pgb.show()
            sleep(0.1)
        if pgb.button_A():
            language=opti
            with open("language.conf", "w") as w:
                w.write(str(opti))
            with open("Main Text.csv") as w:
                global dum
                data=w.read().split("\n")[language]
                data=data.split(", ")
                dum=data[3].split("/")
                del data
            sleep(0.1)
            return
        pgb.show()

def background():
    global bgcolor565
    global bgcolor
    global white
    global black
    global tcolor
    global ttcolor
    global runcheck
    global ottcolor
    global selectcolor
    global bindex
    opt=0
    
    while True:
        pgb.fill(bgcolor565)
        if language==0:
            pgb.create_text("Settings",-1,10,ttcolor)
        elif language==1:
            pgb.create_text("Ajustes",-1,10,ttcolor)
        elif language==2:
            pgb.create_text("Parametres",-1,10,ttcolor)
        elif language==3:
            pgb.create_text("Einstellungen",-1,10,ttcolor)
        elif language==4:
            pgb.create_text("Impostazioni",-1,10,ttcolor) 
        pgb.create_text("PicoBoy            "+version,10,225,ttcolor)
        if language==0:
            options=["Drawing Background","Color Background", "Exit"]
        elif language==1:
            options=["Tema de dibujo","Tema de color","Salir"]
        elif language==2:
            options=["Fond de dessin", "Fond de couleur", "Quitter"]
        elif language==3:
            options=["Hintergrund zeichnen", "Hintergrundfarbe", "Beenden"]
        elif language==4:
            options=["Sfondo disegno","Colore sfondo", "Esci"]
        
        for i,option in enumerate(options):
            pgb.rect(10,25+i*30,220,20,white)
            pgb.rect(11,26+i*30,218,18,black)
            if i==opt:
                pgb.fill_rect(12,27+i*30,216,16,selectcolor)
            pgb.create_text(option,-1,32+i*30,ttcolor)
        if pgb.button_up() and opt>0:
            opt-=1
            pgb.show()
            sleep(0.1)
        if pgb.button_down() and opt<len(options)-1:
            opt+=1
            pgb.show()
            sleep(0.1)
        if pgb.button_A():
            if opt==1:
                sleep(0.2)
                while True:
                    pgb.fill(bgcolor565)
                    if language==0:
                        pgb.create_text("Choose a background color",-1,-1,ttcolor)
                        pgb.create_text("using the left and right",-1,125,ttcolor)
                        pgb.create_text("buttons.",-1,140,ttcolor)
                        pgb.create_text("Press A to exit",-1,220,ttcolor)
                    elif language==1:
                        pgb.create_text("Elige un color de tema",-1,-1,ttcolor)
                        pgb.create_text("Usando la izquierda y",-1,125,ttcolor)
                        pgb.create_text("la derecha botones.",-1,140,ttcolor)
                        pgb.create_text("Presione A para salir",-1,220,ttcolor)
                    elif language==2:
                        pgb.create_text("Choisissez une couleur de",-1,-1,ttcolor)
                        pgb.create_text("fond en utilisant la gauche ",-1,125,ttcolor)
                        pgb.create_text("et la droite boutons.",-1,140,ttcolor)
                        pgb.create_text("Appuyez sur A pour quitter",-1,220,ttcolor)
                    elif language==3:
                            pgb.create_text("Wahlen Sie eine Hintergrund",-1,-1,ttcolor)
                            pgb.create_text("farbe umit der linken und",-1,125,ttcolor)
                            pgb.create_text("rechten tasten.",-1,137,ttcolor)
                            pgb.create_text("Drucken Sie A, um den",-1,210,ttcolor)
                            pgb.create_text("Vorgang zu beenden",-1,220,ttcolor)
                    elif language==4:
                        pgb.create_text("Scegli un colore di sfondo",-1,-1,ttcolor)
                        pgb.create_text("usando sinistra e destra",-1,125,ttcolor)
                        pgb.create_text("pulsanti.",-1,140,ttcolor)
                        pgb.create_text("Premi A per uscire",-1,220,ttcolor)
                    if runcheck:
                        runcheck=False
                    if pgb.button_A():
                        return
                    if pgb.button_B():
                        sleep(0.2)
                        break
                    if pgb.button_left() and bindex>0:
                        bindex-=1
                        runcheck=True
                    if pgb.button_right() and bindex<len(bgcolors)-1:
                        bindex+=1
                        runcheck=True
                    pgb.show()
                    if runcheck:
                        bgcolor=bgcolors[bindex]
                        bgcolor565=PicoGameBoy.color(*bgcolor)
                        if sum(bgcolor)<765:
                            tcolor=1
                        else:
                            tcolor=0
                        ttcolor=PicoGameBoy.color(255,255,255)
                        if tcolor==0:
                            ttcolor=PicoGameBoy.color(0,0,0)
                        with open("background.conf","w") as w:
                            w.write(str(bindex))
                        if tcolor==0:
                            ottcolor=white
                        else:
                            ottcolor=black
                        selectcolor=PicoGameBoy.color(127,127,127)
                        if tcolor==0:
                            selectcolor=PicoGameBoy.color(200,200,200)
                        pgb.fill(bgcolor565)
                        if language==0:
                            pgb.create_text("Choose a background color",-1,-1,ttcolor)
                            pgb.create_text("using the left and right",-1,125,ttcolor)
                            pgb.create_text("buttons.",-1,140,ttcolor)
                            pgb.create_text("Press A to exit",-1,220,ttcolor)
                        elif language==1:
                            pgb.create_text("Elige un color de tema",-1,-1,ttcolor)
                            pgb.create_text("Usando la izquierda y",-1,125,ttcolor)
                            pgb.create_text("la derecha botones.",-1,140,ttcolor)
                            pgb.create_text("Presione A para salir",-1,220,ttcolor)
                        elif language==2:
                            pgb.create_text("Choisissez une couleur de",-1,-1,ttcolor)
                            pgb.create_text("fond en utilisant la gauche ",-1,125,ttcolor)
                            pgb.create_text("et la droite boutons.",-1,140,ttcolor)
                            pgb.create_text("Appuyez sur A pour quitter",-1,220,ttcolor)
                        elif language==3:
                            pgb.create_text("Wahlen Sie eine Hintergrund",-1,-1,ttcolor)
                            pgb.create_text("farbe umit der linken und",-1,125,ttcolor)
                            pgb.create_text("rechten tasten.",-1,137,ttcolor)
                            pgb.create_text("Drucken Sie A, um den",-1,210,ttcolor)
                            pgb.create_text("Vorgang zu beenden",-1,220,ttcolor)
                        elif language==4:
                            pgb.create_text("Scegli un colore di sfondo",-1,-1,ttcolor)
                            pgb.create_text("usando sinistra e destra",-1,125,ttcolor)
                            pgb.create_text("pulsanti.",-1,140,ttcolor)
                            pgb.create_text("Premi A per uscire",-1,220,ttcolor)
                            pgb.show()
                        sleep(0.2)
            if opt==0:
                sleep(0.2)
                bgs=os.listdir("/bglist")
                page=0
                while True:
                    pgb.fill(bgcolor565)
                    options=[]
                    for x in range(4):
                        try:
                            options.append(bgs[x+(page*4)])
                        except:
                            "End of list"
                    if language==0:
                        options.append("Exit")
                        pgb.create_text("Choose a background",-1,10,ttcolor)
                    elif language==1:
                        options.append("Salida")
                        pgb.create_text("Elige un tema",-1,10,ttcolor)
                    elif language==2:
                        options.append("Quitter")
                        pgb.create_text("Choisissez un fond",-1,10,ttcolor)
                    elif language==3:
                        options.append("Ausfahrt")
                        pgb.create_text("Wahlen Sie einen Hintergrund",-1,10,ttcolor)
                    elif language==4:
                        options.append("Uscita")
                        pgb.create_text("Scegli uno sfondo",-1,10,ttcolor)


                    for i,option in enumerate(options):
                        pgb.rect(10,25+i*30,220,20,white)
                        pgb.rect(11,26+i*30,218,18,black)
                        if i==opt:
                            pgb.fill_rect(12,27+i*30,216,16,selectcolor)
                        pgb.create_text(option,-1,32+i*30,ttcolor)
                    if language==0:
                        pgb.create_text(f"Page {page+1}/{int((len(bgs)-1)/4)+1}",-1,172,ttcolor)
                        pgb.create_text("Use the left/right buttons",-1,190,ttcolor)
                        pgb.create_text("to scroll your backgrounds",-1,200,ttcolor)
                        pgb.create_text("Drawing backgrounds won't",-1,215,ttcolor)
                        pgb.create_text("show in the settings menu.",-1,225,ttcolor)
                    elif language==1:
                        pgb.create_text(f"Pagina {page+1}/{int((len(bgs)-1)/4)+1}",-1,172,ttcolor)
                        pgb.create_text("Usa los botones izquierda y",-1,190,ttcolor)
                        pgb.create_text("derecha navegar sus temas",-1,200,ttcolor)
                        pgb.create_text("Dibujar temas no mostrar",-1,215,ttcolor)
                        pgb.create_text("en el menu de configuracion.",-1,225,ttcolor)
                    elif language==2:
                        pgb.create_text(f"Page {page+1}/{int((len(bgs)-1)/4)+1}",-1,172,ttcolor)
                        pgb.create_text("User les boutons gauch et",-1,187,ttcolor)
                        pgb.create_text("droit faire defiler vos fonds",-1,197,ttcolor)
                        pgb.create_text("Les fonds de dessin ne seront",-1,210,ttcolor)
                        pgb.create_text("pas montrer dans le menu",-1,220,ttcolor)
                        pgb.create_text("des parametres.",-1,230,ttcolor)
                    elif language==3:
                        pgb.create_text(f"Seite {page+1}/{int((len(bgs)-1)/4)+1}",-1,169,ttcolor)
                        pgb.create_text("Nutzung Sie die Links/Rechts",-1,180,ttcolor)
                        pgb.create_text("Tasten um Ihre Hintergrunde",-1,190,ttcolor)
                        pgb.create_text("zu scrollen.",-1,200,ttcolor)
                        pgb.create_text("Bildhintergrund werden im",-1,210,ttcolor)
                        pgb.create_text("Einstellungsmenu nicht",-1,220,ttcolor)
                        pgb.create_text("angezeigt",-1,230,ttcolor)
                    elif language==4:
                        pgb.create_text(f"Pagina {page+1}/{int((len(bgs)-1)/4)+1}",-1,172,ttcolor)
                        pgb.create_text("Uso i pulsanti sinistra e",-1,185,ttcolor)
                        pgb.create_text("destra per scorrere sfondi",-1,195,ttcolor)
                        pgb.create_text("Disegnare gli sfondi no",-1,208,ttcolor)
                        pgb.create_text("mostrare nel menu delle",-1,218,ttcolor)
                        pgb.create_text("impostazioni.",-1,228,ttcolor)


                    if pgb.button_up() and opt>0:
                        opt-=1
                        pgb.show()
                        sleep(0.1)
                    if pgb.button_down() and opt<len(options)-1:
                        opt+=1
                        pgb.show()
                        sleep(0.1)
                    if pgb.button_left():
                        sleep(0.2)
                        if page==0:
                            page=int((len(bgs)-1)/4)
                        else:
                            page-=1
                    if pgb.button_right():
                        sleep(0.2)
                        if page==int((len(bgs)-1)/4):
                            page=0
                        else:
                            page+=1
                    if pgb.button_A():
                        if opt==len(options)-1:
                            return
                        else:
                            with open("background.conf","w") as w:
                                w.write(f"/backgrounds/{bgs[opt+(page*4)]}.pbd")
                                bgcolor=bgcolors[8]
                                bindex=8
                                bgcolor565=PicoGameBoy.color(*bgcolor)
                                if sum(bgcolor)<426:
                                    tcolor=1
                                else:
                                    tcolor=0
                                ttcolor=PicoGameBoy.color(255,255,255)
                                if tcolor==0:
                                    ttcolor=PicoGameBoy.color(0,0,0)
                                if tcolor==0:
                                    ottcolor=white
                                else:
                                    ottcolor=black
                            sleep(0.2)
                            return
                    if pgb.button_B():
                        sleep(0.2)
                        break
                    pgb.show()
            if opt==2:
                return
        if pgb.button_B():
            return
        pgb.show()    

scrollpos=0
max_on_screen=6
vpin=machine.ADC(29)
pastpercentage=[]
while True:
    pgb.fill(bgcolor565)
    if language==0:
        pgb.create_text("Settings",-1,10,ttcolor)
    elif language==1:
        pgb.create_text("Ajustes",-1,10,ttcolor)
    elif language==2:
        pgb.create_text("Parametres",-1,10,ttcolor)
    elif language==3:
        pgb.create_text("Einstellungen",-1,10,ttcolor)
    elif language==4:
        pgb.create_text("Impostazioni",-1,10,ttcolor) 
    adc_reading  = vpin.read_u16()
    adc_voltage  = (adc_reading * 3.3) / 65535
    vsys_voltage = adc_voltage * 12
    console=0
    if vsys_voltage>10:
        vsys_voltage = adc_voltage * 3
        percentage=int(int(((round(vsys_voltage,3)-1.9)/2.7)*100))
        console=1
    else:
        percentage=int(int(((round(vsys_voltage,3)-1.9)/1)*100))
        console=0
    if console==0:
        if percentage>100 and percentage<125:
            percentage=100
        if percentage<130:
            pastpercentage.append(percentage)
            if len(pastpercentage)>200:
                pastpercentage.pop(0)
            percentage=int(int(sum(pastpercentage)/len(pastpercentage)))
    elif console==1:
        if percentage>100 and percentage<110:
            percentage=100
        if percentage<110:
            pastpercentage.append(percentage)
            if len(pastpercentage)>200:
                pastpercentage.pop(0)
            percentage=int(int(sum(pastpercentage)/len(pastpercentage)))
    pgb.create_text("PicoBoy            "+version,10,225,ttcolor)
    if percentage>100:
        pgb.create_text("USB",100,225, ttcolor)
    else:
        pgb.create_text(str(percentage)+"%",100,225,ttcolor)
    if language==0:
        if animated:
            ani="True"
        else:
            ani="False"
        options=["Change Brightness", "Change Volume", "Change Background", "Data Upload Mode", "Animation: "+ani, "Language", "Exit"]
    elif language==1:
        if animated:
            ani="Cierto"
        else:
            ani="Falso"
        options=["Cambiar brillo", "Cambiar volumen", "Cambiar tema", "Modo de carga de datos", "Animacion: "+ani, "Idioma", "Salir"]
    elif language==2:
        if animated:
            ani="Vrai"
        else:
            ani="Faux"
        options=["Modifier la luminosite", "Modifier le volume", "Modifier l'fond", "Mode donnees", "Animation: "+ani, "Langue", "Quitter"]
    elif language==3:
        if animated:
            ani="Wahr"
        else:
            ani="Falsch"
        options=["Helligkeit andern", "Lautstarke andern", "Hintergrund andern", "Daten-Upload-Modus", "Animation: "+ani, "Sprache", "Beenden"]
    elif language==4:
        if animated:
            ani="Vero"
        else:
            ani="Falso"
        options=["Cambia luminosita", "Cambia volume", "Cambia sfondo", "Modalita dati", "Animazione: "+ani, "Lingua", "Esci"]
    if tcolor==0:
        ottcolor=white
    else:
        ottcolor=black
    pgb.fill_rect(215,20,20, 180,selectcolor)
    pgb.fill_rect(220,25+(scrollpos*30),10, int(max_on_screen/len(options)* 165),ttcolor)
    noptions=options[0+scrollpos:max_on_screen+scrollpos]
    for i,option in enumerate(noptions):
        pgb.rect(10,25+i*30,200,20,white)
        pgb.rect(11,26+i*30,198,18,black)
        if i==opt:
            pgb.fill_rect(12,27+i*30,196,16,selectcolor)
        pgb.create_text(option,(120- int(len(option)/2 * 8))-10,32+i*30,ttcolor)
    if pgb.button_up():
        if opt>0:
            opt-=1
        elif opt==0 and scrollpos>0:
            scrollpos-=1
        pgb.show()
        sleep(0.1)
    if pgb.button_down():
        if opt<len(noptions)-1:
            opt+=1
        elif opt==len(noptions)-1 and opt+scrollpos<len(options)-1:
            scrollpos+=1
        pgb.show()
        sleep(0.1)
    if pgb.button_A():
        if opt+scrollpos==0:
            sleep(0.2)
            while True:
                pgb.fill(bgcolor565)
                pgb.rect(20,110,200,20,ttcolor)
                brightness=pgb.bl.duty_u16()-10000
                width=int((brightness/55000)*198)
                percentage=int((brightness/55000)*100)
                pgb.fill_rect(21,111,width,18,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                if language==0:
                    pgb.create_text("Use the left and right",-1,140,ttcolor)
                    pgb.create_text("buttons to change the",-1,150,ttcolor)
                    pgb.create_text("brightness.",-1,160,ttcolor)
                    pgb.create_text("Press A to exit.",-1,220,ttcolor)
                elif language==1:
                    pgb.create_text("Usa la izquierda y la derecha",-1,140,ttcolor)
                    pgb.create_text("botones para cambiar el",-1,150,ttcolor)
                    pgb.create_text("brillo.",-1,160,ttcolor)
                    pgb.create_text("Presione A para salir.",-1,220,ttcolor)
                elif language==2:
                    pgb.create_text("User la gauche et la droite",-1,140,ttcolor)
                    pgb.create_text("boutons pour modifier le",-1,150,ttcolor)
                    pgb.create_text("luminosite.",-1,160,ttcolor)
                    pgb.create_text("Appuyez sur A pour quitter.",-1,220,ttcolor)
                elif language==3:
                    pgb.create_text("Benutzen Sie links und rechts",-1,140,ttcolor)
                    pgb.create_text("Tasten zum Andern der",-1,150,ttcolor)
                    pgb.create_text("Helligkeit.",-1,160,ttcolor)
                    pgb.create_text("Drucken Sie A, um den",-1,210,ttcolor)
                    pgb.create_text("Vorgang zu beenden.",-1,220,ttcolor)
                elif language==4:
                    pgb.create_text("Usa la sinistra e la destra",-1,140,ttcolor)
                    pgb.create_text("pulsanti per modificare il",-1,150,ttcolor)
                    pgb.create_text("luminosita.",-1,160,ttcolor)
                    pgb.create_text("Premi A per uscire.",-1,220,ttcolor)
                if pgb.button_left():
                    pgb.decrease_brightness()
                    pgb.fill_rect(0,95,240,40,bgcolor565)
                    pgb.rect(20,110,200,20,ttcolor)
                    brightness=pgb.bl.duty_u16()-10000
                    width=int((brightness/55000)*198)
                    percentage=int((brightness/55000)*100)
                    pgb.fill_rect(21,111,width,18,ttcolor)
                    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                    pgb.show()
                    sleep(0.0825)
                if pgb.button_right():
                    pgb.increase_brightness()
                    pgb.fill_rect(0,95,240,40,bgcolor565)
                    pgb.rect(20,110,200,20,ttcolor)
                    brightness=pgb.bl.duty_u16()-10000
                    width=int((brightness/55000)*198)
                    percentage=int((brightness/55000)*100)
                    pgb.fill_rect(21,111,width,18,ttcolor)
                    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                    pgb.show()
                    sleep(0.0825)
                if pgb.button_A() or pgb.button_B():
                    sleep(0.2)
                    break
                pgb.show()
        if opt+scrollpos==1:
            sleep(0.2)
            while True:
                pgb.fill(bgcolor565)
                pgb.rect(20,110,200,20,ttcolor)
                volume=pgb.vol
                width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
                percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
                pgb.fill_rect(21,111,width,18,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                if language==0:
                    pgb.create_text("Use the left and right",-1,140,ttcolor)
                    pgb.create_text("buttons to change the",-1,150,ttcolor)
                    pgb.create_text("volume.",-1,160,ttcolor)
                    pgb.create_text("Press A to exit.",-1,220,ttcolor)
                elif language==1:
                    pgb.create_text("Usa la izquierda y la derecha",-1,140,ttcolor)
                    pgb.create_text("botones para cambiar el",-1,150,ttcolor)
                    pgb.create_text("volumen.",-1,160,ttcolor)
                    pgb.create_text("Presione A para salir.",-1,220,ttcolor)
                elif language==2:
                    pgb.create_text("User la gauche et la droite",-1,140,ttcolor)
                    pgb.create_text("boutons pour modifier le",-1,150,ttcolor)
                    pgb.create_text("volume.",-1,160,ttcolor)
                    pgb.create_text("Appuyez sur A pour quitter.",-1,220,ttcolor)
                elif language==3:
                    pgb.create_text("Benutzen Sie links und rechts",-1,140,ttcolor)
                    pgb.create_text("Tasten zum Andern der",-1,150,ttcolor)
                    pgb.create_text("Volumen.",-1,160,ttcolor)
                    pgb.create_text("Drucken Sie A, um den",-1,210,ttcolor)
                    pgb.create_text("Vorgang zu beenden.",-1,220,ttcolor)
                elif language==4:
                    pgb.create_text("Usa la sinistra e la destra",-1,140,ttcolor)
                    pgb.create_text("pulsanti per modificare il",-1,150,ttcolor)
                    pgb.create_text("volume.",-1,160,ttcolor)
                    pgb.create_text("Premi A per uscire.",-1,220,ttcolor)
                if pgb.button_left():
                    pgb.decrease_vol()
                    pgb.fill_rect(0,95,240,40,bgcolor565)
                    pgb.rect(20,110,200,20,ttcolor)
                    volume=pgb.vol
                    width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
                    percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
                    pgb.fill_rect(21,111,width,18,ttcolor)
                    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                    pgb.show()
                    pgb.sound(200)
                    sleep(0.0825)
                    pgb.sound(0)
                if pgb.button_right():
                    pgb.increase_vol()
                    pgb.fill_rect(0,95,240,40,bgcolor565)
                    pgb.rect(20,110,200,20,ttcolor)
                    volume=pgb.vol
                    width=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*198)
                    percentage=int(((volume-pgb.vol_min)/(pgb.vol_max-pgb.vol_min))*100)
                    pgb.fill_rect(21,111,width,18,ttcolor)
                    pgb.create_text(str(percentage)+"%",-1,95,ttcolor)
                    pgb.show()
                    pgb.sound(200)
                    sleep(0.0825)
                    pgb.sound(0)
                if pgb.button_A() or pgb.button_B():
                    sleep(0.2)
                    break
                pgb.show()
        if opt+scrollpos==2:
            sleep(0.2)
            pgb.show()
            background()
            sleep(0.2)
        if opt+scrollpos==3:
            pgb.fill(bgcolor565)
            pgb.create_text(dum[0],-1,20,ttcolor)
            pgb.create_text(dum[1],-1, 45,ttcolor)
            pgb.create_text(dum[2],-1,57,ttcolor)
            pgb.create_text(dum[3],-1,69,ttcolor)
            pgb.create_text(dum[4],-1,81,ttcolor)
            pgb.create_text(dum[5],-1,200,ttcolor)
            pgb.create_text(dum[6],-1,212,ttcolor)
            pgb.create_text(dum[7],-1,224,ttcolor)
            readchunk_mask("Data Upload Mode.pbimg", 72,90,100,100,cmask=PicoGameBoy.color(31,17,9))
            pgb.show()
            sys.exit()
        if opt+scrollpos==4:
            if animated:
                animated=False
            else:
                animated=True
            with open("animated.conf", "w") as w:
                w.write(str(animated))
            sleep(0.1)
        if opt+scrollpos==5:
            languages()
        if opt+scrollpos==6:
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
    if pgb.button_Home():
        homebootstop=open("/noboot", "w")
        homebootstop.close()
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()
        break
    pgb.show()



