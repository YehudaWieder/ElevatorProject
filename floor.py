from button import *

class Floor:
    floors = []

    def __init__(self, pos: (int, int)):

        self.floor_num = len(self.floors)
        self.size = FLOOR_WIDTH, FLOOR_HEIGHT
        self.image = pygame.image.load(FLOOR_IMG_PATH)
        self.image = pygame.transform.scale(self.image, self.size)
        self.pos = pos
        self.button = Button((pos[0] + (FLOOR_WIDTH / 2), pos[1] + (FLOOR_HEIGHT / 2)), self.floor_num)
        self.is_elv_on_way = False

        Floor.floors.append(self)


    def draw_timer(self, screen):
        if self.button.pressed_timer > 0:
            pygame.draw.rect(screen, LIGHT_BLUE, (self.pos[0] + 5, self.pos[1] + 20, 90, 40), 0, 30)
            floor_timer = pygame.font.SysFont("floor timer", FONT_SIZE, True, False)
            floor_timer = floor_timer.render(str(int(self.button.pressed_timer) + 1), False, BLACK)
            screen.blit(floor_timer, (self.pos[0] + FLOOR_WIDTH / 6, self.pos[1] + FLOOR_HEIGHT / 2.5))

    def draw(self, screen, pos):
        screen.blit(self.image, pos)
        if self.floor_num < (len(self.floors) - 1):
            pygame.draw.line(screen, BLACK, pos, (pos[0] + FLOOR_WIDTH, pos[1]), 7)
        self.draw_timer(screen)
        self.button.draw((pos[0] + (FLOOR_WIDTH / 2), pos[1] + (FLOOR_HEIGHT / 2)), screen)
