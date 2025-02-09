from elevatorClass import Elevator
from buildingClass import Button

def get_closest_elv(task_pos : (int, int)):
    min_time = 100000
    closest_elv = None

    for elv in Elevator.elevators:
        lest_task = Elevator.get_lest_task(elv)
        current_task_time = Elevator.get_current_task_time(elv, task_pos, lest_task)
        if elv.tasks_timer + current_task_time < min_time:
            min_time = elv.tasks_timer + current_task_time
            closest_elv = elv
    return closest_elv, min_time

def is_button_clicked(pos: (int, int)):
    is_button_pressed, button_pos = Button.onclick(pos)
    if is_button_pressed:
        closest_elv, min_time = get_closest_elv(button_pos[1])
        Elevator.get_new_task(closest_elv, button_pos[1])