import flask
from flask import request, jsonify
import numpy
import pickle
import json
import sys
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
app = flask.Flask(__name__)
app.config["DEBUG"] = True

filename = 'finalized_model.pkl'
@app.route('/api/v0/verify', methods=['GET','POST'])
def predict_new_transaction():
    vec = pd.DataFrame([request.json])
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
    res = str(loaded_model.predict(vec))
    result = [
    {'id': 0,
     'prediction': res} ]
    return jsonify(result)