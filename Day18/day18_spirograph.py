from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

screen.colormode(255)
timmy.shape("turtle")
timmy.color("black", "DarkOliveGreen4")
# Sets the speed of turtle
timmy.speed("fastest")

def choose_random_color():
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return random_color


# 1st solution
# for _ in range(100):   
#     timmy.color(choose_random_color())
#     timmy.circle(100)
#     # timmy.setheading(random.choice(directions))
#     # timmy.setheading(5.0)
#     timmy.setheading(timmy.heading() + 10)
#     # timmy.left(5)

# 2nd solution
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):   
        timmy.color(choose_random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()