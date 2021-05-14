import time
from snake import Snake
from turtle import Screen
from scoreboard import Score
from food import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)

score = Score()

snake = Snake()

food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

switch = False
while not switch:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

    # Detect collision of snake head with other parts fo the snake
    for i in snake.snake:
        if i == snake.head:
            pass
        elif snake.head.distance(i.position()) < 5:
            switch = True
            score.game_over()

    # Detect collision with wall
    if snake.head.xcor() > 280.00 or snake.head.xcor() < - 280.00 or snake.head.ycor() > 280.00 or snake.head.ycor() < -280.00:
        switch = True
        score.game_over()
screen.exitonclick()
