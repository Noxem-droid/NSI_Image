from turtle import *
from math import *
window = Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")
bgcolor("#003466")


def carre(ching):  #fonction du carré
  for loop in range(4):
   forward(ching)
   left(90)



def rectangle(longueur, largeur): #fonction du rectangle
  for loop in range(2):
    forward(longueur)
    left(90)
    forward(largeur)
    left(90)




done()  # done

"""
Colors :
Back ground :
Rainbow :
Cat :
Planets :
"""
