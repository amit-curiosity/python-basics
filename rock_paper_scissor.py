import random

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

# Write your code below this line 👇

game_choices = [rock, paper, scissors]
game_string = ["rock", "paper", "scissors"]

# Get User's Choice
users_choice = int(input("What do you choose? \n\t Type 0 for Rock \n\t Type 1 for Paper \n\t Type 2 for Scissors\n"))
if users_choice < 0 or users_choice >= 3:
    print("Invalid Input: You lose!")
else:
    print(f"\nYours Choice: {game_string[users_choice]} {game_choices[users_choice]}")

    # Random Computer's Choice
    computers_choice = random.randint(0, 2)
    print(f"\nComputer's Choice: {game_string[computers_choice]} {game_choices[computers_choice]}")

    # Game logic
    if (users_choice == 0 and computers_choice == 2) or (users_choice == 1 and computers_choice == 0) or (
            users_choice == 2 and computers_choice == 1):
        print("You win.")
    elif users_choice == computers_choice:
        print("It's a draw.")
    else:
        print("You lose.")
