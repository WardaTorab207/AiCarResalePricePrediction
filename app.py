from flask import Flask, request, jsonify
import pickle
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Initialize Flask app
app = Flask(__name__)

# Load the saved model (check project/model/ then parent folder)
model_name = 'Gradient Boosting_model.pkl'
model_path = os.path.join(os.path.dirname(__file__), 'model', model_name)
if not os.path.exists(model_path):
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), model_name)
if not os.path.exists(model_path):
    raise FileNotFoundError(
        f"Model file '{model_name}' not found. "
        "Run Muawwaz.py from project root first to train and save the model."
    )
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Feature preprocessing (ensure consistent scaling)
numerical_features = ['Power (hp)', 'Consumption (l/100 km)', 'Number of doors', 'Number of seats']
scaler = StandardScaler()

# Define a route for home
@app.route('/')
def home():
    return "Welcome to the Car Price Prediction API!"

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Convert input JSON to a DataFrame
        input_data = pd.DataFrame([data])
        
        # Preprocess numerical features
        input_data[numerical_features] = scaler.fit_transform(input_data[numerical_features])
        
        # Make predictions
        prediction = model.predict(input_data)
        
        # Return the prediction as JSON
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
