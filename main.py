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
        if isinstance(el[0], int):
            total += el[0]
        elif not isinstance(el[0], int):
            total += 10
        elif el == "A" and total <= 10:
            total += 11
        else:
            total += 11

    return total

# Distribuer les cartes
def distrib(player):
    """Fonction permettant de piocher une carte"""
    card = random.choice(cards)
    cards.remove(card)
    player.append(card)
    for i in range(len(player)):
        gameDisplay.blit(pioche, (100+(i*10), 500))

hasCardPlayer = False

font = pg.font.SysFont(None, 24)
img = font.render(str(total(playerHand)), True, (0, 0, 255))
gameDisplay.blit(img, (800, 500))

# Boucle de jeu
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(playerHand)
                distrib(playerHand)

    pg.display.update()  # Mettre à jour l'écran une fois par boucle

    clock.tick(30)

pg.quit()
quit()
