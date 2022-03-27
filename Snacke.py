from turtle import Turtle



UP = 90
DOWN= 270
RIGHT = 0
LEFT = 180

class Snake:


    def __init__(self):
        self.snakes = []
        self.amount = 3
        self.create_snake()
        self.head= self.snakes[0]
        self.xArr = [0, -20, -40]


    def create_snake(self):
        for t in range(0, 3):
            xArr = [0, -20, -40]
            new_t = Turtle("square")
            new_t.color("white")
            new_t.speed(10)
            new_t.penup()
            new_t.setposition(x=xArr[t], y=0)
            self.snakes.append(new_t)

    def move(self):
        for num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[num - 1].xcor()
            new_y = self.snakes[num - 1].ycor()
            self.snakes[num].setposition(x=new_x, y=new_y)
        self.head.forward(10)



    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(90)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(270)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(0)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(180)

    def get_pos(self):
        return self.snakes[0].position()

    def eat(self):
        new_t = Turtle("square")
        new_t.penup()
        new_t.color("white")
        new_t.speed(10)
        new_t.setposition(self.snakes[-1].position())
        self.amount += 1
        self.snakes.append(new_t)

    def reset(self):
        for s in self.snakes:
            s.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]






