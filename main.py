from turtle import Turtle, Screen
import time
from Snacke import Snake
from food import Food
from score import Score

BOUNDERY = 285

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()


score = Score()

food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_running = True
score.display_score()
while is_running:

    screen.update()
    time.sleep(0.1)
    snake.move()
    if food.distance(snake.head) < 15:
        score.clear()
        score.increce_score()
        score.display_score()
        snake.eat()
        food.refresh()

    if snake.head.xcor() <= -BOUNDERY or snake.head.xcor() >= BOUNDERY or snake.head.ycor() <= -BOUNDERY or snake.head.ycor() >= BOUNDERY:
        score.reset()
        snake.reset()

    for s in snake.snakes[1:]:
        if snake.head.distance(s) < 8:
            score.reset()
            snake.reset()










screen.exitonclick()