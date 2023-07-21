from random import choice

import colorgram
import turtle as t

# hirst_colors = colorgram.extract('hirst_painting.jpg', 20)
# hirst_colors = [(x.rgb.r, x.rgb.g, x.rgb.b) for x in hirst_colors]
# print(hirst_colors)

HIRST_COLORS = [(230, 227, 225), (229, 223, 226), (217, 227, 220), (195, 172, 121), (222, 227, 232), (157, 97, 59),
                (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85), (118, 162, 175),
                (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82),
                (207, 202, 146)]

WIDTH, HEIGHT = 500, 500

screen = t.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Hirst Paint - kind of')

t.colormode(255)

tim = t.Turtle()
tim.speed(0)
tim.hideturtle()

tim.penup()
print()


# def draw_dot(size=10, color="blue"):
#     tim.pendown()
#     tim.dot(size, color)
#     tim.penup()

def draw_dot(size=10, color="blue", use_dot=True):
    tim.pendown()
    tim.fillcolor(color)
    tim.pencolor(color)
    tim.begin_fill()
    tim.circle(size, steps=4)
    tim.end_fill()
    tim.penup()


def hirst_turtle(width, height, rows, columns, dot_size=20, colors=["red", "blue"], offset=None):
    if not offset:
        offset_x = width / (rows + 1)
        offset_y = height / (rows + 1)

    offset_x = offset
    offset_y = offset

    tim.penup()
    tim.setpos(((-width / 2) + offset_x, (-height / 2) + offset_y))

    for row in range(1, rows + 1):
        for column in range(columns):
            color = choice(colors)
            tim.forward(offset_x)
            draw_dot(dot_size, color)

        tim.setpos(((-width / 2) + offset_x, (-height / 2) + offset_y * (row + 1)))


# hirst_turtle(WIDTH, HEIGHT, 10, 10, colors = HIRST_COLORS)

hirst_turtle(WIDTH, HEIGHT, 10, 10, dot_size=10, colors=HIRST_COLORS, offset=50)

t.exitonclick()
