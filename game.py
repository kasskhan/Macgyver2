import pygame

pygame.init() #initialisation
size = (563, 375) #Taille de l'écran
win = pygame.display.set_mode(size)
pygame.display.set_caption('Jeu Macgiver') #Titre de la fenêtre
framework = pygame.image.load('image/real_background.jpg')
png = pygame.image.load('image/walk_cycle.gif')
state = True #Lancer l'application
x, y = 0, 0

while state:

    win.blit(framework, (0, 0))
    win.blit(png, (x, y))

    pygame.time.Clock().tick(30)
    x += 20
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False