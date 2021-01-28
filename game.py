import pygame

from managers.manager import Manager
from managers.event_manager import EventManager
from entities.entity_manager import EntityManager
from levels.level_manager import LevelManager
from managers.screen_manager import ScreenManager

from messages.message import Message

class Game(Manager):
    def start(self):
        pygame.init()
        
        self.level_manager = LevelManager(self.message_bus)
        self.event_manager = EventManager(self.message_bus)
        self.entity_manager = EntityManager(self.message_bus)
        self.screen_manager = ScreenManager(self.message_bus)

        self.message_bus.subscribe(self)
        self.message_bus.subscribe(self.level_manager)
        self.message_bus.subscribe(self.event_manager)
        self.message_bus.subscribe(self.entity_manager)
        self.message_bus.subscribe(self.screen_manager)

        self.message_bus.post_message(Message("LOAD_LEVEL", "level_one"))

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True

        self.update()

    def update(self):
        while(self.running):
            delta_time = self.clock.tick(self.fps) / 1000
            
            self.event_manager.update(delta_time)
            self.entity_manager.update(delta_time)
            self.screen_manager.update(delta_time)

    def handle_message(self, message : Message):
        if message.message_type == "QuitGame":
            self.running = False

pygame.quit()