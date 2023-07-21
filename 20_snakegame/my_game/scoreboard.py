from turtle import Turtle

ALIGMENT = 'center'
FONT = ('Courier', 14, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.write(f"SCORE: {self.score}", align=ALIGMENT, font=FONT)

    def make_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}",  align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGMENT, font=FONT)

