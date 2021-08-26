
# подключаем модули
import time
from myClasses.Window import Window
from myClasses.Score import Score
from myClasses.Paddle import Paddle
from myClasses.Ball import Ball
from myClasses.Barrier import Barrier
from myClasses.GameDifficulty import GameDifficulty
speed = 2
# точка входа нашей программы
if __name__ == '__main__':
    gamedifficulty = GameDifficulty()
    # создаем наше игровое окно
    window = Window()

    mas_barriers = []
    # создаём объект — зелёный счёт
    score =Score(window.canvas, 'black')
    # создаём объект — белую платформу
    paddle = Paddle(window.canvas, 'White')
    for i in range(0,1):
        for j in range(0,9):
            barrier = Barrier(window.canvas,j*56,i*23,'green')
            mas_barriers.append(barrier)


    # создаём объект — красный шарик
    ball = Ball(window.canvas, paddle, score,mas_barriers,window,speed,'red')
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

