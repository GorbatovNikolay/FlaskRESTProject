from random import choice, randrange

from database.models import Student
from .group_objects_creation import group_objects
from .test_data import students


def get_student_objects() -> list:
    """Randomly assign students to groups and returns a list of student objects."""
    student_objects = []

    for group_obj in group_objects:
        number_of_students_in_a_group = choice([i for i in range(0, 31) if i == 0 or i > 9])
        for step in range(number_of_students_in_a_group):
            remaining_student = len(students)
            if remaining_student > 0 and remaining_student >= number_of_students_in_a_group:
                student = students.pop(randrange(remaining_student))
                student_objects.append(Student(
                    first_name=student['name'],
                    last_name=student['lastname'],
                    group=group_obj
                ))

    for student in students:
        student_objects.append(Student(
            first_name=student['name'],
            last_name=student['lastname']
        ))

    return student_objects
