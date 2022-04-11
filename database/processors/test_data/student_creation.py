from random import choice

from database.processors.consts.data_consts import NAMES, LASTNAMES


def get_students() -> list:
    return [{'name': choice(NAMES), 'lastname': choice(LASTNAMES)} for i in range(200)]
