import requests

def fetch_events(api_key, city, start_date, end_date):
    url = "https://app.ticketmaster.com/discovery/v2/events"
    params = {
        'apikey': api_key,
        'city': city,
        'classificationName': 'music',
        'startDateTime': start_date,
        'endDateTime': end_date
    }
    response = requests.get(url, params=params)
    print(f"Request URL: {response.url}")  # Debug statement
    print(f"Status Code: {response.status_code}")  # Debug statement
    if response.status_code == 200:
        print("Response received")  # Debug statement
        return response.json()
    else:
        print(f"Error: {response.status_code}")  # Debug statement
        return None

def parse_events(response):
    events = response.get('_embedded', {}).get('events', [])
    if not events:
        print("No events found")  # Debug statement
    parsed_events = []
    for event in events:
        name = event.get('name')
        url = event.get('url')
        dates = event.get('dates', {}).get('start', {}).get('localDate')
        venues = event.get('_embedded', {}).get('venues', [{}])[0].get('name')
        parsed_events.append({
            'name': name,
            'url': url,
            'date': dates,
            'venue': venues
        })
    return parsed_events

api_key = 'yqQIdv4Qcv5m4bs4T8ZmhClyQXP1QeTD'
city = 'Boston'
start_date = '2024-08-11T00:00:00Z'
end_date = '2024-08-11T23:59:59Z'

response = fetch_events(api_key, city, start_date, end_date)
if response:
    events = parse_events(response)
    for event in events:
        print(f"Artist/Concert: {event['name']}, Date: {event['date']}, Venue: {event['venue']}, URL: {event['url']}")
else:
    print("No events found or there was an error with the request.")
