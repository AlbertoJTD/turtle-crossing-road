from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", 'pink', 'black', 'brown', 'salmon', 'turquoise', 'SlateBlue', 'YellowGreen', 'snow4']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color(random.choice(COLORS))
        self.goto()

    def reset_position(self):
        pass

