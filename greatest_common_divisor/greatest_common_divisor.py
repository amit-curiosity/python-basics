# copyright (c) 2022 amit-curiosity
from sys import stderr


# compute GCD of firstNumber and secondNumber
def gcd_finder(first_number, second_number):
    if isinstance(first_number, int) and isinstance(second_number, int):

        # GCD(a, b) = GCD(-a, b) = GCD(a, -b) = GCD(-a, -b)
        first_number = abs(first_number)
        second_number = abs(second_number)

        # get a and b
        a = min(first_number, second_number)
        b = max(first_number, second_number)

        while a != 0:
            temp = a
            a = b % a
            b = temp
        return b
    else:
        # -1 indicates that instance of
        # first or second isn't integer
        return -1


if __name__ == '__main__':
    # get firstNumber and secondNumber
    first = int(input("Enter firstNumber: "))
    second = int(input("Enter secondNumber: "))

    # compute GCD
    gcd_value = gcd_finder(first, second)

    # print appropriate message
    if gcd_value == -1:
        print("Invalid Input! Non-Integer Values.", file=stderr)
    else:
        print(f'GCD({first}, {second}): {gcd_value}')
