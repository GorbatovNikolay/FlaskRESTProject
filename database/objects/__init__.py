from .course_objects_creation import get_course_objects
from .group_objects_creation import group_objects
from .student_objects_creation import get_student_objects

db_objects = [group_objects, get_student_objects(), get_course_objects()]
