from turtle import Turtle, Screen
screen = Screen()
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

position = [(0.00, 0.00), (-20.0, 0.00), (-40.00, 0.00)]
x = -40.00
y = 0.00


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        self.add_snake(position[0], 'yellow')
        for i in position[1::]:
            self.add_snake(i, 'red')

    def add_snake(self, i, colour):
        tim = Turtle(shape='circle')
        tim.speed(0)
        tim.color(colour)
        tim.penup()
        tim.goto(i)
        self.snake.append(tim)

    def extend_snake(self):
        self.add_snake(self.snake[-1].position(), 'red')

    def move(self):

        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
