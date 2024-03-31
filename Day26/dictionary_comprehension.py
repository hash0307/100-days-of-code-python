# new_dict = {new_key:new_value for item in list}

# Creating a dictionary from an existing dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# Using Pandas DataFrame
# new_dict = {new_key:new_value for (index,row) in df.iterrows()}

import random
names = ["Alan", "Beth", "Carol", "Devin", "Ember", "Freddie"]

students = {name:random.randint(1,100) for name in names}
print(students)
passed_students = {name:score for (name,score) in students.items() if score > 60}
print(passed_students)

#Dictionary Comprehension Excercise
# sentence = input("Enter something for Dict Comprehension: ").strip()
# # new_list = sentence.split()
# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather_c = eval(input("Enter for Exercise #2: "))
# print(weather_c)
# weather_f = {day:(temp*9/5)+32 for (day,temp) in weather_c.items()}
# print(weather_f)

student_dict = {
    "student" : ["Angela", "James","Lily"],
    "score" : [56,76,98]
}

#Looping through Dictionaries
# for (key,value) in student_dict.items():
#     print(value)

import pandas
student_df = pandas.DataFrame(student_dict)
print(student_df)
#Loop through a DataFrame
# for (key,value) in student_df.items():
#     print(value)  #This loops through each of the columns in DF

# Pandas has inbuilt method - iterrows(), which allows us to loop through rows of a DF
for (index, row) in student_df.iterrows():
    # print(index)    # Prints the index of DF like - 0 1 2
    # print(row)      # Prints the actual rows - each rows as Pandas.series object
    # print(row.student)  # Prints - Angela James Lily in seperate lines
    # print(row.score)  # Prints - Scores - 56 76 98 in seperate lines
    if row.student == "Angela":
        print(row.score)
