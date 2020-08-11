from turtle import *
# speed(0)
tracer(10, 1)
hideturtle()
screen = Screen()
screen.colormode(255)
screen.setup(1200,800)
penup()
goto(-2000,750)
pendown()
def draw_square(length, color=(0, 0, 0)):
  fillcolor(color)
  begin_fill()
  for i in range(4):
    fd(length)
    right(90)
  end_fill()


def draw_line(length, width, color=(133, 133, 133)):
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
x_shift_arr = [0, 10, 20]

x = 0
y = 0
penup()
goto((x, y))
pendown()


# START
for row in range(1, 14):
  # 方塊
  for i in range(0, 14, 2):
    draw_square(edge,)
    penup()
    goto((edge*i+x, y))
    pendown()
    draw_square(edge,)

  # 座標下移
  x = 0
  y = ycor()-edge
  penup()
  goto((x, y))
  pendown()

  #線
  draw_line(edge*14, width,)

  # 座標下移
  x = x_shift_arr[row % 3]
  y = ycor()-width
  penup()
  goto((x, y))
  pendown()

penup()
goto((0, 0))
pendown()
pensize(2)
pencolor(133, 133, 133)
for i in range(2):
  fd(edge*14)
  right(90)
  fd(edge*13+2*13)
  right(90)
done()
