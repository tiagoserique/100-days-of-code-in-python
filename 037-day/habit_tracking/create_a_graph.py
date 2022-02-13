import requests


USERNAME = "tecseit"
TOKEN = "ASJDLSADJKSKDJJDLK"


pixela_endpoint = "https://pixe.la/v1/users"

# create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
	"id": "graph1",
	"name": "Running Graph",
	"unit": "Km",
	"type": "float",
	"color":"momiji",
}

headers = {
	"X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
