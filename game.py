import pygame

pygame .init() #initialisation
size = (400, 400) #Taille de l'écran
pygame.display.set_mode(size)
pygame.display.set_caption('Jeu Macgiver') #Titre de la fenêtre

state = True #Lancer l'application

while state:
    pygame.display.update()