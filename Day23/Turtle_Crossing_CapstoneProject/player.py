from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280
GAME_LEVEL = 1

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("sea green")
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        # if new_y > FINISH_LINE:
        #     print("TURTLE WINS !!")
            # self.reset_player()
    
    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def reset_player(self):
        # self.clear()
        # self.color("sea green")
        # self.shape("turtle")
        # self.penup()
        self.goto(START_POSITION)
        # self.setheading(90)