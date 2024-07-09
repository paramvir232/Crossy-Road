from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update levels"""
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level : {self.level}", align='center', font=FONT)
        # self.goto(-)

    def increase_level(self):
        """Increases levels"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display Game Over text"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)

    def reset_scoreboard(self):
        """Reset scoreboard to initial"""
        self.level = 1
        self.update_scoreboard()
