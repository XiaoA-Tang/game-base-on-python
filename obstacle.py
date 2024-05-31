import pygame

last_obstacle_x = 0  # 全局变量，用于存储最近生成的障碍物位置

# 障碍物类
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -20:
            self.kill()
