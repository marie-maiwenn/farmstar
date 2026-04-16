import pygame

class BarreMorale:
    def __init__(self, x=300,y=20,w=200, h=20):
        self.score = 50
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.font=pygame.font.SysFont(None,20)

    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, (255, 100, 100), (self.x, self.y, self.w // 2, self.h))
        pygame.draw.rect(fenetre, (100, 255, 100), (self.x + self.w // 2, self.y, self.w // 2, self.h))
        pygame.draw.line(fenetre, (255, 0, 0), (self.x + self.w // 2, self.y - 5),(self.x + self.w // 2, self.y + self.h + 5), 3)
        pos_curseur = self.x + (self.score / 100) * self.w
        pygame.draw.circle(fenetre, (255, 255, 255), (int(pos_curseur), self.y + self.h // 2), 6)
        fenetre.blit(self.font.render("Profit", True, (255, 255, 255)), (self.x - 40, self.y + 3))
        fenetre.blit(self.font.render("Écolo", True, (255, 255, 255)), (self.x + self.w + 5, self.y + 3))

    def modifier_score(self, valeur):
        self.score+=valeur
        if self.score>100:
            self.score=100
        elif self.score<0:
            self.score=0