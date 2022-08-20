# copyright (c) 2022 amit-curiosity
from sys import stderr
from random import randint


def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    computer_guessed_number = randint(1, 100)
    # print(computer_guessed_number)
    difficulty_choice = input("Choose a difficulty. Type 'Easy' or 'Hard': ")
    if difficulty_choice.lower() == 'hard':
        number_of_attempts = 5
    elif difficulty_choice.lower() == 'easy':
        number_of_attempts = 10
    else:
        print("Invalid Input", file=stderr)
        return None

    have_you_won = False
    while True:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_guessed_number = int(input("Make a guess: "))
        if user_guessed_number == computer_guessed_number:
            have_you_won = True
            break
        elif user_guessed_number < computer_guessed_number:
            print("Too low.")
        else:
            print("Too high.")
        number_of_attempts -= 1
        if number_of_attempts > 0:
            print("Guess again.")
        else:
            break

    if have_you_won:
        print(f"\nYou have guessed it!\nGuessed Number: {computer_guessed_number}.")
    else:
        print(f"\nYou have lost!\nGuessed Number: {computer_guessed_number}.")


if __name__ == '__main__':
    guess_the_number()
