from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# creating a Function to be passed as argument for onkey()
def move_forward():
    timmy.forward(10)

#Listen for events on screen
screen.listen()
# When function is passed as argument to a function '()' are not required 
# Higher order functions, by practice use keyword arguments instead of positional arguments
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()

