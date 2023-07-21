
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_x, paddle_size=4, move_speed=20):
        super().__init__()
        self.move_speed = move_speed

        self.shape('square')
        self.speed('fastest')
        self.color('white')
        self.shapesize(stretch_len=paddle_size)
        self.setheading(90)
        self.penup()
        self.goto((start_x, 0))

    def up(self):
        self.forward(self.move_speed)

    def down(self):
        self.forward(-self.move_speed)

if __name__ == '__main__':
    paddle = Paddle(-200)
