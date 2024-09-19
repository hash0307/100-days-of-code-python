import tkinter
from tkinter import END

def button_clicked():
    # print("Button was clicked")
    # label_1.config(text="I sense the Button was clicked.")
    # label_1.config(text=user_input)
    label_1.config(text=input.get()) # Updates the label based on input in Entry


window = tkinter.Tk()
window.title("Understanding Layouts in Tkinter")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Label
label_1 = tkinter.Label(text="This is a Label", font= ("Cambria", 20, "bold"))
# Problem with pack , difficult to precise place an element
# label_1.pack(side="top")
# Problem with place, it is too precise - when thousands of widgets difficult to handle the coordinates
# label_1.place(x=20, y=5)
# Cannot use grid & pack together - incompatible
label_1.grid(column=0, row=0)

# Button
button_1 = tkinter.Button(text="Click Me.", command=button_clicked)
# button_1.pack(side="top")
button_1.grid(column=1,row=1)

# Entry (Input component)
input = tkinter.Entry(width=50)
# How to get hold of above value
user_input = input.get()
print(user_input)
# input.pack(side="top")
input.grid(column=3, row=2)

# Challenge - Add new button in row=0, column=2
button_2 = tkinter.Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)

# Generally at the end of the program
# This keeps the window alive
window.mainloop()