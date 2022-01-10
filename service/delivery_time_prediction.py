from datetime import datetime
from flask_restful import Resource
from flask import request, jsonify
import json

from models.get_prediction import get_model_prediction
from data import get_data
from models.get_model_type import get_model_type
from logs.write_log import write_log

class DeliveryTime(Resource):
    def get(self):
        args = request.args
        if 'data' in request.args:
            d = request.args.get('data', default=None, type=None)
            
            data = json.loads(d)
            df = get_data(data)
            model = data["model"]
            model = get_model_type(data["model"])
            time = get_model_prediction(model, df)
            mess = time
            write_log(data, model, time)

        else:
            mess = 'Invalid input'    
        
        return mess
