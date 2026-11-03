#region init
from turtle import *
from math import *
window = Screen()
window.setup (width=1350, height=700, startx=0, starty=0)
window.title(" 1ere - Turtle ")

bgcolor("#0D4178")


#region func
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


def traine_aller_retour(nb_blocs):
    '''
    fonction qui dessine des rectangles de couleurs en collones pour faire une trainée de couleur.
    Entrée : nombre de collonne (nb_collone) en valeur int = nombre de colonnes à dessiner.
    Sortie : des rectangles de couleurs en collones pour faire une trainée de couleur.
    
    '''
    longueur = 90 # longueur d'une bande ou rectangle de couleur.
    largeur_bande = 30 # largeur d'une bande ou rectangle de couleur.
    decalage = 10  # Valeur du décalage pour l'effet de difference entre les colonnes (en pixels).

    # Variable pour compter les colonnes si pair ou impair selon nombre pour decollage de taille.
    bande = 1

    for i in range(nb_blocs):
        # On calcule le décalage selon que la colonne est paire ou impaire.
        hauteur_decalage = decalage if (bande % 2 == 1) else 0

        # Placement de la colonne avec le décalage
        penup()
        left(90)
        forward(hauteur_decalage)
        right(90)
        pendown()

        # definition de la variable pour les couleurs (commence à 1) pour chnager celle ci au fur et a mesure.
        couleur_num = 1

        # Tracé des 6 bandes de couleur
        while couleur_num <= 6:
            # Changement de couleur selon la valeur de la variable couleur_num
            if couleur_num == 1:
                pencolor("red")
            elif couleur_num == 2:
                pencolor("orange")
            elif couleur_num == 3:
                pencolor("yellow")
            elif couleur_num == 4:
                pencolor("green")
            elif couleur_num == 5:
                pencolor("#217E85")
            elif couleur_num == 6:
                pencolor("#920DAD")

            
            # On trace des lignes grace a la focntion begin fill pour remplir le rectgle.
            for k in range(largeur_bande):
                forward(longueur)
                backward(longueur)
                left(90)
                forward(1)
                right(90)

            #Revient à la position de départ pour rectangle suivant
            right(90)
            forward(largeur_bande)
            left(90)

            # Descendre pour passer à la bande de couleur suivante
            right(90)
            forward(largeur_bande)
            left(90)

            # on ajoute 1 a la variable couleur_num pour passer à la couleur suivane.

            couleur_num = couleur_num + 1

        # Remonter le curseur tout en haut du bloc et avancer vers la nouvelle colone.
        penup()
        left(90)
        forward(6 * largeur_bande)
        right(90)
        forward(longueur)
        pendown()

        # Remettre la tortue à l'horizontale de base en annulant le décalage
        penup()
        right(90)
        forward(hauteur_decalage)
        left(90)
        pendown()

        # On ajoute 1 à la variable "bande" pour la colonne suivante (pair ou impair)
        bande = bande + 1

# Position initiale de départ sur l'écran.
penup()
setposition(-500, 0)
pendown()

# Appel des fonctions
traine_aller_retour(4)

done()  # done
#endregion

"""
Colors :
Back ground : ("#003466")
Rainbow :
Cat :
Planets :
"""
