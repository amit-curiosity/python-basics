# function to encrypt message
def encode_message(plain_text: str, shift_amount: int):
    encoded_message = []
    for _ in plain_text:
        encoded_message.append('')
    # print(encoded_message)

    index, ascii_length = 0, 128
    for each_char in plain_text:
        # get required character's ascii position
        character_number = ord(each_char) + shift_amount

        # get required ascii character
        encoded_message[index] = chr((character_number + ascii_length) % ascii_length)
        index += 1
    return ''.join(encoded_message)


# function to decrypt message
def decode_message(cipher_text: str, shift_amount: int):
    decoded_message = []
    for _ in cipher_text:
        decoded_message.append('')
    # print(encoded_message)

    index, ascii_length = 0, 128
    for each_char in cipher_text:
        # get required character's ascii position
        character_number = ord(each_char) - shift_amount

        # get required ascii character
        decoded_message[index] = chr((character_number + ascii_length) % ascii_length)
        index += 1
    return ''.join(decoded_message)


# encrypted_message = encode_message(plain_text='amit kumar', shift_amount=2)
# decrypted_message = decode_message(cipher_text=encrypted_message, shift_amount=2)

# print(f'Encrypted Message: {encrypted_message}')
# print(f'Decrypted Message: {decrypted_message}')
def driver_program():
    continue_procedure = True
    while continue_procedure:
        user_choice = input('Do you want to \'encrypt\' or \'decrypt\' the message?: ')

        # Encryption Procedure
        if user_choice.lower() == 'encrypt':
            text_message = input('Please enter the text message, to start encryption procedure: ')
            shift_length = int(input('Please enter shift length for encryption: '))
            print(encode_message(plain_text=text_message, shift_amount=shift_length))

        # Decryption Procedure
        elif user_choice.lower() == 'decrypt':
            cipher_message = input('Please enter the text message, to start decryption procedure: ')
            shift_length = int(input('Please enter shift length for decryption: '))
            print(decode_message(cipher_text=cipher_message, shift_amount=shift_length))

        # Incorrect Choice
        else:
            print('Chosen option isn\'t available, please check!')

        # Game Continue Condition
        termination_choice = input('Do you want to continue with caesar cipher? (Y/N): ')
        if termination_choice.lower() in ['n', 'no']:
            continue_procedure = False
            print('Good Bye! thanks for using caesar cipher.')
        elif termination_choice.lower() not in ['y', 'yes']:
            continue_procedure = False
            print(f'Chosen option \"{termination_choice}\" isn\'t available.')
            print('Good Bye! thanks for using caesar cipher.')


# driver program
if __name__ == '__main__':
    driver_program()
