from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #Circle size by default is created as 20,20 so we have halved it.
        self.color("green")
        self.speed("fastest")
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        # self.goto(random_x, random_y)
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

