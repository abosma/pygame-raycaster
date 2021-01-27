import pygame
from managers.manager import Manager
from messages.message import Message

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

class EventManager(Manager):
    def start(self):
        pass
    
    def update(self, dt: float):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.message_bus.post_message(Message("KB_PRESS_ESC"))
                if event.key == K_UP:
                    self.message_bus.post_message(Message("KB_PRESS_UP"))
                if event.key == K_DOWN:
                    self.message_bus.post_message(Message("KB_PRESS_DOWN"))
                if event.key == K_LEFT:
                    self.message_bus.post_message(Message("KB_PRESS_LEFT"))
                if event.key == K_RIGHT:
                    self.message_bus.post_message(Message("KB_PRESS_RIGHT"))
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.message_bus.post_message(Message("KB_RELEASE_ESC"))
                if event.key == K_UP:
                    self.message_bus.post_message(Message("KB_RELEASE_UP"))
                if event.key == K_DOWN:
                    self.message_bus.post_message(Message("KB_RELEASE_DOWN"))
                if event.key == K_LEFT:
                    self.message_bus.post_message(Message("KB_RELEASE_LEFT"))
                if event.key == K_RIGHT:
                    self.message_bus.post_message(Message("KB_RELEASE_RIGHT"))
            elif event.type == QUIT:
                self.message_bus.post_message(Message("QuitGame"))

    def handle_message(self, message: Message):
        pass