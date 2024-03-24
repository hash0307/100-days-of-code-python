from turtle import Turtle
GAME_NAME = "PING - PONG"
GAME_OVER = "GAME OVER"
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Impact", 14, "bold")
GAME_FONT = ("Impact", 36, "bold")
GAME_NAME_CORDINATE = (0,245)
GAME_OVER_CORDINATE = (0,0)
SCORE_CORDINATE = [(-180,250), (180,250)]

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()
        # self.goto(150,250)
        # self.write(self.right_score, align="center", font=("Courier", 24, "normal"))

    def left_point(self):
        """ Update score for left paddle when right paddle misses """
        self.left_score += 1
        self.update_score()

    def right_point(self):
        """ Update score for right paddle when left paddle misses """
        self.right_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(GAME_NAME_CORDINATE)
        self.write(GAME_NAME, align=SCORE_ALIGNMENT, font=GAME_FONT)
        self.goto(SCORE_CORDINATE[0])
        self.write(self.left_score, align=SCORE_ALIGNMENT , font=SCORE_FONT)
        self.goto(SCORE_CORDINATE[1])
        self.write(self.right_score, align=SCORE_ALIGNMENT , font=SCORE_FONT)

    def game_over(self):
        self.update_score()
        self.goto(GAME_OVER_CORDINATE)
        self.write(GAME_OVER, align=SCORE_ALIGNMENT, font=GAME_FONT)

