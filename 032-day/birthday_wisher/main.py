import pandas
import random
import smtplib
import datetime as dt


MY_EMAIL = "your_email@email.com"
MY_PASSWORD = "your_password"


birthday_people = []

now = dt.datetime.now()
today = now.day
month = now.month 

data = pandas.read_csv("birthdays.csv")
data = pandas.DataFrame(data)

birthday_people = [row for (index, row) in data.iterrows() 
					if ( today == row.day ) and ( month == row.month )
				]

print(birthday_people)
for person in birthday_people:
	person_name = person["name"]
	person_email = person["email"]

	file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
	with open(file_path, "r") as file:
		letter = file.read()
		letter = letter.replace("[NAME]", person_name)

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=MY_EMAIL, password=MY_PASSWORD)
		connection.sendmail(from_addr=MY_EMAIL, to_addrs=person_email,
								msg="Subject:Happy Birthday!!!\n\n"
								f"{letter}"
							)