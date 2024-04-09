import pygame as pg
import random

# Initialisation
run = True
playerHand = dealerHand = []


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "Jack", "Queen", "King", 
         2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "Jack", "Queen", "King", 
         2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "Jack", "Queen", "King", 
         2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "Jack", "Queen", "King"]

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



def somme(hand):
    """Calcul le total d'une main"""
    total = 0
    for el in hand:
        if isinstance(el, int):
            total += el
        elif el == 'A':
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += 10

    return total

# Distribuer les cartes
def distrib(player):
    """Fonction permettant de piocher une carte"""
    card = random.choice(cards)
    cards.remove(card)
    player.append(card)
    for i in range(len(player)):
        gameDisplay.blit(pioche, (100+(i*50), 500))

hasCardPlayer = False

def winCond():
    """"""
    global run
    if somme(playerHand) > 21:
        loseGUI = font.render("Perdu", True, (200, 0, 0))
        gameDisplay.blit(loseGUI, (380, 300))
        run = False

    elif somme(playerHand) == 21:
        blackjackGUI = font.render("BlackJack", True, (200, 0, 0))
        gameDisplay.blit(blackjackGUI, (380, 300))

font = pg.font.SysFont(None, 30)

# Boucle de jeu
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif len(playerHand) > 7 or len(dealerHand) > 7:
            run = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                distrib(playerHand)
                print(playerHand)
                print(somme(playerHand))
                
    winCond()
    totalGUI = font.render(str(somme(playerHand)), True, (0, 0, 255))   
    gameDisplay.fill((22, 166, 7), (770, 500, 100, 20))
    gameDisplay.blit(totalGUI, (770, 500))
    pg.display.update()  # Mettre à jour l'écran une fois par boucle

    clock.tick(30)

pg.quit()
quit()
