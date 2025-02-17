import xgboost as xgb
import os
import numpy as np
import json

def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model.bin")
    booster = xgb.Booster()
    booster.load_model(model_path)
    return booster

def input_fn(request_body, content_type='text/csv'):
    import pandas as pd
    from io import StringIO
    return pd.read_csv(StringIO(request_body), header=None)

def predict_fn(input_data, model):
    dmatrix = xgb.DMatrix(input_data)
    predictions = model.predict(dmatrix)
    return predictions

def output_fn(prediction, accept='application/json'):
    return json.dumps({"predictions": prediction.tolist()})
