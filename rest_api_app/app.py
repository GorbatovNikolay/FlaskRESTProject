from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from rest_api_app.resources import (
    AddStudent, AddToCourse, DeleteStudent,
    Groups, RemoveFromCourse, Students
)


def create_app():
    template = {
        'swagger': '2.0',
        'info': {
            'title': 'Task 10 API',
            'description': 'API for Task 10 App',
            'version': '0.1'
        },
        'host': '127.0.0.1:5000',
        'basePath': '/api',
        'schemes': ['http'],
    }

    app = Flask(__name__)
    api = Api(app)
    swagger = Swagger(app, template=template)

    api.add_resource(DeleteStudent, '/api/student/<int:student_id>')
    api.add_resource(AddStudent, '/api/student/<string:first_name>/<string:last_name>')
    api.add_resource(Students, '/api/students/<string:course_name>')
    api.add_resource(Groups, '/api/groups/<int:number_of_students>')
    api.add_resource(RemoveFromCourse, '/api/student/<int:student_id>/course/<int:course_id>')
    api.add_resource(AddToCourse, '/api/courses/student/<int:student_id>')

    return app
