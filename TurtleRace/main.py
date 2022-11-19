from turtle import Turtle, Screen
import random

is_race_on = False
# list that will hold all created turtles
turtle_list = []
# list of turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]
screen = Screen()
# set screen width and height
screen.setup(width=500, height=400)
x = -230
y = -70

# get user guess
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# for each color of turtle, create the turtle and set them
# to starting position. add turtle to turtle_list
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 30
    turtle_list.append(new_turtle)

# if user has made a choice, set variable to true
if user_choice:
    is_race_on = True

# while there is no winner, continue to add a random distance
# to a random turtle
while is_race_on:
    rand_distance = random.randint(0, 10)
    rand_turtle = random.randint(0, len(colors) - 1)
    turtle_list[rand_turtle].forward(rand_distance)
    # if a turtle reaches x coordinate of 250, it is declared the winnder
    if turtle_list[rand_turtle].xcor() >= 230:
        # find the color of the turtle that won
        winner = turtle_list[rand_turtle].pencolor()
        is_race_on = False

# print the color of the turtle that won
# check if turtle is the same has user choice
print(f"The {winner} turtle has won!")
if user_choice.lower() == winner:
    print("You guessed correctly!")
else:
    print("You did not guess correctly!")

screen.exitonclick()