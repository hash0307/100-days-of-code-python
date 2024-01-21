from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
turtle_colors = ['CornflowerBlue', "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]
directions = [0, 90, 180, 270]

timmy.shape("turtle")
timmy.color("black", "DarkOliveGreen4")
# Sets the width/thickness of the line
timmy.pensize(12)
# Sets the speed of turtle
timmy.speed("fastest")

def choose_random_color():
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # print(random_color)
    return random_color

for _ in range(100):
    # timmy.color(random.choice(turtle_colors))
    
    screen.colormode(255)
    
    timmy.color(choose_random_color())
    timmy.forward(40)
    timmy.setheading(random.choice(directions))

screen.exitonclick()