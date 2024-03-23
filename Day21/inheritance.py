class Animal:
    def __init__(self) -> None:
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale -- Exhale.")


#Inheritance Example
# class Fish:
class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    def swim(self):
        print("Moving In Water....")

    def breathe(self):
        super().breathe()
        print("Underwater")
    
nemo = Fish()
nemo.swim()
nemo.breathe()  # Calling method from parent class using child object
print(nemo.num_of_eyes)