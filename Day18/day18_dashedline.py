from turtle import Turtle, Screen
# Creating alias for import
# import turtle as t
# tim = t.Turtle()

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("black", "DarkOliveGreen4")

for _ in range(50):
    timmy.forward(2)
    timmy.penup()
    timmy.forward(2)
    timmy.pendown()

screen.exitonclick()