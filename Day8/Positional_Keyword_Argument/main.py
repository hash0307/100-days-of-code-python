
def greet():
    print("Hello!!")
    print("How are you doing?")
    print("Hope, you have a good day ! :)")


# Function that allows for an input
def greet_with_name(name):
    print(f"\nHello {name}!!")
    print(f"How are you doing {name}?")
    print("Hope, you have a good day ! :)")


# Function with more than one input
def greet_with(name, location):
    print(f"\nHello {name}!!")
    print(f"How's the weather in {location}")


greet()
greet_with_name("Dave")
# Keyword arguments
greet_with(location="London", name="John")
