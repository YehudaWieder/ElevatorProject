from globals import *


class Button:

    def __init__(self, floor_num: int):
        self.floor_num = floor_num
        self.pos = (BASE_BUTTON_POS_X, BASE_BUTTON_POS_Y - (FLOOR_HEIGHT * self.floor_num))
        self.mouse_over = None

    # draw button and floor number
    def draw(self, surface, color: (int, int, int)):
        pygame.draw.circle(surface, color, self.pos, BUTTON_SIZE)
        pygame.draw.circle(surface, GRAY_FOR_BUTTON_BORDER, self.pos, BUTTON_SIZE, width=2)
        floor_num = pygame.font.SysFont("floor number", FONT_SIZE, True, False)
        floor_num = floor_num.render(str(self.floor_num), False, WHITE)
        floor_num_pos = floor_num.get_rect()
        floor_num_pos.center = self.pos
        surface.blit(floor_num, floor_num_pos)

    # check if button clicked
    def onclick(self, click_pos: (int, int)):
        x, y = click_pos
        bx, by = self.pos
        if ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 <= BUTTON_SIZE:
            return True
        return False

    # check if mouse over the button
    def is_mouse_over(self, pos: (int, int)):
        over = False
        x, y = pos
        bx, by = self.pos
        if ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 <= BUTTON_SIZE:
            self.mouse_over = True
            over = True
        else:
            self.mouse_over = False
        return over
