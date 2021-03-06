import random
# Описываем класс Ball, который будет отвечать за шарик
class Ball:
    # конструктор — он вызывается в момент создания нового объекта на основе этого класса
    def __init__(self, canvas, paddle, score, mas_barriers,speed,color):
        # задаём параметры объекта, которые нам передают в скобках в момент создания
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.mas_barriers = mas_barriers
        self.speed = speed
        # цвет нужен был для того, чтобы мы им закрасили весь шарик
        # здесь появляется новое свойство id, в котором хранится внутреннее название шарика
        # а ещё командой create_oval мы создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.id = canvas.create_oval(10,10, 25, 25, fill=color)
        # помещаем шарик в точку с координатами 245,100
        self.canvas.move(self.id, 245, 250)
        # задаём список возможных направлений для старта
        starts = [-self.speed, -self.speed, self.speed, self.speed]
        # перемешиваем его
        random.shuffle(starts)
        # выбираем первый из перемешанного — это будет вектор движения шарика
        self.x = starts[0]
        # в самом начале он всегда падает вниз, поэтому уменьшаем значение по оси y
        self.y = -self.speed
        # шарик узнаёт свою высоту и ширину
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # свойство, которое отвечает за то, достиг шарик дна или нет. Пока не достиг, значение будет False
        self.hit_bottom = False
    # обрабатываем касание платформы, для этого получаем 4 координаты шарика в переменной pos (левая верхняя и правая нижняя точки)
    def hit_paddle(self, pos):
        # получаем кординаты платформы через объект paddle (платформа)
        paddle_pos = self.canvas.coords(self.paddle.id)
        # если координаты касания совпадают с координатами платформы
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                # возвращаем метку о том, что мы успешно коснулись
                return True
        # возвращаем False — касания не было
        return False
    def hit_barrier(self,pos):
        self.barrier_pos = []
        for self.bar in self.mas_barriers:
            self.barrier_pos.append(self.canvas.coords(self.bar.id))

        for self.barr in self.barrier_pos:

            if pos[2] >= self.barr[0] and pos[0] <= self.barr[2]:
                if pos[3] >= self.barr[1] and pos[1] <= self.barr[3]:
                    # увеличиваем счёт (обработчик этого события будет описан ниже)
                    self.score.hit()
                    position = self.barrier_pos.index(self.barr)
                    self.mas_barriers[position].destruction()
                    self.barrier_pos.remove(self.barr)
                    self.mas_barriers.remove(self.mas_barriers[position])

                    # возвращаем метку о том, что мы успешно коснулись
                    return True
            # возвращаем False — касания не было
        return False


    # обрабатываем отрисовку шарика
    def draw(self):
        # передвигаем шарик на заданные координаты x и y
        self.canvas.move(self.id, self.x, self.y)
        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.id)
        # если шарик падает сверху
        if pos[1] <= 0:
            # задаём падение на следующем шаге = speed
            self.y = self.speed
        # если шарик правым нижним углом коснулся дна
        if pos[3] >= self.canvas_height:
            # помечаем это в отдельной переменной
            self.hit_bottom = True
            # выводим сообщение и количество очков
            self.canvas.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')
        # если сломаны все препятствия выводим победу
        if  len(self.mas_barriers) == 0:
            self.hit_bottom = True
            self.canvas.create_text(250, 120, text='Вы выйграли', font=('Courier', 30), fill='green')

        # если было касание платформы
        if self.hit_paddle(pos) == True:
            # отправляем шарик наверх
            self.y = -self.speed
        # если коснулись левой стенки
        if pos[0] <= 0:
            # движемся вправо
            self.x = self.speed
        # если коснулись правой стенки
        if pos[2] >= self.canvas_width:
            # движемся влево
            self.x = -self.speed
        if self.hit_barrier(pos) == True:

            self.y = self.speed
