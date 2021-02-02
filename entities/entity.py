import abc
from components.component import Component

class Entity(metaclass=abc.ABCMeta):
    def __init__(self):
        self.components: list[Component] = []
        self.start()
    
    def add_component(self, component: Component):
        if component not in self.components:
            self.components.append(component)

    def remove_component(self, component: Component):
        if component in self.components:
            self.components.append(component)

    def get_component(self, component_type: type) -> Component:
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

    @abc.abstractmethod
    def start(self):
        raise NotImplementedError

    def update(self, dt: float) -> None:
        for component in self.components:
            component.update(dt)

    def handle_message(self, message) -> None:
        for component in self.components:
            component.handle_message(message)