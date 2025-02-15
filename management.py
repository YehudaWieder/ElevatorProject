import pygame.mouse
from elevator import Elevator
from floor import Floor
from button import Button
from globals import *


def get_closest_elv(building, task_pos: (int, int)):
    min_time = float("inf")
    closest_elevator = None

    for elevator in building.elevators:
        lest_task_y = elevator.get_lest_elevator_y()
        current_task_time = elevator.get_current_task_time(task_pos, lest_task_y)
        if elevator.tasks_time + current_task_time < min_time:
            min_time = elevator.tasks_time + current_task_time
            closest_elevator = elevator
    return closest_elevator, min_time


def is_button_clicked(building, pos: (int, int)):
    is_button_pressed, floor = building.is_floors_button_clicked(pos)
    if is_button_pressed  and not floor.is_elv_on_way:
        closest_elevator, min_time = get_closest_elv(building, floor.pos[1])
        if closest_elevator.current_floor != floor.floor_num:
            floor.floor_timer = min_time
            floor.is_elv_on_way = True
            closest_elevator.get_new_task(floor)




def draw_reset_button(screen, color: (int, int, int)):
    pygame.draw.circle(screen, GRAY_FOR_BUTTON_BORDER, RESET_BUTTON_POS, RESET_SIZE + 3, 0)
    pygame.draw.circle(screen, color, RESET_BUTTON_POS, RESET_SIZE, 0)
    reset_screen = pygame.font.SysFont("reset", FONT_SIZE, False, False)
    reset_screen = reset_screen.render("reset", False, WHITE)
    screen.blit(reset_screen, (RESET_BUTTON_POS[0] - 24, RESET_BUTTON_POS[1] - 10))

def reset(building, pos: (int, int)):
    if ((pos[0] - RESET_BUTTON_POS[0]) ** 2 + (pos[1] - RESET_BUTTON_POS[1]) ** 2) ** 0.5 < RESET_SIZE:
        for elevator in building.elevators:
            elevator.pos = elevator.pos[0], BASE_ELEVATOR_POS[1]
            elevator.current_floor = 0
            elevator.tasks = []
            elevator.tasks_time = 0
            elevator.suspending_for_floor = 120

        for floor in building.floors:
            floor.is_elv_on_way = False
            floor.floor_timer = 0
        return ENVIRONMENT_HEIGHT - SCREEN_HEIGHT

def reset_mouse_over(pos: (int, int), screen):
    draw_reset_button(screen, GRAY_FOR_OVER)

    if ((pos[0] - RESET_BUTTON_POS[0]) ** 2 + (pos[1] - RESET_BUTTON_POS[1]) ** 2) ** 0.5 <= RESET_SIZE:
        draw_reset_button(screen, GRAY_FOR_OVER)
        return True

def mouse_over(building, pos: (int, int), surface):
    x, y = pos
    reset_button_y = y - (ENVIRONMENT_HEIGHT - SCREEN_HEIGHT)
    reset = reset_mouse_over((x, reset_button_y), surface)
    button = None
    for floor in building.floors:
        if floor.button.is_mouse_over(pos) and floor.floor_timer == 0:
            button = True
    if reset or button:
        pygame.mouse.set_cursor(pygame.cursors.tri_left)
    else:
        pygame.mouse.set_cursor(pygame.cursors.arrow)
