class Barrier:
    def __init__(self,canvas,starting_x,starting_y,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,50,20,fill = color)
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.hit = False
        self.canvas.move(self.id,self.starting_x,self.starting_y)
    def deli(self):

        self.canvas.delete(self.id)
