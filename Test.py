from turtle import *
from math import *
window = Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

bgcolor("#003466")

def polygone(long,cot,color):
  pendown()
  pencolor("#"(color))
  angle = 360 / cot
  for i in range(cot):
    forward(long)
    right(angle)


polygone(50,5,"00FF00")