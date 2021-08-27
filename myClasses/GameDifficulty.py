# подключаем модули
from tkinter import *
import time
from myClasses.Window import Window
from myClasses.Score import Score
from myClasses.Paddle import Paddle
from myClasses.Ball import Ball
from myClasses.Barrier import Barrier


class GameDifficulty:
    def __init__(self):
        self.tk = Tk()

        self.b1 = Button(text="Легкий",
                         width=15, height=3)
        self.b1['command'] = lambda sp=1: self.start(sp)
        self.b1.pack()
        self.b2 = Button(text="Средний",
                         width=15, height=3)
        self.b2['command'] = lambda sp=2: self.start(sp)
        self.b2.pack()
        self.b3 = Button(text="Тяжелый",
                         width=15, height=3)
        self.b3['command'] = lambda sp=3: self.start(sp)
        self.b3.pack()
        self.tk.mainloop()

    def start(self, e):
        global speed
        speed = e
        self.tk.destroy()
        window = Window()

        mas_barriers = []
        # создаём объект — зелёный счёт
        score = Score(window.canvas, 'black')
        # создаём объект — белую платформу
        paddle = Paddle(window.canvas, 'White')
        for i in range(0, 1):
            for j in range(0, 9):
                barrier = Barrier(window.canvas, j * 56, i * 23, 'green')
                mas_barriers.append(barrier)

        # создаём объект — красный шарик
        ball = Ball(window.canvas, paddle, score, mas_barriers, window, speed, 'red')
        # пока шарик не коснулся дна
        while not ball.hit_bottom:

            # если игра началась и платформа может двигаться
            if paddle.started == True:
                # двигаем шарик
                ball.draw()
                # двигаем платформу
                paddle.draw()
            # обновляем наше игровое поле, чтобы всё, что нужно, закончило рисоваться
            window.tk.update_idletasks()
            # обновляем игровое поле, и смотрим за тем, чтобы всё, что должно было быть сделано — было сделано
            window.tk.update()
            # замираем на одну сотую секунды, чтобы движение элементов выглядело плавно
            time.sleep(0.01)
        # если программа дошла досюда, значит, шарик коснулся дна. Ждём 3 секунды, пока игрок прочитает финальную надпись, и завершаем игру
        time.sleep(3)




