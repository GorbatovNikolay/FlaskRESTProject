from flask_restful import Resource

from rest_api_app.database.db_creation import session
from rest_api_app.database.services import MyQueries


class AddStudent(Resource):
    def post(self, first_name: str, last_name: str):
        """Adds a new student with a given name and last name to the database.
        ---
        tags:
            - Add new student
        parameters:
            - name: first_name
              in: path
              type: string
              required: true
              description: First name of the student
            - name: last_name
              in: path
              type: string
              required: true
              description: Last name of the student.
        responses:
            200:
                description: No unexpected error.
        """
        return MyQueries.add_new_student(session, first_name, last_name)
