import numpy as np
import pickle

# Load model and encoders
with open('model_and_encoders.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    model = loaded_data['model']
    label_encoders = loaded_data['label_encoders']

# Test data
test_data = {
    'Temperature': 20.0,
    'Humidity': 50.0,
    'Wind Speed': 21.0,
    'Precipitation': 122.0,
    'Cloud Cover': 'partly cloudy',
    'Atmospheric Pressure': 2.0,
    'UV Index': 3.0,
    'Season': 'Spring',
    'Visibility': 10.0,
    'Location': 'inland'
}

# Encode features
encoded_features = [
    float(test_data['Temperature']),
    float(test_data['Humidity']),
    float(test_data['Wind Speed']),
    float(test_data['Precipitation']),
    label_encoders['cloud_cover'].transform([test_data['Cloud Cover']])[0],
    float(test_data['Atmospheric Pressure']),
    float(test_data['UV Index']),
    label_encoders['season'].transform([test_data['Season']])[0],
    float(test_data['Visibility']),
    label_encoders['location'].transform([test_data['Location']])[0]
]

# Convert to 2D array
features_array = np.array(encoded_features).reshape(1, -1)

# Predict
prediction = model.predict(features_array)[0]
print("Prediction:", prediction)
