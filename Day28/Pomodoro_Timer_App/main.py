from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
CHECKMARK_GREEN = "#79AC78"
YELLOW = "#f7f5dd"
FONT_NAME = "Cambria"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", font=(FONT_NAME, 40, "bold"),
                    bg=YELLOW, fg=GREEN, 
                    highlightthickness=0)
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", font=(FONT_NAME, 40, "bold"),
                    bg=YELLOW, fg=RED, 
                    highlightthickness=0)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", font=(FONT_NAME, 40, "bold"),
                    bg=YELLOW, fg=PINK, 
                    highlightthickness=0)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", font=(FONT_NAME, 40, "bold"),
                    bg=YELLOW, fg=GREEN, 
                    highlightthickness=0)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" # DYNAMIC TYPING - updating data type of int to str here

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)
        


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
#canvas.create_text(108,132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
timer_text = canvas.create_text(108,132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
# count_down(5) #MOVED INSIDE START_TIMER FUNCTION
# canvas.pack()

#TIMER LABEL
timer_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"),
                    bg=YELLOW, fg=GREEN, 
                    highlightthickness=0)
timer_label.grid(column=2, row=1)

#START BUTTON
start_button = Button(text="START", font=(FONT_NAME, 12, "bold"),
                    highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

#RESET BUTTON
reset_button = Button(text="RESET", font=(FONT_NAME, 12, "bold"),
                    highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

#CHECKMARK LABEL
checkmark_text = "✔"
checkmark_label = Label(font=(FONT_NAME, 10, "bold"),
                        bg=YELLOW, fg=CHECKMARK_GREEN,
                        highlightthickness=0)
checkmark_label.grid(column=2, row=4)


window.mainloop()