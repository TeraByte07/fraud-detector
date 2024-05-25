import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

# Load your data
# Replace this with the actual loading mechanism
df = pd.read_csv('fraud_detector/fraud.csv')

# Replace these with actual feature names and target
df = df.rename(columns={'type': 'payment_type'})
x = df[['amount', 'oldbalanceOrg', 'newbalanceOrig']]
y = df['isFraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.7, random_state=111)

# Train the model
model = RandomForestClassifier(random_state=123)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {test_accuracy}")

# Save the model
model_dir = 'C:\\Users\\Abu Nodrat\\Desktop\\fraud\\fraud_detector\\ml\\models\\'
model_path = os.path.join(model_dir, 'mlp.h5')

# Ensure the directory exists
os.makedirs(model_dir, exist_ok=True)

try:
    joblib.dump(model, model_path)
    print(f"Model saved successfully at {model_path}")
except Exception as e:
    print(f"Error saving the model: {e}")
