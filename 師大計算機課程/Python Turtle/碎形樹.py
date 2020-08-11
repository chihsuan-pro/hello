from turtle import *
# speed(5)
tracer(8, 10)


def f(length, depth):
  if depth == 0:
    fd(length)
    left(45)
    fd(length)
    fd(-length)
    right(45)
    right(45)
    fd(length)
    fd(-length)
    left(45)
    fd(-length)
  else:
    fd(length)
    left(45)
    # 左邊新的一枝
    f(length/2, depth-1)
    right(45)
    right(45)
    # 右邊新的一枝
    f(length/2, depth-1)
    left(45)
    fd(-length)


left(90)
for i in range(10):
  f(100, 0)
  left(36)
done()