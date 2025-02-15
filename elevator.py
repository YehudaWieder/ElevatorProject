from floor import Floor
from globals import *


class Elevator:

    def __init__(self, elevator_num: int):
        self.elevator_num = elevator_num
        self.image = pygame.image.load(ELV_ING_PATH)
        self.image = pygame.transform.scale(self.image, (ELEVATOR_WIDTH, ELEVATOR_HEIGHT))
        self.pos = BASE_ELEVATOR_POS[0] + (ELEVATOR_WIDTH * self.elevator_num), BASE_ELEVATOR_POS[1]
        self.current_floor = 0
        self.tasks = []
        self.tasks_time = 0
        self.suspending_for_floor = 120


    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def set_suspending_in_floor(self):
        if self.suspending_for_floor == 120:
            pygame.mixer.music.load(DING_FILE_PATH)
            pygame.mixer.music.play()
        if self.suspending_for_floor == 0:
            self.tasks[0].is_elv_on_way = False
            self.tasks.pop(0)
            self.suspending_for_floor = 120
        else:
            self.suspending_for_floor -= 1

    def update(self, delta_time: float):
        if self.tasks:
            task_y = self.tasks[0].pos[1]# - (ELEVATOR_HEIGHT / 2)
            self.current_floor = None
            elevator_x, elevator_y = self.pos
            if task_y < elevator_y:
                self.pos = elevator_x, max(elevator_y - ELEVATOR_VELOCITY * delta_time, task_y)
            elif task_y > elevator_y:
                self.pos = elevator_x, min(elevator_y + ELEVATOR_VELOCITY * delta_time, task_y)
            else:
                self.current_floor = self.tasks[0].floor_num
                self.set_suspending_in_floor()
            self.tasks_time -= 1 / REFRESH_PER_SECOND
        else:
            self.tasks_time = 0

    def get_lest_elevator_y(self):
        current_elevator_y = self.pos[1]
        if self.tasks:
            lest_task_y = self.tasks[len(self.tasks) - 1].pos[1]
            return lest_task_y
        else:
            return current_elevator_y

    def get_current_task_time(self, task_pos: int, lest_task: int):
        current_task_time = 0
        if lest_task > task_pos:
            current_task_time = (lest_task - task_pos) / ELEVATOR_VELOCITY
        elif lest_task < task_pos:
            current_task_time = (task_pos - lest_task) / ELEVATOR_VELOCITY
        return current_task_time

    def get_new_task(self, floor):
        lest_elevator_y = self.get_lest_elevator_y()
        self.tasks.append(floor)
        self.tasks_time += self.get_current_task_time(floor.pos[1], lest_elevator_y) + 2
