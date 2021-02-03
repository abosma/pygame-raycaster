from components.camera.main_camera import MainCamera
from entities.entity import Entity

class Camera(Entity):
    def start(self):
        self.add_component(MainCamera(self))

    def get_camera(self):
        return self.get_component(MainCamera)