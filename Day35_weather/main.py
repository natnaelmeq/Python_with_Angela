import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "21da191c1dafa5ebe269f2147c83c79a"

weather_parms = {
    "lat": 55.676098,
    "lon": 12.568337,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_parms)
response.raise_for_status()
weather_data = response.json()
# print(response.json()["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")



