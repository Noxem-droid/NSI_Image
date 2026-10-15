from turtle import *
from math import *

#region setting
window = Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

bgcolor("#003466")

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

def polygone(long, larg, cot):
  angle = 360 / cot
  for i in range(cot):
    forward(long)
    right(angle)
    forward(larg)
    right(angle)

polygone(50,50,5)

done()  # done

"""
Colors :
Back ground :
Rainbow :
Cat :
Planets :
"""
