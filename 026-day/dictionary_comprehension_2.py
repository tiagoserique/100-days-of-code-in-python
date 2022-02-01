
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

def convert(temp_c):
    return (temp_c * 9/5) + 32

weather_f = {key: convert(values) for (key, values) in weather_c.items()}

print(weather_f)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.items()

# print(x) 