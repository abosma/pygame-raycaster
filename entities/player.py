from components.camera.main_camera import MainCamera
from pygame import Surface, Rect
from entities.entity import Entity
from components.input.player_movement import PlayerMovement
from components.renderer.entity_renderer import EntityRenderer

class Player(Entity):
    def start(self):
        #player_surf = Surface((50, 50))
        #player_surf.fill((255,255,255))

        #self.add_component(EntityRenderer(self, player_surf))
        self.add_component(MainCamera(self, 640, 480))
        self.add_component(PlayerMovement(self))