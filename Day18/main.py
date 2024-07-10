import turtle
from turtle import Turtle, Screen
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
turtle.colormode(255)
# timmy_the_turtle.color("red")

#for making square line
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

#for making broken line
# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

list_of_color = [
  "Red",
  "Green",
  "Blue",
  "Yellow",
  "Cyan",
  "Magenta",
  "Black",

  "Gray",
  "Orange"
]
timmy_the_turtle.speed("fastest")
def draw_shap(no_of_degree):
    angle = 360/no_of_degree
    for _ in range(no_of_degree):
        timmy_the_turtle.circle(100)
        timmy_the_turtle.right(angle)


for l in range(3,15):
    timmy_the_turtle.color(random.choice(list_of_color))
    draw_shap(l)

# this for Random walk

# directions = [360]
# timmy_the_turtle.pensize(15)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color= (r , g, b)
#     return random_color
#
# for _ in range(100):
#   timmy_the_turtle.forward(30)
#   timmy_the_turtle.color(random_color())
#   timmy_the_turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
