from turtle import *
from math import *
window = Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

def carre(ching):  #fonction du carré
  for loop in range(4):
   forward(ching)
   left(90)

def hexa(grr): #focntion de l'hexagone
  left(30)
  for loop in range(6):
    forward(grr)
    left(60)




done()  # done
