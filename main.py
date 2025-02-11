from buildingClass import Building
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

building = Building(NUMBER_OF_FLOORS, NUMBER_OF_ELEVATORS)

clock = pygame.time.Clock()

previous_time = pygame.time.get_ticks()

run = True
while run:
    surface.fill(LIGHT_BLUE)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                management.is_button_clicked(event.pos)

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - previous_time) / 1000

    building.draw(surface, delta_time)

    surface.scroll(SCREEN_WIDTH, ENVIRONMENT_HEIGHT)
    screen.blit(surface, (0, 0), )

    previous_time = current_time
    pygame.display.update()
    clock.tick(REFRESH_PER_SECOND)

pygame.quit()
