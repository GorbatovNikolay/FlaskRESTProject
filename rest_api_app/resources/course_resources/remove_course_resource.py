from flask_restful import Resource

from rest_api_app.database.db_creation import session
from rest_api_app.database.services import MyQueries


class RemoveFromCourse(Resource):
    def put(self, student_id: int, course_id: int):
        """Removes a student from the course.
        ---
        tags:
            - Remove student from course
        parameters:
            - name: student_id
              in: path
              type: integer
              required: true
              description: ID of the student.
            - name: course_id
              in: path
              type: integer
              required: true
              description: ID of the course.
        responses:
            200:
                description: No unexpected error.
        """
        return MyQueries.remove_student_from_course(session, student_id, course_id)
