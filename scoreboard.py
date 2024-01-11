from turtle import Turtle
alignment = "center"
font = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

        try:
            with open("data.txt", "r") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            # If the file doesn't exist, create it with initial high score 0
            with open("data.txt", "w") as data:
                data.write("0")

        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=alignment, font=font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def score_add(self):
        self.score += 1
        self.update_score()
