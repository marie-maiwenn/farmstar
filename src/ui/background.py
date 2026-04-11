import pygame


class Background:
    def __init__(self):
        self.fenetre = pygame.display.set_mode((800, 600))
        self.VERT = (153, 179, 61)
        self.field_original = pygame.image.load("../../assets/field.png")
        self.largeur_field = 470
        self.hauteur_field = 300
        self.field = pygame.transform.scale(self.field_original,(self.largeur_field, self.hauteur_field))
        self.field_rect = pygame.Rect(7,142,195,175)
        self.x_field=-130
        self.y_field=90
        self.img_maison = pygame.image.load("../../assets/maison.png")
        self.img_maison = pygame.transform.scale(self.img_maison, (200, 200))
        self.x_maison = 300
        self.y_maison = 150
        self.maison_rect = pygame.Rect(300, 150, 200, 200).inflate(-100, -125)

    def afficher(self, fenetre):
        fenetre.fill(self.VERT)
        fenetre.blit(self.field, (self.x_field, self.y_field))
        fenetre.blit(self.img_maison, (self.x_maison, self.y_maison))

    def agrandir_cahmp(self, bonus_largeur, bonus_hauteur):
        self.largeur_field +=bonus_largeur
        self.hauteur_field +=bonus_hauteur
        self.field=pygame.transform.scale(self.field_original,(self.largeur_field, self.hauteur_field))
        self.field_rect.width +=bonus_largeur
        self.field_rect.height +=bonus_hauteur
        self.x_field-=5
        self.y_field-=2