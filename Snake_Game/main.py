import time
from turtle import Screen
from score_board import Score
from snake import  Snake
from food import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
scoreboard = Score()
food = Food()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

segments = []
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_the_snake()
    #detect collision of food and snake
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()
