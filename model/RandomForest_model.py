import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from pathlib import Path
import joblib

# Đường dẫn tới thư mục gốc của dự án
project_root = Path(__file__).resolve().parent.parent

# Đường dẫn tới tệp CSV
csv_path = project_root / 'data' / 'Maternal_Health_Risk.csv'

# Load your dataset
data = pd.read_csv(csv_path)

# Assuming the last column is the target variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Save the model
model_path = project_root / 'model' / 'RandomForest_model.pkl'
joblib.dump(model, model_path)
print(f'Model saved to {model_path}')