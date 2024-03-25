"""
We will divide in seven modules:
1. Create a snake body
2. Move the snake
3. Control the snake (using keyboard controls) across the screen
4. Detect collision with food
5. Create scoreboard
6. Detect collision with wall
7. Detect collision with tail
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

#Create The Snake
snake = Snake()

#Create The Food
food = Food()

#Create The ScoreBoard
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


is_game_on = True
    
while is_game_on:
    #Updates screen with refresh interval of 0.5 sec.
    screen.update()
    time.sleep(0.1)

    #Move the Snake
    snake.move()

    #Detect Collision with Food
    if snake.head.distance(food) < 15:
        # print("EATING MY GREENS !! NOM NOM NOM .. . ...")
        food.refresh_food()
        snake.extend()
        score.update_score()

    #Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        score.reset()
        snake.reset()
        # score.game_over()

    #Detect collision with Tail
    #If head collides with any part of the body in the tail --> GAME OVER.
    for body in snake.snake_body[1:]:
        #Use slicing to exclude the snake's head, as snake body starts with snake.head and would return True for below if condition
        if snake.head.distance(body) < 10:
            # is_game_on = False
            score.reset()
            snake.reset()
            # score.game_over()
    

screen.exitonclick()