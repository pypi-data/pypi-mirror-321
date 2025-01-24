import string
import secrets

def generate_password(length=16, include_lower=True, include_upper=True, include_digits=True, include_special=True, min_strength=2):
    lowercase = string.ascii_lowercase if include_lower else ""
    uppercase = string.ascii_uppercase if include_upper else ""
    digits = string.digits if include_digits else ""
    special_chars = string.punctuation if include_special else ""

    char_pool = lowercase + uppercase + digits + special_chars

    if not char_pool:
        raise ValueError("No characters available to generate password. Enable at least one character set.")

    password = []
    strength = 0

    if include_lower and lowercase:
        password.append(secrets.choice(lowercase))
        strength += 1
    if include_upper and uppercase:
        password.append(secrets.choice(uppercase))
        strength += 1
    if include_digits and digits:
        password.append(secrets.choice(digits))
        strength += 1
    if include_special and special_chars:
        password.append(secrets.choice(special_chars))
        strength += 1

    while len(password) < length:
        password.append(secrets.choice(char_pool))

    secrets.SystemRandom().shuffle(password)

    if strength < min_strength:
        return generate_password(length, include_lower, include_upper, include_digits, include_special, min_strength)

    return ''.join(password)
