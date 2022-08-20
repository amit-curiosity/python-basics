from sys import stderr
from hangman_arts import hangman_logo, current_stage
from hangman_words import possible_words_list
from random import choice


# define initial state of guessed_word
def initial_state_of_guessed_word(length_of_word):
    word = []
    for _ in range(length_of_word):
        word += '_'
    return word


# print hangman logo
print(hangman_logo)

# get chosen_word
chosen_word = choice(possible_words_list)
# print(chosen_word)

number_of_lives_left = len(current_stage)
# define string to store current_form of guessed_word
guessed_word = initial_state_of_guessed_word(len(chosen_word))

end_of_game_reached = False

# keep track of already guessed letters
already_guessed_letters = []

while not end_of_game_reached:
    # let user guess a letter
    user_guessed_letter = input('Make A Letter Guess: ').lower()

    # check whether current user_guessed_letter has already been guessed
    if user_guessed_letter in already_guessed_letters:
        print(f'You have already guessed \'{user_guessed_letter}\'.')
        print(f'Already Guessed Letters Are: [{", ".join(already_guessed_letters)}]')

    # check whether user_guessed_letter is of single letter
    elif len(user_guessed_letter) >= 2:
        print('Guessed letter has multiple character!', file=stderr)
    else:
        already_guessed_letters += user_guessed_letter

        # check whether user_guessed_letter is in chosen_word
        if user_guessed_letter not in chosen_word:

            # print current status of guessed_word
            print(f'Guessed Word Status: {" ".join(guessed_word)}')

            # user_message to enhance experience
            print(f'You guessed \'{user_guessed_letter}\', that\'s not in the word.\nSorry! you have lost a life.')

            number_of_lives_left -= 1
            print(current_stage[number_of_lives_left])

            # check whether life is left to continue
            if number_of_lives_left == 0:
                end_of_game_reached = True
                print('You lose.')
        else:
            # user message after correct_guess
            print('Wow!, you have guessed right letter.')

            # update guessed_word status
            index = 0
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == user_guessed_letter:
                    guessed_word[position] = letter
                position += 1

            # print current status of guessed_word
            print(f'Guessed Word Status: {" ".join(guessed_word)}')

            # check whether chosen_word has been guessed
            if '_' not in guessed_word:
                end_of_game_reached = True
                print('You won.')
