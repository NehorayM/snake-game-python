from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.update_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} highest score : {self.high_score}", align=ALIGNMENT, font=("Arial", 15, "normal"))

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.get_high_score()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt",mode = "w") as file_high_score:
            converted_num = str(self.high_score)
            file_high_score.write(converted_num)

    def update_high_score(self):
        with open("data.txt",mode = "r") as high_score:
            high_score_int = int(high_score.read())
            self.high_score = high_score_int
