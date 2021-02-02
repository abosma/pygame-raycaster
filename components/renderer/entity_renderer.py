import pygame
from components.component import Component

class EntityRenderer(Component):
    def start(self):
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()