from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
screen = Screen()
rgb_colors = []
number_of_dots = 100

screen.colormode(255)
timmy.shape("turtle")
timmy.color("black", "DarkOliveGreen4")
# Sets the speed of turtle
timmy.speed("fastest")

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)


def choose_color_from_image():
    # colors = colorgram.extract('sample_image.jpg', 5)
    # print(colors)
    # for color in colors:
    #     r = color.rgb.r
    #     g = color.rgb.g
    #     b = color.rgb.b
    #     new_color = (r, g, b)
    #     rgb_colors.append(new_color)
    # print(rgb_colors)
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return random_color


for dot_count in range(1, number_of_dots):
# timmy.dot(20, random.choice(rgb_colors))
    timmy.dot(20, choose_color_from_image())
    # timmy.penup()
    timmy.forward(50)
    # timmy.pendown()

    if dot_count % 10 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
        

screen.exitonclick()