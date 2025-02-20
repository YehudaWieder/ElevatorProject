
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

    def draw_timer(self, screen) -> None:
        """
        draws the floor's timer
        :param screen: teh pygam surface to draw on it
        :return: None
        """
        if self.floor_timer > 0:
            x, y = self.pos
            pygame.draw.rect(screen, WHITE, (x + 5, y + 20, TIMER_BG_WIDTH, TIMER_BG_HEIGHT), 0, 30)
            floor_timer_font = pygame.font.SysFont("floor timer", FONT_SIZE, True, False)
            floor_timer = floor_timer_font.render(str(int(self.floor_timer) + 1), False, BLACK)
            screen.blit(floor_timer, (x + TIMER_POS_ON_FLOOR_X, y + TIMER_POS_ON_FLOOR_Y))

    def button_color(self) -> (int, int, int):
        """
        chooses the color of the floor's button
        :return: color (int, int, int)
        """
        color = GRAY
        if self.floor_timer:
            color = RED
        elif self.button.mouse_over:
            color = GRAY_FOR_OVER
        return color

    def draw(self, surface) -> None:
        """
        draws the floor
        :param surface: teh pygam surface to draw on it
        :return: None
        """
        surface.blit(self.image, self.pos)
        self.draw_timer(surface)
        color = self.button_color()
        self.button.draw(surface, color)

    def update(self, delta_time: float) -> None:
        """
        updates the floor's timer
        :param delta_time: the time between last update and current update, float
        :return: None
        """
        if self.floor_timer > 0:
            self.is_elv_on_way = True
            self.floor_timer -= delta_time
        else:
            self.is_elv_on_way = False
            self.floor_timer = 0
