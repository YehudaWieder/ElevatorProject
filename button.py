import pygame.draw
from globals import *


class Button:

    buttons = []

    def __init__(self, pos : (int, int), size: int, color : (int, int, int), screen, func):

        self.pos = pos
        self.size = size
        self.color = color
        self.screen = screen
        self.func = func

        Button.buttons.append(self)
        # self.draw((200, 500), 50, BLACK, screen)


    def draw(self, pos : (int, int), size :int, color : (int, int, int) , screen):
        pygame.draw.circle(screen, color, pos, size, 50 )

    def on_click(self, pos: (int, int)):
        if ((pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2)**0.5 <= self.size:
            self.func()
            return True
        return False

    @classmethod
    def onclick(cls, pos : (int, int)):
        for button in cls.buttons:
            if button.on_click(pos):
                break

    def __del__(self):
        pass
