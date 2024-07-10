FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scorboard()

    def update_scorboard(self):
        self.clear()
        self.goto(200, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_scorboard()

    def game_over(self):
        self.color("black")
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over: {self.score}", align="center", font=FONT)
