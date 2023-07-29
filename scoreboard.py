from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 40, 'normal')
SCORE_COORDINATES = (0, 230)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.generate_scoreboard()

    def centre_line(self):
        """Draws the centre line of the Pong court."""
        self.shape("square")
        self.shapesize(0.5)
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        for _ in range(0, 25):
            self.stamp()
            self.forward(25)

    def generate_scoreboard(self):
        self.penup()
        self.goto(SCORE_COORDINATES)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_1}  {self.score_2}", False, align=ALIGNMENT, font=FONT)
        self.centre_line()

    def up_score_1(self):
        self.score_1 += 1
        self.clear()
        self.generate_scoreboard()

    def up_score_2(self):
        self.score_2 += 1
        self.clear()
        self.generate_scoreboard()

