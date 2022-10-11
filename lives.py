from turtle import Turtle

class Lives():
    def __init__(self):
        self.lives = []
        xlive = -270
        ylive = -270
        for n in range(2):
            live = Turtle()
            live.shape("ship.gif")
            live.penup()
            live.goto(xlive, ylive)
            live.setheading(90)
            xlive += 40
            self.lives.append(live)

class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(-290, -250)
        self.pendown()
        self.goto(280, -250)
        self.penup()
        self.goto(200, -280)
        self.write(f"Score: {self.score}")

    def add_points(self):
        self.clear()
        self.score += 30
        self.penup()
        self.goto(-290, -250)
        self.pendown()
        self.goto(280, -250)
        self.penup()
        self.goto(200, -280)
        self.write(f"Score: {self.score}")

    def game_over(self):
        self.clear()
        self.goto(-60,0)
        self.write(f"GAME OVER\nFinal score: {self.score}", font=("Arial", 16, "normal"))


