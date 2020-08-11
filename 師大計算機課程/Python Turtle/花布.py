#創作理念:設計理念：以花園作為雛形的最初構想，在黑底白線條的基礎下希望做出華麗但低調的感覺，想要做出能夠成為亮點的花布。
#設計團隊:北一女中10631227 黃鈺婷 2018/06/20
#創作版本:1.0
#授權方式:姓名標示─非商業性─相同方式分享


from turtle import*
from random import randint
tracer(60)
speed(0)
xz = -200
yz = 200
h1 = 40
penup()
goto(xz, yz+h1*(2**0.5)/2)
pendown()
begin_fill()
color(33, 32, 30)
for i in range(4):
  forward(h1*(2**0.5)*10)
  right(90)
end_fill()


def Huang(h):
  for i in range(2):
    forward(h)
    left(90)
    forward(h)
    left(90)


def Yu(u):
  for i in range(2):
    forward(u)
    left(120)
    forward(u)
    left(60)


def Ting(t):
  forward(t)
  left(90)
  forward(3**0.5*t)
  left(120)
  forward(3**0.5*t)
  left(90)
  forward(t)
  left(60)


#first layer
xa = -200
ya = 200

pencolor(229, 219, 200)
pensize(2)

penup()
goto(xa, ya)
pendown()

h = 40

right(90/2)
for j in range(10):
  for i in range(10):
    penup()
    x1 = xa+(2*1/2**0.5*h)*i
    y1 = ya-(2*1/2**0.5*h)*j
    goto(x1, y1)
    pendown()

    Huang(h)


#second layer
xb = xa-h*(2**0.5)*0.1
yb = ya

penup()
goto(xb, yb)
pendown()

right(15)
u = h*(2**0.5)*0.1*2
for l in range(10):
  for k in range(11):
    penup()
    x2 = xb+(h*(2**0.5))*k
    y2 = yb-(h*(2**0.5))*l
    goto(x2, y2)
    pendown()
    begin_fill()
    color((229, 219, 200), (33, 62, 106))
    Yu(u)
    end_fill()

#third layer
xc = xa+h*(2**0.5)/2
yc = ya+h*(2**0.5)/2

penup()
goto(xc, yc)
pendown()

t = (h*(2**0.5)-u)/4

for n in range(11):
  for m in range(10):
    penup()
    x3 = xc+(h*(2**0.5))*m
    y3 = yc-(h*(2**0.5))*n
    goto(x3, y3)
    pendown()

    begin_fill()
    pensize(1.5)
    color((173, 9, 20), (229, 219, 200))
    for i in range(8):
      Ting(t)
      right(45)
    end_fill()


hideturtle()
