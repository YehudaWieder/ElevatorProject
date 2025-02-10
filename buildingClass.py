from elevatorClass import *
from floorClass import *


class Building(pygame.sprite.Sprite):
    buildings = []

    def __init__(self, floors_num, elevators_num):
        super().__init__()

        self.floors_num = floors_num
        self.elevators_num = elevators_num

        Building.buildings.append(self)
        self.draw()

    def draw(self):
        for i in range(self.floors_num):
            Floor((FLOOR_POS[0], FLOOR_POS[1] - (FLOOR_HEIGHT * i)), (FLOOR_WIDTH, FLOOR_HEIGHT))

        for i in range(self.elevators_num):
            Elevator(0, (ELEVATOR_POS[0] + (ELEVATOR_WIDTH * i), ELEVATOR_POS[1]), (ELEVATOR_WIDTH, ELEVATOR_HEIGHT))
