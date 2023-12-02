from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def plus_level(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-250, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f" Game Over", align="center", font=FONT)