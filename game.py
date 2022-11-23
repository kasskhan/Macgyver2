import pygame

pygame.init() #initialisation
size = (800, 800) #Taille de l'écran
win = pygame.display.set_mode(size)
pygame.display.set_caption('Jeu Macgiver') #Titre de la fenêtre
framework = pygame.image.load('/image/real_background.jpg')

state = True #Lancer l'application

while state:

    win.blit(framework(0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False