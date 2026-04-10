import pygame


class Background:
    def __init__(self):
        self.fenetre = pygame.display.set_mode((800, 600))
        self.VERT = (153, 179, 61)
        self.field = pygame.image.load("../../assets/field.png")
        self.field = pygame.transform.scale(self.field, (470, 300))
        self.field_rect= pygame.Rect(-130,80,470,300).inflate(-275,-125)
        self.img_maison = pygame.image.load("../../assets/maison.png")
        self.img_maison = pygame.transform.scale(self.img_maison, (200, 200))
        self.x_maison = 300
        self.y_maison = 150
        self.maison_rect = pygame.Rect(300, 150, 200, 200).inflate(-100, -125)

    def afficher(self, fenetre):
        fenetre.fill(self.VERT)
        fenetre.blit(self.field, (-130, 90))
        fenetre.blit(self.img_maison, (self.x_maison, self.y_maison))
