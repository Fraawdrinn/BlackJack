import pygame as pg
import random
from main import cards

# Distribuer les cartes
def distrib(player):
    """Fonction permettant de piocher une carte"""
    card = random.choice(cards)
    cards.remove(card)
    player.append(card)

def pioche(carte):
    """"""
    