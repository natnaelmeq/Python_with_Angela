import requests
from datetime import datetime

LATITUDE = 55.676098
LONGITUDE = 12.568337
FORMATTED = 1,
UNFORMED = 0

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)
print(iss_position)

# sunrise and sunset api
# /////////////////////////////////

parameters = {"lat": LATITUDE, "lng": LONGITUDE, "formatted": UNFORMED

              }

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
print(sunset, sunrise)
