# copyright (c) 2022 amit-curiosity

# define histogram creation logic
def create_histogram(list_of_numbers):
    for number in list_of_numbers:
        print('|', end='')
        for _ in range(number):
            print('*-', end='')
        print('*')


if __name__ == '__main__':
    numbers = [7, 6, 8, 9, 1, 5, 12]
    create_histogram(numbers)
