import pygame as pg
import random

# Initialisation
run = True
playerHand = []
dealerHand = []
suits = ["card_clubs_", "card_diamonds_", "card_hearts_", "card_spades_"]

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K", 
         2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K", 
         2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K", 
         2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]

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

def randCardType(cartes):
    """Choisit un type de carte au hasard"""
    result = random.choice(cartes)
    if result == cartes[0]: result2 = "clubs"
    elif result == cartes[1]: result2 = "diamonds"
    elif result == cartes[2]: result2 = "hearts"
    elif result == cartes[3]: result2 = "spades"
    return (result, result2)
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
def distribPlayer(player):
    """Fonction permettant de piocher une carte"""
    card = random.choice(cards)
    cards.remove(card)
    player.append(card)
    
    for i in range(len(player)):
        gameDisplay.blit(pioche, (100+(i*50), 500))
hasCardPlayer = False


def distribDealer(dealer):
    """Fonction permettant de piocher une carte"""
    global cardType, randCardType
    card = random.choice(cards)
    cards.remove(card)
    dealer.append(card)
    dealerC1 = randCardType(suits)
    if isinstance(card, int) and card < 10:
        cardDisplay = pg.image.load(f'assets/cartes/{dealerC1[1]}/{dealerC1[0]}0{card}.png')
        cardDisplay = pg.transform.scale(cardDisplay, (100, 100))
    else:
        cardDisplay = pg.image.load(f'assets/cartes/{dealerC1[1]}/{dealerC1[0]}{card}.png')
        cardDisplay = pg.transform.scale(cardDisplay, (100, 100))
    gameDisplay.blit(cardDisplay, (100+(len(dealerHand)*62), 50))


for i in range(2):
    distribDealer(dealerHand)

def choiceGUI(GUI):
    """Affichage du dilemme"""
    pass

def winCond():
    """Condition d'arrêt"""
    global run, choiceGUI
    def loseGUI():
        """Fonction permettant d'afficher le message de défaite"""
        GUI = font.render("Lost", True, (200, 0, 0))
        gameDisplay.blit(GUI, (380, 300))
        run = False
    def winGUI():
        """Fonction permettant d'afficher le message de victoire"""
        GUI = font.render("BlackJack", True, (0, 200, 0))
        gameDisplay.blit(GUI, (380, 300))
        run = False
    def drawGUI():
        """Fonction permettant d'afficher le message d'égalité"""
        GUI = font.render("Draw", True, (100, 100, 100))
        gameDisplay.blit(GUI, (380, 300))
        run = False
    # Condition n°1
    if somme(playerHand) == 21:
        winGUI()
    elif somme(dealerHand) == 21:
        loseGUI()
    # Condition n°2
    elif somme(playerHand) > 21:
        loseGUI()
    elif somme(dealerHand) > 21:
        winGUI()
    # Condition n°3
    elif 21 - somme(dealerHand) < 21 - somme(playerHand):
        loseGUI()
    elif 21 - somme(dealerHand) < 21 - somme(playerHand):
        loseGUI()
    # Condition n°4
    elif somme(dealerHand) == somme(playerHand) <= 21:
        drawGUI()

font = pg.font.SysFont(None, 30)
font2 = pg.font.SysFont(None, 36)


# Boucle de jeu
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif len(playerHand) > 7 or len(dealerHand) > 7:
            run = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                distribPlayer(playerHand)
                print('Player: ', playerHand)


    winCond()
    # Affichage des scores
        # Affichage du score du Joueur
    playerTotalGUI = font.render(str(somme(playerHand)), True, (0, 0, 255))   
    gameDisplay.fill((22, 166, 7), (770, 500, 100, 20))
    gameDisplay.blit(playerTotalGUI, (770, 500))
        # Affichage du score du croupier
    DealerTotalGUI = font.render(str(somme(dealerHand)), True, (0, 200, 200))   
    gameDisplay.fill((22, 166, 7), (770, 50, 100, 20))
    gameDisplay.blit(DealerTotalGUI, (770, 50))
    
    if somme(dealerHand) <= 17 and len(dealerHand) <= 3:
        distribDealer(dealerHand) 
    else:
        pg.time.wait(200)
        choice = font2.render('Voulez-vous continuer de piocher ?', False, (0, 0, 0))
        gameDisplay.blit(choice, (200, 250))

    pg.display.update()  # Mettre à jour l'écran une fois par boucle

    clock.tick(30)
pg.time.wait(500)
pg.quit()
quit()