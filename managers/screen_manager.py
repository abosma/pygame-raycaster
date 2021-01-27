import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from managers.manager import Manager
from messages.message import Message

class ScreenManager(Manager):
    def start(self):
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH), pygame.RESIZABLE)
        self.to_draw_entities = []

    def update(self, dt: float):
        self.screen.fill((0,0,0))
        for entity in self.to_draw_entities:
            self.screen.blit(entity.surf, entity.rect)
        pygame.display.flip()

    def handle_message(self, message: Message):
        if message.message_type == "ADD_DRAWABLE_ENTITY":
            self.to_draw_entities.append(message.message_content)