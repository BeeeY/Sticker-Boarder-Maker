from PIL import Image
from PIL import ImageFilter

path = input("Put image path (no quotes): ")
thickness = int(input("Put border Size (pxls): "))

img = Image.open(path)
img = img.convert("RGBA")

w, h = img.size
canvas = Image.new("RGBA", (w + 2*thickness, h + 2*thickness), (0, 0, 0, 0))
canvas.paste(img, (thickness, thickness))

mask = canvas.getchannel("A")

mask = mask.filter(ImageFilter.MaxFilter(thickness*2+1))

border = Image.new("RGBA", canvas.size, (255, 255, 255, 255))
border.putalpha(mask)

sticker = Image.alpha_composite(border, canvas)

sticker.save("sticker.png")
print("done")

