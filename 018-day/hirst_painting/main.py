import colorgram
import random
import turtle as t
from colors import color_list


def extract_image_colors():
	colorgram_colors = colorgram.extract('image.jpg', 30)

	rgb_colors = []

	for item in colorgram_colors:
		rgb_colors.append(tuple(item.rgb)) 

	return rgb_colors


tortoise = t.Turtle()
tortoise.speed("fastest")
t.colormode(255)

dots_count = 100

tortoise.penup()
tortoise.hideturtle()
tortoise.setx(-250)
tortoise.sety(-250)

for dot in range(1, dots_count + 1):
	tortoise.dot(20, random.choice(color_list))
	tortoise.forward(50)
	
	if ( dot % 10 == 0 ):
		tortoise.setheading(90)
		tortoise.forward(50)
		tortoise.setx(-250)
		tortoise.setheading(0)

screen = t.Screen()
screen.exitonclick()
