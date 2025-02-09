import pygame
from button import *


class Floor(pygame.sprite.Sprite):

    floors = pygame.sprite.Group()

    def __init__(self, pos : (int, int), size : (int, int)):
        super().__init__()

        self.floor_num = len(Floor.floors)
        self.pos = pos
        self.image = pygame.image.load(FLOOR_IMG_PATH)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(midtop=pos)
        Button((pos[0], pos[1] + (FLOOR_HEIGHT / 2)), 20, GRAY,"???", self.floor_click)

        Floor.floors.add(self)

    def floor_click(self):
        pass

