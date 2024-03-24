from turtle import Turtle
import random

CAR_COLOR = ["RED", "YELLOW", "WHITE", "BLUE", "PURPLE", "PINK", "ORANGE"]
STARTING_MOVE_DISTANCE = 5
# CAR_MOVEMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        # self.START_POSITION = 280
        # self.make_car()
        # self.position_car()
        # self.setheading(90)
    
    
    def make_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 2:
            new_car = Turtle("square")
            new_car.color(random.choice(CAR_COLOR))
            new_car.shapesize(stretch_len=3,stretch_wid=1)
            new_car.penup()
            new_car.goto(280,random.randint(-280,280))
            self.all_cars.append(new_car)

    # def position_car(self):
    #     self.goto(280,random.randint(-280,280))

    def move_car(self):
        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())
            # if self.START_POSITION == -280:
            #     new_x = car.xcor() + STARTING_MOVE_DISTANCE
            #     car.goto(new_x, car.ycor())
            # else:
            #     new_x = car.xcor() - STARTING_MOVE_DISTANCE
            #     car.goto(new_x, car.ycor())
            # if new_x == -280:
            #     car.reset_car()
        
    # def reset_car(self):
    #     print("Cars Reset")
    #     self.clear()
    #     # self.color(CAR_COLOR[random.randint(0,6)])
    #     # self.shape("square")
    #     # self.shapesize(stretch_len=3,stretch_wid=1)
    #     # self.penup()
    #     # self.goto(280,0)
    #     self.position_car()
    #     self.move_car()