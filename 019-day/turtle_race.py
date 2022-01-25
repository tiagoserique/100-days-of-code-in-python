from tkinter import Y
from turtle import Turtle, Screen
import random
import turtle


colors 	= ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

screen_width 	= 500
screen_height 	= 400

start_x = -round(screen_width / 2) + 20
end_x	= round(screen_width / 2) - 20

start_y = -100



is_race_on = False

screen = Screen()
screen.setup(width=screen_width, height=screen_height)

user_bet = screen.textinput(title="Make your bet", 
				prompt="Which turtle will win the race? Enter a color: ")

for color in colors:
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(color)
	new_turtle.penup()
	new_turtle.goto(x=start_x, y=start_y)
	turtles.append(new_turtle)
	start_y += 30

if ( user_bet ):
	is_race_on = True

while ( is_race_on ):
	for turtle in turtles:
		if ( turtle.xcor() > end_x ):
			is_race_on = False
			winning_color = turtle.pencolor()
			
			if ( winning_color == user_bet ):
				print(f"You've won! The {winning_color} turtle is the winner!")
			
			else:
				print(f"You've lost! The {winning_color} turtle is the winner!")

		rand_distance = random.randint(0, 10)
		turtle.forward(rand_distance)


screen.exitonclick()