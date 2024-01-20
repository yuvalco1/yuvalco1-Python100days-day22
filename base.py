import time
from turtle import Turtle, Screen
MOVE_DISTANCE = 30
class Base(Turtle):

    def __init__(self, Xposition):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(Xposition, 0)



    def up(self):
        xpos = self.xcor()
        ypos = self.ycor() + MOVE_DISTANCE
        self.goto(xpos, ypos)

    def down(self):
        xpos = self.xcor()
        ypos = self.ycor() - MOVE_DISTANCE
        self.goto(xpos, ypos)







