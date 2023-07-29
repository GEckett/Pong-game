from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
score_board = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(paddle.up_1, "Up")
screen.onkey(paddle.down_1, "Down")
screen.onkey(paddle.up_2, "w")
screen.onkey(paddle.down_2, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.speed)
    if ball.the_ball[0].ycor() >= 295 and ball.the_ball[0].heading() == 45:
        ball.bounce_top_r()
    elif ball.the_ball[0].ycor() >= 295 and ball.the_ball[0].heading() == 135:
        ball.bounce_top_l()
    elif ball.the_ball[0].distance(paddle.paddles[0]) < 70 and ball.the_ball[0].xcor() > 340:
        if ball.speed < 0:
            ball.speed -= 0.1
            ball.the_ball[0].setheading((ball.the_ball[0].heading() + 90))
        else:
            ball.the_ball[0].setheading((ball.the_ball[0].heading() + 90))
    elif ball.the_ball[0].distance(paddle.paddles[1]) < 70 and ball.the_ball[0].xcor() < -340:
        if ball.speed < 0:
            ball.speed -= 0.1
            ball.the_ball[0].setheading((ball.the_ball[0].heading() + 90))
        else:
            ball.the_ball[0].setheading((ball.the_ball[0].heading() + 90))
    elif ball.the_ball[0].xcor() >= 390:
        score_board.up_score_1()
        ball.reset()
        paddle.reset()
    elif ball.the_ball[0].ycor() <= -295 and ball.the_ball[0].heading() == 225:
        ball.bounce_bot_l()
    elif ball.the_ball[0].ycor() <= -295 and ball.the_ball[0].heading() == 315:
        ball.bounce_bot_r()
    elif ball.the_ball[0].xcor() <= -390:
        score_board.up_score_2()
        ball.reset()
        paddle.reset()
    ball.move()

screen.exitonclick()
