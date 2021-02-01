import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from managers.manager import Manager
from messages.message import Message

class ScreenManager(Manager):
    def start(self):
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH), pygame.RESIZABLE)
        self.to_draw_entities = []
        self.to_draw_text = []

    def update(self, dt: float):
        self.screen.fill((0,0,0))
        self.draw_text()
        self.draw_entities()
        pygame.display.flip()

    def draw_text(self):
        for entity in self.to_draw_entities:
            self.screen.blit(entity.surf, entity.rect)
        
        self.to_draw_entities.clear()

    def draw_entities(self):
        for text in self.to_draw_text:
            self.screen.blit(text, (10,0))
        
        self.to_draw_text.clear()

    def handle_message(self, message: Message):
        if message.message_type == "DRAW_ENTITY":
            self.to_draw_entities.append(message.message_content)
        if message.message_type == "DRAW_TEXT":
            self.to_draw_text.append(message.message_content)