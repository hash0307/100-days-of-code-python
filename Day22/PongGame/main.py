"""
1. Create the screen for Pong Game
2. Create two paddles
3. Move the paddle
4. Create a ball and move the ball
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle miss
8. Maintain Score for each player
"""
from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time

MOVE_DISTANCE = 20
R_START_POSITION = (475,0)
L_START_POSITION = (-475,0)

screen = Screen()

#Setup the Screen for Pong Game
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("PONG GAME")
screen.tracer(0)

right_paddle = Paddle(R_START_POSITION)
left_paddle = Paddle(L_START_POSITION)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()

    #Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 440) or \
       (ball.distance(left_paddle) < 50 and ball.xcor() < -440):
        ball.bounce_off_paddle()

    #Detect when paddle misses
    if (ball.xcor() > 480):
        # print("Right Paddle missed")
        ball.reset_position()
        score.left_point()        
    
    if (ball.xcor() < -480):
        # print("Left Paddle Missed")
        ball.reset_position()
        score.right_point() 
    
    #GAME-OVER
    if score.left_score == 1 or score.right_score == 1:
        game_is_on = False
        score.game_over()


screen.exitonclick()