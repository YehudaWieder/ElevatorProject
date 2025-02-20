from elevator import *
from floor import Floor


class Building:

    def __init__(self, floors_num: int, elevators_num: int):
        self.floors = [Floor(i) for i in range(floors_num)]
        self.elevators = [Elevator(i) for i in range(elevators_num)]

    def draw(self, surface, delta_time: float) -> None:
        """
        updates and draws any floor and any elevator
        :param surface: teh pygam surface to draw on it
        :param delta_time: the time between last update and current update, float
        :return: None
        """
        # update and draw any floor
        for floor in self.floors:
            floor.update(delta_time)
            floor.draw(surface)

        # update and draw any elevator
        for elevator in self.elevators:
            elevator.update(delta_time)
            elevator.draw(surface)

    def is_floors_button_clicked(self, click_pos: (int, int)) -> tuple[bool, Floor] | tuple[bool, None]:
        """
        checks if button in any floor was clicked
        :param click_pos: the mouse click position (x, y) tuple
        :return: True or False
        """
        for floor in self.floors:
            if floor.button.onclick(click_pos):
                return True, floor
        return False, None
