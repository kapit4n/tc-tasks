from flask import request
from flask_restful import Resource
from constants.tasks import tasks


class TaskListResource(Resource):
    def get(self):
        return tasks

    def post(self):
        post_body = request.get_json()
        tasks.append({"name": post_body['name'], "id": str(len(tasks))})
        return tasks[-1]

