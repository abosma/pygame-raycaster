import pygame
from managers.manager import Manager
from messages.message import Message
from messages.message_bus import MessageBus

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class EventManager(Manager):
    def start(self):
        pass
    
    def update(self, dt: float):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.message_bus.post_message(Message("QuitGame"))
                if event.key == K_UP:
                    self.message_bus.post_message(Message("KB_UP"))
                if event.key == K_DOWN:
                    self.message_bus.post_message(Message("KB_DOWN"))
                if event.key == K_LEFT:
                    self.message_bus.post_message(Message("KB_LEFT"))
                if event.key == K_RIGHT:
                    self.message_bus.post_message(Message("KB_RIGHT"))
            elif event.type == QUIT:
                self.message_bus.post_message(Message("QuitGame"))

    def handle_message(self, message):
        pass