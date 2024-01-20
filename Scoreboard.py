from turtle import Turtle


def draw_middle_line():
    line = Turtle()
    line.penup()
    line.color("white")
    line.width(4)
    for y in range(500, -500, -20):
        line.goto(0, y)
        line.penup()
        line.goto(0, y - 10)
        line.pendown()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(x=0, y=420)
        self.SL = 0
        self.SR = 0
        self.score_write(self.SL, self.SR)
        draw_middle_line()

    def score_write(self, scoreL, scoreR):
        self.clear()
        self.write(f"{scoreL}     {scoreR}", False, align="center", font=('Arial', 40, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Arial', 20, 'normal'))

    def update_score(self, side):
        if side == "L":
            self.SL += 1
        else:
            self.SR += 1
        self.score_write(self.SL, self.SR)