import pygame
import random

class Cow:
    def __init__(self,x,y,w,h,image,zone):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.image= pygame.transform.scale(image, (60, 60))
        self.dx=0
        self.dy=0
        self.vitesse=0.2
        self.zone=zone
        self.faim=True
        self.timer_faim = 0

    def get_rect(self):
        return pygame.Rect(self.x+10,self.y+10,self.w-20,self.h-20)

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
        if not self.faim:
            self.timer_faim+=1
            if self.timer_faim >300:
                self.faim=True
                self.timer_faim=0

    def afficher(self,fenetre):
        fenetre.blit(self.image,(self.x,self.y))
