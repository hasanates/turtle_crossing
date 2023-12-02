from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from care_manager import Car
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
game_on = True

screen.listen()
screen.onkey(player.move_up, "w")

cars = []
while game_on:
    screen.update()
    if random.randint(0,20) == 5:
        car = Car()
        cars.append(car)
    for x in cars:
        x.move()
        if player.distance(x) < 20:
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.repostion()
        scoreboard.plus_level()

screen.exitonclick()
