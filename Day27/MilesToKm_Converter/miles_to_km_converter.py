import tkinter

# Function to calculate miles to km
def miles_to_km():
    miles = float(entrybox.get())
    km = miles * 1.609
    label_output.config(text=f'{km}')
    # return km


# Creating a window with title
window = tkinter.Tk()
window.config(width=400, height=200, padx=10, pady=10)
window.title("Miles to Km Converter")

# Creating widgets
# 1. Entry Box
entrybox = tkinter.Entry(text="Enter miles", width=10)
# miles = entrybox.get()
entrybox.grid(column=1, row=0)

# 2. Label for Miles
label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

# 3. Label for km output
label_output = tkinter.Label()
label_output.grid(column=1, row=1)

# 4. Label for Km
label_km = tkinter.Label(text="Km")
label_km.grid(column=2, row=1)

# 5. Button to calculate
calculate_button = tkinter.Button(text="Calculate", width=10, command=miles_to_km)
calculate_button.grid(column=1, row=2)

# 6. Extra Labels
label_print = tkinter.Label(text="is equal to")
label_print.grid(column=0, row=1)


window.mainloop()