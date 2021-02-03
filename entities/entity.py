import abc

from pygame.math import Vector2
from components.physics.transform import Transform
from components.component import Component

class Entity(metaclass=abc.ABCMeta):
    def __init__(self, message_bus, initial_position: Vector2 = Vector2(0,0)):
        self.components: list[Component] = []
        self.message_bus = message_bus
        self.transform : Transform = self.add_component(Transform(self, initial_position))
        self.start()
    
    def add_component(self, component: Component) -> Component:
        if component not in self.components:
            self.components.append(component)
            return component

    def remove_component(self, component: Component):
        if component in self.components:
            self.components.append(component)

    def get_component(self, component_type: type) -> Component:
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

    def get_transform(self) -> Transform:
        return self.transform

    def get_position(self) -> Vector2:
        return self.transform.get_location()

    @abc.abstractmethod
    def start(self):
        raise NotImplementedError

    def update(self, dt: float) -> None:
        for component in self.components:
            component.update(dt)

    def handle_message(self, message) -> None:
        for component in self.components:
            component.handle_message(message)