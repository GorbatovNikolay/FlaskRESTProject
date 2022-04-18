from flask_restful import Resource

from rest_api_app.database.db_creation import session
from rest_api_app.database.services import MyQueries


class Students(Resource):
    def get(self, course_name: str):
        """Returns all students connected with a given course.
        ---
        tags:
            - Get all students by course name
        parameters:
            - name: course_name
              in: path
              type: string
              required: true
              description: Name of the course, which students are to be got.
        responses:
            200:
                description: No unexpected error.
        """
        return MyQueries.get_students_by_course_name(session, course_name)
