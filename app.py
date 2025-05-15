from flask import Flask, render_template, request
import requests
from datetime import datetime
import os
import logging
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    raise EnvironmentError("No environment variable OPENWEATHER_API_KEY")

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))

locations = {
    "Poland": {
        "Warszawa": {"lat": 52.2298, "lon": 21.0118},
        "Kraków": {"lat": 50.0647, "lon": 19.9450},
        "Gdańsk": {"lat": 54.3520, "lon": 18.6466}
    },
    "USA": {
        "New York": {"lat": 40.7128, "lon": -74.0060},
        "Los Angeles": {"lat": 34.0522, "lon": -118.2437},
        "Chicago": {"lat": 41.8781, "lon": -87.6298}
    },
    "Germany": {
        "Berlin": {"lat": 52.5200, "lon": 13.4050},
        "Monachium": {"lat": 48.1351, "lon": 11.5820},
        "Hamburg": {"lat": 53.5511, "lon": 9.9937}
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    selected_country = list(locations.keys())[0]
    selected_city = list(locations[selected_country].keys())[0]

    if request.method == "POST":
        selected_country = request.form.get("country")
        selected_city = request.form.get("city")
        coords = locations.get(selected_country, {}).get(selected_city)

        if coords:
            url = (
                f"http://api.openweathermap.org/data/2.5/weather"
                f"?lat={coords['lat']}&lon={coords['lon']}"
                f"&appid={API_KEY}&units=metric&lang=en"
            )
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": "Failed to get weather"}
        else:
            weather_data = {"error": "Wrong location."}

    return render_template("index.html",
                           locations=locations,
                           selected_country=selected_country,
                           selected_city=selected_city,
                           weather=weather_data)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(f"App started on {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    logging.info(f"Author: Filip Chyla")
    logging.info(f"Listening on port {PORT}")
    app.run(host="0.0.0.0", port=PORT)
