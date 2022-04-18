from flask_restful import Resource

from rest_api_app.database.db_creation import session
from rest_api_app.database.services import MyQueries


class DeleteStudent(Resource):
    def delete(self, first_name: str, last_name: str):
        """Deletes a student from the database.
        ---
        tags:
            - Delete student
        parameters:
            - name: first_name
              in: path
              type: string
              required: true
              description: First name of the student that has to be deleted.
            - name: last_name
              in: path
              type: string
              required: true
              description: Last name of the student that has to be deleted.
        responses:
            200:
                description: No unexpected error.
        """
        return MyQueries.delete_student(session, first_name, last_name)
