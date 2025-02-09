import pygame.draw
from globals import *
from elevatorClass import Elevator


class Button:

    buttons = []

    def __init__(self, pos : (int, int), size: int):

        self.pos = pos
        self.size = size

        Button.buttons.append(self)

    def draw(self, pos : (int, int), size :int, screen):
        pygame.draw.circle(screen, GRAY, pos, size, 50 )

    def on_click(self, pos: (int, int)):
        if ((pos[0] - self.pos[0])**2 + (pos[1] - self.pos[1])**2)**0.5 <= self.size:
            Elevator.elevators[2].get_task(pos)
            return True
        return False

    @classmethod
    def onclick(cls, pos : (int, int)):
        for button in cls.buttons:
            if button.on_click(pos):
                break

    def __del__(self):
        pass
