import tkinter as tk

class game:
    mainFrame = 0
    master = 0
    others = 0
    label1 = 0
    button1 =0
    def __init__(self):
        self.master = tk.Tk()
        self.mainFrame = tk.Canvas(self.master, width=600, height=300, relief=tk.GROOVE, borderwidth=2)
        self.others = tk.Frame(self.master, relief=tk.GROOVE, borderwidth=2)
        self.label1 = tk.Label(self.others, text="something: ")
        self.button1 = tk.Button(self.others, text="do something")

        self.master.minsize(width=800, height=300)

        self.others.pack(side=tk.LEFT, fill=tk.BOTH)
        self.label1.pack()
        self.button1.pack()
        self.mainFrame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.master.mainloop()


game_main = game()