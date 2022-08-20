from sys import stderr


# determine character is consonant or vowel
def is_vowel_or_consonant(char):
    if len(char) == 1 and char.isalpha():
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            return 'Vowel'
        elif char.lower() not in ['a', 'e', 'i', 'o', 'u']:
            return 'Consonant'
    else:
        return 'Invalid Input'


if __name__ == '__main__':
    character = 'C'
    result = is_vowel_or_consonant(character)

    # print appropriate message
    if result == 'Invalid Input':
        print(result, file=stderr)
    else:
        print(result)
