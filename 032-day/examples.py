import smtplib


my_email = ""
password = ""
to_adrrs = ""

# connection = smtplib.SMTP("smtp.gmail.com")
with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()
	connection.login(user=my_email, password=password)
	connection.sendmail(from_addr=my_email,
						to_addrs=to_adrrs, 
						msg="Subject:Hello\n\nThis is the body of my email")

# connection.close()


import datetime as dt

now = dt.datetime.now()
# print(now)
year = now.year
month = now.month

date_of_birth = dt.datetime(year=2012, month=12, day=12)
# print(date_of_birth)
