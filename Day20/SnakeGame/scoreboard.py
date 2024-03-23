from turtle import Turtle
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Gothic", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"SCORE: {self.score}", move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)
        self.hideturtle()
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)
        
