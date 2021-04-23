import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца."""
    # Классу Alien не нужен метод для вывода на экран; вместо этого мы воспользуемся методом групп Pygame,
    # который автоматически рисует все элементы группы на экране.

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/жириновский_100x120.png')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width  # слева от пришельца добавляется интервал, равный ширине пришельца, а над ним
        # — интервал, равный высоте
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)
