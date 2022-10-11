from turtle import Turtle, Screen
import time
import functools
from player import Player
from aliens import Aliens
from bullets import Bullets
from bombs import Bombs
from lives import Lives, Points

screen = Screen()


screen.title("Space invaders by AstaK")
screen.setup(600, 600)
screen.bgcolor("Black")
screen.addshape('alien.gif')
screen.addshape('ship.gif')
screen.tracer(0)

game_is_on = True

player = Player()
aliens = Aliens()
bullets = Bullets()
bombs = Bombs()
lives = Lives()
points = Points()


while game_is_on:
    screen.update()
    time.sleep(0.1)

    aliens.move()
    for alien in aliens.all_aliens:
        if alien.xcor() > 200:
            aliens.change_move()
        if alien.xcor() < -200:
            aliens.change_move()
    bombs.create_bomb()
    bombs.fall()
    for bomb in bombs.all_bombs:
        if bomb.distance(player.xcor(), player.ycor()) < 20:
            bomb.shapesize(1,1)
            time.sleep(1)
            bomb.goto(1000,1000)
            if len(lives.lives) > 0:
                lives.lives[-1].goto(1000,1000)
                lives.lives.pop()
            else:
                points.game_over()

    bullets.shoot()
    for bullet in bullets.all_bullets:
        for alien in aliens.all_aliens:
            if bullet.distance(alien.xcor(), alien.ycor()) < 20:
                alien.goto(1000,1000)
                bullet.goto(1000,1000)
                points.add_points()

    screen.listen()
    screen.onkey(player.move_left, "Left")
    screen.onkey(player.move_right, "Right")
    screen.onkey(functools.partial(bullets.create_bullet, playerx=player.xcor(), playery=player.ycor()), "Up")




screen.exitonclick()
