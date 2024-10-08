from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}")

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over : {self.score}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
