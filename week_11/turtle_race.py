import turtle
import random


START_X = -350
FINISH_X = 350
LANES = [150, 50, -50, -150]
COLORS = ["red", "blue", "green", "purple"]


def create_turtles():
    racers = []

    for color, lane in zip(COLORS, LANES):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.goto(START_X, lane)
        racers.append(racer)

    return racers


def draw_finish_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.penup()
    line.goto(FINISH_X, -200)
    line.pendown()
    line.goto(FINISH_X, 200)


def race(racers):
    winner = None

    while winner is None:
        for racer in racers:
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= FINISH_X:
                winner = racer
                break

    print(f"The {winner.pencolor()} turtle wins!")


screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=800, height=500)

draw_finish_line()
racers = create_turtles()
race(racers)

screen.mainloop()
