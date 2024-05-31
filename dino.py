import pygame

# 小恐龙类
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # 40x40像素的图片 小恐龙
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 50  # 初始位置在屏幕左侧50像素处
        self.rect.y = 300  # 初始位置在屏幕底部100像素处
        self.jump_speed = -15
        self.gravity = 1  # 重力加速度
        self.velocity = 0  # 速度
        self.is_jumping = False  # 初始化时不在跳跃状态

    def update(self):
        if self.is_jumping:
            self.velocity += self.gravity
            self.rect.y += self.velocity
            if self.rect.y >= 300:
                self.rect.y = 300
                self.is_jumping = False
                self.velocity = 0

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity = self.jump_speed
