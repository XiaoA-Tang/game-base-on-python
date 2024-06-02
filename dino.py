import pygame
import os

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("png", "stand_dino.png"))  # 加载小恐龙图片
        self.image = pygame.transform.scale(self.image, (50, 50))  # 调整图片大小
        self.rect = self.image.get_rect()
        self.rect.x = 50  # 小恐龙的初始X坐标
        self.rect.y = 250  # 小恐龙的初始Y坐标
        self.jump_speed = -15  # 跳跃速度
        self.gravity = 1  # 重力加速度
        self.velocity = 0  # 当前速度
        self.on_ground = True  # 是否在地面上
        self.jump_count = 0  # 跳跃计数器

    def jump(self):
        if self.on_ground or self.jump_count < 2:  # 如果在地面上或跳跃次数小于2
            self.velocity = self.jump_speed
            self.on_ground = False
            self.jump_count += 1  # 增加跳跃次数

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.y >= 250:  # 如果小恐龙在地面上
            self.rect.y = 250
            self.on_ground = True
            self.velocity = 0
            self.jump_count = 0  # 重置跳跃计数器
