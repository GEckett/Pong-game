from turtle import Turtle
import random
SERVE = [45, 135, 225, 315]

class Ball:
    """Models the Pong Ball."""

    def __init__(self):
        self.the_ball = []
        self.create_ball()
        self.the_ball[0].setheading(45)
        self.speed = 0.1

    def reset(self):
        self.the_ball[0].goto(0, 0)
        self.the_ball[0].setheading(random.choice(SERVE))
        self.move()
        self.speed = 0.1

    def create_ball(self):
        ball = Turtle(shape="circle")
        ball.color("white")
        ball.shapesize(stretch_wid=1, stretch_len=1)
        ball.penup()
        ball.goto(0, 0)
        self.the_ball.append(ball)

    def move(self):
        self.the_ball[0].forward(20)

    def bounce_top_r(self):
        self.the_ball[0].setheading(315)

    def bounce_top_l(self):
        self.the_ball[0].setheading(225)

    def bounce_rw(self):
        self.the_ball[0].setheading(225)

    def bounce_bot_l(self):
        self.the_ball[0].setheading(135)

    def bounce_bot_r(self):
        self.the_ball[0].setheading(45)

    def bounce_lw(self):
        self.the_ball[0].setheading(45)
