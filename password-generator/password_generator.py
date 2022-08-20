# Generate Strong Password
import string
import random


# generate a list of characters
def generate_string():
    req_str = f'{string.ascii_letters}{string.digits}@#$%&!()*+'
    req_list = [str(char) for char in req_str]
    # random.shuffle(req_list)
    return req_list


# generate random password
def generate_password():
    character_string = generate_string()
    generated_password = ''
    length_of_choice_string = len(character_string)
    for _ in range(16):
        index = random.randint(0, length_of_choice_string - 1)
        generated_password += character_string[index]
    print(f'Generated Password: {generated_password}')


# Main Function - Entry Point
if __name__ == '__main__':
    # Generate Password
    generate_password()
