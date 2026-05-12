from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    """"detect collision with food"""
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        score.increase_score()

    """Detect collision with wall"""
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    """Detect collision with tail"""
    for segment in snake.segments[1:]:
        """using a slice list [1:] allows to reduce the code."""
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

    """if head collides with any segment in the tail: trigger game over"""

screen.exitonclick()