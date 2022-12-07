import pygame

pygame.init() #initialisation
size = (563, 375) #Taille de l'écran
win = pygame.display.set_mode(size)
pygame.display.set_caption('Jeu Macgiver') #Titre de la fenêtre
framework = pygame.image.load('image/real_background.jpg')


png = pygame.image.load('image/walk_cycle.gif')

object = pygame.image.load('image/gold.jpg')
object = pygame.transform.scale(object, (30, 30))

state = True #Lancer l'application

x, y = 0, 0

mouvement = ""
fleche_haut = pygame.K_UP
fleche_bas = pygame.K_DOWN
fleche_gauche = pygame.K_LEFT
fleche_droite = pygame.K_RIGHT

while state:

    win.blit(framework, (0, 0))
    win.blit(png, (x, y))
    win.blit(object, (430, 300))

    if mouvement == fleche_droite:
        pygame.time.Clock().tick(30)
        x += 10

    elif mouvement == fleche_gauche:
        pygame.time.Clock().tick(30)
        x -= 10

    elif mouvement == fleche_haut:
        pygame.time.Clock().tick(30)
        y += 10

    if mouvement == fleche_bas:
        pygame.time.Clock().tick(30)
        y -= 10

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False