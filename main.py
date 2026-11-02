from turtle import *
from math import *
window = Screen()
window.setup (width=1350, height=700, startx=0, starty=0)
window.title(" 1ere - Turtle ")

bgcolor("#061C81")

tracer(0)  # Cache les animations
#endregion



def carre(long):  #fonction du carré
  for loop in range(4):
   forward(long)
   left(90)

def rectangle(longueur, largeur): #fonction du rectangle
  for loop in range(2):
    forward(longueur)
    left(90)
    forward(largeur)
    left(90)

def polygone(long,cot,color):
  pendown()
  pencolor("#" + color)
  angle = 360 / cot
  fillcolor("#" + color)
  begin_fill()
  for i in range(cot):
    forward(long)
    right(angle)
  end_fill()

polygone(50,5,"00FF00")

done()  # done

"""
Colors :
Back ground : ("#003466")
Rainbow :
Cat :
Planets :
"""
