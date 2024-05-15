import pygame
import random
import color  # Import du fichier color.py contenant les couleurs

# Initialisation de Pygame
pygame.init()
pygame.display.set_caption("Jeu de BlackJack")
FramePerSec = pygame.time.Clock()
window_width = 800
window_height = 600
FPS = 60

# Chargement de l'image de fond et initialisation de l'écran de jeu
background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (window_width, window_height))
gameDisplay = pygame.display.set_mode((window_width, window_height))
gameDisplaySurface = (0, 0, window_width, window_height)

# Initialisation des polices de caractères
font = pygame.font.SysFont(None, 30)
font1 = pygame.font.SysFont(None, 14)
font3 = pygame.font.SysFont(None, 22)
font2 = pygame.font.SysFont(None, 36)
bloxat = pygame.font.Font('assets/Bloxat.ttf', 56)
bloxat2 = pygame.font.Font('assets/Bloxat.ttf', 26)

# Chargement d'images de la pioche des cartes
pioche_img = pygame.image.load('assets/cartes/card-extras/card_back.png')
pioche_scaled = pygame.transform.scale(pioche_img, (200, 200))
pioche_rect = pioche_scaled.get_rect(topleft=(-20, 200))

# Initialisation des mains du joueur et du croupier
playerHand = ['player']
dealerHand = ['dealer']

# Liste de cartes et enseignes
deck = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
    2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
    2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
    2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
suits = ["clubs", "diamonds", "hearts", "spades"]

# Fonction pour dessiner un rectangle sur l'écran et afficher du texte à l'intérieur
def dessiner_rect(rect_color, rect_x, rect_y, rect_width, rect_height, text):
    draw = pygame.draw.rect(gameDisplay, rect_color, (rect_x, rect_y, rect_width, rect_height))
    gameDisplay.blit(text, (rect_x + 15, rect_y + 15))
    return (rect_x, rect_y, rect_width, rect_height, pygame.Rect(rect_x, rect_y, rect_width, rect_height))

# Classe pour les cartes
class Card:
    def __init__(self, cardList, suitsList):
        self.suit = random.choice(suitsList)
        self.value = random.choice(cardList)
        cardList.remove(self.value)
        self.isHidden = False
        if isinstance(self.value, int) and self.value < 10:
            self.image = pygame.image.load(f'assets/cartes/{self.suit}/card_{self.suit}_0{self.value}.png')
        else:
            self.image = pygame.image.load(f'assets/cartes/{self.suit}/card_{self.suit}_{self.value}.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.back = pygame.image.load('assets/cartes/card-extras/card_back.png')
        self.back = pygame.transform.scale(self.back, (150, 150))
        if self.isHidden:
            self.image = self.back
        self.rect = self.image.get_rect()

    # Masquer ou montrer la carte
    def hide(self):
        """Cacher une carte"""
        if not self.isHidden:
            self.isHidden = True
        else:
            self.isHidden = False

    # Distribuer une carte à une main
    def distrib(self, hand):
        """Ajouter une carte à une main"""
        self.hand = hand[0]
        self.parent = hand
        hand.append(self)

# Afficher la carte sur l'écran
def draw_hand(hand, aBool=False):
        """Afficher les mains"""
        if aBool: # Si aBool renvoie True, On affiche même les cartes cachées
            for index, card in enumerate(hand[1:]):
                if hand[0] == "player":
                        gameDisplay.blit(card.image, (card.rect.x + (index * 50), card.rect.y + window_height - 100))
                elif hand[0] == "dealer":
                        gameDisplay.blit(card.image, (card.rect.x + (index * 50), card.rect.y))
        else:
            for index, card in enumerate(hand[1:]):
                if hand[0] == "player":
                    if card.isHidden:
                        gameDisplay.blit(card.back, (card.rect.x + (index * 50), card.rect.y + window_height - 100))
                    else:
                        gameDisplay.blit(card.image, (card.rect.x + (index * 50), card.rect.y + window_height - 100))
                elif hand[0] == "dealer":
                    if card.isHidden:
                        gameDisplay.blit(card.back, (card.rect.x + (index * 50), card.rect.y))
                    else:
                        gameDisplay.blit(card.image, (card.rect.x + (index * 50), card.rect.y))


# Fonction pour piocher une carte dans une main
def pioche(hand, statement=True):
    new_card = Card(deck, suits)
    new_card.distrib(hand)
    if not statement:
        new_card.hide()

# Calculer la somme des cartes dans une main
def sum(hand):
    total = 0
    for el in hand:
        if el == 'player' or el == 'dealer':
            pass
        elif isinstance(el.value, int):
            total += el.value
        elif el.value == 'A':
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += 10
    return total

# Fonctions pour l'affichage graphique
def playerGUI():
    # Affichage du score du Joueur
    text = "Joueur: " + str(sum(playerHand))
    playerTotalGUI = font.render(text, True, color.blue)   
    gameDisplay.fill(color.bg, ((window_width - 100), (window_height - 110), 100, 20))
    gameDisplay.blit(playerTotalGUI, (window_width - 110, window_height - 110))
    return (playerTotalGUI, (((window_width - 100), (window_height - 110), 100, 20)), (window_width - 110, window_height - 110))

def dealerGUI():
    # Affichage du score du croupier
    text = "Croupier: " + str(sum(dealerHand))
    dealerTotalGUI = font.render(text, True, color.light_blue)   
    gameDisplay.fill(color.bg, ((window_width - 120), 110, 120, 20))
    gameDisplay.blit(dealerTotalGUI, (window_width - 120, 110))
    return (dealerTotalGUI, (window_width - 120, 110))

def winGUI():
    # Affichage en cas de victoire
    text = bloxat.render('VICTOIRE', True, color.green)
    dessiner_rect(color.bg, (window_width/2 - 50), (window_height/2), 200, 100, text)

def loseGUI():
    # Affichage en cas de défaite
    text = bloxat.render('DEFAITE', True, color.red)
    dessiner_rect(color.bg, (window_width/2 - 70), (window_height/2), 200, 100, text)

def drawGUI():
    # Affichage en cas d'égalité
    text = bloxat.render('ÉGALITÉ', True, color.grey)
    dessiner_rect(color.bg, (window_width/2 - 50), (window_height/2), 200, 100, text)

def blackjackGUI():
    # Affichage en cas de Blackjack
    text = bloxat.render('BLACKJACK', True, color.purple)
    dessiner_rect(color.bg, (window_width/2 - 100), (window_height/2), 200, 100, text)

def stopGUI():
    # Affiche le bouton pour arrêter de piocher
    text = font.render('STAND', False, color.white)
    dessiner_rect(color.red, window_width-100, window_height-200, 100, 50, text)
    return pygame.Rect(window_width-100, window_height-200, 100, 60)

def dealGUI():
    # Indique comment piocher
    text = font.render('DEAL', False, color.black)
    dessiner_rect(color.white, 25, 200, 100, 50, text)

# Fonction principale du jeu
def game():
    global pioche_rect

    # Initialisation des variables et des états du jeu
    game_over = False
    game_state = ""
    piochable = True
    start_time = pygame.time.get_ticks()
    
    # Définition de l'événement DEALER_DRAW en dehors de la boucle principale
    DEALER_DRAW = pygame.USEREVENT + 1
    pygame.time.set_timer(DEALER_DRAW, 500)  # Déclenche l'événement toutes les 500 millisecondes

    message = font3.render('Vous arrêtez de piocher, au croupier maintenant', True, color.white)
    pioche(dealerHand, True) # Afficher la première carte
    pioche(dealerHand, False)

    # Boucle principale du jeu
    while not game_over:

        # Affichage de l'arrière-plan et de la pioche des cartes
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(pioche_scaled, (-20, 200))
        stopGUI()
        dealGUI()
        draw_hand(playerHand)
        draw_hand(dealerHand)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or len(playerHand) > 7 or len(dealerHand) > 7:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pioche_rect.collidepoint(event.pos) and piochable:
                    pioche(playerHand)
                elif stopGUI().collidepoint(event.pos) and piochable:
                    gameDisplay.blit(message, (window_width/2 - 100, window_height-150))
                    piochable = False
                

        # Conditions de fin du jeu
        if sum(playerHand) == 21:
            blackjackGUI()
            game_state = 'bj'
            game_over = True
        elif sum(dealerHand) == 21:
            loseGUI()
            game_state = 'lose'
            game_over = True
        if sum(playerHand) > 21:
            loseGUI()
            game_state = 'lose'
            game_over = True
        elif sum(dealerHand) > 21:
            winGUI()
            game_state = 'win'
            game_over = True

        # Jeu
        if not piochable:
            if not sum(dealerHand) >= 17:
                pioche(dealerHand, True)
                game_state = 'finito'
        

        if game_state == 'finito':
            if sum(playerHand) == 21:
                blackjackGUI()
                game_state = 'bj'
                game_over = True
            elif sum(dealerHand) == 21:
                loseGUI()
                game_state = 'lose'
                game_over = True
            elif sum(playerHand) > 21:
                loseGUI()
                game_state = 'lose'
                game_over = True
            elif sum(dealerHand) > 21:
                winGUI()
                game_state = 'win'
                game_over = True
            elif sum(playerHand) < sum(dealerHand):
                loseGUI()
                game_state = 'lose'
                game_over = True
            elif sum(playerHand) > sum(dealerHand):
                winGUI()
                game_state = 'win'
                game_over = True
            else:
                drawGUI()
                game_state = 'draw'
                game_over = True

        # Affichage graphique durant le jeu
        dealerGUI()
        playerGUI()

        pygame.display.update()  # Mettre à jour l'écran une fois par boucle
        FramePerSec.tick(FPS)

    for card in dealerHand[1:]:
        if card.isHidden:
            card.hide()
            
    return game_state

def replay():
    global deck, suits, playerHand, dealerHand
    replay_button = dessiner_rect(color.blue, window_width/3, window_height-200, window_width/8+100, window_height/8, bloxat2.render('Rejouer', False, color.white))
    # Liste de cartes et enseignes
    deck = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
    suits = ["clubs", "diamonds", "hearts", "spades"]
    return replay_button

def main():
    run = True
    played = False
    result = None  # Variable pour stocker le résultat du jeu (gagné ou perdu)
    player_hand = playerGUI()
    dealer_hand = dealerGUI()
    while run:
        # Background
        gameDisplay.blit(background, (0, 0))
        if not played:
            play_button = dessiner_rect(color.red, window_width/4, window_height - 200, window_width/8, window_height/8, bloxat2.render('Jouer', False, color.white))
        else:
            # Afficher le total actuel du joueur
            gameDisplay.blit(playerGUI()[0], playerGUI()[-1])
            # Afficher le total actuel du joueur
            gameDisplay.blit(dealerGUI()[0], dealerGUI()[-1])
            
            draw_hand(playerHand)
            draw_hand(dealerHand)
            replay()
            # Afficher le résultat du jeu s'il existe
            if result:
                if result == 'bj': blackjackGUI()
                elif result == 'win': winGUI()
                elif result == 'lose': loseGUI()
                elif result == 'draw': drawGUI()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not played and play_button[-1].collidepoint(event.pos):
                    result = game()  # Stocker le résultat du jeu
                    played = True
                elif played and replay()[-1].collidepoint(event.pos):
                    played = False
                    result = None  # Réinitialiser le résultat du jeu

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    main()

# Affichage des scores
playerGUI()
dealerGUI()

pygame.time.wait(1500)
pygame.quit()
quit()
