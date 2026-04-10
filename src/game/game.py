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
    keys=pygame.key.get_pressed()
    fermier.deplacer(keys,[bg.maison_rect,bg.field_rect, marche.marche_rect])
    for vache in vaches:
        vache.bouger()
    bg.afficher(fenetre)
    marche.afficher(fenetre)
    fermier.afficher(fenetre)
    #Marche.afficher_popup(marche)/creer une nouvelle fenetre
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
    pygame.display.update()

