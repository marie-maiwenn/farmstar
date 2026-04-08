import pygame
import sys

pygame.init()

# --- Fenêtre ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farmstar")

clock = pygame.time.Clock()

# --- Chargement des images ---
IMG_MENU_PATH = "menu_image.png"
IMG_CHAMP_PATH = "Ferme tranquille entourée de forêt.png"
IMG_COLLISION_PATH = "Colision_image.png"  # <--- Ta carte en Noir et Blanc

try:
    img_menu = pygame.image.load(IMG_MENU_PATH).convert_alpha()
    img_champ = pygame.image.load(IMG_CHAMP_PATH).convert()
    # On charge la carte de collision
    img_collision = pygame.image.load(IMG_COLLISION_PATH).convert()
except FileNotFoundError as e:
    print("❌ Image introuvable :", e)
    pygame.quit()
    sys.exit()

# Mise à l'échelle pour que tout corresponde parfaitement aux 800x600
img_menu = pygame.transform.scale(img_menu, (WIDTH, HEIGHT))
img_champ = pygame.transform.scale(img_champ, (WIDTH, HEIGHT))
img_collision = pygame.transform.scale(img_collision, (WIDTH, HEIGHT))

# --- Zones cliquables Menu ---
BTN_JOUER = pygame.Rect(250, 280, 300, 80)
BTN_QUITTER = pygame.Rect(250, 380, 300, 80)


# ---------------------------------------------------------
# ✅ BOUCLE DE JEU
# ---------------------------------------------------------
def game_loop():
    curseur_taille = 10
    curseur_x = WIDTH // 2
    curseur_y = HEIGHT // 2
    vitesse = 4

    running_game = True
    while running_game:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running_game = False  # Retour menu

        # --- Déplacement curseur avec vérification de collision ---
        touches = pygame.key.get_pressed()

        # On calcule la position suivante potentielle
        prochain_x = curseur_x
        prochain_y = curseur_y

        if touches[pygame.K_LEFT]:  prochain_x -= vitesse
        if touches[pygame.K_RIGHT]: prochain_x += vitesse
        if touches[pygame.K_UP]:    prochain_y -= vitesse
        if touches[pygame.K_DOWN]:  prochain_y += vitesse

        # Vérification des limites de l'écran pour éviter les erreurs de pixels hors-champ
        prochain_x = max(0, min(prochain_x, WIDTH - 1))
        prochain_y = max(0, min(prochain_y, HEIGHT - 1))

        # TEST DE COLLISION : On regarde la couleur sur la carte N&B
        # On prend le pixel au centre du curseur pour la précision
        couleur = img_collision.get_at((int(prochain_x), int(prochain_y)))

        # Si le pixel est Blanc (255,255,255), on autorise le mouvement
        # On vérifie seulement les 3 premières valeurs (R, G, B)
        if couleur[0] > 200 and couleur[1] > 200 and couleur[2] > 200:
            curseur_x = prochain_x
            curseur_y = prochain_y

        # --- Affichage jeu ---
        screen.blit(img_champ, (0, 0))  # On affiche le beau terrain

        # On dessine le joueur (un rond rouge pour mieux voir)
        pygame.draw.circle(screen, (255, 0, 0), (int(curseur_x), int(curseur_y)), curseur_taille)

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


# Lancer le programme
menu_loop()
pygame.quit()
