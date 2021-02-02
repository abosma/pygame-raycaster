from entities.entity import Entity
from components.input.player_movement import PlayerMovement
from components.renderer.entity_renderer import EntityRenderer

class Player(Entity):
    def start(self):
        self.add_component(EntityRenderer(self))
        self.add_component(PlayerMovement(self))