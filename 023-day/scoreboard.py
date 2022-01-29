from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("black")
		self.penup()
		self.hideturtle()
		self.goto(-280, 250)
		self.level = 1
		self.update_scoreboard()


	def increase_level(self):
		self.level += 1
		self.update_scoreboard()


	def update_scoreboard(self):
		self.clear()
		text = f"Level: {self.level}"
		self.write(arg=text, align="left", font=FONT)


	def game_over(self):
		text = "GAME OVER"
		self.goto(0, 0)
		self.write(arg=text, align="center", font=FONT)