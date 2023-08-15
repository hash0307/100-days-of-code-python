from art import logo
# CALCULATOR

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Create a dictionary where the keys are the operation mode and values are the name of the functions.
operations = {
  "+": add,
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

# RECURSSION
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f" {num1} {operation_symbol} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calcualtion, or type 'exit' to end: ").lower()
    if choice == "y":
      num1 = answer
    elif choice == 'n':
      should_continue = False
      calculator() # Recurssion - Function calling itself
    else:
      should_continue = False

calculator()

# Add square root, exponent capability etc.