import pygame as pg
import random

# Initialisation
run = True

playerHand = dealerHand = []
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", 
         "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
         "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
         "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

pg.init()
pg.display.set_caption("BlackJack Game")
window_width = 800
window_height = 600

background = pg.image.load('assets/bg.png') # Chargement de l'image
background = pg.transform.scale(background, (window_width, window_height)) # Taille de l'image

gameDisplay = pg.display.set_mode((window_width, window_height)) # Taille de la page
gameDisplay.blit(background, (0, 0)) # Affiche l'image de fond

    # Chargement d'images
pioche = pg.image.load('assets/cartes/card-extras/card_back.png')
pioche = pg.transform.scale(pioche, (200, 200))
gameDisplay.blit(pioche, (-20, 200))



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
