from database.models import Course
from database.processors.consts import COURSES


class FillCourseProcessor:
    @classmethod
    def get_course_objects(cls) -> list:
        return [Course(name=course['name'], description=course['description']) for course in COURSES]
