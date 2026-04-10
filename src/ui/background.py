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


img_maison = pygame.image.load("../../assets/maison.png")
img_maison = pygame.transform.scale(img_maison,(200,200))
x_maison= 300
y_maison=150
maison_rect = pygame.Rect(300,150,200,200).inflate(-100,-125)

field = pygame.image.load("../../assets/field.png")
field = pygame.transform.scale(field,(470,300))

while runnin:
    fenetre.fill(VERT)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runnin=False
    fenetre.blit(field, (-130, 90))
    fenetre.blit(img_maison,(x_maison,y_maison))
    pygame.display.update()
pygame.quit()

