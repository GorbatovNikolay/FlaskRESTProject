from .conftest import client
from .test_functions.add_student import test_add_student
from .test_functions.delete_student import test_delete_student, test_delete_does_not_exist
from .test_functions.get_groups import test_get_groups, test_get_groups_with_invalid_student_number
from .test_functions.student_to_course import test_add_student_to_course, test_add_does_not_exist
from .test_functions.students_by_course import test_get_students, test_get_students_with_invalid_course


def run_application_test():
    test_add_student(client)
    test_delete_student(client)
    test_delete_does_not_exist(client)
    test_add_student_to_course(client)
    test_add_does_not_exist(client)
    test_get_students(client)
    test_get_students_with_invalid_course(client)
    test_get_groups(client)
    test_get_groups_with_invalid_student_number(client)


if __name__ == '__main__':
    run_application_test()
