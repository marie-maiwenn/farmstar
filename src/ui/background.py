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

        self.jour = 1
        self.heures = 6
        self.minutes = 0
        self.compteur_temps = 0
        self.voile_nuit = pygame.Surface((800,600))
        self.voile_nuit.fill((0,0,40))

    def update_temps(self):
        self.compteur_temps+=1
        if self.compteur_temps>=200:
            self.compteur_temps=0
            self.minutes+=10
            if self.minutes>=60:
                self.minutes = 0
                self.heures +=1

    def get_opacite_nuit(self):
        if 6<= self.heures<18:
            return 0
        elif 18<= self.heures<20:
            return 60
        elif 20<= self.heures<22:
            return 120
        else :
            return 180

    def afficher_nuit(self, fenetre):
        opacite = self.get_opacite_nuit()
        if opacite>0:
            self.voile_nuit.set_alpha(opacite)
            fenetre.blit(self.voile_nuit,(0,0))

    def afficher(self, fenetre):
        fenetre.fill(self.VERT)
        fenetre.blit(self.field, (self.x_field, self.y_field))
        fenetre.blit(self.img_maison, (self.x_maison, self.y_maison))

    def agrandir_champ(self, bonus_largeur, bonus_hauteur):
        self.largeur_field +=bonus_largeur
        self.hauteur_field +=bonus_hauteur
        self.field=pygame.transform.scale(self.field_original,(self.largeur_field, self.hauteur_field))
        self.field_rect.width +=bonus_largeur
        self.field_rect.height +=bonus_hauteur
        self.x_field-=5
        self.y_field-=2