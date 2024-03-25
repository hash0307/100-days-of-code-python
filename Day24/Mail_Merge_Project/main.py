#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
TEXT_TO_REPLACE = "[name]"

# Read all the names in invited_names.txt
with open("Input/Names/invited_names.txt", "r") as f:
    names = f.readlines()

# print(names)

# Read the starting_letter.txt and replace [name] with names in the list
with open("Input/Letters/starting_letter.txt","r") as l:
    letter_content = l.read()
#Replace [name] with list of names
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(TEXT_TO_REPLACE, stripped_name)
        with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", "w") as out:
            out.write(new_letter)    