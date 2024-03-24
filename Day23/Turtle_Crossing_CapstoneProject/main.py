"""
1. Create the Screen - 600*600
2. Create a Turtle for racing and position it at the bottom of the screen
3. Add movement to the turtle - up, down, left, right
4. Create Cars on the road and move them right to left
5. Detect collision with car 
6. If collision detected - GAME OVER (in the center of the screen)
7. Check if turtle reaches the end of screen - Player wins
8. Increase the level if road is crossed and reposition the turtle at starting position
9. Maintain scoreboard and level of the play
10. Add more cars and increase the speed of car as the level gets higher.
"""
import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard

is_game_on = True
# TOTAL_CARS = 10
# cars = {} #Dictionary to store all the car objects

#Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.bgcolor("black")
screen.tracer(0)

player_1 = Player()
cars = Car()
score = Scoreboard()

#Control movement of turtle with keys
screen.listen()
screen.onkeypress(fun=player_1.move_up, key="Up")
screen.onkeypress(fun=player_1.move_down, key="Down")
screen.onkeypress(fun=player_1.move_left, key="Left")
screen.onkeypress(fun=player_1.move_right, key="Right")

while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.make_car()
    cars.move_car()

    #Detect collision with car
    for car in cars.all_cars:
        if car.distance(player_1) < 20:
            is_game_on = False
            score.game_over()

    #Detect turtle finishes the race
    if player_1.ycor() > 280:
        player_1.reset_player()
        score.level_up()

screen.exitonclick()