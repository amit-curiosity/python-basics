# import colorgram
#
# colors = colorgram.extract('./images/image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = red, green, blue
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
from random import choice

jerry = Turtle()

jerry.hideturtle()
jerry.speed(0)

screen = Screen()
screen.colormode(255)

colors = [
    (199, 168, 94), (227, 239, 232), (129, 179, 191), (163, 58, 78), (234, 221, 121),
    (49, 113, 167), (241, 217, 222), (104, 87, 83), (143, 187, 119), (239, 245, 249),
    (216, 151, 171), (67, 125, 76), (94, 124, 180), (85, 165, 94), (190, 71, 90),
    (161, 34, 49), (142, 119, 116), (221, 173, 182), (175, 205, 174), (163, 202, 211),
    (204, 116, 48), (75, 60, 56), (67, 56, 52), (176, 190, 213), (215, 180, 177),
    (78, 140, 175)
]


def shift_turtle_origin(xcor, ycor):
    jerry.penup()
    jerry.goto(xcor, ycor)
    jerry.pendown()


# print(colors)
def draw_single_dotted_line(distance, direction, dot_size, n_vertical_lines):
    for _ in range(n_vertical_lines):
        jerry.dot(dot_size, choice(colors))
        jerry.penup()
        if direction == 'forward':
            jerry.forward(distance)
        else:
            jerry.backward(distance)
        jerry.pendown()


def draw_hirst_painting(n_horizontal_lines, n_vertical_lines, dot_size, distance_between_dots):
    x, y = (n_vertical_lines * distance_between_dots) / 2, (n_horizontal_lines * distance_between_dots) / 2
    for i in range(n_horizontal_lines):
        y -= distance_between_dots
        if i % 2 == 0:
            shift_turtle_origin(-x + distance_between_dots / 2, -y - distance_between_dots / 2)
            draw_single_dotted_line(distance=distance_between_dots, direction='forward', dot_size=dot_size,
                                    n_vertical_lines=n_vertical_lines)
        else:
            shift_turtle_origin(x - distance_between_dots / 2, -y - distance_between_dots / 2)
            draw_single_dotted_line(distance=distance_between_dots, direction='backward', dot_size=dot_size,
                                    n_vertical_lines=n_vertical_lines)


draw_hirst_painting(n_horizontal_lines=20, n_vertical_lines=20, dot_size=10, distance_between_dots=25)
screen.exitonclick()
