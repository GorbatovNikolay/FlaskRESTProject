from random import choice

names = [
    'Gabriel', 'John', 'Rhona', 'Meredith', 'Hilda',
    'Wyoming', 'Kiona', 'James', 'Hans', 'Lacy',
    'Lucy', 'Neville', 'Mary', 'Cassandra', 'Lillith',
    'Ivan', 'Abra', 'Trevor', 'Kadeem', 'Max'
]

lastnames = [
    'Riley', 'Calhoun', 'Vincent', 'Nolan', 'Clark',
    'Maynard', 'Montoya', 'Schwartz', 'Anderson', 'Lloyd',
    'Franks', 'Ratliff', 'Maldonado', 'Mcconnell', 'Guthrie',
    'Bruce', 'Fitzgerald', 'Acevedo', 'Cooley', 'Davidson'
]


def get_students() -> list:
    return [{'name': choice(names), 'lastname': choice(lastnames)} for i in range(200)]
