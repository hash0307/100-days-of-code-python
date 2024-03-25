from turtle import Turtle
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Gothic", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"SCORE: {self.score} High Score: {self.high_score}", move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)
        self.hideturtle()
    

    def get_highscore(self):
        with open("data.txt") as f:
            return int(f.read())
        
    def set_highscore(self, score):
        with open("data.txt", mode="w") as f:
            f.write(score)


    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score} High Score: {self.get_highscore()}", move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)
        
    def reset(self):
        if self.score > self.high_score:
            # self.high_score = self.score
            self.set_highscore(str(self.score))
        self.score = 0
        self.update_score()
