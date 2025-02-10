import pygame
from button import *


class Floor(pygame.sprite.Sprite):

    floors = []

    def __init__(self, pos : (int, int), size : (int, int)):
        super().__init__()

        self.floor_num = len(self.floors)
        self.image = pygame.image.load(FLOOR_IMG_PATH)
        self.image = pygame.transform.scale(self.image, size)
        self.pos = pos
        self.middle_pos = pos[0] + (FLOOR_WIDTH / 2), pos[1] + (FLOOR_HEIGHT / 2)
        self.button = Button((pos[0] + (FLOOR_WIDTH / 2), pos[1] + (FLOOR_HEIGHT / 2)), 20)

        Floor.floors.append(self)

    def draw(self, screen, pos):
        screen.blit(self.image, pos)

        if self.floor_num < (len(self.floors) - 1):
            pygame.draw.line(screen, BLACK, pos,(pos[0] + FLOOR_WIDTH, pos[1]), 10)
        self.button.draw(self.middle_pos, BUTTON_SIZE, screen)

        floor_num = pygame.font.SysFont("floor number", FONT_SIZE, True, False)
        floor_num = floor_num.render(str(self.floor_num), False, LIGHT_BLUE)
        screen.blit(floor_num, (self.middle_pos[0] - FONT_SIZE / 4, self.middle_pos[1] - FONT_SIZE / 4))


