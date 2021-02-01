import pygame
from entities.entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

        self.speed = 500

        self.key_up_pressed = False
        self.key_down_pressed = False
        self.key_left_pressed = False
        self.key_right_pressed = False
    
    def start(self):
        pass

    def update(self, dt: float):
        if self.key_up_pressed:
            self.rect.move_ip(0, -self.speed * dt)
        if self.key_down_pressed:
            self.rect.move_ip(0, self.speed * dt)
        if self.key_left_pressed:
            self.rect.move_ip(-self.speed * dt, 0)
        if self.key_right_pressed:
            self.rect.move_ip(self.speed * dt, 0)

    def handle_message(self, message):
        if message.message_type == "KB_PRESS_UP" or message.message_type == "KB_RELEASE_UP":
            self.key_up_pressed = not self.key_up_pressed
        if message.message_type == "KB_PRESS_DOWN" or message.message_type == "KB_RELEASE_DOWN":
            self.key_down_pressed = not self.key_down_pressed
        if message.message_type == "KB_PRESS_LEFT" or message.message_type == "KB_RELEASE_LEFT":
            self.key_left_pressed = not self.key_left_pressed
        if message.message_type == "KB_PRESS_RIGHT" or message.message_type == "KB_RELEASE_RIGHT":
            self.key_right_pressed = not self.key_right_pressed