from turtle import *
# speed(0)
tracer(100, 0)
hideturtle()
penup()
pensize(0)
screen = Screen()
screen.colormode(255)

def square():
  for i in range(2):
    fd(1)
    right(90)
    fd(50)
    right(90)


for red in range(255):
  pencolor((red, 0, 0))
  fillcolor((red, 0, 0))
  begin_fill()
  square()
  end_fill()
  penup()
  fd(1)
  pendown()
  if red % 25 == 0:
    write(red)


# penup()
# goto(0,-50)
# pendown()

# for green in range(255):
#   pencolor((0,green,0))
#   fillcolor((0,green,0))
#   begin_fill()
#   square()
#   end_fill()
#   penup()
#   fd(1)
#   pendown()

#   penup()
# goto(0,-100)
# pendown()

# for blue in range(255):
#   pencolor((0,0,blue))
#   fillcolor((0,0,blue))
#   begin_fill()
#   square()
#   end_fill()
#   penup()
#   fd(1)
#   pendown()
done()