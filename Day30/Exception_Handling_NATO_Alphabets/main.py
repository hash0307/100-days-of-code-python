import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows() }
print(phonetic_dict)

def generate_phonetic():
    user_input = input("Enter your word: ").upper()
    # print(type(user_input))
    try:
        phonetic_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic() # To give user provision to re-enter the word, in input is incorrect initially
    else:
        print(phonetic_list)

generate_phonetic()