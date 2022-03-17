import random

import colorgram
import turtle as t

t.colormode(255)

colors = []
image_colors = colorgram.extract('trees.jpg', 30)
for color in image_colors:
    rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
    colors.append(rgb)

pen = t.Turtle()
pen.hideturtle()
pen.speed("fastest")


def draw_row(num_dots, gap):
    for i in range(num_dots):
        rand_color = random.choice(colors)
        pen.pencolor(rand_color)

        pen.pendown()
        pen.dot(gap / 2)
        pen.penup()
        pen.forward(gap)


def next_row(gap):
    pen_dir = pen.heading()
    pen.pendown()
    pen.dot(gap / 2)
    pen.penup()
    if pen_dir == 0.0:
        pen.left(90)
        pen.forward(gap)
        pen.left(90)
    else:
        pen.right(90)
        pen.forward(gap)
        pen.right(90)

def init_pos():
    pen.penup()
    pen.setposition(-250,-250)

def draw_painting(num_rows):
    screen = t.Screen()

    init_pos()

    gap = 50
    for i in range(num_rows):
        draw_row(num_rows, gap)
        next_row(gap)

    screen.exitonclick()

draw_painting(10)
