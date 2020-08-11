from turtle import *
import random
# speed(0)
tracer(50, 8)
hideturtle()
screen = Screen()
screen.colormode(255)

def random_color_dark():
  r, g, b = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))
  return r, g, b


def random_color_medium():
  r, g, b = (random.randint(85, 170), random.randint(85, 170), random.randint(85, 170))
  return r, g, b


def random_color_bright():
  r, g, b = (random.randint(170, 255), random.randint(170, 255), random.randint(170, 255))
  return r, g, b


def random_color():
  r, g, b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  return r, g, b


def draw_square(length, colors):
  print(colors)
  pencolor(colors)
  fillcolor(colors)
  begin_fill()
  for i in range(4):
    fd(length)
    right(90)
  end_fill()


def draw_line(length, width, color=(255, 255, 255)):
  fillcolor(color)
  penup()
  begin_fill()
  for i in range(2):
    fd(length)
    right(90)
    fd(width)
    right(90)
  end_fill()


step = 10
edge = 30
width = 2

x = 0
y = 0
penup()
goto((x, y))
pendown()


# START
for row in range(1, 3):
  # 方塊
  for i in range(0, 3, 1):
    draw_square(edge ,random_color())
    penup()
    goto((edge*i+3*i, y))
    pendown()
    # draw_square(edge,random_color())

  # 座標下移
  x = 0
  y = ycor()-edge
  penup()
  goto((x, y))
  pendown()

  #線
  draw_line(edge*14, width, (255, 255, 255))

  # 座標下移
  x = 0
  y = ycor()-width
  penup()
  goto((x, y))
  pendown()
done()
