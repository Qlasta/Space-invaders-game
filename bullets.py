from turtle import Turtle

class Bullets():
    def __init__(self):
        self.all_bullets = []

    def create_bullet(self, playerx, playery):
        bullet = Turtle()
        bullet.shape("square")
        bullet.penup()
        bullet.color("white")
        bullet.shapesize(0.2,0.1)
        bullet.goto(playerx,playery)
        self.all_bullets.append(bullet)


    def shoot(self):
        for bullet in self.all_bullets:
            bullet.goto(bullet.xcor(), bullet.ycor()+30)