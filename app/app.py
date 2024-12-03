import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify
import joblib
import pickle
from pathlib import Path
app = Flask(__name__,template_folder="templates")
# Đường dẫn tới thư mục gốc của dự án
project_root = Path(__file__).resolve().parent.parent



@app.route('/')
def home():
    return render_template('index.html')
   
@app.route('/predict',methods=['GET'])
def predict():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predictPost():
    
    
    typeModel = request.form['model']
    int_features = [float(x) for key, x in request.form.items() if key != 'model']
    
    final_features = [np.array(int_features)]
    if typeModel == '0':
        model_path = project_root / 'model' / 'decision_tree_model.pkl'
    elif typeModel == '1':
        model_path = project_root / 'model' / 'RandomForest_model.pkl'
    elif typeModel == '3':
        model_path = project_root / 'model' / 'neural_network_model.pkl'
    elif typeModel == '2':
        model_path = project_root / 'model' / 'logistic_regression_model.pkl'

    model = joblib.load(model_path)
    print("Model loaded:", model)  # In ra mô hình để kiểm tra

    prediction = model.predict(final_features)
    output = prediction[0]
    
    return jsonify({'prediction_text': format(output)})


if(__name__=='__main__'):
    app.run(debug=True)