import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from pathlib import Path
import pickle

# Đường dẫn tới tệp CSV
project_root = Path(__file__).resolve().parent.parent
csv_path = project_root / 'data' / 'Maternal_Health_Risk.csv'

# Load the dataset
data = pd.read_csv(csv_path)

# Preprocess the data
X = data.drop('RiskLevel', axis=1)
y = data['RiskLevel']  # Chuyển sang dạng số

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Logistic Regression model
model = LogisticRegression(solver='lbfgs', max_iter=500)

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(class_report)

# Save the model
model_path = project_root / 'model' / 'logistic_regression_model.pkl'
with open(model_path, 'wb') as file:
    pickle.dump(model, file)
