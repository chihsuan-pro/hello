from turtle import *
import math
speed(0)
hideturtle()
screen = Screen()

x_turtle = Turtle()
x_turtle.hideturtle()
x_turtle.pencolor('red')
y_turtle = Turtle()
y_turtle.hideturtle()
y_turtle.pencolor('green')


radius = 100


def circle_dot():
  x_pre, y_pre = 0, 0
  for theta in range(0, 361, int(360/60)):
    x = radius * math.cos(math.radians(theta))
    y = radius * math.sin(math.radians(theta))

    penup()
    x_turtle.penup()
    y_turtle.penup()

    goto(x, y)
    x_turtle.goto(x, 0)
    y_turtle.goto(0, y)

    pendown()
    x_turtle.pendown()
    y_turtle.pendown()

    dot(3)
    x_turtle.dot(3)
    y_turtle.dot(3)

    clear()
    x_turtle.clear()
    y_turtle.clear()


# run = True
# while(run):
circle_dot()

# screen.onkey(circle_dot, "Up")
# screen.listen()
# screen.ontimer(circle_dot, 1)
done()