#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#Option # 2
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows() }
print(phonetic_dict)

user_input = input("Enter your word: ").strip().upper()
phonetic_list = [phonetic_dict[letter] for letter in user_input if letter in phonetic_dict.keys()]
print(phonetic_list)
#Option # 2

#Option # 1
# phonetic_code = []
# with open("nato_phonetic_alphabet.csv") as f:
#     phonetic_code = f.readlines()

# # print(phonetic_code)
# # print()
# phonetic_dict = {element.split(",")[0]:element.split(",")[1].strip() for element in phonetic_code[1:]}

# # print(type(phonetic_dict))
# print(phonetic_dict)

# user_input = input("Enter your word: ").strip().upper()
# phonetic_list = [phonetic_dict[letter] for letter in user_input if letter in phonetic_dict.keys()]
# print(phonetic_list)
#Option # 1