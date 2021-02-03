from pygame import Surface
from components.component import Component
from components.physics.transform import Transform
from messages.message import Message

class EntityRenderer(Component):
    def __init__(self, entity, surf: Surface):
        self.entity = entity
        self.message_bus = entity.message_bus
        self.start(surf)
    
    def start(self, surf: Surface):
        self.entity_transform : Transform = self.entity.get_component(Transform)
        self.surf = surf
        self.rect = self.surf.get_rect()

    def update(self, dt: float):
        self.rect.x = self.entity_transform.x
        self.rect.y = self.entity_transform.y

        self.message_bus.post_message(Message("DRAW_ENTITY", self))