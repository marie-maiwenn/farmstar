import pygame
from src.core.fermier import Farmer
from src.core.vaca import Cow
from src.core.objets import Nourriture
from src.ui.background import Background
from src.core.marche import Marche

pygame.init()
bg=Background()
fenetre = pygame.display.set_mode((800, 600))
clock=pygame.Clock()

img_fermier = pygame.image.load("../../assets/fermier.png")
img_vache = pygame.image.load("../../assets/vache.png")
img_marche=pygame.image.load("../../assets/shop_sprite.png")

marche = Marche(550,-50,400,200,img_marche)
fermier = Farmer(375,295,60,60,img_fermier)
zone_vaches= pygame.Rect(0,100,200,250)
vaches = []
for i in range(5):
    vaches.append(Cow(100,200,60,60,img_vache,zone_vaches))
nourritures =[]

runnin = True
while runnin:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                zone_interaction=marche.marche_rect.inflate(100,100)
                if fermier.get_rect().colliderect(zone_interaction):
                    marche.popup = not marche.popup
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1 and marche.popup:
                action = marche.gerer_clic(pygame.mouse.get_pos(), fermier)
                if action== "NOUVELLE_VACHE":
                    nouvelle_vache = Cow(100,200,60,60, img_vache, zone_vaches)
                    vaches.append(nouvelle_vache)
                elif action == "AGRANDIR_ENCLOS":
                    print("L'enclos s'agrandit !")
                    bonus_w=25
                    bonus_h=50
                    zone_vaches.width+=bonus_w
                    zone_vaches.height+=bonus_h
                    bg.agrandir_cahmp(bonus_w,bonus_h)
                elif action == "CONSTRUIRE_FROMAGERIE":
                    print("La fromagerie est débloqué !")
    if not marche.popup:
        keys=pygame.key.get_pressed()
        fermier.deplacer(keys,[bg.maison_rect,bg.field_rect, marche.marche_rect])
    for vache in vaches:
        vache.bouger()
    bg.afficher(fenetre)
    marche.afficher(fenetre)
    fermier.afficher(fenetre)
    for vache in vaches:
        vache.afficher(fenetre)
    for nourriture in nourritures :
        for vache in vaches :
            if vache.faim and vache.get_rect().colliderect(nourriture.get_rect()):
                vache.faim=False
                vache.timer_faim=0
                nourritures.remove(nourriture)
                break
        nourriture.afficher(fenetre)
    marche.afficher_popup(fenetre, fermier)
    pygame.display.update()

