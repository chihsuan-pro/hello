from turtle import *
# speed(9)
tracer(8, 10)


def f(length, depth):
  if depth == 1:
    forward(length)
    left(30)
    forward(length)
    backward(length)
    right(30)
    right(30)
    forward(length)
    backward(length)
    left(30)
    backward(length)
  else:
    forward(length)
    left(30)
    f(length*.75, depth-1)
    right(30)
    right(30)
    f(length*.75, depth-1)
    left(30)
    backward(length)


left(90)
f(100, 5)
# for i in range(5):
#   f(600,3)
#   left(72)


# left(90)
# fd(100)

# left(45)
# fd(50)
# fd(-50)
# right(90)
# fd(50)
done()