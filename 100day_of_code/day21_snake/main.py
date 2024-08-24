from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if (
        snake.head.xcor() > 300
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -300
    ):
        score.reset()
        snake.reset()

    # Detect collision with tail
    # if head collides with any segment in the tail:
    # trigger Game over
    for segment in snake.segments_positions[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
