import pygame as pg
import random
import color

pg.init()
pg.display.set_caption("BlackJack Game")
clock = pg.time.Clock()
window_width = 800
window_height = 600
run = True



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

def choiceGUI():
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

# Boucle de jeu
while run:
    choiceGUI()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(choiceGUI())

        

    pg.display.update()  # Mettre à jour l'écran une fois par boucle

    clock.tick(30)
pg.quit()
quit()