import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
   
@app.route('/predict')
def predict():
    return render_template('predict.html')

if(__name__=='__main__'):
    app.run(debug=True)