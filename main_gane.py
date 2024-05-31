import pygame
import random

# 初始化Pygame
pygame.init()
pygame.font.init()  # 初始化字体模块

# 屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 创建屏幕
pygame.display.set_caption("小恐龙")  # 设置标题

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 小恐龙类
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # 40x40像素的图片 小恐龙
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 50  # 初始位置在屏幕左侧50像素处
        self.rect.y = SCREEN_HEIGHT - 100  # 初始位置在屏幕底部100像素处
        self.jump_speed = -15
        self.gravity = 1  # 重力加速度
        self.velocity = 0  # 速度
        self.is_jumping = False  # 初始化时不在跳跃状态

    def update(self):
        if self.is_jumping:
            self.velocity += self.gravity
            self.rect.y += self.velocity
            if self.rect.y >= SCREEN_HEIGHT - 100:
                self.rect.y = SCREEN_HEIGHT - 100
                self.is_jumping = False
                self.velocity = 0

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity = self.jump_speed

# 障碍物类
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -20:
            self.kill()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_button(text, x, y, w, h, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    small_text = pygame.font.SysFont("simhei", 20)
    draw_text(text, small_text, BLACK, screen, x + 10, y + 10)

def game_end_screen():
    font = pygame.font.SysFont("simhei", 55)
    draw_text('Game End', font, RED, screen, SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 100)

    end_screen_active = True
    while end_screen_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if SCREEN_WIDTH//2 - 100 <= mouse_pos[0] <= SCREEN_WIDTH//2 + 100:
                    if SCREEN_HEIGHT//2 <= mouse_pos[1] <= SCREEN_HEIGHT//2 + 50:
                        return True
                    elif SCREEN_HEIGHT//2 + 60 <= mouse_pos[1] <= SCREEN_HEIGHT//2 + 110:
                        pygame.quit()
                        return False

        draw_button('再来一把', SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2, 200, 50, GREEN, (0, 200, 0))
        draw_button('退出游戏', SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 60, 200, 50, RED, (200, 0, 0))

        pygame.display.update()

def main_game_loop():
    dino = Dino()
    all_sprites = pygame.sprite.Group()  # 所有精灵组
    all_sprites.add(dino)  # 添加小恐龙到精灵组
    obstacles = pygame.sprite.Group()  # 障碍物组

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():  # 处理事件
            if event.type == pygame.QUIT:  # 退出事件
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:  # 按键事件
                if event.key == pygame.K_SPACE:  # 空格键跳跃
                    dino.jump()  # 跳跃

        if random.randint(1, 100) > 98:  # 随机生成障碍物
            obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - 100)  # 障碍物在屏幕右侧
            all_sprites.add(obstacle)  # 添加障碍物到精灵组
            obstacles.add(obstacle)  # 添加障碍物到障碍物组

        all_sprites.update()

        if pygame.sprite.spritecollideany(dino, obstacles):  # 小恐龙和障碍物碰撞
            running = False  # 退出游戏

        screen.fill(WHITE)  # 填充白色背景
        all_sprites.draw(screen)  # 绘制所有精灵
        pygame.display.flip()  # 刷新屏幕

        clock.tick(30)

    return True

if __name__ == "__main__":
    while main_game_loop():
        if not game_end_screen():
            break
    pygame.quit()
