import time

from turtle import Screen

from paddle import Paddle
from ball import Ball

WIDTH = 800
HEIGHT = 600
PADDLE_POSITION = 360

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


first_player = Paddle(-PADDLE_POSITION, paddle_size=3)
second_player = Paddle(PADDLE_POSITION, paddle_size=3)
ball = Ball()


screen.listen()
screen.onkey(first_player.up, "w")
screen.onkey(first_player.down, "s")
screen.onkey(second_player.up, "Up")
screen.onkey(second_player.down, "Down")

y_collision_point = HEIGHT/2 - 20

game_on = True



while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if abs(ball.ycor()) >= y_collision_point:
        ball.collision()

    if (ball.xcor() >= -PADDLE_POSITION+5 and ball.distance(first_player) <= 50) or \
        (ball.xcor() >= PADDLE_POSITION-5 and ball.distance(second_player) <= 50):

        ball.paddle_collision()


screen.exitonclick()
