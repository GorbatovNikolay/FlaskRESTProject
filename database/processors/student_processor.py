from random import choice, randrange, randint, sample

from database.models import Student, Group


class FillStudentProcessor:
    @classmethod
    def create_st_obj(cls, std: dict, gr_obj: Group = None) -> Student:
        """Creates instances of Student with or without group."""
        if gr_obj:
            return Student(
                first_name=std['name'],
                last_name=std['lastname'],
                group=gr_obj
            )
        return Student(
            first_name=std['name'],
            last_name=std['lastname']
        )

    @classmethod
    def add_students_with_groups(cls, students: list, groups: list) -> tuple:
        st_objects = []

        for group_obj in groups:
            number_of_students_in_a_group = choice([i for i in range(0, 31) if i == 0 or i > 9])
            if not number_of_students_in_a_group:
                continue
            for step in range(number_of_students_in_a_group):
                unassigned_students = len(students)
                if unassigned_students not in range(1, 10):
                    student = students.pop(randrange(unassigned_students))
                    st_objects.append(cls.create_st_obj(student, group_obj))

        return students, st_objects

    @classmethod
    def get_student_objects(cls, students: list, groups: list) -> list:
        """Randomly assign students to groups and returns a list of student processors."""
        last_students, student_objects = cls.add_students_with_groups(students, groups)

        for student in last_students:
            student_objects.append(cls.create_st_obj(student))

        return student_objects

    @classmethod
    def assign_courses_to_students(cls, s_objects: list, c_objects: list) -> None:
        """Assigns 1 to 3 random courses to each student."""
        for student in s_objects:
            courses = sample(c_objects, k=randint(1, 3))
            student.courses.extend(courses)
