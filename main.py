import pygame as pg
import random

# Initialisation
run = True

playerHand = dealerHand = []
cards = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", 
         "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
         "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
         "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

pg.init()
pg.display.set_caption
window_width = 800
window_height = 600

background = pg.image.load('assets/bg.png') #Chargement de l'image
background = pg.transform.scale(background, (window_width, window_height)) # Taille de l'image

gameDisplay = pg.display.set_mode((window_width, window_height)) # Taille de la page
gameDisplay.blit(background, (0, 0)) # Affiche l'image de fond



pg.time.Clock()


# Distribuer les cartes
def distrib(player):
    """Fonction permettant de piocher une carte"""
    card = random.choice(cards)
    cards.remove(card)
    player.append(card)

# Calculer le total


# Vérifier le gagnant

# Boucle de jeu

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.update()
pg.quit()
quit()
