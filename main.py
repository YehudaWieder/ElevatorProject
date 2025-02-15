import pygame.mouse

import button
from building import Building
import management
from globals import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("elevators system")
surface = pygame.Surface((ENVIRONMENT_WIDTH, ENVIRONMENT_HEIGHT))

# usr_input = True
# while usr_input:
#     surface.fill(LIGHT_BLUE)
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             usr_input = False
#             pygame.quit()
#     NUMBER_OF_FLOORS = 5
#     NUMBER_OF_ELEVATORS = 2
#     pygame.display.update()

my_building = Building(NUMBER_OF_FLOORS, NUMBER_OF_ELEVATORS)

clock = pygame.time.Clock()

previous_time = pygame.time.get_ticks()

scroll_speed = 20
scroll_y = ENVIRONMENT_HEIGHT - SCREEN_HEIGHT

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                y += scroll_y
                management.is_button_clicked(my_building, (x, y))
                reset_pos = management.reset(my_building, event.pos)
                if reset_pos is not None:
                    scroll_y = reset_pos
            elif event.button == 4:
                scroll_y = max(0, scroll_y - scroll_speed)
            elif event.button == 5:
                scroll_y = min(scroll_y + scroll_speed, ENVIRONMENT_HEIGHT - SCREEN_HEIGHT)


    current_time = pygame.time.get_ticks()
    delta_time = (current_time - previous_time) / 1000 # converting ms to seconds

    surface.fill(WHITE)
    my_building.draw(surface, delta_time)
    screen.blit(surface, (0, 0), (0, scroll_y, SCREEN_WIDTH, SCREEN_HEIGHT))

    management.draw_reset_button(screen, GRAY)
    x, y = pygame.mouse.get_pos()
    y += scroll_y
    management.mouse_over(my_building, (x, y), surface)

    previous_time = current_time
    clock.tick(REFRESH_PER_SECOND)
    pygame.display.flip()

pygame.quit()
