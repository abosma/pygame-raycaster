from messages.message import Message
import abc

class Component(abc.ABC):
    def __init__(self, entity):
        self.entity = entity
        self.message_bus = entity.message_bus
        self.start()
    
    @abc.abstractmethod
    def start(self):
        raise NotImplementedError
    
    def update(self, dt: float):
        pass

    def handle_message(self, message: Message):
        pass