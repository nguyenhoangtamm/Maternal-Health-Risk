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
    model_path = project_root / 'model' / 'decision_tree_model.pkl'

    # Lấy dữ liệu từ form
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # Load the model
    model = joblib.load(model_path)

    # Ensure the input data has the same structure as the training data
    feature_names = ['Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate']
    input_df = pd.DataFrame(final_features, columns=feature_names)

    # Make prediction
    prediction = model.predict(input_df)
    output = prediction[0]
    
    return jsonify({'prediction_text': format(output)})

if(__name__=='__main__'):
    app.run(debug=True)