#Option #1
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#Option #2
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#To write a file
# w = write
# a = append
with open("my_file.txt", mode="w") as file:
    file.write("\n New Text.")