import pygame

class Screen():
    def __init__(self, SCREEN_HEIGHT: int, SCREEN_WIDTH: int):
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH), pygame.RESIZABLE)

    def update(self, dt: float, *argv):
        for entity in argv:
            self.screen.blits(entity.surf, entity.rect)
        
        pygame.display.flip()