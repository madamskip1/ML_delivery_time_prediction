import sys
sys.path.insert(1, '../src')
from simple_model import *
from sklearn.ensemble import RandomForestRegressor
from joblib import load


def get_model_prediction(model, data):

    if model['id'] == 0:
        model = SimpleModel()
        time = model.predict(data)
    else:
        model = load("../models/random_forest_model.joblib")
        time = model.predict(data)[0]

    return time
