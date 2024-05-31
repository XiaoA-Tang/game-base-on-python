import pygame

# 在屏幕上绘制文本
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# 绘制按钮
def draw_button(text, x, y, w, h, color, hover_color, action=None):
    screen = pygame.display.get_surface()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # 如果鼠标位于按钮范围内，则绘制悬停颜色
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        # 如果鼠标左键点击且存在操作，则执行操作
        if click[0] == 1 and action is not None:
            action()
    else:
        # 否则绘制正常颜色
        pygame.draw.rect(screen, color, (x, y, w, h))

    # 绘制按钮文本
    small_text = pygame.font.SysFont("simhei", 20)
    draw_text(text, small_text, (0, 0, 0), screen, x + 10, y + 10)
