import turtle as t
import random


def random_color():
	r = random.randrange(1, 255)
	g = random.randrange(1, 255)
	b = random.randrange(1, 255)

	return (r, g, b)


directions = [0, 90, 180, 270]

turtle_tha 	= t.Turtle()

turtle_tha.pensize(10)
turtle_tha.speed(10)
t.colormode(255)

for _ in range(200):
	direction 	= random.choice(directions)
	color 		= random_color()
	
	turtle_tha.color(color)
	turtle_tha.setheading(direction)
	turtle_tha.forward(30)

screen = t.Screen()
screen.exitonclick()
