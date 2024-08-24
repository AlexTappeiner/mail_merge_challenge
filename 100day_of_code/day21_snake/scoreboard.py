from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)  # Position the scoreboard at the top center of the screen
        self.write_score()

    def write_score(self):
        self.clear()  # Clear previous text if any
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 12, "normal"),
        )

    def increase_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 12, "normal"))
