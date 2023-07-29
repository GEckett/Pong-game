from turtle import Turtle
UP = 90
DOWN = 270
STARTING_POSITIONS = [(350, 0), (-350, 0)]


class Paddle:
    """Models the Paddles that moves on screen"""

    def __init__(self):
        """Generates the paddles for both players"""
        self.paddles = []
        self.create_paddles()

    def reset(self):
        self.paddles[0].goto(STARTING_POSITIONS[0])
        self.paddles[1].goto(STARTING_POSITIONS[1])

    def create_paddles(self):
        for position in STARTING_POSITIONS:
            paddle = Turtle(shape="square")
            paddle.color("white")
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.penup()
            paddle.goto(position)
            self.paddles.append(paddle)

    def up_1(self):
        new_y_1 = self.paddles[0].ycor() + 40
        self.paddles[0].goto(350, new_y_1)

    def down_1(self):
        new_y_1 = self.paddles[0].ycor() - 40
        self.paddles[0].goto(350, new_y_1)

    def up_2(self):
        new_y_2 = self.paddles[1].ycor() + 40
        self.paddles[1].goto(-350, new_y_2)

    def down_2(self):
        new_y_2 = self.paddles[1].ycor() - 40
        self.paddles[1].goto(-350, new_y_2)

