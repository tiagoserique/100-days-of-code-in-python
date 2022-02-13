import requests
from datetime import datetime


USERNAME = "tecseit"
TOKEN = "ASJDLSADJKSKDJJDLK"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

today = datetime.now()

graph_config = {
	"id": GRAPH_ID,
	"name": "Running Graph",
	"unit": "Km",
	"type": "float",
	"color":"momiji",
}

pixel_data = {
	"date": today.strftime("%Y%m%d"),
	"quantity": "1.91",
}

headers = {
	"X-USER-TOKEN": TOKEN,
}

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
