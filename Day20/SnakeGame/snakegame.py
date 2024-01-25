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
from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

#Create The Snake
snake = Snake()

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







screen.exitonclick()