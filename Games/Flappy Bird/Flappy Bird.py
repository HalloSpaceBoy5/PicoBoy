# Rewritten by HalloSpaceBoy
from os import rename
rename("./main.py", "./Flappy Bird.py")
rename("./title.py", "./main.py")
from PicoGameBoy import PicoGameBoy
pgb = PicoGameBoy()
bird_sprite=bytearray(b'v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9')
pgb.add_sprite(bird_sprite,34,24)
del bird_sprite
pipe=bytearray(b'v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9')
pgb.add_sprite(pipe,52,26)
del pipe
pipe_bottom=bytearray(b'v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8u\xe5u\xe5\x9f+\x9f+\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8u\xe5u\xe5\x9f+\x9f+\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8')
pgb.add_sprite(pipe_bottom,52,26)
del pipe_bottom
pipe_top=bytearray(b'Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8u\xe5u\xe5\x9f+\x9f+\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8u\xe5u\xe5\x9f+\x9f+\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\x9f+\x9f+\xe7\xf1\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5u\xe5\x9f+\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04T\x04u\xe5u\xe5T\x04T\x04T\x04T\x04Q\xc8Q\xc8v9v9')
pgb.add_sprite(pipe_top,52,26)
del pipe_top
from time import ticks_ms, ticks_diff, sleep
from random import randint
from math import sqrt
jumpheight=7
fallrate=1
pipespace=125
score=0
def check_collision(speed,detectionradius, posx, posy, width, height, posx2, posy2, width2, height2):
    bbox1 = (posx, posy, posx + width, posy + height)
    bbox2 = (posx2, posy2, posx2 + width2, posy2 + height2)

    if bbox1[0] < bbox2[2] and bbox1[2] > bbox2[0] and bbox1[1] < bbox2[3] and bbox1[3] > bbox2[1]:
        if posx + width + speed >= posx2 and posx - speed <= posx2 + width2 and posy + height + speed >= posy2 and posy - speed <= posy2 + height2:
            return True
    return False
def main_game():
    soundpos=0
    global score
    pipepos1=240
    pipepos2=pipepos1+150
    playerspeed=0
    pipespeed=3.5
    playerx=103
    playery=103
    score=0
    button_pressed=False
    prev_button_pressed=False
    began=False
    sleep(0.25)
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.fill(PicoGameBoy.color(112,197,206))
        pgb.fill_rect(0, 230, 240, 10, PicoGameBoy.color(0,154,23))
        
        #Bird jumping
        prev_button_pressed=button_pressed
        if not began:
            while True:
                pgb.fill(PicoGameBoy.color(112,197,206))
                pgb.fill_rect(0, 230, 240, 10, PicoGameBoy.color(0,154,23))
                pgb.create_text("Press A to begin",-1,50, PicoGameBoy.color(255,255,255))
                pgb.sprite(0, playerx, playery)
                pgb.show()
                if pgb.button_A():
                    button_pressed=True
                    began=True
                    break
                if pgb.button_Home():
                    homebootstop=open("/noboot", "w")
                    homebootstop.close()
                    pgb.fill(PicoGameBoy.color(0,0,0))
                    pgb.show()
                    machine.reset()
                    break
        if ((pgb.button_A() or pgb.button_B()) and not playery<6):
            button_pressed=True
        else:
            button_pressed=False
        
        if (prev_button_pressed==False and button_pressed==True):
            playerspeed=-jumpheight
            soundpos=1
        else:
            playerspeed=playerspeed+fallrate
        playery+=playerspeed
        pgb.sprite(0, playerx, playery)
        
        if soundpos==1:
            pgb.sound(116)
            soundpos=2
        elif soundpos==2:
            pgb.sound(146)
            soundpos=3
        elif soundpos==3:
            pgb.sound(233)
            soundpos=4
        else:
            pgb.sound(0)
            soundpos=0
        
        if pipepos1>=240:
            pipey1=randint(-25, 0)
            pipey11=randint(pipey1+25, pipey1+50)
        pipepos1-=int(pipespeed)
        pgb.sprite(1, pipepos1, pipey1)
        pgb.sprite(1, pipepos1, pipey1+26)
        pgb.sprite(1, pipepos1, pipey11)
        pgb.sprite(1, pipepos1, pipey11+26)
        pgb.sprite(2, pipepos1, pipey11+38)
        pgb.sprite(1, pipepos1, pipey11+12+pipespace+26)
        pgb.sprite(1, pipepos1, pipey11+12+pipespace+52)
        pgb.sprite(1, pipepos1, pipey11+12+pipespace+104)
        pgb.sprite(1, pipepos1, pipey11+12+pipespace+78)
        pgb.sprite(3, pipepos1, pipey11+12+pipespace)
        if pipepos1<-52:
            pipepos1=240
            
        if pipepos2>=240:
            pipey2=randint(-25, 0)
            pipey21=randint(pipey2+25, pipey2+50)
        pipepos2-=int(pipespeed)
        pgb.sprite(1, pipepos2, pipey2)
        pgb.sprite(1, pipepos2, pipey2+26)
        pgb.sprite(1, pipepos2, pipey21)
        pgb.sprite(1, pipepos2, pipey21+26)
        pgb.sprite(2, pipepos2, pipey21+38)
        pgb.sprite(1, pipepos2, pipey21+12+pipespace+26)
        pgb.sprite(1, pipepos2, pipey21+12+pipespace+52)
        pgb.sprite(1, pipepos2, pipey21+12+pipespace+104)
        pgb.sprite(1, pipepos2, pipey21+12+pipespace+78)
        pgb.sprite(3, pipepos2, pipey21+12+pipespace)
        if pipepos2<-52:
            pipepos2=240
        if playery>230:
            return
        if check_collision(1, 75, playerx, playery, 34, 24, pipepos1, 0, 52, abs((pipey11+12+52))) or check_collision(17, 75, playerx, playery, 34, 24, pipepos1, pipey11+12+pipespace, 52, abs((pipey11+12+pipespace)-240)) or check_collision(1, 75, playerx, playery, 34, 24, pipepos2, 0, 52, abs((pipey21+12+52))) or check_collision(17, 75, playerx, playery, 34, 24, pipepos2, pipey21+12+pipespace, 52, abs((pipey21+12+pipespace)-240)):
            return
        if check_collision(1, 75, playerx, playery, 34, 24, pipepos1+51, pipey11+12, 1, pipespace) or check_collision(1, 75, playerx, playery, 34, 24, pipepos2+51, pipey21+12, 1, pipespace):
            score+=1
            pipespeed+=0.005
        pgb.create_text(str(int(score/10)), -1, 10, PicoGameBoy.color(255,255,255))
        pgb.show()
        if pgb.button_start():
                pgb.fill_rect(10,90,220,80,PicoGameBoy.color(0,0,0))
                pgb.center_text("Game Paused",PicoGameBoy.color(255,255,255))
                pgb.create_text("Press Start to resume", -1, 135, PicoGameBoy.color(255,255,255))
                pgb.show()
                sleep(0.5)
                while True:
                    pgb.fill_rect(10,90,220,80,PicoGameBoy.color(0,0,0))
                    pgb.center_text("Game Paused",PicoGameBoy.color(255,255,255))
                    pgb.create_text("Press Start to resume", -1, 135, PicoGameBoy.color(255,255,255))
                    pgb.show()
                    if pgb.button_Home():
                        homebootstop=open("/noboot", "w")
                        homebootstop.close()
                        pgb.fill(PicoGameBoy.color(0,0,0))
                        pgb.show()
                        machine.reset()
                        break
                    elif pgb.button_start():
                        sleep(0.5)
                        break
now = ticks_ms()
while True:
    if pgb.button_Home():
        homebootstop=open("/noboot", "w")
        homebootstop.close()
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.show()
        machine.reset()
        break
    pgb.load_image("flappybird_title.bin")
    pgb.show()
    if pgb.button_start():
            x=open("highscoresFlappy Bird.sc", "r")
            scores=x.read()
            x.close()
            del x
            scores=scores.split("\n")
            while True:
                if pgb.button_B():
                    sleep(0.1)
                    break
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
                    pgb.create_text("Score "+str(i+1)+": "+str(scores[i])+" Pipes", -1, 50+i*15, PicoGameBoy.color(255,255,255))
                pgb.create_text("Press B to exit", -1, 220, PicoGameBoy.color(255,255,255))
                pgb.show()
            del scores
    elif pgb.any_button():
        break
    if ticks_diff(ticks_ms(), now) > 200:
        now = ticks_ms()
        pgb.create_text("PRESS ANY BUTTON",20, 120,PicoGameBoy.color(0,0,0))
        pgb.create_text("TO PLAY",50, 130, PicoGameBoy.color(0,0,0))
        pgb.show()
        pgb.free_mem()
        while ticks_diff(ticks_ms(), now) < 200:
            sleep(0.020)
            pgb.free_mem()
        now = ticks_ms()
while True:
    main_game()
    pgb.fill(PicoGameBoy.color(0,0,0))
    pgb.create_text("GAME OVER",-1, 85,PicoGameBoy.color(255,255,255))
    pgb.text("Press A to play again.", 35, 105, PicoGameBoy.color(255,255,255))
    pgb.text("Press home to quit.", 40, 120, PicoGameBoy.color(255,255,255))
    pgb.create_text("Press start", -1, 135, PicoGameBoy.color(255,255,255))
    pgb.create_text("to view scores.", -1, 150, PicoGameBoy.color(255,255,255))
    pgb.create_text("Score: "+str(int(score/7)), -1, 165, PicoGameBoy.color(255,255,255))
    pgb.show()
    pgb.sound(110)
    sleep(0.05)
    pgb.sound(0)
    sleep(0.1)
    pgb.sound(110)
    sleep(0.05)
    pgb.sound(0)
    sleep(0.1)
    with open("highscoresFlappy Bird.sc", "r") as s:
        scores=s.read().split("\n")
        for r in range(len(scores)):
            scores[r]=int(scores[r])
    newscores=scores
    newscores.append(int(score/10))
    newscores.sort(reverse=True)
    for i in range(len(newscores)): newscores[i]=str(newscores[i])
    with open("highscoresFlappy Bird.sc", "w+") as w:
        w.write("\n".join(newscores[:10]))
    del newscores
    del scores
    while True:
        if pgb.button_Home():
            homebootstop=open("/noboot", "w")
            homebootstop.close()
            pgb.fill(PicoGameBoy.color(0,0,0))
            pgb.show()
            machine.reset()
            break
        pgb.fill(PicoGameBoy.color(0,0,0))
        pgb.create_text("GAME OVER",-1, 85,PicoGameBoy.color(255,255,255))
        pgb.text("Press A to play again.", 35, 105, PicoGameBoy.color(255,255,255))
        pgb.text("Press home to quit.", 40, 120, PicoGameBoy.color(255,255,255))
        pgb.create_text("Press start", -1, 135, PicoGameBoy.color(255,255,255))
        pgb.create_text("to view scores.", -1, 150, PicoGameBoy.color(255,255,255))
        pgb.create_text("Score: "+str(int(score/10)), -1, 165, PicoGameBoy.color(255,255,255))
        pgb.show()
        if pgb.button_start():
                x=open("highscoresFlappy Bird.sc", "r")
                scores=x.read()
                x.close()
                del x
                scores=scores.split("\n")
                while True:
                    if pgb.button_B():
                        sleep(0.1)
                        break
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
                        pgb.create_text("Score "+str(i+1)+": "+str(scores[i])+" Pipes", -1, 50+i*15, PicoGameBoy.color(255,255,255))
                    pgb.create_text("Press B to exit", -1, 220, PicoGameBoy.color(255,255,255))
                    pgb.show()
                del scores
        elif pgb.button_A():
            score=0
            break