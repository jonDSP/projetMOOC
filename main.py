import math
import turtle
from CONFIGS import *

def lire_matrice(fichier):
    """lit un fichier texte et renvoie une matrice representant la map du jeu"""
    with open(fichier, "r", encoding="utf-8") as map_file:
        return [[int(colonne) for colonne in ligne.split()]for ligne in map_file]

def calculer_pas(matrice):
    """calcule la dimension des cases
    doit prendre en compte la hauteur et la largeur de la zone d'affichage de la map
    et diviser par le nombre de cases en largeur et en hauteur et retenir la plus petite valeur"""
    largeur = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
    hauteur = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])
    nbre_case_largeur = len(matrice[0])
    nbre_case_hauteur = len(matrice)
    pas = math.floor(min(largeur/nbre_case_largeur, hauteur/nbre_case_hauteur))
    return pas

def coordonnees(case,pas):
    """ calcul les coordonnées en px-turtle du coin inf gauche d'une case spécifiée par ses coordonnées
    (n°ligne, n°colonne), nb: le plus en bas a gauche est (-240, -240)
    attention les lignes augmentent de haut en bas alors que l'axe y diminue de haut en bas """
    numero_ligne = case[0]
    numero_colonne = case[1]
    abs_coin_inf_gauche = -240 + pas * numero_colonne # les numeros de colonne augmentent sur l'axe abscisse
    ord_coin_inf_gauche = -240 + pas *(26-numero_ligne)
    return abs_coin_inf_gauche, ord_coin_inf_gauche

def tracer_carre(dimension):
    """ trace le carré dont la dimension en px-turtle est fournie en argument"""
    for i in range(4):
        turtle.forward(dimension)
        turtle.left(90)

def tracer_case(case, couleur, pas):
    """ recoit un couple de coordonnées en indice (ligne colonne) appelle la fonction tracer_carre"""
    turtle.up()
    turtle.goto(coordonnees(case, pas)) # permet de convertir les coord-indices de la case en coord-px
    turtle.down()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.hideturtle()
    tracer_carre(pas)
    turtle.end_fill()

def afficher_plan(matrice):
    """trace la map avec le module turtle a partir de la matrice en appellant la fonction tracer_case
     avec 2 boucles imbriquées"""
    for l in range(len(matrice)):
        for c in range(len(matrice[l])):
            tracer_case((l,c), COULEURS[matrice[l][c]], pas)



class Player:
    def __init__(self):
        self.couleur = COULEUR_PERSONNAGE
        self.diametre = RATIO_PERSONNAGE * pas
        self.start_position = POSITION_DEPART
        self.position = POSITION_DEPART

    def draw_player(self, destination):
        """ fonction permettant de dessiner le joueur sur la case spécifiée sous forme (ligne,colonne"""
        def centre_joueur():
            """calcul du centre de la case en coord-px  pour savoir ou tracer le cercle turtle.dot"""
            coin_case =  coordonnees(destination, pas)
            centre_abs = coin_case[0] + 7.5
            centre_ord = coin_case[1] + 7.5 # pour centrer le cercle dans la case
            return centre_abs, centre_ord
        turtle.up()
        turtle.goto(centre_joueur())
        turtle.down()
        turtle.dot(self.diametre, self.couleur)

    def deplacer(self, position, mouvement):
        destination = position[0]+mouvement[0], position[1]+mouvement[1]
        couleur_dest = COULEURS[matrice[destination[0]][destination[1]]]
        if 0<=destination[0]<= len(matrice) and 0<=destination[1]<= len(matrice[0]) and couleur_dest != "grey":
            tracer_case(position, COULEURS[matrice[position[0]][position[1]]], pas )
            self.draw_player((destination[0], destination[1]))
            self.position = destination


    def deplacer_gauche(self, mouvement=(0,-1)):
        """ position et mouvement sous forme de tuple(ligne, colonne)
        en pratique on dessine le joueur sur la case destination et on redessine la case de départ"""
        turtle.onkeypress(None, "Left")
        self.deplacer(self.position, mouvement)
        turtle.onkeypress(self.deplacer_gauche, "Left")

    def deplacer_droite(self, mouvement =(0,1)):
        """ position et mouvement sous forme de tuple(ligne, colonne)
        en pratique on dessine le joueur sur la case destination et on redessine la case de départ"""
        turtle.onkeypress(None, "Right")
        self.deplacer(self.position, mouvement)
        turtle.onkeypress(self.deplacer_droite, "Right")

    def deplacer_haut(self, mouvement=(-1,0)):
        """ position et mouvement sous forme de tuple(ligne, colonne)
        en pratique on dessine le joueur sur la case destination et on redessine la case de départ"""
        turtle.onkeypress(None, "Up")
        self.deplacer(self.position, mouvement)
        turtle.onkeypress(self.deplacer_haut, "Up")

    def deplacer_bas(self, mouvement=(1,0)):
        """ position et mouvement sous forme de tuple(ligne, colonne)
        en pratique on dessine le joueur sur la case destination et on redessine la case de départ"""
        turtle.onkeypress(None, "Down")
        self.deplacer(self.position, mouvement)
        turtle.onkeypress(self.deplacer_bas, "Down")


if __name__ == "__main__":
    # calcul de certaines variables utiles pour le tracé
    matrice = lire_matrice("essai_map.txt")
    pas = 15  # a remettre a la fin, ici c'esst juste pour les essais calculer_pas(matrice)

    # tracé de la map
    turtle.speed(0)
    afficher_plan(matrice)

    # instanciation du joueur et placement initial
    player = Player()
    player.draw_player(player.start_position)

    # boucle du jeu
    turtle.listen()  # Déclenche l’écoute du clavier
    turtle.onkeypress(player.deplacer_gauche, "Left")  # Associe à la touche Left une fonction appelée deplacer_gauche
    turtle.onkeypress(player.deplacer_droite, "Right")
    turtle.onkeypress(player.deplacer_haut, "Up")
    turtle.onkeypress(player.deplacer_bas, "Down")
    turtle.mainloop()



