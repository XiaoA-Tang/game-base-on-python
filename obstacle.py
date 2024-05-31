import pygame
import random

# 障碍物类
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, ground_height):
        super().__init__()
        width = random.randint(20, 50)  # 障碍物的随机宽度
        height = random.randint(20, 60)  # 障碍物的随机高度，最大高度保证 Dino 可以跳过
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = ground_height - height  # 确保障碍物从地面向上延伸

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -self.rect.width:
            self.kill()
