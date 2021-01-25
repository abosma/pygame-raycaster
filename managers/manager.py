import abc

class Manager(metaclass=abc.ABCMeta):
    def __init__(self):
        self.start()
    
    @abc.abstractmethod
    def start(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, dt: float) -> None:
        raise NotImplementedError