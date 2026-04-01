import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

colors = ["red", "pink", "green", "blue", "black", "purple"]
y_positions = [-80, -40, 0, 40, 80, 120]

all_turtles = []

# Create turtles FIRST
for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230, y_positions[i])
    all_turtles.append(t)

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Enter the color you bet on: "
)

is_race_on = bool(user_bet)

# Start race
while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You won! The winner is {winning_color}")
            else:
                print(f"You lost! The winner is {winning_color}")

screen.exitonclick()
