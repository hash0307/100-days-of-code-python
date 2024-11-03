from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#DAY 5 - Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")

    # nr_letters= random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # py_pass = []
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    #UPDATED BELOW FOR LOOP TO LIST COMPREHENSIONS
    # for _ in range(0, nr_letters):
    #   py_pass += random.choice(letters)
    
    # for _ in range(0, nr_symbols):
    #   py_pass += random.choice(symbols)
    
    # for _ in range(0, nr_numbers):
    #   py_pass += random.choice(numbers)
    py_pass = password_letters + password_symbols + password_numbers
    shuffle(py_pass)

    new_pass = "".join(py_pass)
    # new_pass = ""
    # for char in py_pass:
    #   new_pass += char
    pass_entry.insert(0, new_pass)
    pyperclip.copy(new_pass)
  

# ---------------------------- SAVE PASSWORD ------------------------------- #
# def get_data():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = pass_entry.get()

#     return website, email, password # RETURNS TUPLE
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0  or len(password) == 0:
        messagebox.showinfo(title="ERROR", message="Please make sure you haven't left any field empty.")
    else:
        # messagebox.showinfo(title="Popup")
        is_ok = messagebox.askokcancel(title=website, 
                            message=f"You entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save ?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=60, pady=60)
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# canvas.pack()
canvas.grid(row=0,column=1)

#LABELS
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#BUTTONS
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

#ENTRY'S
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abc@gmail.com")
# email_entry.insert(END, "abc@gmail.com")

pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

window.mainloop()