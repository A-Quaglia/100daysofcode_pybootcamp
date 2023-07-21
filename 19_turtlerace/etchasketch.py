from turtle import Turtle, Screen


class EtchAScketch:

    def __init__(self):
        self.pen = None

        self.heading = 0

    def set_up(self):
        self.pen = Turtle()
        self.screen = Screen()
        self.screen.title("Etch A Sketch")

    def run(self):
        self.set_up()
        self.game_update()

    def move_forwards(self):
        self.pen.forward(10)

    def move_backwards(self):
        self.pen.backward(10)

    def move_left(self):
        self.heading += 15
        self.pen.setheading(self.heading)

    def move_right(self):
        self.heading -= 15
        self.pen.setheading(self.heading)

    def clear(self):
        self.pen.clear()
        self.pen.penup()
        self.pen.home()
        self.pen.pendown()

    def game_update(self):
        self.screen.listen()
        self.screen.onkey(key='w', fun=self.move_forwards)
        self.screen.onkey(key='s', fun=self.move_backwards)
        self.screen.onkey(key='a', fun=self.move_left)
        self.screen.onkey(key='d', fun=self.move_right)
        self.screen.onkey(key='c', fun=self.clear)
        self.screen.exitonclick()


if __name__ == '__main__':
    game = EtchAScketch()
    game.run()
