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
# Rules of the game
# Rock win Against Scissors
# Paper win Against Rock
# Scissors win against paper

import random

print("Welcome to the game of ROCK, PAPER & SCISSORS\n")

Graphics = [rock,paper,scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input >= 3 or user_input < 0:
    print("INVALID NUMBER!!!, You Loose")
else:

    print(f'You Choose {user_input}' + Graphics[user_input])

    # Getting computer to choose
    computer_choice = random.randint(0,2)
    print(f"Computer choose {computer_choice}" + Graphics[computer_choice])

    # Using if else statement 

    if user_input == 0 and computer_choice == 2:
        print("You win")
    elif user_input == 2 and computer_choice == 0:
        print("You Loose")
    elif user_input > computer_choice:
        print("You win")
    elif user_input == computer_choice:
        print("It's a Draw")
    else:
        print("You Loose")

