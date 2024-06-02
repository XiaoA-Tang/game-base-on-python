import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, ground_height, speed, obstacle_type="normal"):
        super().__init__()
        self.type = obstacle_type
        if self.type == "normal":
            width = random.randint(20, 50)  # 障碍物的随机宽度
            height = random.randint(40, 80)  # 障碍物的随机高度，最大高度保证 Dino 可以跳过
            self.image = pygame.Surface((width, height))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = ground_height - height  # 确保障碍物从地面向上延伸
        else:  # crouch
            width = random.randint(20, 60)  # 障碍物的随机宽度
            height = random.randint(30, 80)  # 需要趴下才能通过的障碍物高度
            self.image = pygame.Surface((width, height))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = ground_height - height -35  # 将障碍物放置在上半部分


        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.kill()
