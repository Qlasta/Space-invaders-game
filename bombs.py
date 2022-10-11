from turtle import Turtle
import random

class Bombs():
    def __init__(self):
        self.all_bombs = []

    def create_bomb(self):
        random_numb = random.randint(1,10)
        if random_numb == 10:
            bomb = Turtle()
            bomb.shape("circle")
            bomb.penup()
            bomb.color("yellow")
            bomb.shapesize(0.2,0.2)
            bomb.goto(random.randrange(-200,200, 10), 200)
            self.all_bombs.append(bomb)

    def fall(self):
        for bomb in self.all_bombs:
            bomb.goto(bomb.xcor(), bomb.ycor()-15)