from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen ()

timmy.shape("turtle")
timmy.color("black", "DarkOliveGreen4")

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_counter_clockwise():
    timmy.left(5)

def move_clockwise():
    timmy.right(5)

def clear_drawing():
    # screen.clear()
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_counter_clockwise)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkeypress(key="c", fun=clear_drawing)
screen.exitonclick()
