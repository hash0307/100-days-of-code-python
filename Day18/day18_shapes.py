from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
turtle_colors = ('red', "green", "blue", "brown", "black", "violet", "pink", "purple")

timmy.shape("turtle")
timmy.color("black", "DarkOliveGreen4")

# 1st solution
# for side in range(3, 11):
#     timmy.pencolor(random.choice(turtle_colors))
#     for _ in range(side):
#         timmy.forward(60)
#         timmy.right(360/side)

# 2nd solution
def draw_shape(side):
    for _ in range(side):
        timmy.forward(60)
        timmy.right(360/side)

for side in range(3, 11):
    timmy.color(random.choice(turtle_colors))
    draw_shape(side)


screen.exitonclick()