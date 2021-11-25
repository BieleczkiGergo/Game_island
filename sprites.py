import tkinter as tk
from frame import mainFrame

#Ez a fájl hülyeség, de ne töröld

class rectangle:
    posx = 0
    posy = 0
    width = 0
    height = 0
    nest = 0

    def __init__(self, nest, position_x, position_y, width, height):
        nest.create_polygon(position_x, position_y, position_x+width, position_y+height)

game = mainFrame()
