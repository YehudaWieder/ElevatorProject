from pygame.examples.vgrade import timer

from globals import *
import pygame



class Elevator(pygame.sprite.Sprite):

    elevators = pygame.sprite.Group()

    def __init__(self, current_floor : int,  pos : (int, int), size : (int, int)):
        super().__init__()

        self.id = len(Elevator.elevators)
        self.current_floor = current_floor
        self.image = pygame.image.load(ELV_ING_PATH)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(midtop=pos)
        self.tasks = []
        self.tasks_time = 0
        self.timer_for_floor = 60
        self.v = 160 # P/S

        Elevator.elevators.add(self)

    def update(self, delta_time):
        if self.tasks:
            if self.tasks[0] < self.rect.y:
                self.rect.y = max(self.rect.y - self.v * delta_time, self.tasks[0])
            elif self.tasks[0] > self.rect.y:
                self.rect.y = min(self.rect.y + self.v * delta_time, self.tasks[0])
            else:
                if self.timer_for_floor == 120:
                    pygame.mixer.music.play()
                if self.timer_for_floor == 0:
                    self.tasks.pop(0)
                    self.timer_for_floor = 120
                else:
                    self.timer_for_floor -= 1




    def get_task(self, pos):
        self.tasks.append(pos[1])
        self.tasks_time = self.rect.y - pos[1]



