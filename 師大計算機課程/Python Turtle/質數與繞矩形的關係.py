from turtle import *
speed(0)
# hideturtle()
align_dict = {90: 'left', 180: 'center', 270: 'right', 0: 'right'}
seth(0)
sum = 1
for length in range(1, 10):
  for first_seg in range(length):
    write(sum, align=align_dict[heading()], font=("Arial", 12, "normal"))
    fd(50)
    sum += 1

  left(90)

  for second_seg in range(length):
    write(sum, align=align_dict[heading()], font=("Arial", 12, "normal"))
    fd(50)
    sum += 1
  left(90)
done()