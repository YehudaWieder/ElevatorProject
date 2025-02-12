from elevator import *
from floor import *


class Building:
    buildings = []

    def __init__(self, floors_num, elevators_num):

        self.floors = Floor.floors
        self.elevators = Elevator.elevators
        self.create_building(floors_num, elevators_num)

        Building.buildings.append(self)

    def create_building(self, floors_num, elevators_num):
        for i in range(floors_num):
            Floor((FLOOR_POS[0], FLOOR_POS[1] - (FLOOR_HEIGHT * i)))
            if i == 0:
                Floor.floors[0].is_elv_here = True

        for i in range(elevators_num):
            Elevator((ELEVATOR_POS[0] + (ELEVATOR_WIDTH * i), ELEVATOR_POS[1]))

    def draw(self, screen, delta_time):
        for floor in Floor.floors:
            floor.draw(screen, floor.pos)

        for elevator in Elevator.elevators:
            elevator.draw(elevator.pos, screen)
            elevator.update(delta_time)

        for button in Button.buttons:
            button.update()