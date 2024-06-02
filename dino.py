import pygame
import os

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_stand = pygame.image.load(os.path.join("png", "stand_dino.png"))  # 加载小恐龙站立图片
        self.image_stand = pygame.transform.scale(self.image_stand, (50, 50))  # 调整图片大小
        self.image_crouch = pygame.image.load(os.path.join("png", "lie_dino.png"))  # 加载小恐龙趴下图片
        self.image_crouch = pygame.transform.scale(self.image_crouch, (50, 25))  # 调整图片大小
        self.image = self.image_stand
        self.rect = self.image.get_rect()
        self.rect.x = 50  # 小恐龙的初始X坐标
        self.rect.y = 250  # 小恐龙的初始Y坐标
        self.jump_speed = -15  # 跳跃速度
        self.gravity = 1  # 重力加速度
        self.velocity = 0  # 当前速度
        self.on_ground = True  # 是否在地面上
        self.jump_count = 0  # 跳跃计数器
        self.is_crouching = False  # 是否趴下

    def jump(self):
        if self.on_ground or self.jump_count < 2:  # 如果在地面上或跳跃次数小于2
            self.velocity = self.jump_speed
            self.on_ground = False
            self.jump_count += 1  # 增加跳跃次数

    def crouch(self):
        if self.on_ground:  # 只有在地面上才能趴下
            self.is_crouching = True
            self.image = self.image_crouch
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
            self.rect.y = 275  # 设置趴下时的y轴位置，确保贴近地面

    def uncrouch(self):
        self.is_crouching = False
        self.image = self.image_stand
        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        self.rect.y = 250  # 设置取消趴下时的y轴位置

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.y >= 250 and not self.is_crouching:  # 如果小恐龙在地面上且未趴下
            self.rect.y = 250
            self.on_ground = True
            self.velocity = 0
            self.jump_count = 0  # 重置跳跃计数器
        elif self.rect.y >= 275 and self.is_crouching:  # 如果小恐龙在地面上且趴下
            self.rect.y = 275
            self.on_ground = True
            self.velocity = 0
            self.jump_count = 0  # 重置跳跃计数器
