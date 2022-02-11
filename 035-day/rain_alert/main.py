import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


MY_PHONE = ""
MY_TWILIO = ""


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = ''
auth_token = os.environ.get("AUTH_TOKEN")

weather_parameters = {
	"lat": -0.000990,
	"lon": -51.077000,
	"appid": api_key,
	"exclude": "current,minutely,daily,alerts",
}

response = requests.get(
	OWM_Endpoint, 
	params=weather_parameters,
)

response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
	condition_code = int(hour_data["weather"][0]["id"])
	if ( condition_code < 700 ):
		will_rain = True

if ( will_rain ):
	proxy_client = TwilioHttpClient()
	proxy_client.session.proxies = {'https': os.environ['https_proxy']}

	client = Client(account_sid, auth_token, http_client=proxy_client)
	message = client.messages.create(
		body="It's going to rain today. Remember to bring an umbrella",
		from_=MY_TWILIO,
		to=MY_PHONE
	)
	print(message.status)