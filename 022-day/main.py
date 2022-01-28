from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle 	= Paddle((-350, 0))
right_paddle 	= Paddle(( 350, 0))
ball			= Ball()
scoreboard		= Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on 	= True
while (game_is_on):
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	# Detect collision with wall
	if ( ball.ycor() > 280 ) or ( ball.ycor() < -280 ):
		ball.bounce_y()
	
	# Detect collision with paddle
	collision_r = ( ball.distance(right_paddle) < 50 ) and ( ball.xcor() > 320 )
	collision_l = ( ball.distance(left_paddle) < 50 ) and ( ball.xcor() < -320 )

	if ( collision_r ) or ( collision_l ):
		ball.bounce_x()

	# Detect R paddle misses
	if ( ball.xcor() > 380 ):
		ball.reset_position()
		scoreboard.l_point()

	# Detect L paddle misses
	if ( ball.xcor() < -380 ):
		ball.reset_position()
		scoreboard.r_point()


screen.exitonclick()