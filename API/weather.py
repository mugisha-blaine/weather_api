
from flask import Flask, render_template, request
import json
import requests


app = Flask(__name__)

WEATHER_KEY = '4b3cad69b1579ba9194bcb281b206f84'

@app.route('/', methods=['GET', 'POST'])
def main():
    """function that displays weather infomration"""
    weather_data = None
    if request.method == 'POST':
        city_name = request.form.get('city')
        if city_name:
            weather_data = fetch_weather(city_name)
    return render_template('weather.html', weather_data=weather_data)

def fetch_weather(city_name):
    """function that fetches data for city that you provided"""
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    return {'temperature': temperature, 'description': description}

if __name__ == '__main__':
    app.run(debug=True)
