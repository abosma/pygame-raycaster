from managers.manager import Manager
from messages.message import Message
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
        level_name = level + ".yaml"
        to_load_level = Path.cwd() / "levels" / "level_information" / level_name
        
        try:
            level_contents_text = open(to_load_level).read()
        except:
            log.error(f'Could not load level: {to_load_level}')
