

# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
#
# def move_counter():
#     tim.circle(10)
#
# def move_right():
#     tim.right(90)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_counter)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear)



#turtule race
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-100,-50,0,50,100]
all_turtle = []


for turtle_lis in range (5):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_lis])
    new_turtle.goto(-230, y_positions[turtle_lis])
    all_turtle.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
     for turtle in all_turtle:
         if turtle.xcor() > 230:
             is_race_on = False
             winning_color = turtle.pencolor()
             if winning_color == user_bet:
                print(f"you won with {winning_color}")
             else:
                print(f"you lost the winning color {winning_color}")

         random_distance = random.randint(0,10)
         turtle.forward(random_distance)






screen.exitonclick()