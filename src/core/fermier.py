import pygame

class Farmer :
    def __init__(self, x, y, w, h, image):
        self.x= x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.transform.scale(image, (self.w, self.h))
        self.vitesse = 2
        self.argent =100
        self.inventaire = {"Foin": 0, "Lait":0, "Fromage":0}
        self.niveau_enclos = 0
        self.a_fromagerie = False
        self.mode_visee= False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h).inflate(-10,-10)

    def deplacer(self, keys, obstacles):
        dx=0
        dy=0
        if keys[pygame.K_RIGHT]:
            dx=self.vitesse
        if keys[pygame.K_LEFT]:
            dx=-self.vitesse
        if keys[pygame.K_DOWN]:
            dy=self.vitesse
        if keys[pygame.K_UP]:
            dy=-self.vitesse
        for i in range(abs(dx)):
            step = 1 if dx>0 else -1
            rect = pygame.Rect(self.x+step, self.y, self.w, self.h)
            if not any(rect.colliderect(o) for o in obstacles):
                self.x+=step
            else :
                break
        for i in range(abs(dy)):
            step = 1 if dy>0 else -1
            rect = pygame.Rect(self.x, self.y+step, self.w, self.h)
            if not any(rect.colliderect(o) for o in obstacles):
                self.y+=step
            else :
                break

    def afficher(self,fenetre):
        fenetre.blit(self.image,(self.x,self.y))

    def interact(self,obj_rect):
        zone = obj_rect.inflate(20,20)
        return self.get_rect().colliderect(zone)
