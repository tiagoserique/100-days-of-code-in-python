
# unlimited_positional_arguments
# *args

from distutils.archive_util import make_archive
from numpy import multiply


def add(*args):
	sum = 0
	for n in args:
		sum += n
	return sum

print(add(1, 2, 0, 3, 4))


# many_keyworded_arguments
# **kwargs

def calculate(n, **kwargs):
	# print(kwargs)
	# for key, value in kwargs.items():
	# 	print(key)
	# 	print(value)
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)

calculate(2, add=3, multiply=5)


class Car:
	def __init__(self, **kw):
		self.make  = kw.get("make")
		self.model = kw.get("model")
		self.color = kw.get("color")
		self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)