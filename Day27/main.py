import tkinter
from tkinter import END

window = tkinter.Tk()
window.title("My First Tkinter GUI Program")
window.minsize(width=500, height=300)

# Label
label_1 = tkinter.Label(text="This is a Label", font= ("Cambria", 20, "bold"))
label_1.pack()  # wont show on the screen, if this is missing, centers it on screen
# label_1.pack(side="left", expand=True)
label_1.pack(side="top")

def button_clicked():
    # print("Button was clicked")
    # label_1.config(text="I sense the Button was clicked.")
    # label_1.config(text=user_input)
    label_1.config(text=input.get()) # Updates the label based on input in Entry


# Button
button_1 = tkinter.Button(text="Click Me.", command=button_clicked)
# button_1.pack(side="left", expand=True)
button_1.pack(side="top")

# Entry (Input component)
input = tkinter.Entry(width=50)
input.pack(side="top")
# How to get hold of above value
# user_input = input.get()
# print(user_input)

# Text Entry Box
text_entry = tkinter.Text(height=5, width=40)
# Puts cursor in textbox
text_entry.focus()
# Add some default text to the textbox at beginning of program
text_entry.insert(END, "Enter multi-line comments here.")
#Gets current value in textbox at line1, character 0
# text_entry.get("1.0", END)
print(text_entry.get("1.0", END))
text_entry.pack(side="top")

# Spinbox
def spinbox_used():
    # Gets current value in spinbox
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack(side="top")

# Scale
def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=5, command=scale_used,orient="horizontal")
scale.pack(side="top")

# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0
    print(checkbutton.get())

# Variable to hold on to checked state, 0 is off, 1 is on
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack(side="top")


# Radiobutton
def radio_used():
    print(radio_state.get())

# Variable to hold on to which radio button value is checked
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack(side="top")
radiobutton2.pack(side="top")

# List box
def listbox_used(event):
    # Gets current selection from list box
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Banana", "Carrot", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack(side="top")

# Generally at the end of the program
# This keeps the window alive
window.mainloop()