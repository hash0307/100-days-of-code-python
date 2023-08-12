# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hello!!")
    print("How are you doing?")
    print("Hope, you have a good day ! :)")


# Function that allows for an input
def greet_with_name(name):
    print(f"\nHello {name}!!")
    print(f"How are you doing {name}?")
    print("Hope, you have a good day ! :)")


greet()
greet_with_name("Dave")


# Function with more than one input
def greet_with(name, location):
    print(f"\nHello {name}!!")
    print(f"How's the weather in {location}")


# Keyword arguments
greet_with(location="London", name="John")
