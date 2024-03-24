from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_off_wall(self):
        self.y_move *= -1

    def bounce_off_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.95
        
    def reset_position(self):
        """ Reset ball position to (0,0) when a paddle misses the ball """
        self.goto(0,0)
        self.bounce_off_paddle()
        self.move_speed = 0.1
