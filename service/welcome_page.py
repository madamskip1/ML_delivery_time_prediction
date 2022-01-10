from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        hello = "Hello, this is IUM application. To predict delivery time go to /delivery and put data query"
        return hello
