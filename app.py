from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('model_and_encoders.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    model = loaded_data['model']
    label_encoders = loaded_data['label_encoders']

le_location = label_encoders['location']
le_cloud_cover = label_encoders['cloud_cover']
le_season = label_encoders['season']

weather_mapping = {
    0: 'Sunny',
    1: 'Cloudy',
    2: 'Rainy',
    3: 'Snowy'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print("Received data:", data)

    try:
        encoded_features = [
            float(data['Temperature']),
            float(data['Humidity']),
            float(data['Wind Speed']),
            float(data['Precipitation']),
            le_cloud_cover.transform([data['Cloud Cover']])[0].item(),
            float(data['Atmospheric Pressure']),
            float(data['UV Index']),
            le_season.transform([data['Season']])[0].item(),
            float(data['Visibility']),
            le_location.transform([data['Location']])[0].item()
        ]

        features_array = np.array(encoded_features).reshape(1, -1)
        print("Encoded features:", features_array)
        
        prediction = model.predict(features_array)[0]
        print("Prediction (numeric):", prediction)

        predicted_weather = weather_mapping.get(int(prediction), 'Unknown')
        print("Prediction (weather type):", predicted_weather)
        
        return jsonify({'prediction': predicted_weather})
    except KeyError as e:
        print(f'KeyError: {str(e)}')
        return jsonify({'error': f'Missing key in input data: {str(e)}'}), 400
    except Exception as e:
        print(f'Exception: {str(e)}')
        return jsonify({'error': f'Error processing the request: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
