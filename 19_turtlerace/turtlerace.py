from random import randint

from turtle import Turtle, Screen

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen = Screen()
screen.setup(width=500, height=400)


def set_racers(num_racers=6):
    racers = []

    x_ini = - 230
    offset_y = (screen.window_height() / (num_racers+1))

    racers_pos = [(x_ini, (-screen.window_height() / 2) + (offset_y * (i + 1))) for i in range(num_racers)]

    for racer_pos, color in zip(racers_pos, COLORS):
        racer = Turtle(shape='turtle')
        racer.color(color)
        racer.penup()
        racer.goto(racer_pos)
        racer.pendown()
        racers.append(racer)

    return racers

def race(racers, user_bet):
    user_bet = user_bet.lower()
    racers_colors = [racer.pencolor() for racer in racers]

    if not user_bet in racers_colors:
        print('Please enter a valid bet')
        return
    while True:
        for racer in racers:
            speed = randint(10,30)
            racer.forward(speed)
            if racer.xcor() > 230:
                print(f"{racer.pencolor()} Won the race")
                if user_bet == racer.pencolor():
                    print("You Won the Bet!!")
                else:
                    print("You Lost the Bet")
                return



racers = set_racers()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")
race(racers, user_bet)

screen.exitonclick()
