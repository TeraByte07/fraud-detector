import joblib
import os

# Assuming best_estimator is your trained model
# You need to replace this with the actual code to train or load your model
# For example, best_estimator = ... (your model training/loading code here)

# Dummy code to represent your trained model (replace this)
from sklearn.ensemble import RandomForestClassifier
best_estimator = RandomForestClassifier()

# Define the directory and path for saving the model
model_dir = 'C:\\Users\\Abu Nodrat\\Desktop\\fraud\\fraud_detector\\ml\\models\\'
model_path = os.path.join(model_dir, 'mlp.h5')

# Ensure the directory exists
os.makedirs(model_dir, exist_ok=True)

try:
    # Save the model
    joblib.dump(best_estimator, model_path)
    print(f"Model saved successfully at {model_path}")
except Exception as e:
    print(f"Error saving the model: {e}")
