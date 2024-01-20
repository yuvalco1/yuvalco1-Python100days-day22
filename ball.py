import time
from turtle import Turtle, Screen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.setheading(45)  # 45 degrees



    def move(self):
        self.penup()
        if self.ycor() >= 490 or self.ycor() <= -490:
            self.setheading(-self.heading())
        self.forward(10)
        self.pendown()

    def set_heading(self, heading):
        self.setheading(heading)









