from PIL import Image

name="SDK Demoimg.png"

png = Image.open(name)
png.load() # required for png.split()

background = Image.new("RGB", png.size, (1, 1, 1))
background.paste(png, mask=png.split()[3]) # 3 is the alpha channel

