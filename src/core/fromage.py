import pygame

class Fromagerie:
    def __init__(self, x, y, w, h, image):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.image = pygame.transform.scale(image, (self.w, self.h))
        self.rect=pygame.Rect(self.x, self.y, self.w, self.h)
        self.zone_interaction = self.rect.inflate(-40,-40)
        self.ouvert = False
        self.interface = False
        self.font = pygame.font.SysFont(None, 24)
        self.btn_transformer = pygame.Rect(300,300,200,50)

    def afficher(self, fenetre):
        fenetre.blit(self.image,(self.x, self.y))

    def afficher_interface(self, fenetre, fermier):
        if not self.interface:
            return
        fond = pygame.Rect(200,150,400,300)
        pygame.draw.rect(fenetre,(200,200,255), fond, border_radius=15)
        pygame.draw.rect(fenetre,(0,0,100), fond, 5, border_raddius=15)
        txt = self.font.render(f"Lait disponible : {fermier.inventaire['Lait']}", True, (0,0,0))
        fenetre.blit(txt,(250,200))
        couleur_btn = (10,255,100) if fermier.inventaire['Lait']>0 else (150,150,150)
        pygame.draw.rect(fenetre, couleur_btn, self.btn_transformer, border_radius=10)
        txt_btn = self.font.render("Transformer 1 Lait -> 1 Fromage", True,(0,0,0))
        fenetre.blit(txt_btn,(self.btn_transformer.x+10, self.btn_transformer.y+15))

    def gerer_clic(self, pos, fermier):
        if self.btn_transformer.collidepoint(pos):
            if fermier.inventaire["Lait"]>0:
                fermier.inventaire["Lait"]-=1
                fermier.inventaire["Fromage"]+=1
                return True
        return False