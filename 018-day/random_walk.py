# https://en.wikipedia.org/wiki/Random_walk
from turtle import Turtle, Screen
import random


colours = ["black", "gray", "royal blue", "blue", "medium turquoise", "red", 
	"medium sea green", "lime green", "medium orchid", "dark violet", "indigo",
	"coral", "orange", "maroon", "pale violet red"
]

directions = [0, 90, 180, 270]

turtle_tha 	= Turtle()

turtle_tha.pensize(10)
turtle_tha.speed(10)

for _ in range(200):
	direction 	= random.choice(directions)
	color 		= random.choice(colours)
	turtle_tha.color(color)

	turtle_tha.setheading(direction)
	turtle_tha.forward(30)

screen = Screen()
screen.exitonclick()