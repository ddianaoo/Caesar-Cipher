import string


def caesar_cipher(text, shift, direction='encode'):
    shift = shift % 26
    if direction == 'decode':
        shift = -shift

    result = []
    alphabet = string.ascii_lowercase
    for char in text:
        if char.lower() in alphabet:
            new_char = alphabet[(alphabet.index(char.lower()) + shift) % 26]
            if char.isupper():
                result.append(new_char.upper())
            else:
                result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)
