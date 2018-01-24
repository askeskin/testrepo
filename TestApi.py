from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps


app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        return ["A","B","C"]




api.add_resource(Employees, '/employees')  # Route_1


if __name__ == '__main__':
    app.run(port=5002)