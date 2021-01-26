import abc

class Entity(metaclass=abc.ABCMeta):
    def __init__(self):
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