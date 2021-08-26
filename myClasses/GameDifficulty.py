from tkinter import *
from Window import Window

class GameDifficulty:
    def __init__(self,window):
        self.window = window
        self.tk = Tk()
        global speed
        self.b1 = Button(text="Легкий",
                    width=15, height=3)
        self.b1['command'] = lambda sp=1: self.speed_ball(sp)
        self.b1.pack()
        self.b2 = Button(text="Средний",
                    width=15, height=3)
        self.b2['command'] = lambda sp=2: self.speed_ball(sp)
        self.b2.pack()
        self.b3 = Button(text="Тяжелый",
                    width=15, height=3)
        self.b3['command'] = lambda sp=3: self.speed_ball(sp)
        self.b3.pack()
        self.tk.mainloop()
    def speed_ball(self,e):
        self.speed = e
        self.tk.withdraw()
        window.tk.deiconify()