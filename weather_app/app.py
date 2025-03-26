from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "1d14d2a73f894c2884c70349252603"  # Replace with your WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form['city']
        response = requests.get(BASE_URL, params={
            "key": API_KEY,
            "q": city
        })
        
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["location"]["name"],
                "country": data["location"]["country"],
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "icon": data["current"]["condition"]["icon"],
                "is_day": data["current"]["is_day"]
            }
        else:
            error = "City not found or API issue."

    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
