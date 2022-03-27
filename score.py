from turtle import  Turtle

ALIMENT = "center"
FONT = ("Courier", 18, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.highScore = self.init_highScore()


    def init_highScore(self):
        with open("High_Score.txt", "w") as file:
            high_score= file.write("0")
        return high_score

    def increce_score(self):
        self.score += 1


    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("High_Score.txt", "w") as file:
                file.write(str(self.highScore))
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score:{self.highScore}", align=ALIMENT, font=FONT)




