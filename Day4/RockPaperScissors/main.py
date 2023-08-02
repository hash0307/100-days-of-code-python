rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line ??
import random
user_choice = int(input("What do you choose ? \n Type 0 for Rock, 1 for Paper and 2 for Scissors. "))

options = [rock, paper, scissors]

print(f"You Chose: {user_choice} \n {options[user_choice]}")
computer_choice = random.randint(0,len(options)-1)
print(f"Computer Chose: {computer_choice} \n {options[computer_choice]}")

if user_choice == computer_choice:
  print("It's a Draw !!!")
elif user_choice == 0:
  if computer_choice == 1:
    print("You Lose !!!")
  else:
    print("You Win !!!!")
elif user_choice == 1:
  if computer_choice == 0:
    print("You Win !!!!")
  else:
    print("You Lose !!!")
elif user_choice == 2:
  if computer_choice == 0:
    print("You Lose !!!")
  else:
    print("You Win !!!!")