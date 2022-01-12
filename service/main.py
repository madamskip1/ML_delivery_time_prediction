from flask import Flask, request, render_template
from flask_restful import Api, Resource
from delivery_time_prediction import DeliveryTime
from welcome_page import HelloWorld
app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(DeliveryTime, '/delivery')


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)