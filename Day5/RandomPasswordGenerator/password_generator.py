#Password Generator Project
import random
from alphanumeric_template import letters, numbers, symbols


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
py_pass = []
for _ in range(0, nr_letters):
  py_pass += random.choice(letters)
  
for _ in range(0, nr_symbols):
  py_pass += random.choice(symbols)
  
for _ in range(0, nr_numbers):
  py_pass += random.choice(numbers)

random.shuffle(py_pass)

new_pass = ""
for item in py_pass:
  new_pass += item
  
print(f"Generated Pasword is: {new_pass}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P