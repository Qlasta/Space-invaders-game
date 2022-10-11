from turtle import Turtle
import time

class Aliens():
    def __init__(self):
        self.all_aliens = []
        xcoordinate = -200
        ycoordinate = 80
        for line in range(5):
            for n in range(8):
                self.create_alien(xcoordinate, ycoordinate)
                xcoordinate += 50
            xcoordinate = -200
            ycoordinate += 50
        self.step = 5

    def create_alien(self, xcoordinate, ycoordinate):
        alien = Turtle()
        alien.penup()
        alien.color("green")
        alien.shape("alien.gif")
        alien.shapesize(2,2)
        alien.goto(xcoordinate,ycoordinate)
        self.all_aliens.append(alien)

    def move(self):
        for alien in self.all_aliens:
            alien.goto(alien.xcor()+self.step, alien.ycor())

    def change_move(self):
        self.step *= -1



