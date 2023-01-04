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

x, y = 130, 300


while state:

# Position des éléments
    win.blit(framework, (0, 0))
    win.blit(png, (x, y))
    print(x, y)
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
        #mur 1
        if x == 75 and 15 < y < 100:
            x == 75
        #mur 2
        elif x == 370 and -18 < y < 25:
            x = 370
        #escalier
        elif 27 < y < 135 and x == 260:
            x == 260
        #côté escalier
        elif x == 195 and 105 < y < 135:
            x == 195
        #caisse
        elif x == 325 and 95 < y < 120:
            x == 325
        #tonneau
        elif x == 160 and 90 < y < 125:
            x == 160
        #colonne de béton1
        elif x == 45 and 170 < y < 245:
            x == 45
        #colonne de béton2
        elif x ==40 and 265 < y < 310:
            x == 40
        #colonne de béton3
        elif x == -30 and 219 < y < 276:
            x == -30
        #vase
        elif x == -15 and 170 < y < 190:
            x == -15
        #mur 3 bas
        elif x == 450 and 20 < y < 97:
            x == 450
        #caisse2
        elif x == 460 and 90 < y < 135:
            x == 460
        #mur4
        elif x == 457 and 135 < y < 165:
            x == 457
        else:
            x += 5

    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        pygame.time.Clock().tick(30)
        #bord de la fenêtre
        if x == -40:
            x = -40
        #escalier
        elif 27 < y < 135 and x == 225:
            x == 225
        #coté escalier
        elif 27 < y < 135 and x == 290:
            x == 280
        #mur1 côté
        elif x == 110 and 90 < y < 170:
            x == 110
        #colonne de béton1
        elif x == 105 and 160 < y < 245:
            x == 105
        #colonne de béton2
        elif x == 100 and 260 < y < 310:
            x == 100
        #colonne de béton3
        elif x == 35 and 215 < y < 275:
            x == 35
        #vase
        elif x == 45 and 170 < y < 190:
            x == 45
        #caisse
        elif x == 380 and 90 < y < 120:
            x == 120
        #mur 3 bas
        elif x == 405 and 20 < y < 96:
            x == 405
        else:
            x -= 5

    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        pygame.time.Clock().tick(30)
        #1er mur
        if -45 < x < 80 and y == 95:
            y = 95
        #2e mur
        elif 75 < x < 230 and y == 20:
            y = 20
        #3e mur
        elif 256 < x < 375 and y == 20:
            y = 20
        #bas de la fenêtre
        elif y == 300:
            y = 300
        #colonne de béton2
        elif 53 < x < 99 and y == 265:
            y == 265
        #colonne de béton3
        elif -20 < x < 27 and y == 215:
            y == 215
        #mur4
        elif 457 < x < 459 and y == 130:
            y == 130
        else:
            y += 5
    elif pygame.key.get_pressed()[pygame.K_UP]:
        pygame.time.Clock().tick(30)
        #haut de la fenêtre
        if y == -15:
            y = -15
        #mur 2 bas
        elif 288 < x < 400 and y == 100:
            y = 100
        #escalier
        elif 260 < x < 288 and y == 135:
            y == 135
        elif 190 < x < 225 and y == 135:
            y == 135
        #tonneau
        elif 160 < x < 200 and y == 120:
            y == 120
        #mur2 bas
        elif 100 < x < 165 and y == 100:
            y == 100
        elif 100 < x < 110 and y == 170:
            y == 170
        #colonne de béton1
        elif 45 < x < 110 and y == 245:
            y == 245
        #colonne de béton3
        elif -20 < x <30 and y == 280:
            y == 280
        #mur1 bas
        elif -50 < x < 47 and y == 180:
            y == 180
        #vase
        elif -15 < x < 45 and y == 190:
            y == 190
        #caisse
        elif 325 < x < 385 and y == 125:
            y == 125
        #mur 3 bas
        elif 400 < x < 455 and y == 30:
            y == 30
        #mur 4 haut
        elif x == 460 and y == 100:
            y == 100
        else:
            y -= 5