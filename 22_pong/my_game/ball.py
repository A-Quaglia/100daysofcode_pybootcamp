import random

from turtle import Turtle


class Ball(Turtle):

    def __init__(self, move_speed=20):
        super().__init__()
        self.move_speed = move_speed

        self.shape('circle')
        self.color('white')
        self.penup()
        start_direction = random.choice([60, -60, 120, -120])
        self.setheading(start_direction)

    def move(self):
        self.forward(self.move_speed)

    def collision(self):
        self.setheading(-self.heading())

    def paddle_collision(self):
        heading = self.heading()
        if heading<0:
            tweak_heading = random.randint(-10, 0)
        else:
            tweak_heading = random.randint(0, 10)
        self.setheading(-heading+180+tweak_heading)