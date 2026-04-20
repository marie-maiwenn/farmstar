import pygame

class Foin :
    def __init__(self, start_x, start_y, target_x,target_y):
        self.start_x=start_x
        self.start_y = start_y
        self.target_x = target_x
        self.target_y = target_y
        self.x = start_x
        self.y = start_y
        self.taille = 10
        self.t = 0.0
        self.vitesse = 0.01
        self.hauteur_max = 60
        self.au_sol = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.taille, self.taille)

    def update(self):
        if self.au_sol :
            return
        self.t+=self.vitesse
        if self.t >=1.0:
            self.t=1.0
            self.au_sol = True
        self.x = self.start_x+(self.target_x-self.start_x)*self.t
        self.y = self.start_y+(self.target_y-self.start_y)*self.t

    def afficher(self, fenetre):
        ombre_rect = pygame.Rect(self.x, self.y + 5, self.taille, self.taille//2)
        pygame.draw.ellipse(fenetre,(100,100,100), ombre_rect)
        hauteur = 0 if self.au_sol else 4*self.hauteur_max*self.t*(1-self.t)
        rect_visuel = pygame.Rect(self.x, self.y - hauteur, self.taille, self.taille)
        pygame.draw.rect(fenetre,(200,180,0), rect_visuel)

class Foret :
    def __init__(self,x,y,w,h,image):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.image=pygame.transform.scale(image,(self.w, self.h))
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h).inflate(-20,-20)

    def afficher(self,fenetre):
        fenetre.blit(self.image,(self.x,self.y))