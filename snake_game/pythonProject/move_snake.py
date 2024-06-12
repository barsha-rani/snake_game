from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.listen()
timmy = Turtle("turtle")
timmy.color("white")


def up():
    timmy.setheading(0)
    timmy.left(90)
    timmy.forward(20)


def down():
    timmy.setheading(0)
    timmy.left(270)
    timmy.forward(20)


screen.onkey(up, "Up")
screen.onkey(down, "Down")
# screen.onkey(left, "Left")
# screen.onkey(right, "Right")

screen.exitonclick()
