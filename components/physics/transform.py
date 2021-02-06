from pygame.math import Vector2
from components.component import Component

class Transform(Component):
    def __init__(self, entity, initial_position: Vector2 = Vector2(0,0)):
        self.x = initial_position.x
        self.y = initial_position.y
        
        self.following = False
        self.to_follow_entity = None

        super().__init__(entity)
    
    def start(self):
        pass

    def update(self, dt: float):
        if self.following:
            self.set_location(self.to_follow_entity.transform.get_location())

    def get_location(self):
        return Vector2(self.x, self.y)

    def set_location(self, new_location: Vector2):
        self.x = new_location.x
        self.y = new_location.y

    def follow_entity(self, entity):
        self.to_follow_entity = entity
        self.following = True

    def stop_following(self):
        self.to_follow_entity = None
        self.following = False