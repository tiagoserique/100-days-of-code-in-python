from turtle import Turtle


MOVE_DISTANCE = 20

UP 		= 90
DOWN 	= 270


class Paddle(Turtle):
	def __init__(self, start_position):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(start_position)


	def go_up(self):
		new_y = self.ycor() + MOVE_DISTANCE
		self.goto(self.xcor(), new_y)


	def go_down(self):
		new_y = self.ycor() - MOVE_DISTANCE
		self.goto(self.xcor(), new_y)