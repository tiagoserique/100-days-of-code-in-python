import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard 	= Scoreboard()
player 		= Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on  = True
while ( game_is_on ):
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move()


    for car in car_manager.all_cars:
        if ( car.distance(player) < 20 ):
            scoreboard.game_over()
            game_is_on = False


    if ( player.is_at_finish_line() ):
        scoreboard.increase_level()
        car_manager.increse_speed()
        player.reset_position()

    car_manager.reset_cars()


screen.exitonclick()