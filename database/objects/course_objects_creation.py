from database.models import Course
from .test_data import courses


def get_course_objects() -> list:
    course_objects = []

    for course in courses:
        for name, description in course.items():
            course_objects.append(Course(name=name, description=description))

    return course_objects
