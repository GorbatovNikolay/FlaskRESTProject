import string
from random import choices


def get_groups() -> list:
    """Creates 10 randomly generated group names."""
    groups = []
    for step in range(10):
        characters = choices(string.ascii_uppercase, k=2)
        numbers = choices(string.digits[1:], k=2)
        groups.append(f'{characters[0] + characters[1]}-{numbers[0] + numbers[1]}')
    return groups
