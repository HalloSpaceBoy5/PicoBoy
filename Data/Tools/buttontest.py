from PicoGameBoy import PicoGameBoy
import time

pgb=PicoGameBoy()

while True:
    if pgb.button_left():
        print("left")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("left", WHITE)
        #pgb.show()
        pgb.sound(200)
    elif pgb.button_right():
        print("right")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("right", WHITE)
        #pgb.show()
    elif pgb.button_up():
        print("up")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("up", WHITE)
        #pgb.show()
    elif pgb.button_down():
        print("down")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("down", WHITE)
        #pgb.show()
    elif pgb.button_A():
        print("a")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("a", WHITE)
        #pgb.show()
    elif pgb.button_B():
        print("b")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("b", WHITE)
        #pgb.show()
    elif pgb.button_Home():
        print("home")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("home", WHITE)
        #pgb.show()
    elif pgb.button_select():
        print("select")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("select", WHITE)
        #pgb.show()
    elif pgb.button_start():
        print("start")
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #WHITE = PicoGameBoy.color(255,255,255)
        #pgb.center_text("start", WHITE)
        #pgb.show()
    #
    
    #else:
        #pgb.fill(PicoGameBoy.color(0,0,0))
        #pgb.show()
        #pgb.sound(0)
    time.sleep(0.1)
 