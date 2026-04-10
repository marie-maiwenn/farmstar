import pygame

class Marche:
    def __init__(self,x,y,w,h,image):
        self.x= x
        self.y =y
        self.image=pygame.transform.scale(image,(w,h))
        self.marche_rect=pygame.Rect(720,0,880,70)
        self.popup = False

    def afficher(self,fenetre):
        fenetre.blit(self.image,(self.x,self.y))

    def afficher_popup(self):
        self.popup=True
        pygame.display.set_mode((400,300))
