import pygame
import random

# 初始化Pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # 创建屏幕
pygame.display.set_caption("小恐龙")  # 设置标题

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 小恐龙类
class Dino(pygame.sprite.Sprite):
    # 初始化小恐龙
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # 40x40像素的图片 小恐龙
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        # 小恐龙初始位置
        self.rect.x = 50  # 初始位置在屏幕左侧50像素处
        self.rect.y = SCREEN_HEIGHT - 100  # 初始位置在屏幕底部100像素处

        # 小恐龙跳跃速度
        self.jump_speed = -15

        # 小恐龙状态
        self.gravity = 1  # 重力加速度
        self.velocity = 0    # 速度
        self.is_jumping = False  # 初始化时不在跳跃状态

    # 更新小恐龙状态
    def update(self):
        if self.is_jumping:
            self.velocity += self.gravity
            self.rect.y += self.velocity

            if self.rect.y >= SCREEN_HEIGHT - 100:
                self.rect.y = SCREEN_HEIGHT - 100
                self.is_jumping = False
                self.velocity = 0

    # 小恐龙跳跃
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity = self.jump_speed

# 障碍物类
class Obstacle(pygame.sprite.Sprite):
    # 初始化障碍物
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # 更新障碍物状态
    def update(self):
        self.rect.x -= 5
        if self.rect.x < -20:
            self.kill()

# 创建小恐龙和障碍物组
dino = Dino()
all_sprites = pygame.sprite.Group()
all_sprites.add(dino)
obstacles = pygame.sprite.Group()

# 设置时钟
clock = pygame.time.Clock()

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jump()

    # 创建障碍物
    if random.randint(1, 100) > 98:
        obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - 100)
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # 更新所有精灵
    all_sprites.update()

    # 检测碰撞
    if pygame.sprite.spritecollideany(dino, obstacles):
        running = False

    # 绘制
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # 控制帧率
    clock.tick(30)

pygame.quit()
