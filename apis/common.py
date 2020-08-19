from random import randint, choice
from uuid import uuid4
import string


def categorize_text(text: str) -> int:
    return randint(0, len(text))


def generate_random_id() -> str:
    return str(uuid4())


def generate_random_text() -> str:
    length = randint(1, 20)
    letters = string.ascii_lowercase
    text = ''.join(choice(letters) for _ in range(length))
    return text
