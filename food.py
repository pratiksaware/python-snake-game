from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x_axis = random.randint(-280, 280)
        random_y_axis = random.randint(-280, 280)
        self.goto(random_x_axis, random_y_axis)


