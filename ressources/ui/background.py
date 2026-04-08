import pygame
import sys

# Initialisation de Pygame

pygame.init()

# Taille de la fenêtre

LARGEUR = 800
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Farmstar")
clock = pygame.time.Clock()
FPS = 60
VERT=pygame.Color(29,78,17)
clock.tick(FPS)
fenetre.fill((255,255,255))
pygame.draw.rect(fenetre,VERT,(0,0,800,600))
pygame.display.update()
runnin = True
fenetre.fill(VERT)

# Curseur
x_ferm = 40
y_ferm = 30
IMG_ferm = pygame.image.load("../pers/fermier.png")
IMG_ferm = pygame.transform.scale(IMG_ferm,(60,60))


while runnin:
    fenetre.fill(VERT)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runnin=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x_ferm+=1
    if keys[pygame.K_LEFT]:
        x_ferm-=1
    if keys[pygame.K_UP]:
        y_ferm-=1
    if keys[pygame.K_DOWN]:
        y_ferm+=1
    fenetre.blit(IMG_ferm, (x_ferm,y_ferm))
    pygame.display.update()
pygame.quit()

#curseur_taille = 20

#curseur_x = LARGEUR // 2

#curseur_y = HAUTEUR // 20
#vitesse = 5

#clock = pygame.time.Clock()

# Boucle principale

#while True:

    #for event in pygame.event.get():

        #if event.type == pygame.QUIT:
            #pygame.quit()

            #sys.exit()

    # Récupération des touches pressées

    #touches = pygame.key.get_pressed()

    #if touches[pygame.K_LEFT]:
        #curseur_x -= vitesse

    #if touches[pygame.K_RIGHT]:
        #curseur_x += vitesse

    #if touches[pygame.K_UP]:
        #curseur_y -= vitesse

    #if touches[pygame.K_DOWN]:
        #curseur_y += vitesse

    # Empêcher le curseur de sortir de l'écran

    #curseur_x = max(0, min(curseur_x, LARGEUR - curseur_taille))

    #curseur_y = max(0, min(curseur_y, HAUTEUR - curseur_taille))

    # Affichage

    #fenetre.blit(background_image, (0, 0))

    #pygame.draw.rect(fenetre, BLANC, (curseur_x, curseur_y, curseur_taille, curseur_taille))

    #pygame.display.flip()

    #clock.tick(60)

