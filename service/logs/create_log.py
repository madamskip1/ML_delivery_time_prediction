from datetime import datetime

def create_log_data(data, model, prediction):
    log = {
        "date": datetime.now().strftime("%b-%d-%Y %H:%M:%S"),
        "model": model['name'] ,
        "purchase_timestamp": data["purchase_timestamp"],
        "city": data["city"],
        "delivery_company": data["delivery_company"],
        "prediction": prediction
    }
    return log