import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# turtle.shape("shape")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Get x,y cordinates of the image where mouse was clicked
# def get_mouse_click_coor(x,y):
#     print(x,y)

states_data = pd.read_csv("50_states.csv")
# print(states_data)
all_states_list = states_data["state"].to_list()
states_guessed = []

# turtle.onscreenclick(get_mouse_click_coor)

while len(states_guessed) < 50:
    user_guess = screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What's your guess ?").title()
    # print(user_guess)

    if user_guess == "Exit":
        missing_states = []
        for state in all_states_list:
            if state not in states_guessed:
                missing_states.append(state)
        
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if user_guess in all_states_list:
        states_guessed.append(user_guess)
        # print("Correct")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data["state"] == user_guess]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item())
        t.write(user_guess)


#Can comment below code snippet as we already have file with all the coordinates for the state to start the game.
# turtle.mainloop()   # Alternative to screen.exitonclick()
screen.exitonclick()