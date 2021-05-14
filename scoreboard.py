from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = -1
        self.setpos(0.00, 270.00)
        self.color('white')
        self.hideturtle()
        self.update_score()
        self.increase_score()

    def update_score(self):
        self.write(f'Score : {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0.00, 0.00)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
