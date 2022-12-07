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

    win.blit(framework, (0, 0))
    win.blit(png, (x, y))
    win.blit(object, (430, 300))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        pygame.time.Clock().tick(30)
        x += 5

    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        pygame.time.Clock().tick(30)
        x -= 5

    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        pygame.time.Clock().tick(30)
        y += 5

    elif pygame.key.get_pressed()[pygame.K_UP]:
        pygame.time.Clock().tick(30)
        y -= 5
