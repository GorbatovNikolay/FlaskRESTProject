from .group_creation import get_groups
from .student_creation import get_students

courses = [
    {'Science': 'This is the description of the science course.'},
    {'Mathematics': 'This is the description of the math course.'},
    {'Health': 'This is the description of the health course.'},
    {'Handwriting': 'This is the description of the handwriting course.'},
    {'Physical Education': 'This is the description of the PE course.'},
    {'Art': 'This is the description of the art course.'},
    {'Music': 'This is the description of the music course.'},
    {'Literature': 'This is the description of the literature course.'},
    {'Geography': 'This is the description of the geography course.'},
    {'Social Studies': 'This is the description of the social studies course.'}
]

groups = get_groups()
students = get_students()
