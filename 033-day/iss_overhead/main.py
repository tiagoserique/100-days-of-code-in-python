import time
import smtplib
import requests
from datetime import datetime

MY_LAT = -0.000990 # Your latitude
MY_LON = -51.077000 # Your longitude

MY_USER = ""
MY_PASSWORD = ""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    in_my_latitude = ( MY_LAT - 5 ) <= iss_latitude <= ( MY_LAT + 5 )
    in_my_logitude = ( MY_LON - 5 ) <= iss_longitude <= ( MY_LON + 5 )

    return in_my_latitude and in_my_logitude


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset  = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    return sunset <= hour_now <= sunrise 


while ( True ):
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_USER, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_USER, 
                                    to_addrs=MY_USER,
                                    msg="Subject:Look up\n\n"
                                    "The ISS is above you in the sky."
                                )