from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

# moves turtle forward by 10
def move_forwards():
    tim.forward(10)


#move turtle backwards by 10
def move_backwards():
    tim.backward(10)


# turn turtle left or counterclockwise by 10 degrees
def turn_left():
    heading = tim.heading() + 10
    tim.setheading(heading)


# turn turtle right or clockwise by 10 degrees
def turn_right():
    heading = tim.heading() - 10
    tim.setheading(heading)


# clear the screen of all drawings and reset turtle
# to starting location
def clear_screen():
    tim.clear()
    screen.resetscreen()


# set listener
screen.listen()

# set onkey action events
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
# exit window on click
screen.exitonclick()
