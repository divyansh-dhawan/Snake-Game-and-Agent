# step-1 create a snake body
# step-2 move the snake
# step-3 control the snake
# step-4 detect collision with food
# step-5 create a scoreboard
# step-6 detect collision with wall
# step-7 detect collision with tail

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkeypress(snake.up, "Up")
s.onkeypress(snake.down, "Down")
s.onkeypress(snake.left, "Left")
s.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_up()
        snake.size_up()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

s.exitonclick()
