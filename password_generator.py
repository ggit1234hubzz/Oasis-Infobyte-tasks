# password_generator.py
import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Please specify at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
