import pygame
from entities.entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
    
    def start(self):
        pass

    def update(self, dt: float):
        pass

    def handle_message(self, message):
        if message.message_type == "KB_UP":
            self.rect.move_ip(0, -5)
        if message.message_type == "KB_DOWN":
            self.rect.move_ip(0, 5)
        if message.message_type == "KB_LEFT":
            self.rect.move_ip(-5, 0)
        if message.message_type == "KB_RIGHT":
            self.rect.move_ip(5, 0)