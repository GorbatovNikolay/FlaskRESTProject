from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from rest_api_app.resources.course_resources import (
    AddToCourse,
    RemoveFromCourse
)
from rest_api_app.resources.group_resources import Groups
from rest_api_app.resources.student_resources import (
    AddStudent,
    DeleteStudent,
    Students
)


def create_app():
    template = {
        'swagger': '2.0',
        'info': {
            'title': 'Flask REST API',
            'version': '0.1'
        },
        'host': '127.0.0.1:5000',
        'basePath': '/api',
        'schemes': ['http'],
    }

    app = Flask(__name__)
    api = Api(app)
    swagger = Swagger(app, template=template)

    api.add_resource(AddStudent, '/api/student/<string:first_name>/<string:last_name>')
    api.add_resource(DeleteStudent, '/api/student/<string:first_name>/<string:last_name>')
    api.add_resource(Students, '/api/students/<string:course_name>')
    api.add_resource(Groups, '/api/groups/<int:number_of_students>')
    api.add_resource(RemoveFromCourse, '/api/student/<int:student_id>/course/<int:course_id>')
    api.add_resource(AddToCourse, '/api/courses/student/<int:student_id>')

    return app
