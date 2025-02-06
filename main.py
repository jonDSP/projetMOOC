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
    abscisses = []
    ordonnees = []
    for a in range(-240, 50, pas):
        abscisses.append(a)
    for o in range(-240, 200, pas):
        ordonnees.append(o)
    abs_coin_inf_gauche = None
    ord_coin_inf_gauche = None
    print(abscisses)
    print(ordonnees)

def tracer_carre(dimension):
    """ trace le carré dont la dimension en px-turtle est fournie en argument"""

def tracer_case(case, couleur, pas):
    """ recoit un couple de coordonnées en indice (ligne colonne) appelle la fonction tracer_carre"""
def afficher_plan(matrice):
    """trace la map avec le module turtle a partir de la matrice en appellant la fonction tracer_case
     avec 2 boucles imbriquées"""


matrice = lire_matrice("plan_chateau.txt")
pas = calculer_pas(matrice)
coordonnees(1, pas)