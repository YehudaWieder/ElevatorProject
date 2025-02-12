from globals import *


class Button:
    buttons = []

    def __init__(self, pos: (int, int), floor_num):

        self.floor_num = floor_num
        self.pos = pos
        self.size = BUTTON_SIZE
        self.pressed_timer = 0

        Button.buttons.append(self)

    def draw(self, pos: (int, int), screen):
        if self.pressed_timer == 0:
            color = GRAY
        else:
            color = RED
        pygame.draw.circle(screen, color, pos, self.size)
        floor_num = pygame.font.SysFont("floor number", FONT_SIZE, True, False)
        floor_num = floor_num.render(str(self.floor_num), False, LIGHT_BLUE)
        screen.blit(floor_num, (pos[0] - (FONT_SIZE / 4.5), pos[1] - (FONT_SIZE / 4)))

    def update(self):
        if self.pressed_timer > 0:
            self.pressed_timer -= 1 / REFRESH_PER_SECOND
        else:
            self.pressed_timer = 0

    @classmethod
    def onclick(cls, pos: (int, int)):
        for button in cls.buttons:
            if ((pos[0] - button.pos[0]) ** 2 + (pos[1] - button.pos[1]) ** 2) ** 0.5 <= button.size:
                return True, button
        return False, None
