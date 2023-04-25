import turtle
from sun import Sun

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(1400, 900)
    screen.bgcolor("black")
    screen.tracer(0)

    sun = Sun("yellow", (0, 0))

    while True:
        screen.update()

