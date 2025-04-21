import sys
import os
import machine

filestodelete=["PicoBoySDK.py","PicoGameBoy.py","rpmidi.py","st7789.py","Functions.py"]


root=os.listdir("/")
for file in filestodelete:
    if file in root:
        os.remove("/"+file)

os.remove("/main.py")
os.rename("/update.py", "/main.py")
machine.reset()