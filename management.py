import pygame.mouse
import elevator
from globals import *


# choose the quickest elevator
def get_quickest_elv(building, task_pos: (int, int)):
    min_time = float("inf")
    quickest_elevator = None

    for elv in building.elevators:
        if elv.pos[1] == task_pos and elv.suspending_for_floor == 2:
            return elv, 0
        elif elv.pos[1] == task_pos:
            return None, None

        lest_task_y = elv.get_last_elevator_y()
        current_task_time = elevator.get_current_task_time(task_pos, lest_task_y)
        if elv.tasks_time + current_task_time < min_time:
            min_time = elv.tasks_time + current_task_time
            quickest_elevator = elv
    return quickest_elevator, min_time


# checking if button clicked and chooses elevator and then inviting him
def is_button_clicked(building, pos: (int, int)):
    """
    checks if a button was clicked
    :param building: the building to be checked
    :param pos: the mouse click position (x, y) tuple
    :return: None
    """
    # checking if button clicked
    is_button_pressed, floor = building.is_floors_button_clicked(pos)
    if is_button_pressed and not floor.is_elv_on_way:
        # choosing an elevator
        quickest_elevator, min_time = get_quickest_elv(building, floor.pos[1])
        # sending the task to the elevator
        if quickest_elevator:
            floor.floor_timer = min_time
            task_y = floor.pos[1]
            quickest_elevator.get_new_task(task_y)


# draw the reset button
def draw_reset_button(screen, color: (int, int, int)):
    pygame.draw.circle(screen, GRAY_FOR_BUTTON_BORDER, RESET_BUTTON_POS, RESET_BUTTON_SIZE + 3, 0)
    pygame.draw.circle(screen, color, RESET_BUTTON_POS, RESET_BUTTON_SIZE, 0)
    reset_screen = pygame.font.SysFont("reset", FONT_SIZE, False, False)
    reset_screen = reset_screen.render("reset", False, WHITE)
    screen.blit(reset_screen, (RESET_BUTTON_POS[0] - 24, RESET_BUTTON_POS[1] - 10))


# activating the reset function
def reset(building, pos: (int, int)):
    x, y = pos
    bx, by = RESET_BUTTON_POS
    if ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 < RESET_BUTTON_SIZE:
        for elv in building.elevators:
            elv.pos = elv.pos[0], BASE_ELEVATOR_POS_Y
            elv.current_floor = 0
            elv.tasks = []
            elv.tasks_time = 0
            elv.suspending_for_floor = 2

        for floor in building.floors:
            floor.is_elv_on_way = False
            floor.floor_timer = 0
        return ENVIRONMENT_HEIGHT - SCREEN_HEIGHT


# checking mouse over the reset button
def reset_mouse_over(pos: (int, int), screen):
    x, y = pos
    bx, by = RESET_BUTTON_POS
    if ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 <= RESET_BUTTON_SIZE:
        return True


# checking mouse over some floor button or reset button
def mouse_over(building, pos: (int, int), surface):
    x, y = pos
    reset_button_y = y - (ENVIRONMENT_HEIGHT - SCREEN_HEIGHT)
    reset = reset_mouse_over((x, reset_button_y), surface)
    button = None
    for floor in building.floors:
        if floor.button.is_mouse_over(pos) and floor.floor_timer == 0:
            button = True
    # change the cursor
    if reset or button:
        pygame.mouse.set_cursor(pygame.cursors.tri_left)
    else:
        pygame.mouse.set_cursor(pygame.cursors.arrow)
