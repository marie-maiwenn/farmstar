import pygame

class Marche:
    def __init__(self,x,y,w,h,image):
        self.x= x
        self.y =y
        self.image=pygame.transform.scale(image,(w,h))
        self.marche_rect=pygame.Rect(720,0,880,70)
        self.popup = False
        self.font_titre = pygame.font.SysFont(None,40)
        self.font_texte = pygame.font.SysFont(None, 24)
        self.btn_achat_foin = pygame.Rect(120,250,120,40)
        self.btn_achat_vache = pygame.Rect(260, 250, 120, 40)
        self.btn_achat_enclos = pygame.Rect(400, 250, 130, 40)
        self.btn_achat_fromagerie = pygame.Rect(550, 250, 130, 40)
        self.btn_vente_lait = pygame.Rect(250, 400, 120, 40)
        self.btn_vente_fromage = pygame.Rect(400, 400, 120, 40)

    def afficher(self,fenetre):
        fenetre.blit(self.image,(self.x,self.y))

    def _dessiner_bouton(self, fenetre, rect, texte, couleur_fond, actif = True):
        fond = couleur_fond if actif else (150,150,150)
        pygame.draw.rect(fenetre,fond, rect, border_radius = 8)
        pygame.draw.rect(fenetre,(0,0,0), rect,2, border_radius=8)
        img_texte=self.font_texte.render(texte,True,(0,0,0))
        txt_rect = img_texte.get_rect(center=rect.center)
        fenetre.blit(img_texte, txt_rect)

    def afficher_popup(self,fenetre,fermier):
        if not self.popup:
            return
        menu_rect= pygame.Rect(80,80,640,440)
        pygame.draw.rect(fenetre,(240,230,200), menu_rect, border_radius=15)
        pygame.draw.rect(fenetre,(139,69,19), menu_rect,5, border_radius=15)

        titre= self.font_titre.render("Marché", True,(0,0,0))
        fenetre.blit(titre,(280,100))
        infos = f"Argent : {fermier.argent} $  |  Foin : {fermier.inventaire['Foin']}  |  Lait : {fermier.inventaire['Lait']}  | fromage : {fermier.inventaire['Fromage']}"
        txt_infos = self.font_texte.render(infos, True,(0,100,0))
        fenetre.blit(txt_infos,(120,150))
        titre_achat = self.font_texte.render("--- ACHETER ---", True, (100,0,0))
        fenetre.blit(titre_achat,(120,210))
        self._dessiner_bouton(fenetre, self.btn_achat_foin, "Foin (-10$)",(150,255,150), fermier.argent >=10)
        self._dessiner_bouton(fenetre, self.btn_achat_vache, "Vache (-50$)",(150,255,150), fermier.argent>=50)
        texte_enclos = f"Enclos (-100$) [{fermier.niveau_enclos}/3]"
        actif_enclos = fermier.argent >= 100 and fermier.niveau_enclos < 3
        self._dessiner_bouton(fenetre, self.btn_achat_enclos, texte_enclos, (150, 255, 150), actif_enclos)
        texte_fromag = "Fromagerie (Déjà acquis)" if fermier.a_fromagerie else "Fromagerie (-300$)"
        actif_fromag = fermier.argent >= 300 and not fermier.a_fromagerie
        self._dessiner_bouton(fenetre, self.btn_achat_fromagerie, texte_fromag, (150, 255, 150), actif_fromag)
        titre_vente =self.font_texte.render("--- VENDRE ---", True,(0,0,100))
        fenetre.blit(titre_vente,(120,360))
        self._dessiner_bouton(fenetre, self.btn_vente_lait, "Lait (+15$)",(255,150,150), fermier.inventaire['Lait'] >0)
        if fermier.a_fromagerie:
            self._dessiner_bouton(fenetre,self.btn_vente_fromage, "Fromage (+40$)",(255,150,150), fermier.inventaire['Fromage']>0)
        else :
            self._dessiner_bouton(fenetre, self.btn_vente_fromage,"Bloqué", (100,100,100), False)

    def gerer_clic(self, pos_souris, fermier):
        action = None
        if self.btn_achat_foin.collidepoint(pos_souris) and fermier.argent>=10:
            fermier.argent-=10
            fermier.inventaire["Foin"]+=1
        elif self.btn_achat_vache.collidepoint(pos_souris) and fermier.argent>=50:
            fermier.argent -=50
            action = "NOUVELLE_VACHE"
            return action
        elif self.btn_achat_enclos.collidepoint(pos_souris) and fermier.argent>=100 and fermier.niveau_enclos <3:
            fermier.argent -=100
            fermier.niveau_enclos+=1
            action = "AGRANDIR_ENCLOS"
            return action
        elif self.btn_achat_fromagerie.collidepoint(pos_souris) and fermier.argent>=300 and not fermier.a_fromagerie:
            fermier.argent -=300
            fermier.a_fromagerie = True
            action = "CONSTRUIRE_FROMAGERIE"
            return action
        elif self.btn_vente_lait.collidepoint(pos_souris) and fermier.inventaire["Lait"]>0:
            fermier.inventaire["Lait"]-=1
            fermier.argent+=40
        elif self.btn_vente_fromage.collidepoint(pos_souris) and fermier.a_fromagerie and fermier.inventaire["Fromage"]>0:
            fermier.invetnaire["Fromage"]-=1
            fermier.argent+=40