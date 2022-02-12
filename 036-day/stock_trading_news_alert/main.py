# import os
import requests
from twilio.rest import Client
from newsapi import NewsApiClient
# from twilio.http.http_client import TwilioHttpClient


MY_PHONE = ""
MY_TWILIO = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY  = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""


stock_params = {
	"function": "TIME_SERIES_DAILY",
	"symbol": STOCK_NAME,
	"apikey" : STOCK_API_KEY,
}

response = requests.get(
	url=STOCK_ENDPOINT, 
	params=stock_params
)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# Get yesterday's closing stock price.
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

# Get the day before yesterday's closing stock price
before_yesterday_data = data_list[1]
before_yesterday_closing_price = float(before_yesterday_data["4. close"])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the 
# positive difference is 20
difference = yesterday_closing_price - before_yesterday_closing_price

up_down = None
if ( difference > 0 ):
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday 
# and closing price the day before yesterday.
diff_percent = abs(round(difference / yesterday_closing_price * 100))

# If percentage is greater than 5 then use the News API to get articles related 
# to the COMPANY_NAME.
if ( diff_percent > 5 ):
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    all_articles = newsapi.get_everything(qintitle=COMPANY_NAME)["articles"]

    # Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = all_articles[:3]

    # Create a new list of the first 3 article's headline and description using 
    # list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"Headline: {article['title']}. \n"
        f"Brief: {article['description']}" 
        for article in three_articles
    ]

    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # Send each article as a separate message via Twilio. 
    for articles in formatted_articles:
        # client = Client(account_sid, auth_token, http_client=proxy_client)
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=articles,
            from_=MY_TWILIO,
            to=MY_PHONE
        )
