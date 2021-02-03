from pygame import Vector2

class Level():
    def __init__(self, level_size : Vector2):
        self.width = level_size.x
        self.height = level_size.y
        self.map: list[list[int]] = [self.width, self.height]