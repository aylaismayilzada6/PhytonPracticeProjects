from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(-250, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
