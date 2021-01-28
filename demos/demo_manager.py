from managers.manager import Manager
from messages.message import Message

class DemoManager(Manager):
    def start(self):
        pass

    def update(self, dt: float):
        pass

    def handle_message(self, message: Message) -> None:
        pass