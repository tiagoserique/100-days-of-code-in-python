import requests


USERNAME = "tecseit"
TOKEN = "ASJDLSADJKSKDJJDLK"


pixela_endpoint = "https://pixe.la/v1/users"

# create account
user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor":"yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
