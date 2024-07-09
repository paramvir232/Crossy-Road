import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, 'Up')


def restart_game():
    """Restarts the game"""
    user_input = screen.textinput(title="GAME OVER", prompt="Do you want to restart the game ?")
    screen.listen()
    if user_input.lower() == 'y':
        car_manager.max_chances = 4
        player.reset_player()
        car_manager.reset_speed()
        scoreboard.reset_scoreboard()
        return True


def collision_detection():
    """Detects collion with car and end the game"""
    global game_is_on
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            game_is_on = restart_game()


def increase_traffic():
    """Increases number of cars with increasing levels"""
    if scoreboard.level > 3:
        car_manager.max_chances = 3
    elif scoreboard.level > 5:
        car_manager.max_chances = 2
    elif scoreboard.level > 7:
        car_manager.max_chances = 1


def level_completed():
    """ Level completed mechanism"""
    if player.ycor() > 280:
        player.reset_player()
        scoreboard.increase_level()
        car_manager.increase_speed()
        increase_traffic()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()

    # Collision with Cars
    collision_detection()

    # Updates level
    level_completed()

screen.exitonclick()
