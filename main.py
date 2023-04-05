import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Object instances
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# player controls
screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.ycor() > 270:
        player.initial_position()
        car_manager.increase_speed()
        scoreboard.nex_level()

screen.exitonclick()
