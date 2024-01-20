import time
from turtle import Turtle, Screen
from Scoreboard import Score
from ball import Ball
from base import Base

if __name__ == '__main__':
    # build the screen
    screen = Screen()
    screen.setup(width=1400, height=1000)
    screen.bgcolor("black")
    screen.title("Yuval's Pong game")
    screen.tracer(0)


# build the score
    scoreL = 0
    scoreR = 0
    score = Score()
    score.score_write(scoreL, scoreR)

# build the bases
    baseL = Base(-650)
    baseR = Base(650)
    screen.update()
    screen.listen()
    screen.onkeypress(key="Up", fun=baseR.up)
    screen.onkeypress(key="Down", fun=baseR.down)
    screen.onkeypress(key="w", fun=baseL.up)
    screen.onkeypress(key="s", fun=baseL.down)


# build the ball
    ball = Ball()


# game loop

    game_is_on = True
    while game_is_on:
        ball.move()
        if (ball.distance(baseR) < 50 and ball.xcor() > 625):
            ball.set_heading(180-ball.heading())
            score.update_score("R")
        if (ball.distance(baseL) < 50 and ball.xcor() < -625):
            ball.set_heading(180-ball.heading())
            score.update_score("L")
        if ball.xcor() > 700 or ball.xcor() < -700:
            score.game_over()
            game_is_on = False
        time.sleep(0.1)
        screen.update()


    screen.exitonclick()
