import pygame
from entities.entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

        self.key_up_pressed = False
        self.key_down_pressed = False
        self.key_left_pressed = False
        self.key_right_pressed = False
    
    def start(self):
        pass

    def update(self, dt: float):
        if self.key_up_pressed:
            self.rect.move_ip(0, -5)
        if self.key_down_pressed:
            self.rect.move_ip(0, 5)
        if self.key_left_pressed:
            self.rect.move_ip(-5, 0)
        if self.key_right_pressed:
            self.rect.move_ip(5, 0)

    def handle_message(self, message):
        if message.message_type == "KB_PRESS_UP":
            self.key_up_pressed = True
        if message.message_type == "KB_PRESS_DOWN":
            self.key_down_pressed = True
        if message.message_type == "KB_PRESS_LEFT":
            self.key_left_pressed = True
        if message.message_type == "KB_PRESS_RIGHT":
            self.key_right_pressed = True
        if message.message_type == "KB_RELEASE_UP":
            self.key_up_pressed = False
        if message.message_type == "KB_RELEASE_DOWN":
            self.key_down_pressed = False
        if message.message_type == "KB_RELEASE_LEFT":
            self.key_left_pressed = False
        if message.message_type == "KB_RELEASE_RIGHT":
            self.key_right_pressed = False