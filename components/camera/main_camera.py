from components.component import Component
from components.physics.transform import Transform
from entities.entity import Entity

class MainCamera(Component):
    def __init__(self, entity, width: int = 0, height: int = 0):
        self.entity = entity
        self.message_bus = entity.message_bus
        self.width = width
        self.height = height
        self.start()
    
    def start(self):
        self.entity_transform : Transform = self.entity.get_component(Transform)

    def translate_entity_to_screen(self, input_entity: Entity):
        screen_position_x = input_entity.get_transform().x - self.entity.get_transform().x
        screen_position_y = input_entity.get_transform().y - self.entity.get_transform().y

        print(screen_position_x, screen_position_y)