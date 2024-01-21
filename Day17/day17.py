#Creating a new class
class User:
    # Constructor - part of Blueprint
    # init function is being called everytime a new object of class is created
    # def __init__(self) -> None:
    #     pass
    
    # When we add parameters to the constructor, we must pass whenever a new Object is created
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        # Can set default value of attribute as well like below and do not need to be passed while creating object
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


#Creating an object for the class
user_1 = User("001", "Amy")
user_2 = User("002", "Bob")
# user_2 = User()
# user_1.id = "007"
# user_1.username = "John"

print(user_1.id)
print(user_1.followers)
# print(user_2)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

