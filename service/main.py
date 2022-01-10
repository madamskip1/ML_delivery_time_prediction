from flask import Flask, request
from flask_restful import Api, Resource
from delivery_time_prediction import DeliveryTime
from welcome_page import HelloWorld
app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, '/')
api.add_resource(DeliveryTime, '/delivery')


if __name__ == "__main__":
    app.run(debug=True)