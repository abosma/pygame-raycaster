from messages.message import Message
from managers.manager import Manager

import pygame

class DebugManager(Manager):
    def start(self):
        self.font = pygame.font.SysFont("Arial", 18)

    def update(self, dt: float, time: float):
        self.message_bus.post_message(Message("DRAW_TEXT", self.draw_fps(time)))

    def draw_fps(self, time: float):
        fps_text = self.font.render(time, 1, pygame.Color("red"))
        return fps_text

    def handle_message(self, message: Message) -> None:
        pass