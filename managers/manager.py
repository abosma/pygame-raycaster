import abc

class Manager(metaclass=abc.ABCMeta):
    def __init__(self, message_bus):
        self.message_bus = message_bus
        self.start()
    
    @abc.abstractmethod
    def start(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, dt: float) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def handle_message(self, message) -> None:
        raise NotImplementedError