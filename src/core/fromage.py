import pygame

class Fromagerie:
    def __init__(self, x, y, w, h, image):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.image = pygame.transform.scale(image, (self.w, self.h))