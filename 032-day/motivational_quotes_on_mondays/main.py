import datetime as dt
import random
import smtplib


MY_EMAIL = "tecseitteste@gmail.com"
MY_PASSWORD = "1234abcd()"

now = dt.datetime.now()
weekday = now.weekday()

if ( weekday == 0 ): 
	with open("quotes.txt", "r") as quote_file:
		all_quotes = quote_file.readlines()
		random_quote = random.choice(all_quotes)

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=MY_EMAIL, password=MY_PASSWORD)
		connection.sendmail(from_addr=MY_EMAIL, 
								to_addrs=MY_EMAIL, 
								msg="Subject:Motivational Quote\n\n"
								f"{random_quote}"
							)
