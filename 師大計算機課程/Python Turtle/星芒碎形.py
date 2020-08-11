from turtle import *
# speed(0)
tracer(8, 10)


def f(t, length, depth):
  if depth == 0:
    t.forward(length)
    return
  else:
    f(t, length/3, depth-1)
    t.left(60)
    f(t, length/3, depth-1)
    t. right(120)
    f(t, length/3, depth-1)
    t.left(60)
    f(t, length/3, depth-1)


koch = Turtle()
koch.color('red')
for k in range(3):
  for i in range(3):
    f(koch, 120, 2)
    koch.left(120)
  koch.left(120)
done()