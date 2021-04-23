class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1080
        # Назначение цвета фона.
        self.gb_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5

        # Параметры снаряда
        self.bullet_speed = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)

        self.bullet_allowed = 5

