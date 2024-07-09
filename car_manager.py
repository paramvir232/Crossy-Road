from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.moving_speed = STARTING_MOVE_DISTANCE
        self.max_chances = 4

    def reset_chances(self):
        self.max_chances = 4

    def generate_car(self):
        """Generates car traffic"""
        chances = random.randint(1, self.max_chances)
        if chances == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-230, 250))
            self.car_list.append(new_car)

    def reset_speed(self):
        """Reset car moving speed"""
        self.moving_speed = STARTING_MOVE_DISTANCE

    def move(self):
        """Moves cars"""
        for car in self.car_list:
            car.backward(self.moving_speed)

    def increase_speed(self):
        """Increment car speed"""
        self.moving_speed += MOVE_INCREMENT
