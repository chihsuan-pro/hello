
from turtle import *
import math
hideturtle()
speed(0)
screen = Screen()
screen.colormode(255)

def iter_draw(edge_length=300, edge_count=4, iter_times=5, theta=10):
  def polygon(edge_length, edge_count):
    #功能：畫正多邊形
    #edge_length：邊長
    #edge_count：『幾』邊形
    for i in range(edge_count):
      fd(edge_length)
      left(360/edge_count)

  def convert(edge_length, edge_count, theta):
    #功能：求得下一圖形的邊長與畫圖的起始點
    #利用edge_count換算內角
    exterior_angle = 360 / edge_count
    interior_angle = 180 - exterior_angle
    beta = 180 - interior_angle - theta
    # 利用正弦定理求下一個圖的起始點
    b = edge_length*(math.sin(math.radians(theta))) / \
        (math.sin(math.radians(theta))+math.sin(math.radians(beta)))  # 邊長b
    a = edge_length-b  # 邊長a
    # 利用餘弦定理求下一個圖的長度
    # next_edge = math.sqrt(a**2+b**2-2*a*b*math.cos
    # (math.radians(interior_angle)))
    next_edge = b*(math.sin(math.radians(interior_angle)) /
                   math.sin(math.radians(theta)))
    return a, b, next_edge

  for i in range(iter_times):
    if i % 2 == 1:
      fill_color = "white"
    else:
      fill_color = "black"
    color(fill_color)
    begin_fill()
    polygon(edge_length, edge_count)
    end_fill()
    a, b, next_edge = convert(edge_length, edge_count, theta)

    # 走到新的畫圖起始點
    fd(b)
    # 指定下一個圖的長度
    edge_length = next_edge
    ### 轉向下一個角度繼續畫圖
    left(theta)


iter_draw(
    edge_length=300,  # 邊長長度
    edge_count=4,  # 邊長數
    iter_times=19,  # 圖形數量
    theta=5  # 圖形旋轉角度
)
done()