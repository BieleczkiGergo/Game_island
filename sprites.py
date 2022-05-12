import tkinter as tk

#Ez a fájl hülyeség, de ne töröld

class tile:

    def __init__(self, posX, posY, image, nest, nestWidth=600, nestHeight=300, offX=0, offY=0):
        #posX and posY : X and Y offset
        #image : the image file to be imported (use 16*16 png)
        #nest : canvas where the image might be put
        self.image = tk.PhotoImage(file=image)
        self.tile = nest.create_image(posX, posY, anchor=tk.NW, image=self.image)
        self.nestWidth=nestWidth
        self.nestHeight = nestHeight
        self.nest = nest

    def updatePos(self, offX, offY):
        self.nest.move(self.tile, offX, offY)
