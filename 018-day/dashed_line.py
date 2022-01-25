from turtle import Turtle, Screen

turtle_tha 	= Turtle()

distance 	= 15

for _ in range(distance):
	turtle_tha.forward(10)
	turtle_tha.penup()
	turtle_tha.forward(10)
	turtle_tha.pendown()

screen = Screen()
screen.exitonclick()