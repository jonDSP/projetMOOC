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


if __name__ == "__main__":
    # calcul de certaines variables utiles pour le tracé
    matrice = lire_matrice("plan_chateau.txt")
    pas = calculer_pas(matrice)

    # tracé de la map
    turtle.speed(0)
    afficher_plan(matrice)

    # boucle du jeu
    turtle.mainloop()



