import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# Đường dẫn tới thư mục gốc của dự án
project_root = Path(__file__).resolve().parent.parent

# Đường dẫn tới tệp CSV
csv_path = project_root / 'data' / 'Maternal_Health_Risk.csv'

data = pd.read_csv(csv_path)
# Chuẩn bị dữ liệu
X = data.drop('RiskLevel', axis=1)
y = data['RiskLevel']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Xây dựng mô hình Neural Network
model = MLPClassifier(random_state=42, max_iter=300)
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy*100:.2f}%')
print('Classification Report:')
print(report)

# Lưu mô hình
model_path = project_root / 'model' / 'neural_network_model.pkl'
with open(model_path, 'wb') as file:
    pickle.dump(model, file)
