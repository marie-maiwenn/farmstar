
import pygame
import sys
import os

pygame.init()

# --- Fenêtre ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farmstar")

clock = pygame.time.Clock()

# --- Chargement des images ---
IMG_MENU_PATH = "menu_image.png"
IMG_CHAMP_PATH = "Ferme tranquille entourée de forêt.png"

try:
    img_menu = pygame.image.load(IMG_MENU_PATH).convert_alpha()
    img_champ = pygame.image.load(IMG_CHAMP_PATH).convert()
except FileNotFoundError as e:
    print("❌ Image introuvable :", e)
    pygame.quit()
    sys.exit()

# Mise à l'échelle
img_menu = pygame.transform.scale(img_menu, (WIDTH, HEIGHT))
img_champ = pygame.transform.scale(img_champ, (WIDTH, HEIGHT))

# --- Zones cliquables ---
BTN_JOUER = pygame.Rect(250, 280, 300, 80)
BTN_QUITTER = pygame.Rect(250, 380, 300, 80)


# ---------------------------------------------------------
# ✅ BOUCLE DE JEU
# ---------------------------------------------------------
def game_loop():

    curseur_taille = 20
    curseur_x = WIDTH // 2
    curseur_y = HEIGHT // 2
    vitesse = 5

    running_game = True
    while running_game:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running_game = False  # Retour menu

        # Déplacement curseur
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:  curseur_x -= vitesse
        if touches[pygame.K_RIGHT]: curseur_x += vitesse
        if touches[pygame.K_UP]:    curseur_y -= vitesse
        if touches[pygame.K_DOWN]:  curseur_y += vitesse

        # Limites
        curseur_x = max(0, min(curseur_x, WIDTH - curseur_taille))
        curseur_y = max(0, min(curseur_y, HEIGHT - curseur_taille))

        # Affichage jeu
        screen.blit(img_champ, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (curseur_x, curseur_y, curseur_taille, curseur_taille))

        pygame.display.flip()


# ---------------------------------------------------------
# ✅ BOUCLE DE MENU
# ---------------------------------------------------------
def menu_loop():

    running_menu = True
    while running_menu:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if BTN_JOUER.collidepoint(event.pos):
                    game_loop()
                if BTN_QUITTER.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Affichage menu
        screen.blit(img_menu, (0, 0))

        pygame.display.flip()


# ---------------------------------------------------------
# ✅ Lancer le jeu
# ---------------------------------------------------------
menu_loop()
pygame.quit()

