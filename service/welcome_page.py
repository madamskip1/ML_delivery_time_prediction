from flask import Flask, render_template, make_response
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return make_response(render_template("delivery.html"))