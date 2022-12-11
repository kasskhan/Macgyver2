import pygame

pygame.init() #initialisation
size = (563, 375) #Taille de l'écran
win = pygame.display.set_mode(size)
pygame.display.set_caption('Jeu Macgiver') #Titre de la fenêtre
framework = pygame.image.load('image/real_background.jpg')


png = pygame.image.load('image/walk_cycle.gif')
png = pygame.transform.scale(png, (100, 100))

object = pygame.image.load('image/gold.jpg')
object = pygame.transform.scale(object, (30, 30))

state = True #Lancer l'application

x, y = 0, 0


while state:

# Position des éléments
    win.blit(framework, (0, 0))
    win.blit(png, (x, y))
    win.blit(object, (430, 300))

# Réinitialiser la fenètre
    pygame.display.update()

# Fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

#Déplacer le personnage
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        pygame.time.Clock().tick(30)
        if x == 75 and 15 < y < 100:
            x == 75
        elif x == 370 and -18 < y < 25:
            x = 370
        else:
            x += 5

    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        pygame.time.Clock().tick(30)
        if x == -40:
            x = -40
        else:
            x -= 5

    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        pygame.time.Clock().tick(30)
        if -45 < x < 80 and y == 95:
            y = 95
        elif 100 < x < 230 and y == 20:
            y = 20
        elif 256 < x < 375 and y == 20:
            y = 20
        else:
            y += 5
    elif pygame.key.get_pressed()[pygame.K_UP]:
        pygame.time.Clock().tick(30)
        if y == -15:
            y = -15
        else:
            y -= 5