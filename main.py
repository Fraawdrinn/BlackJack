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
font3 = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 36)
bloxat = pygame.font.Font('assets/Bloxat.ttf', 56)

# Chargement d'images de la pioche des cartes
pioche_img = pygame.image.load('assets/cartes/card-extras/card_back.png')
pioche_scaled = pygame.transform.scale(pioche_img, (200, 200))
pioche_rect = pioche_scaled.get_rect(topleft=(-20, 200))

# Initialisation des mains du joueur et du croupier
playerHand = ['player']
dealerHand = ['dealer']

# Liste de cartes et enseignes
cards = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
    2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
    2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
    2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
suits = ["clubs", "diamonds", "hearts", "spades"]

# Fonction pour dessiner un rectangle sur l'écran et afficher du texte à l'intérieur
def dessiner_rect(rect_color, rect_x, rect_y, rect_width, rect_height, text):
    draw = pygame.draw.rect(gameDisplay, rect_color, (rect_x, rect_y, rect_width, rect_height))
    gameDisplay.blit(text, (rect_x + 15, rect_y + 15))
    return (rect_x, rect_y, rect_width, rect_height, draw)

# Classe pour les cartes
class Card:
    def __init__(self) -> None:
        self.suit = random.choice(suits)
        self.value = random.choice(cards)
        cards.remove(self.value)
        self.isHidden = False
        if isinstance(self.value, int) and self.value < 10:
            self.image = pygame.image.load(f'assets/cartes/{self.suit}/card_{self.suit}_0{self.value}.png')
        else:
            self.image = pygame.image.load(f'assets/cartes/{self.suit}/card_{self.suit}_{self.value}.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.back = pygame.image.load('assets/cartes/card-extras/card_back.png')
        self.back = pygame.transform.scale(self.back, (150, 150))
        self.back_rect = self.back.get_rect()
        self.rect = self.image.get_rect()

    # Masquer ou montrer la carte
    def hide(self):
        if not self.isHidden:
            self.isHidden = True
        else:
            self.isHidden = False

    # Distribuer une carte à une main
    def distrib(self, hand):
        self.hand = hand[0]
        self.parent = hand
        hand.append(self.value)

    # Afficher la carte sur l'écran
    def draw(self):
        if not self.isHidden:
            if self.hand == "player":
                gameDisplay.blit(self.image, (self.rect.x + (len(self.parent) * 50), self.rect.y + window_height - 100))
            else:
                gameDisplay.blit(self.image, (self.rect.x + (len(self.parent) * 50), self.rect.y))
        else:
            if self.hand == "player":
                gameDisplay.blit(self.back, (self.back_rect.x + (len(self.parent) * 50), self.back_rect.y + window_height - 100))
            else:
                gameDisplay.blit(self.back, (self.back_rect.x + (len(self.parent) * 50), self.back_rect.y))

# Fonction pour piocher une carte dans une main
def pioche(hand, statement=True):
    new_card = Card()
    new_card.distrib(hand)
    if not statement:
        new_card.hide()
    new_card.draw()

# Calculer la somme des cartes dans une main
def sum(hand):
    total = 0
    for el in hand:
        if isinstance(el, int):
            total += el
        elif el == 'A':
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        elif el == 'player' or el == 'dealer':
            pass
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

def dealerGUI():
    # Affichage du score du croupier
    text = "Croupier: " + str(sum(dealerHand))
    dealerTotalGUI = font.render(text, True, color.light_blue)   
    gameDisplay.fill(color.bg, ((window_width - 120), 110, 120, 20))
    gameDisplay.blit(dealerTotalGUI, (window_width - 120, 110))

def winGUI():
    # Affichage en cas de victoire
    gameDisplay.blit(background, (0, 0))
    text = bloxat.render('VICTOIRE', True, color.green)
    dessiner_rect(color.bg, (window_width/2 - 50), (window_height/2), 200, 200, text)
    print("victoire")

def loseGUI():
    # Affichage en cas de défaite
    gameDisplay.blit(background, (0, 0))
    text = bloxat.render('DEFAITE', True, color.red)
    dessiner_rect(color.bg, (window_width/2 - 70), (window_height/2), 200, 200, text)
    print("défaite")

def drawGUI():
    # Affichage en cas d'égalité
    gameDisplay.blit(background, (0, 0))
    text = bloxat.render('ÉGALITÉ', True, color.grey)
    dessiner_rect(color.bg, (window_width/2 - 50), (window_height/2), 200, 200, text)
    print("égalité")

def blackjackGUI():
    # Affichage en cas de Blackjack
    gameDisplay.blit(background, (0, 0))
    text = bloxat.render('BLACKJACK', True, color.purple)
    dessiner_rect(color.bg, (window_width/2 - 100), (window_height/2), 200, 200, text)
    print("Blackjack")

def stopGUI():
    # Affiche le bouton pour arrêter de piocher
    text = font1.render('Arrêter de piocher', False, color.white)
    dessiner_rect(color.red, window_width-100, window_height-200, 100, 50, text)
    return pygame.Rect(window_width-100, window_height-200, 100, 60)

# Fonction principale du jeu
def main():
    global pioche_rect

    # Affichage de l'arrière-plan et de la pioche des cartes
    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(pioche_scaled, (-20, 200))

    # Initialisation des variables et des états du jeu
    game_over = False
    game_state = ""
    piochable = True
    message = font3.render('Vous arrêtez de piocher, au croupier maintenant', True, color.white)
    pioche(dealerHand, True)
    pioche(dealerHand, False)

    # Boucle principale du jeu
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or len(playerHand) > 7 or len(dealerHand) > 7:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_b:
                    pass
                elif event.key == pygame.K_SPACE:
                    pioche(dealerHand, False)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pioche_rect.collidepoint(event.pos) and piochable:
                    pioche(playerHand)
                elif stopGUI().collidepoint(event.pos):
                    gameDisplay.blit(message, (window_width/2 - 100, window_height-150))
                    piochable = False

        # Conditions de fin du jeu
        if sum(playerHand) == 21:
            blackjackGUI()
            game_over = True
        if sum(dealerHand) == 21:
            loseGUI()
            game_over = True
        if sum(playerHand) > 21:
            loseGUI()
            game_over = True
        if sum(dealerHand) > 21:
            winGUI()
            game_over = True

        # Jeu
        if not piochable:
            pygame.time.wait(500)
            while not sum(dealerHand) >= 17:
                pioche(dealerHand, False)
                game_state = 'finito'

        if game_state == 'finito':
            if sum(playerHand) == 21:
                blackjackGUI()
                game_over = True
            elif sum(dealerHand) == 21:
                loseGUI()
                game_over = True
            elif sum(playerHand) > 21:
                loseGUI()
                game_over = True
            elif sum(playerHand) < sum(dealerHand):
                loseGUI()
                game_over = True
            elif sum(dealerHand) > 21:
                winGUI()
                game_over = True
            elif sum(playerHand) > sum(dealerHand):
                winGUI()
                game_over = True
            else:
                drawGUI()
                game_over = True

        # Affichage graphique durant le jeu
        dealerGUI()
        playerGUI()
        stopGUI()

        pygame.display.update()  # Mettre à jour l'écran une fois par boucle
        FramePerSec.tick(FPS)
      
    return

if __name__ == "__main__":
    main()

# Affichage des scores
playerGUI()
dealerGUI()

pygame.time.wait(1500)
pygame.quit()
quit()