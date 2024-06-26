import pygame
import random
from dino import Dino
from obstacle import Obstacle
import utils

# 初始化Pygame
pygame.init()
pygame.font.init()  # 初始化字体模块

# 屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_HEIGHT = 300  # 地面的高度，对应Dino的脚部高度
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 创建固定尺寸的屏幕
pygame.display.set_caption("小恐龙")  # 设置标题

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 障碍物生成间隔
INITIAL_OBSTACLE_INTERVAL = 2000  # 初始障碍物生成时间间隔（毫秒）
MIN_OBSTACLE_INTERVAL = 1000  # 最小障碍物生成时间间隔（毫秒）
MAX_OBSTACLE_INTERVAL = 2000  # 最长障碍物生成时间间隔（毫秒）
MIN_INTERVAL = 300  # 确保障碍物生成间隔不低于300毫秒

def calculate_obstacle_interval(speed):
    # 根据速度调整障碍物生成间隔，速度越快，间隔越短
    interval = max(MIN_OBSTACLE_INTERVAL / speed*10, MIN_INTERVAL)
    return int(interval)

def game_end_screen():
    font = pygame.font.SysFont("simhei", 55)
    utils.draw_text_centered('Game End', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

    end_screen_active = True
    while end_screen_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if SCREEN_WIDTH // 2 - 100 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 100:
                    if SCREEN_HEIGHT // 2 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 50:
                        return True
                    elif SCREEN_HEIGHT // 2 + 60 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 110:
                        pygame.quit()
                        return False

        utils.draw_button('再来一把', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50, GREEN, (0, 200, 0))
        utils.draw_button('退出游戏', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 60, 200, 50, RED, (200, 0, 0))

        pygame.display.update()

def wait_for_start():
    waiting = True
    font = pygame.font.SysFont("simhei", 40)
    while waiting:
        screen.fill(WHITE)
        utils.draw_text_centered("Press 'space' to start", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 15)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    return True

def main_game_loop():
    global obstacle_speed
    obstacle_speed = 5  # 初始障碍物移动速度
    dino = Dino()
    all_sprites = pygame.sprite.Group()  # 所有精灵组
    all_sprites.add(dino)  # 添加小恐龙到精灵组
    obstacles = pygame.sprite.Group()  # 障碍物组

    clock = pygame.time.Clock()
    running = True
    last_obstacle_time = pygame.time.get_ticks()
    next_obstacle_time = INITIAL_OBSTACLE_INTERVAL  # 初始障碍物生成时间间隔
    start_time = pygame.time.get_ticks()  # 记录游戏开始时间
    font = pygame.font.SysFont("simhei", 30)  # 设置字体

    while running:
        for event in pygame.event.get():  # 处理事件
            if event.type == pygame.QUIT:  # 退出事件
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:  # 按键事件
                if event.key == pygame.K_SPACE:  # 空格键跳跃
                    dino.jump()  # 跳跃
                elif event.key == pygame.K_s:  # S键趴下
                    dino.crouch()  # 趴下
                elif event.key == pygame.K_w:  # W键跳跃
                    dino.jump()  # 跳跃
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:  # 松开S键
                    dino.uncrouch()  # 取消趴下

        current_time = pygame.time.get_ticks()
        if current_time - last_obstacle_time > next_obstacle_time:
            obstacle_type = random.choice(["normal", "crouch"])  # 随机选择障碍物类型
            obstacle = Obstacle(SCREEN_WIDTH, GROUND_HEIGHT, obstacle_speed, obstacle_type)  # 确保障碍物底部在地面高度
            all_sprites.add(obstacle)  # 添加障碍物到精灵组
            obstacles.add(obstacle)  # 添加障碍物到障碍物组
            last_obstacle_time = current_time
            next_obstacle_time = calculate_obstacle_interval(obstacle_speed)  # 根据速度重新计算生成间隔

            # 增加障碍物移动速度
            obstacle_speed += 0.3
            # 同步更新所有已生成障碍物的速度
            for obstacle in obstacles:
                obstacle.speed = obstacle_speed

        all_sprites.update()

        if pygame.sprite.spritecollideany(dino, obstacles):  # 小恐龙和障碍物碰撞
            running = False  # 退出游戏

        screen.fill(WHITE)  # 填充白色背景
        all_sprites.draw(screen)  # 绘制所有精灵

        # 绘制得分
        utils.draw_score(start_time, font, BLACK, screen, SCREEN_WIDTH - 150, 10)

        pygame.display.flip()  # 刷新屏幕

        clock.tick(30)

    return True

if __name__ == "__main__":
    while True:
        if not wait_for_start():
            break
        if not main_game_loop():
            break
        if not game_end_screen():
            break
    pygame.quit()
