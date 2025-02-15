from globals import *


class Button:

    def __init__(self, floor_num: int):
        self.floor_num = floor_num
        self.pos = (BASE_BUTTON_POS[0], BASE_BUTTON_POS[1] - (FLOOR_HEIGHT * self.floor_num))
        self.mouse_over = None


    def draw(self, surface, color):
        pygame.draw.circle(surface, color, self.pos, BUTTON_SIZE)
        pygame.draw.circle(surface, GRAY_FOR_BUTTON_BORDER, self.pos, BUTTON_SIZE, width=2)
        floor_num = pygame.font.SysFont("floor number", FONT_SIZE, True, False)
        floor_num = floor_num.render(str(self.floor_num), False, WHITE)
        surface.blit(floor_num, (self.pos[0] - (FONT_SIZE / 4.5), self.pos[1] - (FONT_SIZE / 4)))

    def onclick(self, click_pos: (int, int)):
        if ((click_pos[0] - self.pos[0]) ** 2 + (click_pos[1] - self.pos[1]) ** 2) ** 0.5 <= BUTTON_SIZE:
            return True
        return False

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

