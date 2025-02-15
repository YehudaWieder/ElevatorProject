from button import *

class Floor:

    def __init__(self, floor_level: int):
        self.floor_num = floor_level
        self.image = pygame.image.load(FLOOR_IMG_PATH)
        self.image = pygame.transform.scale(self.image, (FLOOR_WIDTH, FLOOR_HEIGHT))
        pygame.draw.rect(self.image, BLACK, (0, 0, FLOOR_WIDTH, FLOOR_SPACER_HEIGHT))
        self.pos = (GROUND_FLOOR_POS[0], GROUND_FLOOR_POS[1] - (FLOOR_HEIGHT * self.floor_num))
        self.button = Button(self.floor_num)
        self.is_elv_on_way = False
        self.floor_timer = 0


    def draw_timer(self, screen):
        if self.floor_timer > 0:
            pygame.draw.rect(screen, WHITE, (self.pos[0] + 5, self.pos[1] + 20, 90, 40), 0, 30)
            floor_timer_font = pygame.font.SysFont("floor timer", FONT_SIZE, True, False)
            floor_timer = floor_timer_font.render(str(int(self.floor_timer) + 1), False, BLACK)
            x, y = self.pos
            screen.blit(floor_timer, (x + FLOOR_WIDTH / 6, y + FLOOR_HEIGHT / 2.5))

    def button_color(self):
        color = GRAY
        if self.floor_timer :
            color = RED
        elif self.button.mouse_over:
            color = GRAY_FOR_OVER
        return color

    def draw(self, surface):
        surface.blit(self.image, self.pos)
        self.draw_timer(surface)
        color = self.button_color()
        self.button.draw(surface, color)

    def update(self, delta_time):
        if self.floor_timer > 0:
            self.floor_timer -= 1 * delta_time
        else:
            self.floor_timer = 0

