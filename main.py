#region everything
from turtle import *
from math import *
from random import *

#region setting
window = Screen()
window.setup (width=800, height=600, startx=0, starty=0)
window.title(" 1ere - Turtle ")

bgcolor("#003466")

tracer(0,100)

frame_i = 0

#endregion

#region function
def polygone(long,cot,color):
  """
  Entrée :
    long  : int , longueur du coté du pixel
    cot   : int (entre 1 et 360) , nombre de cotés
    color : str (en héxadécimal sans le #) , couleur du pixel
  Sortie :
    Dessin d'un polygone régulier de couleur, de longeur et de nombre de cotés variable
  """
  pendown()
  pencolor("#" + color)
  angle = 360 / cot
  fillcolor("#" + color)
  begin_fill()
  for i in range(cot):
    forward(long)
    right(angle)
  end_fill()
  forward(long)

def ret_line(pix):
  """
  Entrée : 
    pix : int , longueur du coté du pixel
  Sortie :
    retour à la ligne aproximatif ( nécessite un placement préalabre de la turtle en fin de ligne)
  Retourne à la ligne suivante
  """
  penup()
  right(90)
  forward(pix)
  right(90)
  forward(pix*33)
  right(180)
  pendown()
#endregion

#region stars
def carre(color):
   """
   dessine un pixel de notre image
   """
   fillcolor(color)
   begin_fill()
   for i in range(4):
       forward(4)
       left(90)
   end_fill()

def ligne(color):
    """
    dessine une ligne de 4 pixels de notre image
    """
    for i in range(4):
        carre(color)
        forward(4)


def circlecarre(diamètre):
    """
    fait un cercle avec des carrés
    """
    diamètre = diamètre*4
    for i in range(9):
        carre("white")
        penup()
        circle(diamètre/2, 360/9) # tourne autour du cercle pour placer les carrés
        pendown()
       


def etoile1():
    """
    dessine une étoile avec des carre
    """
    for j in range(10):
        penup()
        setpos(randint(-400, 400), randint(-300, 300)) # position aléatoire pour l'étoile
        pendown()
        pencolor("white")
        for w in range(4):
            ligne("white")
            backward(4*4)
            left(90)
            forward(4)

def etoile2():
    """
    dessine une étoile avec des carrés
    """
    pencolor("white")
    for i in range(6):
        penup()
        setpos(randint(-400, 400), randint(-300, 300)) # position aléatoire pour l'étoile
        pendown()
        carre("white")

def etoile3():
    """
    dessine une étoile :circulaire avec des carrés 
    """
    pencolor("white")
    for i in range(6):
        penup()
        setpos(randint(-400, 400), randint(-300, 300)) # position aléatoire pour l'étoile
        pendown()
        circlecarre(9) # fais un cercle avec des carrés espacés 

def planete():
    """
    dessine une planète avec des carre
    """
    colors = ["red", "orange", "yellow", "green", "purple"] # liste de couleurs pour les planètes
    for _ in range(5):
        pensize(5)
        color = colors[randint(0, 4)] # choisir une couleur aléatoire pour la planète
        penup()
        setpos(randint(-400, 400), randint(-300, 300))  # position aléatoire pour la planète
        pendown()
        rayon_en_carre= randint(3, 10) # rayon aléatoire de la planète en nombre de carrés
        rayon1= rayon_en_carre*4 #rayon en pixels
        fillcolor(color)
        begin_fill()
        circle(rayon1)
        end_fill()
        pensize(1)
           
       
planete()
etoile1()
etoile2()
etoile3()   
#endregion

#region trail
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
                pencolor("#FE2B0C")
            elif couleur_num == 2:
                pencolor("#FFA902")
            elif couleur_num == 3:
                pencolor("#FFF500")
            elif couleur_num == 4:
                pencolor("#31E909")
            elif couleur_num == 5:
                pencolor("#217E85")
            elif couleur_num == 6:
                pencolor("#920DAD")

            
            # On trace des lignes grace a des aller-retour pour remplir le rectangle de couleur.
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
            penup()
            right(90)
            forward(largeur_bande)
            left(90)
            pendown()

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
#endregion

#region cat
def cat_bod(pix):
    """
      Entrée : 
        pix : int , longueur du coté du pixel
      Sortie :
        Dessin du corps du chat
      """

    setpos(-50,30)
    right(90)
    left(90)
    
    for i in range(1):          #ligne 1
        penup()
        forward(8*pix)
        pendown()
        for i in range(17):
            polygone(pix,4,"000000")
        penup()
        forward(8*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 2
        penup()
        forward(7*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(17):
            polygone(pix,4,"fecc9b")
        polygone(pix,4,"000000")
        penup()
        forward(7*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 3
        penup()
        forward(6*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(3):
            polygone(pix,4,"fecc9b")
        for i in range(13):
            polygone(pix,4,"ff99ff")
        for i in range(3):
            polygone(pix,4,"fecc9b")
        polygone(pix,4,"000000")
        penup()
        forward(6*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 4
        penup()
        forward(6*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"fecc9b")
        for i in range(15):
            polygone(pix,4,"ff99ff")
        for i in range(2):
            polygone(pix,4,"fecc9b")
        polygone(pix,4,"000000")
        penup()
        forward(6*pix)
        pendown()

    ret_line(pix)

    for i in range(10):          #ligne 5-15
        for i in range(1):      
            penup()
            forward(6*pix)
            pendown()
            polygone(pix,4,"000000")
            for i in range(1):
                polygone(pix,4,"fecc9b")
            for i in range(17):
                polygone(pix,4,"ff99ff")
            for i in range(1):
                polygone(pix,4,"fecc9b")
            polygone(pix,4,"000000")
            penup()
            forward(6*pix)
            pendown()
        ret_line(pix)

    for i in range(1):          #ligne 16
        penup()
        forward(6*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"fecc9b")
        for i in range(15):
            polygone(pix,4,"ff99ff")
        for i in range(2):
            polygone(pix,4,"fecc9b")
        polygone(pix,4,"000000")
        penup()
        forward(6*pix)
        pendown()
    
    ret_line(pix)

    for i in range(1):          #ligne 17

        penup()
        forward(6*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(3):
            polygone(pix,4,"fecc9b")
        for i in range(13):
            polygone(pix,4,"ff99ff")
        for i in range(3):
            polygone(pix,4,"fecc9b")
        polygone(pix,4,"000000")
        penup()
        forward(6*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 18
        penup()
        forward(7*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(17):
            polygone(pix,4,"fecc9b")
        polygone(pix,4,"000000")
        penup()
        forward(7*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 19
        penup()
        forward(8*pix)
        pendown()
        for i in range(17):
            polygone(pix,4,"000000")
        penup()
        forward(8*pix)
        pendown()

    penup()

def cat_sup(pix):
    """
      Entrée : 
        pix : int , longueur du coté du pixel
      Sortie :
        Dessin le reste du chat (tête, pattes, queue)
      """
    setpos(-50,30)
    right(90)
    forward(5*pix)
    left(90)

    for i in range(1):          #ligne 1
        penup()
        forward(19*pix)
        pendown()
        for i in range(2):
            polygone(pix,4,"000000")
        penup()
        forward(8*pix)
        pendown()
        for i in range(2):
            polygone(pix,4,"000000")
        penup()
        forward(2*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 2
        penup()
        forward(18*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(6*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(1*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 3
        penup()
        forward(18*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(3):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(4*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(3):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(1*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 4
        penup()
        forward(1*pix)
        pendown()
        for i in range(2):
            polygone(pix,4,"000000")
        penup()
        forward(15*pix)
        pendown()
        polygone(pix,4,"000000")    
        for i in range(4):
            polygone(pix,4,"999999")
        for i in range(4):
            polygone(pix,4,"000000")
        for i in range(4):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(1*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 5
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(14*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(12):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(1*pix)
        pendown()

    ret_line(pix)


    for i in range(1):          #ligne 6
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        for i in range(3):
            polygone(pix,4,"000000")
        penup()
        forward(11*pix)
        pendown() 
        polygone(pix,4,"000000")
        for i in range(14):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")


    ret_line(pix)

    for i in range(1):          #ligne 7
        penup()
        forward(1*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(4):
            polygone(pix,4,"999999")
        penup()
        forward(11*pix)
        pendown() 
        polygone(pix,4,"000000")
        for i in range(3):
            polygone(pix,4,"999999")
        polygone(pix,4,"ffffff")
        polygone(pix,4,"000000")
        for i in range(5):
            polygone(pix,4,"999999")
        polygone(pix,4,"ffffff")
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")

    ret_line(pix)

    for i in range(1):          #ligne 8
        penup()
        forward(2*pix)
        pendown()
        for i in range(2):
            polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        penup()
        forward(11*pix)
        pendown() 
        polygone(pix,4,"000000")
        for i in range(3):
            polygone(pix,4,"999999")
        for i in range(2):
            polygone(pix,4,"000000")
        for i in range(3):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        polygone(pix,4,"999999")
        for i in range(2):
            polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")

    ret_line(pix)

    for i in range(1):          #ligne 9
        penup()
        forward(4*pix)
        pendown()
        for i in range(2):
            polygone(pix,4,"000000")
        penup()
        forward(11*pix)
        pendown() 
        polygone(pix,4,"000000")
        polygone(pix,4,"999999")
        for i in range(2):
            polygone(pix,4,"f29898")
        for i in range(9):
            polygone(pix,4,"999999")
        for i in range(2):
            polygone(pix,4,"f29898")
        polygone(pix,4,"000000")

    ret_line(pix)

    for i in range(1):          #ligne 10
        penup()
        forward(17*pix)
        pendown() 
        polygone(pix,4,"000000")
        polygone(pix,4,"999999")
        for i in range(2):
            polygone(pix,4,"f29898")
        polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        polygone(pix,4,"999999")
        for i in range(2):
            polygone(pix,4,"f29898")
        polygone(pix,4,"000000")

    ret_line(pix)

    for i in range(1):          #ligne 11
        penup()
        forward(18*pix)
        pendown() 
        polygone(pix,4,"000000")
        for i in range(3):
            polygone(pix,4,"999999")
        for i in range(7):
            polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(1*pix)
        pendown() 

    ret_line(pix)

    for i in range(1):          #ligne 12
        penup()
        forward(6*pix)
        pendown()
        polygone(pix,4,"000000")
        penup()
        forward(12*pix)
        pendown() 
        polygone(pix,4,"000000")
        for i in range(10):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(2*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 13
        penup()
        forward(5*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        for i in range(22):
            polygone(pix,4,"000000")
        penup()
        forward(3*pix)
        pendown()  

    ret_line(pix)

    for i in range(1):          #ligne 14
        penup()
        forward(5*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(1*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(6*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(1*pix)
        pendown()
        polygone(pix,4,"000000")
        for i in range(2):
            polygone(pix,4,"999999")
        polygone(pix,4,"000000")
        penup()
        forward(4*pix)
        pendown()

    ret_line(pix)

    for i in range(1):          #ligne 15
        penup()
        forward(5*pix)
        pendown()
        for i in range(3):
            polygone(pix,4,"000000")
        penup()
        forward(3*pix)
        pendown()
        for i in range(3):
            polygone(pix,4,"000000")
        penup()
        forward(7*pix)
        pendown()
        for i in range(3):
            polygone(pix,4,"000000")
        penup()
        forward(2*pix)
        pendown()
        for i in range(3):
            polygone(pix,4,"000000")
        penup()
        forward(4*pix)
        pendown()

#endregion

traine_aller_retour(6)
penup()

taille = 10
cat_bod(taille)
cat_sup(taille)
onclick

done()

#endregion
#:3