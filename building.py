from elevator import *
from floor import *


class Building:

    def __init__(self, floors_num: int, elevators_num: int):
        self.floors = [Floor(i) for i in range(floors_num)]
        self.elevators = [Elevator(i) for i in range(elevators_num)]


    def draw(self, surface, delta_time):
        for floor in self.floors:
            floor.draw(surface)
            floor.update(delta_time)

        for elevator in self.elevators:
            elevator.update(delta_time)
            elevator.draw(surface)

    def is_floors_button_clicked(self, click_pos: (int, int)):
        for floor in self.floors:
            if floor.button.onclick(click_pos):
                return True, floor
        return False, None