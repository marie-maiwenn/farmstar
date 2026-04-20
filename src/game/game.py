import pygame
from src.core.fermier import Farmer
from src.core.fromage import Fromagerie
from src.core.vaca import Cow
from src.core.objets import  Foin, Foret
from src.ui.background import Background
from src.core.marche import Marche
from src.ui.morale import BarreMorale

pygame.init()
bg=Background()
fenetre = pygame.display.set_mode((800, 600))
clock=pygame.Clock()
barre = BarreMorale()

img_fermier = pygame.image.load("../../assets/fermier.png")
img_vache = pygame.image.load("../../assets/vache.png")
img_marche=pygame.image.load("../../assets/shop_sprite.png")
img_fromagerie= pygame.image.load("../../assets/fromagerie.png")
img_foret=pygame.image.load("../../assets/foret.png")

fromagerie=Fromagerie(600,420,180,180, img_fromagerie)
marche = Marche(550,-50,400,200,img_marche)
fermier = Farmer(375,295,60,60,img_fermier)

zone_vaches= pygame.Rect(0,100,200,250)
vaches = []
for i in range(5):
    vaches.append(Cow(100,200,60,60,img_vache,zone_vaches))
lait_caisse = 0

foin =[]

foret1 = []
l_bloc = 200
h_bloc = 200
y_f=600-h_bloc+30
espacement = l_bloc-30
for x in range(-10,800,espacement):
    nv_bloc = Foret(x,y_f,l_bloc,h_bloc,img_foret)
    foret1.append(nv_bloc)
foret2=[]
for x in range(-10,200,espacement):
    mini_bloc = Foret(x,y_f-70, l_bloc,90, img_foret)
    foret2.append(mini_bloc)

caisse_rect = pygame.Rect(220,300,40,40)
runnin = True

while runnin:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                zone_interaction=marche.marche_rect.inflate(100,100)
                zvint=bg.field_rect.inflate(100,100)
                zone_maison=bg.maison_rect.inflate(60,60)
                if fermier.get_rect().colliderect(zone_interaction):
                    marche.popup = not marche.popup
                if fermier.get_rect().colliderect(zvint):
                    fermier.mode_visee = not fermier.mode_visee
                if fermier.get_rect().colliderect(zone_maison):
                    if bg.heures>=20 or bg.heures<6:
                        print(f"Zzz... Fin du jour {bg.jour}.")
                        bg.jour +=1
                        bg.heures = 6
                        bg.minutes = 0
                    else :
                        print("Il est trop tôt pour aller dormir !")
            if event.key == pygame.K_f:
                if fromagerie.ouvert and fermier.get_rect().colliderect(fromagerie.zone_interaction):
                    fromagerie.interface = not fromagerie.interface
            if event.key == pygame.K_SPACE:
                if fermier.mode_visee and fermier.inventaire["Foin"]>0:
                    fermier.inventaire["Foin"]-=1
                    mx, my = pygame.mouse.get_pos()
                    centre_x = fermier.x + fermier.w//2
                    centre_y = fermier.y + fermier.h //2
                    nouveau_tir = Foin(centre_x, centre_y, mx, my)
                    foin.append(nouveau_tir)
                    fermier.mode_visee = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1 :
                if fromagerie.interface:
                    fromagerie.gerer_clic(pygame.mouse.get_pos(), fermier)
                if marche.popup:
                    action = marche.gerer_clic(pygame.mouse.get_pos(), fermier)
                    if action== "NOUVELLE_VACHE":
                        nouvelle_vache = Cow(100,200,60,60, img_vache, zone_vaches)
                        vaches.append(nouvelle_vache)
                        barre.modifier_score(-5)
                    elif action == "AGRANDIR_ENCLOS":
                        print("L'enclos s'agrandit !")
                        bonus_w=10
                        bonus_h=20
                        zone_vaches.width+=bonus_w
                        zone_vaches.height+=bonus_h
                        bg.agrandir_champ(bonus_w,bonus_h)
                        caisse_rect.x = zone_vaches.right + 20
                        caisse_rect.y = zone_vaches.bottom - 50
                        barre.modifier_score(+15)
                        for bloc in foret2[:]:
                            if bloc.rect.colliderect(zone_vaches):
                                foret2.remove(bloc)
                                barre.modifier_score(-10)
                    elif action == "CONSTRUIRE_FROMAGERIE":
                        print("La fromagerie est débloqué !")
                        fromagerie.ouvert = True
                        for bloc in foret1[:]:
                            if bloc.rect.colliderect(fromagerie.rect):
                                foret1.remove(bloc)
                                barre.modifier_score(-10)

    bg.update_temps()
    if bg.heures>=24:
        print("Le fermier s'est évanoui de fatigue !")
        bg.jour+=1
        bg.heures=6
        bg.minutes=0
    if not marche.popup and not fromagerie.interface:
        keys=pygame.key.get_pressed()
        obstacles=[bg.maison_rect,bg.field_rect, marche.marche_rect]
        if fromagerie.ouvert :
            obstacles.append(fromagerie.rect)
        for bloc in foret1:
            obstacles.append(bloc.rect)
        for bloc in foret2:
            obstacles.append(bloc.rect)
        fermier.deplacer(keys,obstacles)

    for vache in vaches:
        vache.bouger()
        for fv in foin[:]:
            fv.update()
            if fv.au_sol:
                est_mange = False
                for vache in vaches:
                    if vache.faim and vache.get_rect().colliderect(fv.get_rect()):
                        vache.faim = False
                        vache.timer_faim=0
                        lait_caisse+=1
                        print(f"Lait déposé dans la caisse !🥛 (Total : {lait_caisse})")
                        est_mange = True
                        break
                if est_mange :
                    if fv in foin:
                        foin.remove(fv)

    bg.afficher(fenetre)

    for bloc in foret1:
        bloc.afficher(fenetre)
    for bloc in foret2:
        bloc.afficher(fenetre)

    marche.afficher(fenetre)

    pygame.draw.rect(fenetre, (101, 67, 33), caisse_rect)
    pygame.draw.rect(fenetre, (0, 0, 0), caisse_rect, 2)

    if lait_caisse > 0:
        txt_lait = marche.font_texte.render(str(lait_caisse), True, (255, 255, 255))
        fenetre.blit(txt_lait, (caisse_rect.x + 12, caisse_rect.y + 10))

    if fermier.mode_visee:
        mx, my = pygame.mouse.get_pos()
        centre_x = fermier.x + fermier.w//2
        centre_y = fermier.y + fermier.h//2
        pygame.draw.line(fenetre,(255,255,255),(centre_x,centre_y),(mx,my),2)
        pygame.draw.circle(fenetre,(255,0,0),(mx, my),5)

    if fromagerie.ouvert:
        fromagerie.afficher(fenetre)

    fermier.afficher(fenetre)

    for vache in vaches:
        vache.afficher(fenetre)

    for fv in foin :
        fv.afficher(fenetre)

    if fermier.get_rect().colliderect(caisse_rect) and lait_caisse>0:
        fermier.inventaire["Lait"]+=lait_caisse
        print(f"✅ Récolte terminée ! Tu as ramassé {lait_caisse} bouteilles.")
        lait_caisse = 0

    bg.afficher_nuit(fenetre)

    ui_rect = pygame.Rect(10,10,240,90)
    pygame.draw.rect(fenetre,(40,40,40,200), ui_rect, border_radius=10)
    pygame.draw.rect(fenetre,(200,180,0), ui_rect,2,border_radius=10)
    font_ui = pygame.font.SysFont(None,22)
    temps_str=f"Jour {bg.jour}   |   {bg.heures:02d}h{bg.minutes:02d}"
    texte_temps = font_ui.render(temps_str,True, (255,255,255))
    fenetre.blit(texte_temps,(20,20))
    texte_ag = font_ui.render(f"Argent : {fermier.argent}$", True,(150,255,150))
    fenetre.blit(texte_ag,(20,45))
    inv = fermier.inventaire
    texte_inv = font_ui.render(f"Foin: {inv['Foin']} | Lait: {inv['Lait']} | Fro: {inv['Fromage']}", True, (200,200,200))
    fenetre.blit(texte_inv, (20,70))

    barre.afficher(fenetre)

    if fromagerie.interface:
        fromagerie.afficher_interface(fenetre, fermier)

    marche.afficher_popup(fenetre, fermier)

    pygame.display.update()