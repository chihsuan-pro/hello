from turtle import *
import math
hideturtle()
speed(0)
# tracer(100,10)


def gen_circle_point(step, angle, radius, start_angle=0, x_start=0, y_start=0):
  # 從圓心的右側以逆時針方向畫圓
  # step 將圓切等份點
  # radius 圓的半徑
  # x_start 圓心x座標的起始位置
  theta = start_angle
  circle_list = []
  step_angle = 2*angle/step
  for i in range(step):
    circle_list.append(
        (
            x_start + radius*math.cos(theta),
            y_start + radius*math.sin(theta)
        ))
    theta += step_angle
  # 補回最後一個才可以繞回來
  circle_list.append(circle_list[0])
  penup()
  goto(circle_list[0])
  pendown()
  for x, y in circle_list:
    goto(x, y)
    pendown()
  penup()
  return circle_list


def gen_circle_point2(step, angle, radius, start_angle=0, x_start=0, y_start=0):
  # 從圓心的右側以逆時針方向畫圓
  # step 將圓切等份點
  # radius 圓的半徑
  # x_start 圓心x座標的起始位置
  theta = start_angle
  circle_list = []
  step_angle = 2*angle/step
  for i in range(step):
    circle_list.append(
        (
            x_start + radius*math.cos(theta),
            y_start + radius*math.sin(theta)
        ))
    theta += step_angle

  for x, y in circle_list:
    goto(x, y)
    pendown()
  return circle_list


gen_circle_point(step=60, angle=math.pi, radius=100,)
# print(circle1)
# gen_circle_point2(step = 60,angle = math.pi/2,start_angle = math.radians(90),radius = 50,x_start=0,y_start=0)

colorlist = ['black', 'white']
for i in range(20):
  penup()
  goto(0, 0)
  pendown()
  seth(18*i)
  circle(50, 180)


# left(18)
# gen_circle_point(step = 60,angle = math.pi/2,radius = 50,x_start=50,y_start=0)

def draw_heart_line():
  for point in range(len(circle1)):
    penup()
    goto(circle1[point])
    pendown()
    goto(circle1[point*2 % len(circle1)])


def gen_circle_point2(step, angle, radius, x_start=0, y_start=0):
  # step 將圓切等份點
  # radius 圓的半徑
  # x_start 圓心x座標的起始位置
  theta = 0
  circle_list = []
  step_angle = 2*angle/step
  for i in range(step):
    circle_list.append(
        (
            x_start + radius*math.cos(theta),
            y_start + radius*math.sin(theta)
        ))
    theta += step_angle
  # 補回最後一個才可以繞回來

  penup()
  goto(circle_list[0])
  pendown()
  for x, y in circle_list:
    goto(x, y)
    pendown()
  return circle_list

# circle2 = gen_circle_point2(step = 60,angle = math.pi,radius = 100)
done()