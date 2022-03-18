from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

tasks = [{"id": "1", "name": 'Generics'}, {"id": "2", "name": 'Routines'}]

class TaskListResource(Resource):
    def get(self):
        return tasks

class TaskResource(Resource):
    def get(self, task_id):
        return tasks[int(task_id)]

    def post(self):
        post_body = request.get_json()
        tasks.append({"name": post_body['name'], "id": str(len(tasks))})
        return tasks[-1]

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<task_id>')

if __name__ == '__main__':
    app.run(debug=True)
