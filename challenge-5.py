# 🔹 Challenge 5: Build a Flask API that fetches live weather data from an external API and returns it in JSON format.

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/weather', methods=['GET'])
def get_weather():
    """Fetch live weather data for a given city."""
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "❌ City parameter is required"}), 400

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            return jsonify({"error": data.get("message", "Unknown error")}), response.status_code

        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return jsonify(weather_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)