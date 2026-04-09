import pygame
import random

pygame.init()

LARGEUR = 800
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Farmstar")
clock = pygame.time.Clock()
FPS = 60
VERT=pygame.Color(153,179,61)
clock.tick(FPS)
fenetre.fill((255,255,255))
pygame.draw.rect(fenetre,VERT,(0,0,800,600))
pygame.display.update()
runnin = True
fenetre.fill(VERT)


x_ferm = 375
y_ferm = 295
IMG_ferm = pygame.image.load("../pers/fermier.png")
IMG_ferm = pygame.transform.scale(IMG_ferm,(60,60))


img_vache = pygame.image.load("../pers/vache.png")
img_vache= pygame.transform.scale(img_vache,(60,60))
vaches =[]
for i in range(5):
    vache = {
        "x":100,
        "y":200,
        "dx":0,
        "dy":0
    }
    vaches.append(vache)
zone_x=0
zone_y=100
zone_w=150
zone_f=200


img_maison = pygame.image.load("../pers/maison.png")
img_maison = pygame.transform.scale(img_maison,(200,200))
x_maison= 300
y_maison=150
maison_rect = pygame.Rect(300,150,200,200).inflate(-100,-125)

field = pygame.image.load("../pers/field.png")
field = pygame.transform.scale(field,(470,300))
while runnin:
    fenetre.fill(VERT)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runnin=False
    keys=pygame.key.get_pressed()
    dx=0
    if keys[pygame.K_RIGHT]:
        dx+=1
    if keys[pygame.K_LEFT]:
        dx-=1
    for i in range(abs(dx)):
        step = 1 if dx > 0 else -1
        rect = pygame.Rect(x_ferm+step, y_ferm, 60,60)
        if not rect.colliderect(maison_rect):
            x_ferm+=step
        else :
            break
    dy=0
    if keys[pygame.K_UP]:
        dy-=1
    if keys[pygame.K_DOWN]:
        dy+=1
    for i in range(abs(dy)):
        step = 1 if dy > 0 else -1
        rect= pygame.Rect(x_ferm,y_ferm+step,60,60)
        if not rect.colliderect(maison_rect):
            y_ferm+=step
        else :
            break
    fenetre.blit(field, (-130, 90))
    for vache in vaches:
        if random.randint(0, 50) == 0:
            vache["dx"] = random.choice([-1, 0, 1])
            vache["dy"] = random.choice([-1, 0, 1])
        vache["x"] += vache["dx"] * 0.2
        vache["y"] += vache["dy"] * 0.2
        if vache["x"] < zone_x:
            vache["x"] = zone_x
        if vache["x"] > zone_x + zone_w:
            vache["x"] = zone_x + zone_w
        if vache["y"] < zone_y:
            vache["y"] = zone_y
        if vache["y"] > zone_y + zone_f:
            vache["y"] = zone_y + zone_f
        fenetre.blit(img_vache,(vache["x"],vache["y"]))
    fenetre.blit(img_maison,(x_maison,y_maison))
    fenetre.blit(IMG_ferm, (x_ferm,y_ferm))
    pygame.display.update()
pygame.quit()

