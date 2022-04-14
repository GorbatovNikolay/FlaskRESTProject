from .course_processor import FillCourseProcessor
from .group_processor import FillGroupProcessor
from .student_processor import FillStudentProcessor
from .test_data import students

group_objects = FillGroupProcessor.get_group_objects()

db_objects = [
    group_objects,
    FillStudentProcessor.get_student_objects(students, group_objects),
    FillCourseProcessor.get_course_objects()
]
