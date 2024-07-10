from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("My Pong game")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_Paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()





screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_Paddle.go_up, "w")
screen.onkey(l_Paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#detecting bounceing
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#deteting collistion with x direction
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_Paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
#detect missin ball
    if ball.xcor() > 380:
        ball.reset_poistion()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_poistion()
        scoreboard.r_point()



screen.exitonclick()
