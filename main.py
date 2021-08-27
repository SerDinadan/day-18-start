from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")


def change_color():
    screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)


# Shape properties
def draw_shapes(start_sides, end_sides):
    for sides in range(start_sides, end_sides + 1):
        number_of_sides = sides
        angle = 360 / number_of_sides
        # Randomize color
        change_color()
        for side in range(sides):
            tim.right(angle)
            tim.forward(100)


def random_walk(number_of_times):
    for i in range(number_of_times):
        change_color()
        angle = [90, 180, 270, 360]
        tim.right(random.choice(angle))
        tim.forward(15)


screen = Screen()
tim.width(5)
tim.speed(10)
# random_walk(50)
heading = 0
for i in range(24):
    change_color()
    tim.setheading(heading)
    tim.circle(70, 360)
    heading += 15


screen.exitonclick()
