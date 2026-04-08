import pygame
import sys

# Initialisation de Pygame

pygame.init()

# Taille de la fenêtre

LARGEUR = 800

HAUTEUR = 600

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

pygame.display.set_caption("Déplacement d'un curseur")

try:
    background_image = pygame.image.load("Ferme tranquille entourée de forêt.png").convert()
    # Optionnel : Redimensionner l'image à la taille de la fenêtre
    background_image = pygame.transform.scale(background_image, (LARGEUR, HAUTEUR))
except pygame.error:
    print("Erreur : Impossible de charger l'image. Vérifie le nom du fichier !")
    pygame.quit()
    sys.exit()

BLANC = (255, 255, 255)

# Curseur (un carré)

curseur_taille = 20

curseur_x = LARGEUR // 2

curseur_y = HAUTEUR // 20

vitesse = 5

clock = pygame.time.Clock()

# Boucle principale

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

    # Récupération des touches pressées

    touches = pygame.key.get_pressed()

    if touches[pygame.K_LEFT]:
        curseur_x -= vitesse

    if touches[pygame.K_RIGHT]:
        curseur_x += vitesse

    if touches[pygame.K_UP]:
        curseur_y -= vitesse

    if touches[pygame.K_DOWN]:
        curseur_y += vitesse

    # Empêcher le curseur de sortir de l'écran

    curseur_x = max(0, min(curseur_x, LARGEUR - curseur_taille))

    curseur_y = max(0, min(curseur_y, HAUTEUR - curseur_taille))

    # Affichage

    fenetre.blit(background_image, (0, 0))

    pygame.draw.rect(fenetre, BLANC, (curseur_x, curseur_y, curseur_taille, curseur_taille))

    pygame.display.flip()

    clock.tick(60)

