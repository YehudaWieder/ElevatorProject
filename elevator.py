
from globals import *


def get_current_task_time(task_pos: int, last_task: int) -> float:
    """
    calculates the time for the new task
    :param task_pos: the y point to send an elevator there, int
    :param last_task: the last y point that the elevator needs be there, int
    :return: float
    """
    current_task_time = 0
    if last_task > task_pos:
        current_task_time = (last_task - task_pos) / ELEVATOR_VELOCITY
    elif last_task < task_pos:
        current_task_time = (task_pos - last_task) / ELEVATOR_VELOCITY
    return current_task_time


class Elevator:

    def __init__(self, elevator_num: int):
        self.elevator_num = elevator_num
        self.image = pygame.transform.scale(pygame.image.load(ELV_ING_PATH), (ELEVATOR_WIDTH, ELEVATOR_HEIGHT))
        self.active_elevator_image = pygame.transform.scale(pygame.image.load(ACTIVE_ELV_ING_PATH),(ELEVATOR_WIDTH, ELEVATOR_HEIGHT))
        self.pos = BASE_ELEVATOR_POS_X + (ELEVATOR_WIDTH * self.elevator_num), BASE_ELEVATOR_POS_Y
        self.tasks = []
        self.tasks_time = 0
        self.suspending_for_floor = 2

    def draw(self, surface) -> None:
        """
        draws the elevator
        :param surface: teh pygam surface to draw on it
        :return: None
        """
        surface.blit(self.image, self.pos)
        if self.tasks_time > 0:
            surface.blit(self.active_elevator_image, self.pos)

    def set_suspending_in_floor(self, delta_time: float) -> None:
        """
        suspends the elevator in floor for two seconds
        :param delta_time: the time between last update and current update, float
        :return: None
        """
        if self.suspending_for_floor == 2:
            pygame.mixer.music.load(DING_FILE_PATH)
            pygame.mixer.music.play()
        if self.suspending_for_floor == 0:
            self.tasks.pop(0)
            self.suspending_for_floor = 2
        else:
            self.suspending_for_floor = max(self.suspending_for_floor - delta_time, 0)

    def update(self, delta_time: float) -> None:
        """
        updates the elevator's y position
        :param delta_time: the time between last update and current update, float
        :return: None
        """
        if self.tasks:
            task_y = self.tasks[0]
            elevator_x, elevator_y = self.pos

            if task_y < elevator_y:
                self.pos = elevator_x, max(elevator_y - ELEVATOR_VELOCITY * delta_time, task_y)
            elif task_y > elevator_y:
                self.pos = elevator_x, min(elevator_y + ELEVATOR_VELOCITY * delta_time, task_y)
            else:
                self.set_suspending_in_floor(delta_time)
            self.tasks_time = max(self.tasks_time - delta_time, 0)

    def get_last_elevator_y(self) -> int:
        """
        returns the last y point that the elevator needs be there, int
        :return: the last y point that the elevator needs be there, int
        """
        current_elevator_y = self.pos[1]
        if self.tasks:
            last_task_y = self.tasks[len(self.tasks) - 1]
            return last_task_y
        else:
            return current_elevator_y


    def add_new_task(self, task_y: int) -> None:
        """
        adds a new task to the tasks array
        :param task_y: y point that the elevator needs go there, int
        :return: None
        """
        last_elevator_y = self.get_last_elevator_y()
        self.tasks_time += get_current_task_time(task_y, last_elevator_y) + 2
        self.tasks.append(task_y)
