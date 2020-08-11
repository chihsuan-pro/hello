from turtle import *
speed(0)
hideturtle()

step = 10
dot_size = 1
dot_amount = 20

# 產生X軸的點 (1,0)...(10,0)
pos_x_arr = [(x*step, 0) for x in range(1, dot_amount+1)]
# 產生Y軸的點 (0,1)...(0,10)
pos_y_arr = [(0, y*step) for y in range(1, dot_amount+1)]
# 產生-X軸的點 (1,0)...(10,0)
neg_x_arr = [(-x*step, 0) for x in range(1, dot_amount+1)]
# 產生-Y軸的點 (0,1)...(0,10)
neg_y_arr = [(0, -y*step) for y in range(1, dot_amount+1)]

goto(0, 0)
dot(dot_size)

# 純打點
# for i in range(10):
#   penup()
#   goto(x_arr[i][0],x_arr[i][1])
#   pendown()
#   dot(dot_size)
# for i in range(10):
#   penup()
#   goto(y_arr[i][0],y_arr[i][1])
#   pendown()
#   dot(dot_size)

for i in range(dot_amount):
  penup()
  goto(pos_x_arr[i][0], pos_x_arr[i][1])
  pendown()
  dot(dot_size)
  goto(pos_y_arr[dot_amount-i-1][0], pos_y_arr[dot_amount-i-1][1])
  dot(dot_size)
for i in range(dot_amount):
  penup()
  goto(pos_x_arr[i][0], pos_x_arr[i][1])
  pendown()
  dot(dot_size)
  goto(neg_y_arr[dot_amount-i-1][0], neg_y_arr[dot_amount-i-1][1])
  dot(dot_size)
for i in range(dot_amount):
  penup()
  goto(neg_y_arr[i][0], neg_y_arr[i][1])
  pendown()
  dot(dot_size)
  goto(neg_x_arr[dot_amount-i-1][0], neg_x_arr[dot_amount-i-1][1])
  dot(dot_size)
for i in range(dot_amount):
  penup()
  goto(neg_x_arr[i][0], neg_x_arr[i][1])
  pendown()
  dot(dot_size)
  goto(pos_y_arr[dot_amount-i-1][0], pos_y_arr[dot_amount-i-1][1])
  dot(dot_size)
done()