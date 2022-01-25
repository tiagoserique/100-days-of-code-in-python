from turtle import Turtle, Screen
import random


colours = ["black", "gray", "royal blue", "blue", "medium turquoise", "red", 
	"medium sea green", "lime green", "medium orchid", "dark violet", "indigo",
	"coral", "orange", "maroon", "pale violet red"
]


def draw_shape(sides):
	distance 	= 100
	angle 		= 360 / side

	color = random.choice(colours)
	turtle_tha.color(color)

	for _ in range(side):
		turtle_tha.forward(distance)
		turtle_tha.right(angle)


turtle_tha = Turtle()

for side in range(3, 11):
	draw_shape(side)

screen = Screen()
screen.exitonclick()