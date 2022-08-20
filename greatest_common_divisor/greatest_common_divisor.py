from sys import stderr


# compute GCD of firstNumber and secondNumber
def gcd_finder(first_number, second_number):
    if isinstance(first_number, int) and isinstance(second_number, int):
        if first_number >= 0 and second_number >= 0:
            # get a and b
            a = min(first_number, second_number)
            b = max(first_number, second_number)

            while a != 0:
                temp = a
                a = b % a
                b = temp
            return b
        else:
            # -1 indicates that GCD can't be
            # computed for negative numbers
            return -1
    else:
        # -2 indicates that instance of
        # first or second isn't integer
        return -2


if __name__ == '__main__':
    # get firstNumber and secondNumber
    first = int(input("Enter firstNumber: "))
    second = int(input("Enter secondNumber: "))

    # compute GCD
    gcd_value = gcd_finder(first, second)

    # print appropriate message
    if gcd_value == -1:
        print("Invalid Input! Negative Integers.", file=stderr)
    elif gcd_value == -2:
        print("Invalid Input! Non-Integer Values.", file=stderr)
    else:
        print(f'GCD({first}, {second}): {gcd_value}')
