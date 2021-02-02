from pygame import Surface, Rect
from components.component import Component

class EntityRenderer(Component):
    def __init__(self, entity, surf: Surface):
        self.entity = entity
        self.start(surf)
    
    def start(self, surf: Surface):
        self.surf = surf
        self.rect = self.surf.get_rect()