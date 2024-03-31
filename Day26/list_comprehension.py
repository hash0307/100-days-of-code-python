# List comprehensions
numbers = [1,2,3]

new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [alpha for alpha in name]
print(letters_list)

doubled_numbers = [number*2 for number in range(1,5)]
print(doubled_numbers)

#Conditional list compreshension
# new_list = [new_item for item in list if test]
names = ["Alan", "Beth", "Carol", "Devin", "Ember", "Freddie"]
# Only extract short names
short_names = [f_name for f_name in names if len(f_name) <= 4]
print(short_names)
uppercase_names = [f_name.upper() for f_name in names if len(f_name) > 4]
print(uppercase_names)

#Auditorium Excercise
#Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

list_of_strings = input().split(',')
numbers = [int(x) for x in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)

#Data OVerlap in Files
with open("file1.txt") as f1:
  file1_list = f1.readlines()
  
with open("file2.txt") as f2:
  file2_list = f2.readlines()
 
# print(file1_list)
result = [int(num) for num in file1_list if num in file2_list]
print(result)