import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.onkey(player.move_up, "Up")
car_manager = CarManager()
score = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    car_manager.create_car()
    car_manager.move()

    screen.update()
    #successfull crossing
    if player.ycor() > 280:
        player.reset_player()
        score.point()
        car_manager.increase_speed_of_car()
    # detect game over
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()





screen.exitonclick()