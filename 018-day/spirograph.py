import turtle as t
import random





def random_color():
	r = random.randrange(1, 255)
	g = random.randrange(1, 255)
	b = random.randrange(1, 255)

	return (r, g, b)


def draw_spirograph(size_of_gap):
	for _ in range(int(360 / size_of_gap)):
		color = random_color()

		turtle_tha.color(color)
		turtle_tha.circle(100)
		turtle_tha.left(5)



turtle_tha 	= t.Turtle()

turtle_tha.speed("fastest")
t.colormode(255)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
