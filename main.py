import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
ENEMY_COLOR = (255, 0, 0)
GAME_OVER_RECT_COLOR = (255, 0, 0)
GAME_OVER_TEXT_COLOR = (255, 255, 255)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра на выживание")

# Загрузка звука
hit_sound = pygame.mixer.Sound('archivo.mp3')


# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)


# Класс игрока
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Ограничение перемещения по краям экрана
        self.rect.x = max(0, min(WIDTH - PLAYER_SIZE, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - PLAYER_SIZE, self.rect.y))


# Класс врага
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE),
                                random.randint(0, HEIGHT - ENEMY_SIZE), ENEMY_SIZE, ENEMY_SIZE)


# Основной игровой цикл
def main():
    player = Player()
    enemies = [Enemy() for _ in range(5)]
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 74)

    running = True
    game_over = False

    while running:
        screen.fill(BACKGROUND_COLOR)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False

        if not game_over:
            # Движение игрока
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-5, 0)
            if keys[pygame.K_RIGHT]:
                player.move(5, 0)
            if keys[pygame.K_UP]:
                player.move(0, -5)
            if keys[pygame.K_DOWN]:
                player.move(0, 5)

            # Проверка столкновений с врагами
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    hit_sound.play()
                    game_over = True

                    # Отрисовка врагов
                for enemy in enemies:
                    pygame.draw.rect(screen, ENEMY_COLOR, enemy.rect)

                    # Отрисовка игрока
                pygame.draw.rect(screen, PLAYER_COLOR, player.rect)

                if game_over:
                    # Отрисовка экрана окончания игры
                    pygame.draw.rect(screen, GAME_OVER_RECT_COLOR,
                                     (WIDTH // 2 - 150, HEIGHT // 2 - 50, 300, 100))
                    draw_text("Игра окончена!", font, GAME_OVER_TEXT_COLOR,
                              screen, WIDTH // 2, HEIGHT // 2 - 20)
                    draw_text("Для выхода из игры нажмите пробел.",
                              pygame.font.Font(None, 36), GAME_OVER_TEXT_COLOR,
                              screen, WIDTH // 2, HEIGHT // 2 + 20)

                pygame.display.flip()
                clock.tick(30)

            pygame.quit()
            sys.exit()

        if __name__ == "__main__":
            main()
