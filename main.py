import pygame as pg
from random import randint
import time

# Initialisation
playerHand = dealerHand = []
cards = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", 
         "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
         "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
         "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Distribuer les cartes
def distrib(Hand):
    """Distribution de 2 cartes"""
    for _ in range(2):
        Hand.append(randint(len(cards)))

# Calculer le total
        
# Vérifier le gagnant
        
# Boucle de jeu
    