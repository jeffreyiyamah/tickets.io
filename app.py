from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
from livereload import Server

app = Flask(__name__)

API_KEY = 'yqQIdv4Qcv5m4bs4T8ZmhClyQXP1QeTD'

def get_geolocation(ip_address):
    api_url = f"http://ipwhois.app/json/{ip_address}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('city', 'Unknown City')
    return "Unknown City"

def get_events_by_parameters(api_key, venue=None, date=None, postal_code=None, keyword=None):
    today = datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ')
    api_url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        'apikey': api_key,
        'keyword': keyword,
        'postalCode': postal_code,
        'startDateTime': date + 'T00:00:00Z' if date else today,
        'endDateTime': date + 'T23:59:59Z' if date else today,
        'locale': 'en-us',
        'classificationName' : 'Music'
    }
    params = {k: v for k, v in params.items() if v is not None}
    response = requests.get(api_url, params=params)
    print(f"API URL: {response.url}")
    if response.status_code == 200:
        data = response.json()
        print(f"API Response: {data}")
        return data
    print(f"API Error: {response.status_code} - {response.text}")
    return None

@app.route('/main', methods=['GET', 'POST'])
def geolocation():
    if request.method == 'POST':
        city = request.form['city']
        date = request.form['date']
        keyword = request.form['keyword']
        events = get_events_by_parameters(API_KEY, postal_code=None, date=date, keyword=keyword)
        return render_template('main_page.html', city=city, events=events)
    else:
        user_ip = "141.154.12.154"
        city = get_geolocation(user_ip)
        return render_template('main_page.html', city=city, events=None)
    
@app.route('/searchbar', methods=['GET'])
def searchbar():
    return render_template('searchbar.html')

@app.route('/')
def home():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)
    server = Server(app.wsgi_app)
    server.serve(port=5000, host='0.0.0.0', restart_delay=1)
