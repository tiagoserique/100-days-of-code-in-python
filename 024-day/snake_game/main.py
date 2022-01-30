from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake 		= Snake()
food 		= Food()
scoreboard 	= Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while ( game_is_on ):
	screen.update()
	time.sleep(0.1)

	snake.move()

	# Detect collision with food.
	if ( snake.head.distance(food) < 15 ):
		food.refresh()
		snake.extend()
		scoreboard.increse_score()

	# Detect collision with wall.
	right_wall 	= snake.head.xcor() > 290
	left_wall 	= snake.head.xcor() < -290
	up_wall 	= snake.head.ycor() > 290
	down_wall 	= snake.head.ycor() < -290

	if ( right_wall ) or ( left_wall ) or ( up_wall ) or ( down_wall ):
		scoreboard.reset()
		snake.reset()

	for segment in snake.segments[1:]:
		if ( snake.head.distance(segment) < 10 ):
			scoreboard.reset()
			snake.reset()
