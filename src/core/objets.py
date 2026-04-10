import pygame

class Nourriture:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.taille=10

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.taille,self.taille)

    def afficher(self,fenetre):
        pygame.draw.rect(fenetre,(200,180,0),self.get_rect())
