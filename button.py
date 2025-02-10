import pygame
from globals import *


class Button:

    buttons = []

    def __init__(self, pos : (int, int), size: int):

        self.pos = pos
        self.size = size
        self.pressed_timer = 0

        Button.buttons.append(self)

    def draw(self, pos : (int, int), size :int, screen):
        if self.pressed_timer == 0:
            color = GRAY
        else:
            color = RED
            pygame.draw.rect(screen, LIGHT_BLUE,(50, pos[1] - BUTTON_SIZE, 90 , 40) , 0, 30)
            floor_timer = pygame.font.SysFont("floor timer", FONT_SIZE, True, False)
            floor_timer = floor_timer.render(str(int(self.pressed_timer) + 1), False, BLACK)
            screen.blit(floor_timer, (pos[0] - 50, pos[1] - 10))

        pygame.draw.circle(screen, color, pos, size)

    def update(self):
        if self.pressed_timer > 0:
            self.pressed_timer -= 1 / REFRESH_PER_SECOND
        else:
            self.pressed_timer = 0

    def on_click(self, pos: (int, int)):
        if ((pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2)**0.5 <= self.size:
            return True
        return False

    @classmethod
    def onclick(cls, pos : (int, int)):
        for button in cls.buttons:
            if button.on_click(pos):
                return True, button, button.pos
        return False, None, None


