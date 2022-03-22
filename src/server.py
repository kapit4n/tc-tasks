from flask import Flask, request
from flask_restful import Api
from resources.task_list_resource import TaskListResource
from resources.task_resource import TaskResource
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<task_id>')

if __name__ == '__main__':
    app.run(debug=True)
