import pygame as pg
import random

# Initialisation
run = True

playerHand = dealerHand = []


cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "Jack", "Queen", "King", 
         "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "Jack", "Queen", "King",
         "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "Jack", "Queen", "King",
         "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "Jack", "Queen", "King"]

pg.init()
pg.display.set_caption("BlackJack Game")
clock = pg.time.Clock()
window_width = 800
window_height = 600

background = pg.image.load('assets/bg.png')
background = pg.transform.scale(background, (window_width, window_height))

gameDisplay = pg.display.set_mode((window_width, window_height))
gameDisplay.blit(background, (0, 0))

# CHARGEMENT D'IMAGES
pioche = pg.image.load('assets/cartes/card-extras/card_back.png')
pioche = pg.transform.scale(pioche, (200, 200))
gameDisplay.blit(pioche, (-20, 200))


def total(hand):
    """Calcul le total d'une main"""
    total = int()
    for el in hand:
        total += el
    return total

# Distribuer les cartes
def distrib(player):
    """Fonction permettant de piocher une carte"""
    card = random.choice(cards)
    cards.remove(card)
    player.append(card)
    for i in range(len(player)):
        pg.blit(pioche, (window_width/i, 500))

hasCardPlayer = False



# Boucle de jeu
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pass
    pg.display.update()  # Mettre à jour l'écran une fois par boucle

    clock.tick(30)

pg.quit()
quit()
