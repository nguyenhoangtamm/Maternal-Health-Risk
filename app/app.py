from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    model_choice= request.form.get('model_choice')
    if not model_choice:
        return render_template('index.html', prediction_text='Please select a model')
    model=joblib.load(f'model/{model_choice}.pkl')
    data = request.form.to_dict()
    data.pop('model_choice')
    data = pd.DataFrame([data])
    prediction = model.predict(data)
    return render_template('index.html', prediction_text=f'The prediction is: {prediction[0]}')


    

if __name__ == '__main__':
    app.run(debug=True)