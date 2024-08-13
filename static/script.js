document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const data = {
        Temperature: parseFloat(document.getElementById('temperature').value),
        Humidity: parseFloat(document.getElementById('humidity').value),
        'Wind Speed': parseFloat(document.getElementById('wind_speed').value),
        Precipitation: parseFloat(document.getElementById('precipitation').value),
        'Cloud Cover': document.getElementById('cloud_cover').value,
        'Atmospheric Pressure': parseFloat(document.getElementById('pressure').value),
        'UV Index': parseFloat(document.getElementById('uv_index').value),
        Season: document.getElementById('season').value,
        Visibility: parseFloat(document.getElementById('visibility').value),
        Location: document.getElementById('location').value
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').textContent = `Error: ${data.error}`;
        } else {
            document.getElementById('result').textContent = `Predicted Weather Type: ${data.prediction}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').textContent = `Error: ${error.message}`;
    });
});
