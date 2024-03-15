#!/usr/bin/python

# Converts an RGB image to a framebuffer for the ST7789 display
# The ST7789 display expects 16 bits (2 bytes) per pixel
# encoded in RGB565 format (Least Significant Bit first).
#
# png2fb.py inputfile [outputfile]

import sys
from copy import deepcopy
from PIL import Image

def color(rgb565):
    rgb565=int.from_bytes(rgb565,"little")
    lsb = (rgb565 & 0b0000000011111111)<<8
    msb = (rgb565 & 0b1111111100000000)>>8
    rgb565=(lsb | msb)
    red5 = rgb565 >> 11
    green6 = (rgb565 >> 5) & 0b111111
    blue5 = rgb565 & 0b11111
    red8 = round(red5 / 31 * 255)
    green8 = round(green6 / 63 * 255)
    blue8 = round(blue5 / 31 * 255)
    return red8, green8, blue8

output= Image.new(mode="RGB", size=(480, 480))
image="./out.bin"

with open(image, "rb") as r:
    for y in range(240):
        for x in range(240):
            data=r.read(2)
            for y2 in range(2):
                for x2 in range(2):
                    output.putpixel((x*2+x2,y*2+y2),color(data))

#output.show()
output.save("out.png")
