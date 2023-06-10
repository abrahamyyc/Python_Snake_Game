from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file_in:
            self.high_score = int(file_in.read())
        self.hideturtle()
        self.penup()
        self.color("green")
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Current Score: {self.score}\t"
                   f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file_out:
                file_out.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over!", align=ALIGNMENT, font=(FONT))
