from turtle import Turtle, Screen

turtle_tha = Turtle()

distance 	= 100
angle 		= 90

for _ in range(4):
	turtle_tha.forward(distance)
	turtle_tha.right(angle)


screen = Screen()
screen.exitonclick()