import pygame

# 障碍物类
class Obstacle(pygame.sprite.Sprite):
    # 初始化障碍物对象
    def __init__(self, x, y):
        super().__init__()  # 调用父类的初始化方法
        self.image = pygame.Surface((20, 40))  # 创建障碍物的表面
        self.image.fill((0, 0, 0))  # 填充障碍物的颜色
        self.rect = self.image.get_rect()   # 获取障碍物的矩形区域
        self.rect.x = x  # 设置障碍物矩形区域的x坐标
        self.rect.y = y  # 设置障碍物矩形区域的y坐标

    # 更新障碍物的位置
    def update(self):
        self.rect.x -= 5  # 更新障碍物矩形区域的x坐标
        if self.rect.x < -20:  # 如果障碍物移出屏幕左边界
            self.kill()  # 移除障碍物对象
