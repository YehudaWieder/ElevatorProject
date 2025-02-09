import pygame
from elevatorClass import Elevator
from buildingClass import Building
from floorClass import Floor
from buildingClass import Button
from globals import *


pygame.init()
pygame.mixer.init()
# input_screen = pygame.display.set_mode((350, 200))
# pygame.display.set_caption("elevators system input")
# input_screen.fill((LIGHT_BLUE))
# input_screen.blit(input_screen, (0, 0))
# run = True
# while run:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             run = False
#     pygame.display.update()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("elevators system")
pygame.mixer.music.load(DING_FILE_PATH)
# surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen.fill(LIGHT_BLUE)
# screen.blit(surface, (0, 0))

Building(10, 3)

clock = pygame.time.Clock()

previous_time = pygame.time.get_ticks()

run = True
while run:
    screen.fill(LIGHT_BLUE)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Button.onclick(event.pos)
            # for elv in Elevator.elevators:
            #     elv.get_task(event.pos)

    current_time = pygame.time.get_ticks()


    # Floor.floors.draw(screen)
    for floor in Floor.floors:
        floor.draw(screen, floor.pos)

    for elv in Elevator.elevators:
        elv.draw((elv.pos_x, elv.pos_y), screen)
        elv.update((current_time - previous_time) / 1000)


    previous_time = current_time
    pygame.display.update()
    clock.tick(60)

pygame.quit()

# if __name__ == '__main__':
#     main()