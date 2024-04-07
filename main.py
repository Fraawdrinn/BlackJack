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

pioche = pg.image.load('assets/cartes/card-extras/card_back.png')
pioche = pg.transform.scale(pioche, (200, 200))
gameDisplay.blit(pioche, (-20, 200))

pioche2 = pg.image.load('assets/cartes/card-extras/card_back.png')
pioche2 = pg.transform.scale(pioche2, (200, 200))

# Distribuer les cartes
def distrib(player):
    """Fonction permettant de piocher une carte"""
    card = random.choice(cards)
    cards.remove(card)
    player.append(card)

def AnimPioche():
    """Animation de pioche (vers le premier slot de carte)"""
    pioche2_x = -20  # Position initiale en x de pioche2
    pioche2_y = 200  # Position initiale en y de pioche2

    while pioche2_x < 340 and pioche2_y < 400:
        # Animation de pioche2
        pioche2_x += 2  # Déplacement horizontal
        pioche2_y += 2

        gameDisplay.blit(background, (0, 0))  # Afficher le fond à chaque boucle pour effacer les anciens objets
        gameDisplay.blit(pioche, (-20, 200))  # Afficher pioche
        gameDisplay.blit(pioche2, (pioche2_x, pioche2_y))  # Afficher pioche2 à sa nouvelle position

        pg.display.update()  # Mettre à jour l'écran une fois par boucle

# Boucle de jeu
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                AnimPioche()
    
    pg.display.update()  # Mettre à jour l'écran une fois par boucle

    clock.tick(60)

pg.quit()
quit()
