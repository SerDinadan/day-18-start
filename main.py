from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")


# Shape properties
def draw_shapes(start_sides, end_sides):
    for sides in range(start_sides, end_sides + 1):
        number_of_sides = sides
        angle = 360 / number_of_sides
        # Randomize color
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        tim.color(r, g, b)
        for side in range(sides):
            tim.right(angle)
            tim.forward(100)


screen = Screen()
screen.colormode(255)
draw_shapes(3, 10)
screen.exitonclick()
