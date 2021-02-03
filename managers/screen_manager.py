import pygame
from pygame import Rect
from pygame.surface import Surface
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from managers.manager import Manager
from messages.message import Message
from components.renderer.entity_renderer import EntityRenderer
from components.camera.main_camera import MainCamera

class ScreenManager(Manager):
    def start(self):
        self.screen : Surface = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH), pygame.RESIZABLE)
        self.to_draw_renderers: list[EntityRenderer] = []
        self.to_draw_text = []

    def update(self, dt: float):
        self.screen.fill((0,0,0))
        
        self.draw_entities()
        self.draw_text()

        pygame.display.flip()

    def draw_entities(self):
        for renderer in self.to_draw_renderers:
            if self.main_camera is not None:
                translated_entity_location = self.main_camera.translate_entity_to_screen(renderer.entity)
                translated_entity_rect = Rect(translated_entity_location.x, translated_entity_location.y, renderer.rect.width, renderer.rect.height)
                self.screen.blit(renderer.surf, translated_entity_rect)
            else:
                self.screen.blit(renderer.surf, renderer.rect)
        
        self.to_draw_renderers.clear()

    def draw_text(self):
        for text in self.to_draw_text:
            self.screen.blit(text, (10,0))
        
        self.to_draw_text.clear()

    def handle_message(self, message: Message):
        if message.message_type == "ADD_CAMERA":
            self.main_camera : MainCamera = message.message_content.get_camera()
        if message.message_type == "DRAW_ENTITY":
            self.to_draw_renderers.append(message.message_content)
        if message.message_type == "DRAW_TEXT":
            self.to_draw_text.append(message.message_content)