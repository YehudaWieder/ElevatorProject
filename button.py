from globals import *


class Button:

    def __init__(self, floor_num: int):
        self.floor_num = floor_num
        self.pos = (BASE_BUTTON_POS_X, BASE_BUTTON_POS_Y - (FLOOR_HEIGHT * self.floor_num))
        self.mouse_over = None

    def draw(self, surface, color: (int, int, int)) -> None:
        """
        draws a button with its floor number
        :param surface: teh pygam surface to draw on it
        :param color: the button's color (int, int, int)
        :return: None
        """
        pygame.draw.circle(surface, color, self.pos, BUTTON_SIZE)
        pygame.draw.circle(surface, GRAY_FOR_BUTTON_BORDER, self.pos, BUTTON_SIZE, width=2)
        floor_num = pygame.font.SysFont("floor number", FONT_SIZE, True, False)
        floor_num = floor_num.render(str(self.floor_num), False, WHITE)
        floor_num_pos = floor_num.get_rect()
        floor_num_pos.center = self.pos
        surface.blit(floor_num, floor_num_pos)

    def onclick(self, click_pos: (int, int)) -> bool:
        """
        checks if the button was clicked
        :param click_pos: the mouse click position (x, y) tuple
        :return: True or False
        """
        x, y = click_pos
        bx, by = self.pos
        if ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 <= BUTTON_SIZE:
            return True
        return False

    def is_mouse_over(self, pos: (int, int)) -> bool:
        """
        checks if mouse over the button
        :param pos: the mouse over position (x, y) tuple
        :return: True or False
        """
        over = False
        x, y = pos
        bx, by = self.pos
        if ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 <= BUTTON_SIZE:
            self.mouse_over = True
            over = True
        else:
            self.mouse_over = False
        return over
