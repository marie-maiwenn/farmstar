import pygame
import random

class cow:
    def __init__(self,x,y,w,h,image,zone):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.image=image
        self.dx=0
        self.dy=0
        self.vitesse=0.2
        self.zone=zone
        self.faim=True

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.w,self.h)

    def bouger(self):
        if random.randint(0, 50) == 0:
            self.dx=random.choice([-1,0,1])
            self.dy=random.choice([-1,0,1])
        new_x= self.x+self.dx*self.vitesse
        rect_x=pygame.Rect(new_x,self.y,self.w,self.h)
        if self.zone.contains(rect_x):
            self.x=new_x
        new_y = self.y + self.dy * self.vitesse
        rect_y = pygame.Rect(self.x, new_y, self.w, self.h)
        if self.zone.contains(rect_y):
            self.y = new_y

    def afficher(self,fenetre):
        fenetre.blit(self.image,(self.x,self.y))
