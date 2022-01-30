
from statistics import mode


with open("my_file.txt") as file:
	contents = file.read()
	print(contents)


with open("my_file.txt", mode="a") as file:
	file.write("\nI am 19 years old")


with open("new_file.txt", "x") as file:
	file.write(contents)