from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE 	= 5
MOVE_INCREMENT		 	= 10
CAR_AMOUNT				= 15


class CarManager:
	def __init__(self):
		self.all_cars  = []
		self.car_speed = STARTING_MOVE_DISTANCE


	def create_car(self):
		if ( random.randint(1, 6) == 1 ):
			new_car = Turtle()
			new_car.shape("square")
			new_car.shapesize(1, 2)
			new_car.penup()
			new_car.goto(300, random.randint(-250, 250))
			new_car.color(random.choice(COLORS))
			new_car.speed = self.car_speed
			self.all_cars.append(new_car)


	def move(self):
		for car in self.all_cars:
			new_x = car.xcor() - self.car_speed
			car.goto(new_x, car.ycor())


	def increse_speed(self):
			self.car_speed += MOVE_INCREMENT


	def reset_cars(self):
		for car in self.all_cars:
			if ( car.xcor() < -320 ):
				self.all_cars.remove(car)