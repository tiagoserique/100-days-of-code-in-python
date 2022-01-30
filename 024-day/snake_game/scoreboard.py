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
		self.goto(0, 260)

		self.score = 0
		self.read_high_score()
		self.update_scoreboard()


	def increse_score(self):
		self.score += 1
		self.update_scoreboard()


	def reset(self):
		if ( self.score > self.high_score ):
			self.high_score = self.score
			self.write_high_score()

		self.score = 0
		self.update_scoreboard()


	def read_high_score(self):
		with open("data.txt", "r") as file:
			self.high_score = int(file.read())


	def write_high_score(self):
		with open("data.txt", "w") as file:
			file.write(f"{self.score}")


	def update_scoreboard(self):
		self.clear()
		text_score = f"Score: {self.score} High Score: {self.high_score}"
		self.write(arg=text_score, align=ALINGMENT, font=FONT)