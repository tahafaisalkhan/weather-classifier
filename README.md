# Weather Type Classification

## Overview
The Weather Type Classification project is designed to predict weather types based on various simulated weather-related features. This project utilizes a machine learning model to classify the weather into one of the following categories: Rainy, Sunny, Cloudy, or Snowy. The dataset used for this project is synthetically generated to provide a rich ground for practicing classification algorithms, data preprocessing, and outlier detection.

## Features
- **Input Parameters:** The application uses a variety of weather-related features such as Temperature, Humidity, Wind Speed, Precipitation, Cloud Cover, Atmospheric Pressure, UV Index, Season, Visibility, and Location to predict the weather type.
- **Prediction:** Based on the input features, the machine learning model classifies the weather into one of the four types: Rainy, Sunny, Cloudy, or Snowy.
- **Data Exploration:** The dataset includes outliers and a range of values that allow users to practice data preprocessing, feature engineering, and outlier detection methods.
- **Model Evaluation:** Users can evaluate the performance of various classification algorithms on the dataset.

## Technologies Used
- **Backend:** Python
- **Machine Learning:** scikit-learn (for model training and prediction)
- **Data Handling:** pandas, numpy
- **Data Visualization:** seaborn, matplotlib
  
## Dataset
This project utilizes a synthetically generated dataset designed to simulate weather conditions. The dataset includes features like:
- **Temperature:** Numeric values representing the temperature in degrees Celsius.
- **Humidity:** Numeric values representing the humidity percentage.
- **Wind Speed:** Numeric values representing the wind speed in kilometers per hour.
- **Precipitation:** Numeric values representing the precipitation percentage.
- **Cloud Cover:** Categorical values describing cloud cover.
- **Atmospheric Pressure:** Numeric values representing atmospheric pressure in hPa.
- **UV Index:** Numeric values indicating the strength of ultraviolet radiation.
- **Season:** Categorical values indicating the season during which the data was recorded.
- **Visibility:** Numeric values representing visibility in kilometers.
- **Location:** Categorical values indicating the type of location where the data was recorded.
- **Weather Type:** Categorical target variable for classification.

## How to Use
1. **Clone the Repository:** Clone this repository to your local machine using `git clone`.
2. **Install Dependencies:** Navigate to the project directory and install the necessary dependencies using `pip install -r requirements.txt`.
3. **Run the Model:** Use the provided Python scripts to preprocess the data, train the model, and make predictions.
4. **Experiment:** Modify the code to try out different classification algorithms, feature engineering techniques, and outlier detection methods.

## Future Work
- **Real-World Data Integration:** Incorporate real-world weather data to enhance the model's accuracy and reliability.
- **Web Interface:** Develop a web-based interface for user-friendly interactions with the model.
- **Model Optimization:** Explore and implement advanced machine learning techniques to improve prediction accuracy.

## Screenshots
<img width="1440" alt="Screenshot 2024-08-13 at 5 49 57 PM" src="https://github.com/user-attachments/assets/b1f857da-7e0b-4304-9e91-5ddf3ea9e1f0">
<img width="1440" alt="Screenshot 2024-08-13 at 5 50 03 PM" src="https://github.com/user-attachments/assets/01671a3f-0dac-4837-bbe1-c722773a0d47">

## Acknowledgments
This project is intended for educational and experimental purposes. The dataset is synthetically generated and does not represent real-world weather data. The dataset was obtained from: https://www.kaggle.com/datasets/nikhil7280/weather-type-classification/data
