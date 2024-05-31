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

    def update(self):  # 定义小恐龙的更新函数
        if self.is_jumping:  # 如果在跳跃状态
            self.velocity += self.gravity  # 增加重力加速度
            self.rect.y += self.velocity  # 移动小恐龙
            if self.rect.y >= 300:  # 如果小恐龙超过了屏幕底部100像素处
                self.rect.y = 300   # 限制小恐龙的最大高度
                self.is_jumping = False  # 停止跳跃
                self.velocity = 0   # 重置速度

    def jump(self):      # 定义小恐龙的跳跃函数
        if not self.is_jumping:  # 如果不在跳跃状态
            self.is_jumping = True  # 开始跳跃
            self.velocity = self.jump_speed  # 给小恐龙一个初始速度
