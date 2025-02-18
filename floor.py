from button import *


class Floor:

    def __init__(self, floor_level: int):
        self.floor_num = floor_level
        self.image = pygame.transform.scale(pygame.image.load(FLOOR_IMG_PATH), (FLOOR_WIDTH, FLOOR_HEIGHT))
        pygame.draw.rect(self.image, BLACK, (0, 0, FLOOR_WIDTH, FLOOR_SPACER_HEIGHT))
        self.pos = (GROUND_FLOOR_POS_X, GROUND_FLOOR_POS_Y - (FLOOR_HEIGHT * self.floor_num))
        self.button = Button(self.floor_num)
        self.floor_timer = 0
        self.is_elv_on_way = False

    # draw timer
    def draw_timer(self, screen):
        if self.floor_timer > 0:
            x, y = self.pos
            pygame.draw.rect(screen, WHITE, (x + 5, y + 20, TIMER_BG_WIDTH, TIMER_BG_HEIGHT), 0, 30)
            floor_timer_font = pygame.font.SysFont("floor timer", FONT_SIZE, True, False)
            floor_timer = floor_timer_font.render(str(int(self.floor_timer) + 1), False, BLACK)
            screen.blit(floor_timer, (x + TIMER_POS_ON_FLOOR_X, y + TIMER_POS_ON_FLOOR_Y))

    # choose button color
    def button_color(self):
        color = GRAY
        if self.floor_timer:
            color = RED
        elif self.button.mouse_over:
            color = GRAY_FOR_OVER
        return color

    # draw floor
    def draw(self, surface):
        surface.blit(self.image, self.pos)
        self.draw_timer(surface)
        color = self.button_color()
        self.button.draw(surface, color)

    # update floor timer
    def update(self, delta_time: float):
        if self.floor_timer > 0:
            self.is_elv_on_way = True
            self.floor_timer -= delta_time
        else:
            self.is_elv_on_way = False
            self.floor_timer = 0
