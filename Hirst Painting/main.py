import colorgram
import turtle as t
from turtle import Screen
import random

screen = Screen()
screen.screensize(100, 100)

# code to retrieve colors from image.jpg
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# set initial (x, y) coordinates of turtle
x = -250
y = -200

# change colormode to allow custom colors
t.colormode(255)
# pen up to avoid drawing lines between dots
t.penup()
# set to max drawing speed
t.speed("fastest")
# hide turtle
t.hideturtle()

# list containing all colors
color_list = [(242, 234, 237), (43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147), (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37), (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108), (154, 222, 193), (181, 170, 221), (30, 163, 170), (84, 35, 39), (40, 46, 80), (233, 167, 180), (237, 172, 162), (76, 40, 39), (154, 208, 221), (115, 46, 43)]

# outer loop set the turtle to the proper row.
# increment by 50 to go to next row after printing
for _ in range(10):
    # set turtle to starting point
    t.goto(x, y)
    # print each dot in the row
    for __ in range(10):
        # set dot to proper size, select random color from color_list
        t.dot(20, random.choice(color_list))
        # space each dot equally
        t.forward(50)
    y += 50

screen.exitonclick()