from ctypes import alignment
from turtle import Turtle


ALINGMENT 	= "center"
FONT 		= ("Courier", 24, "normal")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.hideturtle()
		self.penup()
		self.goto(0, 270)

		self.score = 0
		self.update_scoreboard()


	def increse_score(self):
		self.clear()
		self.score += 1
		self.update_scoreboard()


	def game_over(self):
		text_score = "GAME OVER"
		self.goto(0, 0)
		self.write(arg=text_score, align=ALINGMENT, font=FONT)


	def update_scoreboard(self):
		text_score = f"Score: {self.score}"
		self.write(arg=text_score, align=ALINGMENT, font=FONT)