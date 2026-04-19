import sys

import pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1440, 932))
        pygame.display.set_caption('Инопланетное Вторжение')

        # Задание цвета фона.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Запускает основной цикл игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывается экран.
            self.screen.fill(self.bg_color)

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
