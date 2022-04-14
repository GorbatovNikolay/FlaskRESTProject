from flask_restful import Resource

from rest_api_app.database.db_creation import session
from rest_api_app.database.services import MyQueries


class DeleteStudent(Resource):
    def delete(self, student_id: int):
        """Deletes a student with a given id from the database.
        ---
        tags:
            - Delete student by id
        parameters:
            - name: student_id
              in: path
              type: integer
              required: true
              description: ID of the student that has to be deleted.
        responses:
            200:
                description: No unexpected error.
        """
        return MyQueries.delete_student_by_id(session, student_id)
