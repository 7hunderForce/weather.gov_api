import geocoder
import json
import requests

g = geocoder.ip('me')
print(f'\nMy Location: {g.latlng} \n')

lat, lng = g.latlng[0], g.latlng[1]

r1 = requests.get(f'https://api.weather.gov/points/{lat},{lng}')
json_data = json.loads(r1.text)
#print(json_data)

forecast_link = json_data['properties']['forecast']
#print(forecast_link)
r2 = requests.get(forecast_link)
forecast_data = json.loads(r2.text)
#print(forecast_data)

for item in forecast_data['properties']['periods']:
    print(f"Weekday: {item['name']}")
    print(f"Date: {item['startTime'][:10]}")
    print(f"Time: {item['startTime'][11:16]} - {item['endTime'][11:16]}")
    print(f"Temp: {item['temperature']} {item['temperatureUnit']}")
    print(f"Wind: {item['windSpeed']} ({item['windDirection']})")
    print(f"Forecast: {item['detailedForecast']}")
    print('\n')
