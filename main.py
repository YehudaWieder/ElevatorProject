
from building import Building
import management
from globals import *

pygame.init()
pygame.mixer.music.load(DING_FILE_PATH)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("elevators system")
surface = pygame.Surface((ENVIRONMENT_WIDTH, ENVIRONMENT_HEIGHT))

my_building = Building(NUMBER_OF_FLOORS, NUMBER_OF_ELEVATORS)

previous_time = pygame.time.get_ticks()

scroll_speed = 20
scroll_y = ENVIRONMENT_HEIGHT - SCREEN_HEIGHT

run = True

#check if the number of the floors and elevators are legal
if len(my_building.elevators) <= 0:
    print("There isn't exist elevators in the building, you must using the stairs")
    run = False
elif len(my_building.floors) <= len(my_building.elevators):
    print("To use the program the number of floors must be at least one more than the number of elevators")
    run = False

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # checking click event
            if event.button == 1:
                x, y = event.pos
                environment_y = y + scroll_y
                # checking if elevator invited
                management.is_button_clicked(my_building, (x, environment_y))
                # checking reset click
                reset_pos = management.reset(my_building, event.pos)
                if reset_pos is not None:
                    scroll_y = reset_pos
            # checking scroll event
            elif event.button == 4:
                scroll_y = max(0, scroll_y - scroll_speed)
            elif event.button == 5:
                scroll_y = min(scroll_y + scroll_speed, ENVIRONMENT_HEIGHT - SCREEN_HEIGHT)

    # Calculating the time between updates
    current_time = pygame.time.get_ticks()
    delta_time = (current_time - previous_time) / 1000  # converting ms to seconds
    previous_time = current_time

    # draw & update surface
    surface.fill(WHITE)
    my_building.draw(surface, delta_time)
    screen.blit(surface, (0, 0), (0, scroll_y, SCREEN_WIDTH, SCREEN_HEIGHT))

    # draw reset button
    management.draw_reset_button(screen, GRAY)

    # check if mouse over a button
    x, y = pygame.mouse.get_pos()
    y += scroll_y
    management.mouse_over(my_building, (x, y))

    pygame.display.flip()

pygame.quit()
