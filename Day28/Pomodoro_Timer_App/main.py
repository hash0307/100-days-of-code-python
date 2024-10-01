from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(width=800, height=600, 
              padx=100, pady=50,
              background=YELLOW)
window.title("Pomodoro App")

# Canvas Widget 
"""
Canvas widget allows us to layer different widgets.
For ex. In this case, add a timer on top of a tomato image
"""
canvas = Canvas(width=210, height=224,
                bg=YELLOW, highlightthickness=0)
# Widget to add image to canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(108, 112, image=tomato_img)
canvas.create_text(108,132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
# canvas.pack()

timer_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"),
                    bg=YELLOW, fg=GREEN, 
                    highlightthickness=0)
timer_label.grid(column=2, row=1)

start_button = Button(text="START", font=(FONT_NAME, 12, "bold"),
                    highlightthickness=0)
start_button.grid(column=1, row=3)

reset_button = Button(text="RESET", font=(FONT_NAME, 12, "bold"),
                    highlightthickness=0)
reset_button.grid(column=3, row=3)

checkmark_text = "☑"
checkmark_label = Label(text=checkmark_text, bg=YELLOW, fg=GREEN,
                        highlightthickness=0)
checkmark_label.grid(column=2, row=4)


window.mainloop()