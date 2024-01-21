from turtle import Turtle, Screen
# Creating alias for import
# import turtle as t
# tim = t.Turtle()

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("black", "DarkOliveGreen4")

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen.exitonclick()