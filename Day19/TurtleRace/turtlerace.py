from turtle import Turtle, Screen
import random
# timmy = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("sea green")
y_positions = [-100, -60, -20, 20, 60, 100]

turtle_colors = ["Blue", "Light Green", "Yellow", "Orange", "Red", "Black"]
all_turtles = []

is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race ? \n{turtle_colors}\n\nEnter a color: ")
# print(user_bet)

# Creating multiple instances of turtle for the race
for turtle_index in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.color(turtle_colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print("Congratulations!! You have won!")
                print(f"The {winning_color} turtle is the WINNER !")
            else:
                print(f"You have lost. The {winning_color} turtle is the WINNER !")
                break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    

screen.exitonclick()