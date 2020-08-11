from turtle import *
from PIL import Image
TurtleScreen._RUNNING=True
X=1280;Y=1024
screen = Screen()
screen.setup(X,Y)
screen.bgpic('bw.gif')
a=Turtle()
a.shape("turtle")
a.rt(90)
a.fd(230)
a.rt(-90)
a.fd(230)
for i in range(4):
    a.rt(-90)
    a.fd(470)
    

