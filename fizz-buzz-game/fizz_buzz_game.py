# Fizz-Buzz Game
def fizz_buzz_game(end_point):
    for number in range(1, end_point + 1):
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz\n", end="")
        elif number % 3 == 0:
            print("Fizz\n", end="")
        elif number % 5 == 0:
            print("Buzz\n", end="")
        else:
            print(f'{number}\n', end="")


# Main Function - Entry Point
if __name__ == '__main__':
    # Get User's Input
    user_input = int(input("Enter end point: "))

    # Start FizzBuzz Game
    fizz_buzz_game(user_input)
