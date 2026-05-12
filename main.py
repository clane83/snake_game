from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
import json

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

def save_game():
    game_data = {
        "score": score.score,
        "high_score": score.high_score,
        "snake_positions": [(segment.xcor(), segment.ycor()) for segment in snake.segments],
        "snake_heading": snake.head.heading(),
        "food_position": (food.xcor(), food.ycor())
    }

    with open("savegame.json", "w") as file:
        json.dump(game_data, file)


def load_game():
    try:
        with open("savegame.json", "r") as file:
            game_data = json.load(file)

        score.score = game_data["score"]
        score.high_score = game_data["high_score"]
        score.update_scoreboard()

        for segment in snake.segments:
            segment.goto(1000, 1000)

        snake.segments.clear()

        for position in game_data["snake_positions"]:
            snake.add_segment(position)

        snake.head = snake.segments[0]
        snake.head.setheading(game_data["snake_heading"])

        food.goto(game_data["food_position"])

    except FileNotFoundError:
        print("No saved game found.")

def restart_game():
    score.clear()
    score.score = 0
    score.update_scoreboard()

    snake.reset()
    food.refresh()

    global game_is_on
    game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="s", fun=save_game)
screen.onkey(key="l", fun=load_game)
screen.onkey(key="r", fun=restart_game)

game_is_on = True
while True:
    screen.update()
    time.sleep(0.1)

    if game_is_on:
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.game_over()
            game_is_on = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.game_over()
                game_is_on = False

    """if head collides with any segment in the tail: trigger game over"""

screen.exitonclick()