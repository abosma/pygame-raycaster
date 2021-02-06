from entities.entity import Entity
from components.camera.main_camera import MainCamera
from pygame.math import Vector2
from managers.manager import Manager
from messages.message import Message
from entities.player import Player
from pathlib import Path
import logging

log = logging.getLogger()

class LevelManager(Manager):
    def start(self):
        pass

    def update(self, dt: float) -> None:
        pass

    def handle_message(self, message: Message) -> None:
        if message.message_type == "LOAD_LEVEL":
            self.load_level(message.message_content)

    def load_level(self, level: str):
        player : Entity = Player(self.message_bus, Vector2(5, 5))
        
        self.message_bus.post_message(Message("ADD_ENTITY", player))
        self.message_bus.post_message(Message("ADD_CAMERA", player.get_component(MainCamera)))

        level_name = level + ".json"
        to_load_level = Path.cwd() / "levels" / "level_information" / level_name
        
        try:
            level_contents_text = open(to_load_level).read()
        except:
            log.error(f'Could not load level: {to_load_level}')
