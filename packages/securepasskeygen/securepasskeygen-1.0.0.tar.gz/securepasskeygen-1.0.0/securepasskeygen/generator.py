# generator.py

import string
import secrets

def generate_password(length=16, use_uppercase=True, use_numbers=True, use_special_chars=True, min_strength=2):
    """
    Generate a secure password that meets high security standards.
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    char_pool = lowercase
    if use_uppercase:
        char_pool += uppercase
    if use_numbers:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars

    password = []
    strength = 0

    if use_uppercase:
        password.append(secrets.choice(uppercase))
        strength += 1
    if use_numbers:
        password.append(secrets.choice(digits))
        strength += 1
    if use_special_chars:
        password.append(secrets.choice(special_chars))
        strength += 1

    while len(password) < length:
        password.append(secrets.choice(char_pool))

    secrets.SystemRandom().shuffle(password)

    if strength < min_strength:
        return generate_password(length, use_uppercase, use_numbers, use_special_chars, min_strength)

    return ''.join(password)
