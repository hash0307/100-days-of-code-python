from turtle import Turtle, Screen
# Screen is a class which holds the turtle.
# Construct a new object in Python
timmy = Turtle()
print(timmy)
#Change shape, color of Timmy using the methods from Turtle class
timmy.shape("turtle")
timmy.color("black", "DarkOliveGreen4")

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

# Excercise 
# Refer documentation & move the turtle forward by 100 paces
timmy.forward(100)


# This method will allows our program to run until we click on screen
my_screen.exitonclick()
