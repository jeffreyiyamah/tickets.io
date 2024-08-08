from flask import Flask, render_template, request,jsonify
import requests

app = Flask(__name__)

import requests

def get_geolocation(ip_address):
    api_url = f"http://ipwhois.app/json/{ip_address}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('city', 'Unknown City')
    return "Unknown City"


@app.route('/main')
def geolocation():
    user_ip = "8.8.8.8"
    city = get_geolocation(user_ip)
    if city:
        return render_template('main_page.html', city=city)
    else:
        return "Failed to retrieve city data", 500

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/main')
def main():
    return render_template('searchbar.html')

if __name__ == '__main__':
    app.run(debug=True)
