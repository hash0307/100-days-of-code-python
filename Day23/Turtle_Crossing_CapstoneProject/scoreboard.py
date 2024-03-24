from turtle import Turtle
GAME_OVER = "GAME OVER"
GAME_OVER_CORDINATES = (0,0)
LEVEL_CORDINATES = (-250,250)
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Impact", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.goto(LEVEL_CORDINATES)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align="left", font=SCORE_FONT)


    def level_up(self):
        self.level += 1
        self.update_scoreboard()
    

    def game_over(self):
        # self.clear()
        # self.goto(LEVEL_CORDINATES)
        # self.write(f"LEVEL: {self.level}", align="left", font=SCORE_FONT)
        self.goto(0,0)
        self.write(GAME_OVER, align=SCORE_ALIGNMENT, font=SCORE_FONT)