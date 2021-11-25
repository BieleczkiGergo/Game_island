import tkinter as tk

class mainFrame:
    mainFrame = 0
    master = 0
    others = 0
    label1 = 0
    button1 =0
    frames = 0
    def __init__(self):
        self.master = tk.Tk()
        self.mainFrame = tk.Canvas(self.master, width=600, height=300, relief=tk.GROOVE, borderwidth=2)
        self.others = tk.Frame(self.master, relief=tk.GROOVE, borderwidth=2)
        self.label1 = tk.Label(self.others, text="something: ")
        self.button1 = tk.Button(self.others, text="Start", command=start)

        self.master.minsize(width=800, height=300)

        self.others.pack(side=tk.LEFT, fill=tk.BOTH)
        self.label1.pack()
        self.button1.pack()
        self.mainFrame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.master.mainloop()

    def add_sprite(self, sprite):
        pass

    def add_polygon(self, x, y, width, height):
        self.mainFrame.create_polygon(x, y, width+x, height+y)

    def start(self):
        self.add_polygon(10, 10, 20, 20)




game_main = mainFrame()