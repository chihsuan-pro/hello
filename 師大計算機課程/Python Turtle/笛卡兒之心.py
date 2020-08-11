from turtle import *
import math
hideturtle()
speed(0)
# tracer(100,10)


def gen_circle_point(step, angle, radius, x_start=0, y_start=0):
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
  circle_list.append(circle_list[0])
  penup()
  goto(circle_list[0])
  pendown()
  for x, y in circle_list:
    goto(x, y)
    pendown()
  return circle_list


circle1 = gen_circle_point(step=60, angle=math.pi, radius=100,)



def draw_heart_line():
  for point in range(len(circle1)):
    penup()
    goto(circle1[point])
    pendown()
    goto(circle1[point*2 % len(circle1)])



draw_heart_line()

done()