
from flask_restful import Resource
from constants.tasks import tasks

class TaskResource(Resource):
    def get(self, task_id):
        return tasks[int(task_id)]
