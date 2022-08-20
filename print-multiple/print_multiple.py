# copyright (c) 2022 amit-curiosity
def print_multiple():
    number = int(input("Enter a number: "))
    i = 1
    while i <= 10:
        # "<3" - left align of field_width 3
        # ">3" - right align of field_width 3
        # "^4" - center align of field_width 4
        print(f'{number: <3} * {i: >3} = {(i * number): ^4}')
        i += 1


if __name__ == '__main__':
    print_multiple()
