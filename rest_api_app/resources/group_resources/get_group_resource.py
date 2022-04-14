from flask import make_response
from flask_restful import Resource

from rest_api_app.database.db_creation import session
from rest_api_app.database.services import MyQueries


class Groups(Resource):
    def get(self, number_of_students):
        """Returns all groups with number of students less or equal than a given number.
        ---
        tags:
            - Get groups by number of students
        parameters:
            - name: number_of_students
              in: path
              type: integer
              required: true
              description: Number of students to query groups.
        responses:
            200:
                description: No unexpected error.
        """
        return make_response(MyQueries.get_groups_by_amount_of_students(session, number_of_students), 200)
