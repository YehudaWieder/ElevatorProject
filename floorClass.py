import pygame
from button import *


class Floor(pygame.sprite.Sprite):

    floors = []

    def __init__(self, pos : (int, int), size : (int, int)):
        super().__init__()

        self.floor_num = len(Floor.floors)
        self.pos = pos
        self.image = pygame.image.load(FLOOR_IMG_PATH)
        self.image = pygame.transform.scale(self.image, size)
        self.pos = pos
        self.button = Button((pos[0] + FLOOR_WIDTH / 2, pos[1] + FLOOR_HEIGHT / 2), 20)

        Floor.floors.append(self)

    def draw(self, screen, pos):
        screen.blit(self.image, pos)
        pygame.draw.line(screen, BLACK, pos,(pos[0] + FLOOR_WIDTH, pos[1]), 10)
        self.button.draw((pos[0] + FLOOR_WIDTH / 2, pos[1] + FLOOR_HEIGHT / 2), 20, screen)



