from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "eb9e1a6f33mshb6e52ebfe7ede52p12c97cjsn80155e1a84f9"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        if city:
            url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
            querystring = {"city": city}
            headers = {
                "X-RapidAPI-Key": API_KEY,
                "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
            }
            
            response = requests.get(url, headers=headers, params=querystring)
            weather_data = response.json()
    
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
