from globals import *
import pygame



class Elevator(pygame.sprite.Sprite):
    elevators = []
    velocity = 160 # P/S

    def __init__(self, current_floor : int,  pos : (int, int), size : (int, int)):
        super().__init__()

        self.id = len(Elevator.elevators)
        self.current_floor = current_floor
        self.image = pygame.image.load(ELV_ING_PATH)
        self.image = pygame.transform.scale(self.image, size)
        # self.rect = self.image.get_rect(midtop=pos)
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.tasks = []
        self.tasks_timer = 0
        self.timer_for_floor = 120

        Elevator.elevators.append(self)

    def draw(self, pos, screen):
        screen.blit(self.image, pos)

    def update(self, delta_time):
        if self.tasks:
            if self.tasks[0] < self.pos_y:
                self.pos_y = max(self.pos_y - self.velocity * delta_time, self.tasks[0])
            elif self.tasks[0] > self.pos_y:
                self.pos_y = min(self.pos_y + self.velocity * delta_time, self.tasks[0])
            else:
                if self.timer_for_floor == 120:
                    pygame.mixer.music.play()
                if self.timer_for_floor == 0:
                    self.tasks.pop(0)
                    self.timer_for_floor = 120
                else:
                    self.timer_for_floor -= 1
            self.tasks_timer -= 1 / 60
        else:
            self.tasks_timer = 0

    def get_task(self, pos):
        if self.tasks:
            lest_task = self.tasks[len(self.tasks) - 1]
        else:
            lest_task = self.pos_y

        if lest_task > pos[1]:
            self.tasks_timer += (lest_task - pos[1]) / self.velocity + 2
        elif lest_task < pos[1]:
            self.tasks_timer += (pos[1] - lest_task) / self.velocity + 2

        self.tasks.append(pos[1] - ELEVATOR_HEIGHT / 2)



