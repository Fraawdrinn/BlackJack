import pygame as pg
import random
import color

# Initialisation
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
run = True
display = True


background = pg.image.load('assets/bg.png')
background = pg.transform.scale(background, (window_width, window_height))

gameDisplay = pg.display.set_mode((window_width, window_height))
gameDisplay.blit(background, (0, 0))
gameDisplaySurface = (0, 0, window_width, window_height)

# FONTS
font = pg.font.SysFont(None, 30)
font2 = pg.font.SysFont(None, 36)
font3 = pg.font.Font('assets/Bloxat.ttf', 40)

# CHARGEMENT D'IMAGES
pioche = pg.image.load('assets/cartes/card-extras/card_back.png')
pioche = pg.transform.scale(pioche, (200, 200))
gameDisplay.blit(pioche, (-20, 200))
pioche_rect = pioche.get_rect(topleft=(-20, 200))

# Fonction pour dessiner le bouton à l'écran
def dessiner_bouton(bouton_couleur, bouton_x, bouton_y, bouton_width, bouton_height, texte):
    draw = pg.draw.rect(gameDisplay, bouton_couleur, (bouton_x, bouton_y, bouton_width, bouton_height))
    gameDisplay.blit(texte, (bouton_x + 15, bouton_y + 15))
    return (bouton_x, bouton_y, bouton_width, bouton_height, draw)


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
    print('Player: ', player)
    
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
    distribPlayer(playerHand)

def choiceGUI():
    if display:
        mouse = pg.mouse.get_pos()
        choice = font2.render('Voulez-vous continuer de piocher ?', False, color.black)
        gameDisplay.blit(choice, (200, 300))
        yes_button = dessiner_bouton(color.light_grey, 200, 370, 100, 50, font.render('Oui', False, color.dark_green))
        yes_button_rect = yes_button[4]
        no_button = dessiner_bouton(color.light_grey, 500, 370, 100, 50, font.render('Non', False, color.red))
        no_button_rect = no_button[4]
        if yes_button_rect.collidepoint(mouse):
            return True
        elif no_button_rect.collidepoint(mouse):
            return False
        else: 
            pass
    else: pass

def winGUI():
    """Affichage d'écran de victoire"""
    message = font3.render('Victory', True, color.green)
    win_button = dessiner_bouton(color.bg, 200, 270, 450, 150, message)
    display = False
    return True
def loseGUI():
    """Affichage d'écran de défaite"""
    message = font3.render('Lose', True, color.red)
    lose_button = dessiner_bouton(color.bg, 200, 270, 450, 150, message)
    display = False
    return True
def drawGUI():
    """Affichage d'écran d'égalité"""
    message = font3.render('Draw', True, color.grey)
    win_button = dessiner_bouton(color.bg, 200, 270, 450, 150, message)
    display = False
    return True
def blackjackGUI():
    """Affichage d'écran de blackjack"""
    message = font3.render('Blackjack', True, color.purple)
    win_button = dessiner_bouton(color.bg, 200, 270, 450, 150, message)
    display = False
    return True

def winCond():
    """Condition d'arrêt"""
        # Conditions de lose
    if somme(playerHand) < somme(dealerHand):
        loseGUI()
        pg.time.wait(3000)
    elif somme(playerHand) > 21:
        loseGUI()
        pg.time.wait(3000)
        # Conditions de draw
    elif somme(playerHand) == somme(dealerHand):
        drawGUI()
        pg.time.wait(3000)
    else:
        winGUI()


def playerGUI():
    # Affichage du score du Joueur
    playerTotalGUI = font.render(str(somme(playerHand)), True, color.blue)   
    gameDisplay.fill(color.bg, (770, 500, 100, 20))
    gameDisplay.blit(playerTotalGUI, (770, 500))

def dealerGUI():
    # Affichage du score du croupier
    DealerTotalGUI = font.render(str(somme(dealerHand)), True, color.light_blue)   
    gameDisplay.fill(color.bg, (770, 50, 100, 20))
    gameDisplay.blit(DealerTotalGUI, (770, 50))



# Boucle de jeu
while run:
    if somme(playerHand) >= 17: 
        if display:
            choiceGUI()
        else: pass
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif len(playerHand) > 7 or len(dealerHand) > 7:
            loseGUI()
        elif somme(playerHand) > 21: 
            loseGUI() 
        elif somme(dealerHand) > 21: 
            winGUI()
        elif somme(playerHand) == 21: 
            blackjackGUI()

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pioche_rect.collidepoint(event.pos):
                    distribPlayer(playerHand)
                elif choiceGUI(): 
                    print('1')
                    gameDisplay.fill(color.bg, (200, 270, 600, 400))
                    distribPlayer(playerHand)
                elif not choiceGUI():
                    gameDisplay.fill(color.bg, (200, 270, 600, 200))
                    winCond()
                    print('0')


    # Affichage des scores
    playerGUI()
    dealerGUI()

    pg.display.update()  # Mettre à jour l'écran une fois par boucle

    clock.tick(30)
pg.quit()
quit()
