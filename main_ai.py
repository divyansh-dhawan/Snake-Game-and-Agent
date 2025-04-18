# main_ai.py

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from snake_ai import position_to_grid, a_star, grid_to_position
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# OPTIONAL: Debug visuals for A* path (if needed)
DEBUG_VISUALS = False
path_markers = []

def clear_path_markers():
    for marker in path_markers:
        marker.hideturtle()
    path_markers.clear()

def draw_path(path):
    clear_path_markers()
    for grid_x, grid_y in path:
        marker = Turtle()
        marker.shape("square")
        marker.color("gray")
        marker.shapesize(stretch_wid=0.5, stretch_len=0.5)
        marker.penup()
        x = grid_x * 20 - 300 + 10
        y = grid_y * 20 - 300 + 10
        marker.goto(x, y)
        path_markers.append(marker)

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)

    head = position_to_grid(snake.head.position())
    food_pos = position_to_grid(food.position())
    body = [position_to_grid(seg.position()) for seg in snake.segments[1:]]
    path = a_star(head, food_pos, set(body))

    # Optional path visualization
    if DEBUG_VISUALS:
        draw_path(path)

    # Move snake toward next step in path
    if path:
        # skip the first node if it's the current head
        if position_to_grid(snake.head.position()) == path[0]:
            next_move = path[1] if len(path) > 1 else path[0]
        else:
            next_move = path[0]
        head = position_to_grid(snake.head.position())
        next_x, next_y = next_move
        dx = next_x - head[0]
        dy = next_y - head[1]

        if dx == 1:
            snake.head.setheading(0)
        elif dx == -1:
            snake.head.setheading(180)
        elif dy == 1:
            snake.head.setheading(90)
        elif dy == -1:
            snake.head.setheading(270)

    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_up()
        snake.size_up()

    # Wall collision
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.game_over()
        game_is_on = False

    # Self collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

s.exitonclick()
