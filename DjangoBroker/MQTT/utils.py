import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGHT = 8

def generate_random_string(length=STRING_LENGHT, chars=ALPHANUMERIC_CHARS):
    return "".join(random.choice(chars) for _ in range(length))
