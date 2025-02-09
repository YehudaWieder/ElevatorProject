from globals import *
import pygame



class Elevator(pygame.sprite.Sprite):
    elevators = []
    velocity = 160 # P/S

    def __init__(self, current_floor : int,  pos : (int, int), size : (int, int)):
        super().__init__()

        self.image = pygame.image.load(ELV_ING_PATH)
        self.image = pygame.transform.scale(self.image, size)
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.tasks = []
        self.tasks_timer = 0
        self.suspending_for_floor = 120

        Elevator.elevators.append(self)

    def draw(self, pos, screen):
        screen.blit(self.image, pos)

    def set_suspending_in_floor(self):
        if self.suspending_for_floor == 120:
            pygame.mixer.music.play()
        if self.suspending_for_floor == 0:
            self.tasks.pop(0)
            self.suspending_for_floor = 120
        else:
            self.suspending_for_floor -= 1

    def update(self, delta_time):
        if self.tasks:
            if self.tasks[0] < self.pos_y:
                self.pos_y = max(self.pos_y - self.velocity * delta_time, self.tasks[0])
            elif self.tasks[0] > self.pos_y:
                self.pos_y = min(self.pos_y + self.velocity * delta_time, self.tasks[0])
            else:
                self.set_suspending_in_floor()
            self.tasks_timer -= 1 / 60
        else:
            self.tasks_timer = 0

    def get_lest_task(self):
        if self.tasks:
            lest_task = self.tasks[len(self.tasks) - 1]
        else:
            lest_task = self.pos_y
        return lest_task

    def get_current_task_time(self, task_pos, lest_task):
        if lest_task > task_pos:
            current_task_time = (lest_task - task_pos) / self.velocity
        elif lest_task < task_pos:
            current_task_time = (task_pos - lest_task) / self.velocity
        return current_task_time

    def get_new_task(self, task_pos):
        lest_task = self.get_lest_task()
        self.tasks.append(task_pos - ELEVATOR_HEIGHT / 2)
        self.tasks_timer += self.get_current_task_time(task_pos, lest_task) + 2





