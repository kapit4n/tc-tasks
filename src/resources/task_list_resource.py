from flask_restful import Resource
from constants.tasks import tasks


class TaskListResource(Resource):
    def get(self):
        return tasks
