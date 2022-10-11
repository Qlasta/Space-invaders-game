from turtle import Turtle


STEP = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("ship.gif")
        self.color("blue")
        self.shapesize(2,2)
        self.penup()
        self.goto(0, -230)
        self.setheading(90)


    def move_right(self):
        self.goto(self.xcor() + STEP, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - STEP, self.ycor())





