from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.player1_score = 0
        self.player2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(150, 200)
        self.write(f"{self.player1_score}", align="right", font=("courier", 70, "normal"))
        self.goto(-150, 200)
        self.write(f"{self.player2_score}", align="right", font=("courier", 70, "normal"))

    def player1(self):
        self.player1_score += 1
        self.clear()
        self.update_scoreboard()

    def player2(self):
        self.player2_score += 1
        self.clear()
        self.update_scoreboard()
