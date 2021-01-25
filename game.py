import pygame
import config

from managers.entity_manager import EntityManager
from managers.screen_manager import ScreenManager

class Game():
    def __init__(self):
        pygame.init()
        
        self.entity_manager = EntityManager()
        self.screen_manager = ScreenManager()

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True

        self.update()
    
    def update(self):
        while(self.running):
            delta_time = self.clock.tick(self.fps) / 1000
            
            self.entity_manager.update(delta_time)
            self.screen_manager.update(delta_time, self.entity_manager.get_entities())

    def close(self):
        self.running = False
        pygame.quit()