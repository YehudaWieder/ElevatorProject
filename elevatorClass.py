from floorClass import Floor
from globals import *


class Elevator:
    elevators = []
    velocity = 160  # P/S

    def __init__(self, pos: (int, int)):

        self.size = ELEVATOR_WIDTH, ELEVATOR_HEIGHT
        self.image = pygame.image.load(ELV_ING_PATH)
        self.image = pygame.transform.scale(self.image, self.size)
        self.current_floor = 0
        self.pos = pos
        self.tasks = []
        self.tasks_timer = 0
        self.suspending_for_floor = 120

        Elevator.elevators.append(self)

    def draw(self, pos, screen):
        screen.blit(self.image, pos)

    def set_suspending_in_floor(self):
        if self.suspending_for_floor == 120:
            pygame.mixer.music.load(DING_FILE_PATH)
            pygame.mixer.music.play()
        if self.suspending_for_floor == 0:
            Floor.floors[self.tasks[0].floor_num].is_elv_on_way = False
            self.tasks.pop(0)
            self.suspending_for_floor = 120
        else:
            self.suspending_for_floor -= 1

    def update(self, delta_time):
        if self.tasks:
            task = self.tasks[0].pos[1] - (ELEVATOR_HEIGHT / 2)
            self.current_floor = None
            if task < self.pos[1]:
                self.pos = self.pos[0], max(self.pos[1] - self.velocity * delta_time, task)
            elif task > self.pos[1]:
                self.pos = self.pos[0], min(self.pos[1] + self.velocity * delta_time, task)
            else:
                self.current_floor = self.tasks[0].floor_num
                self.set_suspending_in_floor()
            self.tasks_timer -= 1 / REFRESH_PER_SECOND
        else:
            self.tasks_timer = 0

    def get_lest_task(self):
        if self.tasks:
            lest_task = self.tasks[len(self.tasks) - 1].pos[1] - (ELEVATOR_HEIGHT / 2)
        else:
            lest_task = self.pos[1]
        return lest_task

    def get_current_task_time(self, task_pos, lest_task):
        if lest_task > task_pos:
            current_task_time = (lest_task - task_pos) / self.velocity
        elif lest_task < task_pos:
            current_task_time = (task_pos - lest_task) / self.velocity
        return current_task_time

    def get_new_task(self, button):
        lest_task = self.get_lest_task()
        self.tasks.append(button)
        self.tasks_timer += self.get_current_task_time(button.pos[1], lest_task) + 2
