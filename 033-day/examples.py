import requests
from datetime import datetime


MY_LAT = -0.000990
MY_LON = -51.077000

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
response.raise_for_status()

data = response.json()
# print(data)

longitude = data["iss_position"]["longitude"]
latitude  = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

parameters = {
	"lat": MY_LAT,
	"lon": MY_LON,
	"formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset  = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[9])
# print(sunset)

time_now = datetime.now()

print(time_now)



