import tkinter as tk
import sprites

MAPROW = 4
MAPCOL = 4

class MainFrame:

    def __init__(self):
        #create master
        self.master = tk.Tk()
        #create elements
        self.mainFrame = tk.Canvas(self.master, width=600, height=300, relief=tk.GROOVE, borderwidth=2)
        self.others = tk.Frame(self.master, relief=tk.GROOVE, borderwidth=2)
        self.label1 = tk.Label(self.others, text="something: ")
        self.button1 = tk.Button(self.others, text="Start", command=self.start)

        #config elements
        self.master.minsize(width=800, height=300)
        self.tiles = []
        self.build()
        #self.master.bind("a", lambda move: self.updateTiles(2, 2))
        self.master.bind("<Key>", self.keyPressed)

        #pack elements
        self.others.pack(side=tk.LEFT, fill=tk.BOTH)
        self.label1.pack()
        self.button1.pack()
        self.mainFrame.pack(side=tk.LEFT, fill=tk.BOTH)
        #mainloop
        self.master.mainloop()

    #Handle key presses, because apparently, you need it
    def keyPressed(self, event):
        if event.char == "a":
            self.updateTiles(20, 0)
        if event.char == "d":
            self.updateTiles(-20, 0)


    def start(self):
        pass

    def updateTiles(self, offX, offY):
        for i in range(MAPCOL):
            for j in range(MAPROW):
                self.tiles[i][j].updatePos(offX, offY)


    def build(self, offX=20, offY=20):
        for i in range(MAPROW):
            self.tiles.append([])
            for j in range(MAPCOL):
                self.tiles[i].append(sprites.tile(offX, offY, "pics/grass-tile-1-64.png", self.mainFrame))
                offX += 64
            offX -= MAPCOL*64
            offY += 64
game_main = MainFrame()
