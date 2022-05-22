from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Pick: ")
print(user_bet)
colors = ['red','blue','green','yellow','pink','black']
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_pos[i])
    all_turtles.append(new_turtle)
if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"Congrats!, {winner_turtle} has won!")
            else:
                print("Sorry, you lost!")
        number = random.randint(0,10)
        turtle.forward(number)

screen.exitonclick()