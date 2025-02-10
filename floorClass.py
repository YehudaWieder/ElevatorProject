from button import *


class Floor(pygame.sprite.Sprite):
    floors = []

    def __init__(self, pos: (int, int), size: (int, int)):
        super().__init__()

        self.floor_num = len(self.floors)
        self.image = pygame.image.load(FLOOR_IMG_PATH)
        self.image = pygame.transform.scale(self.image, size)
        self.pos = pos
        self.button = Button((pos[0] + (FLOOR_WIDTH / 2), pos[1] + (FLOOR_HEIGHT / 2)), 20)

        Floor.floors.append(self)

    def write_floor_num(self, screen):
        floor_num = pygame.font.SysFont("floor number", FONT_SIZE, True, False)
        floor_num = floor_num.render(str(self.floor_num), False, LIGHT_BLUE)
        screen.blit(floor_num, (self.pos[0] + (FLOOR_WIDTH / 2.2), self.pos[1] + (FLOOR_HEIGHT / 2.5)))

    def draw_timer(self, screen):
        if self.button.pressed_timer > 0:
            pygame.draw.rect(screen, LIGHT_BLUE, (50, self.pos[1] + BUTTON_SIZE, 90, 40), 0, 30)
            floor_timer = pygame.font.SysFont("floor timer", FONT_SIZE, True, False)
            floor_timer = floor_timer.render(str(int(self.button.pressed_timer) + 1), False, BLACK)
            screen.blit(floor_timer, (self.pos[0] + FLOOR_WIDTH / 6, self.pos[1] + FLOOR_HEIGHT / 2.5))

    def draw(self, screen, pos):
        screen.blit(self.image, pos)
        if self.floor_num < (len(self.floors) - 1):
            pygame.draw.line(screen, BLACK, pos, (pos[0] + FLOOR_WIDTH, pos[1]), 7)
        self.draw_timer(screen)
        self.button.draw((pos[0] + (FLOOR_WIDTH / 2), pos[1] + (FLOOR_HEIGHT / 2)), BUTTON_SIZE, screen)
        self.write_floor_num(screen)
