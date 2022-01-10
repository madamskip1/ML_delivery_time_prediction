import os
import json
from logs.create_log import create_log_data

import os
ROOT_DIR = os.getcwd()

def write_log(data, model, prediction):
    data = create_log_data(data, model, prediction)
    file_dir = ROOT_DIR+"/prediction.jsonl"
    if not os.path.isfile(file_dir):
        open(file_dir, 'a').close()
    with open(file_dir, 'a') as file:
        log = json.dumps(data)
        file.write(log + "\n")
    file.close()