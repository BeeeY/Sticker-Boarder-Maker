from PIL import Image
from PIL import ImageFilter
from PIL import ImageTk
import tkinter as Tk
from tkinter import filedialog

path = ""

def choose_file():
    global path
    path = filedialog.askopenfilename()

def boardermaker(img, thickness):

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

root = Tk.Tk()
root.title("Sticker Border Maker")

StickerPath = Tk.Label(root, text="Sticker Path: ")
StickerPath.pack()
PathButton = Tk.Button(root, text="Choose File", command=choose_file)
PathButton.pack()
BoarderSize = Tk.Label(root, text="Boarder Size: ")
BoarderSize.pack()
BoarderScale = Tk.Scale(root,from_=1, to=100, orient="horizontal")
BoarderScale.pack()
Generate = Tk.Button(root, text="Generate", command=boardermaker)
Generate.pack()

root.mainloop()