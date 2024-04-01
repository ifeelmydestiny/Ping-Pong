from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game🏓🏓🏓")
screen.tracer(1)

paddle_r = Paddle()
paddle_l = Paddle()
paddle_r.goto(380, 0)
paddle_l.goto(-380, 0)

y = 0
y_ = 0


def mid():
    paddle.penup()
    paddle.color("white")
    paddle.shape("square")
    paddle.shapesize(stretch_wid=0.3, stretch_len=0.1)
    paddle.speed("fastest")


line = True
while line:
    paddle = Paddle()
    mid()
    if y < 300:
        y += 30
        paddle.goto(0, y)
    else:
        line = False
        game = True
        while game:
            paddle = Paddle()
            mid()

            if y_ > -300:
                y_ -= 30
                paddle.goto(0, y_)
            else:
                game = False
                line = False

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

ball = Ball()
score = Scoreboard()

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -290:
        ball.bounce()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 370 or ball.distance(paddle_l) < 50 and ball.ycor() > -370:
        # ball.ball_speed += 1
        # ball.speed(ball.ball_speed)
        ball.go_opp()
    if ball.xcor() > 400:
        score.player2()
        ball.reset_position()
    if ball.xcor() < -400:
        score.player1()
        ball.reset_position()


screen.exitonclick()
