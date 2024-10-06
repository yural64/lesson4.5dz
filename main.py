import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
PLAYER_SIZE = 20
ENEMY_SIZE = 20
PLAYER_COLOR = (0, 255, 0)
ENEMY_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60
ENEMY_SPAWN_RATE = 30  # Враги появляются каждые 30 кадров

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Игра на выживание')

# Игровые объекты
player_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]

# Враги
enemies = []

# Игровой цикл
clock = pygame.time.Clock()
frame_count = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT] and player_pos[0] < WINDOW_WIDTH - PLAYER_SIZE:
        player_pos[0] += 5
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN] and player_pos[1] < WINDOW_HEIGHT - PLAYER_SIZE:
        player_pos[1] += 5

    # Появление врагов
    if frame_count % ENEMY_SPAWN_RATE == 0:
        enemy_pos = [random.randint(0, WINDOW_WIDTH - ENEMY_SIZE), 0]
        enemies.append(enemy_pos)

    # Обновление положения врагов
    for enemy in enemies:
        enemy[1] += 5  # Враги двигаются вниз

    # Проверка на столкновения
    for enemy in enemies:
        if (enemy[0] < player_pos[0] < enemy[0] + ENEMY_SIZE or
            enemy[0] < player_pos[0] + PLAYER_SIZE < enemy[0] + ENEMY_SIZE) and \
           (enemy[1] < player_pos[1] < enemy[1] + ENEMY_SIZE or
            enemy[1] < player_pos[1] + PLAYER_SIZE < enemy[1] + ENEMY_SIZE):
            running = False

    # Удаление врагов, вышедших за пределы экрана
    enemies = [enemy for enemy in enemies if enemy[1] < WINDOW_HEIGHT]

    # Отрисовка
    window.fill(BACKGROUND_COLOR)
    pygame.draw.rect(window, PLAYER_COLOR,
                     (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    for enemy in enemies:
        pygame.draw.rect(window, ENEMY_COLOR, (enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE))

    pygame.display.flip()

    # Обновление счетчика кадров
    frame_count += 1
    clock.tick(FPS)

pygame.quit()
sys.exit()