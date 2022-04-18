from flask_restful import Resource, request

from rest_api_app.database.db_creation import session
from rest_api_app.database.services import MyQueries


class AddToCourse(Resource):
    def post(self, student_id: int):
        """Adds a student to the courses with ids given in a list.
        ---
        tags:
            - Add student to course
        consumes:
            - application/json
        parameters:
            - name: student_id
              in: path
              type: integer
              required: true
              description: ID of the student.
            - in: body
              name: course_ids
              description: List of course ids.
              schema:
                type: object
                required:
                  - course_ids
                properties:
                  course_ids:
                    type: array
                example: {"course_ids": [1, 2, 3]}
        responses:
            200:
                description: No unexpected error.
        """
        course_ids = request.json['course_ids']
        return MyQueries.add_student_to_course(session, student_id, course_ids)
