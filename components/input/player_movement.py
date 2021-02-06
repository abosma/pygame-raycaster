from math import cos, sin
from messages.message import Message
from components.component import Component
from components.camera.main_camera import MainCamera
from components.physics.transform import Transform

class PlayerMovement(Component):
    def start(self):
        self.transform : Transform = self.entity.get_component(Transform)
        self.camera : MainCamera = self.entity.get_component(MainCamera)

        self.move_speed = 1
        self.rotation_speed = 0.05

        self.key_up_pressed = False
        self.key_down_pressed = False
        self.key_left_pressed = False
        self.key_right_pressed = False

    def update(self, dt: float):
        if self.key_up_pressed:
            if self.camera.map[int(self.transform.x + self.camera.dir_x * self.move_speed * dt)][int(self.transform.y)] == False:
                self.transform.x += self.camera.dir_x * self.move_speed * dt
            if self.camera.map[int(self.transform.x)][int(self.transform.y + self.camera.dir_y * self.move_speed * dt)] == False:
                self.transform.y += self.camera.dir_y * self.move_speed * dt
        if self.key_down_pressed:
            if self.camera.map[int(self.transform.x - self.camera.dir_x * self.move_speed * dt)][int(self.transform.y)] == False:
                self.transform.x -= self.camera.dir_x * self.move_speed * dt
            if self.camera.map[int(self.transform.x)][int(self.transform.y - self.camera.dir_y * self.move_speed * dt)] == False:
                self.transform.y -= self.camera.dir_y * self.move_speed * dt
        if self.key_left_pressed:
            old_dir_x = self.camera.dir_x
            self.camera.dir_x = self.camera.dir_x * cos(self.rotation_speed) - self.camera.dir_y * sin(self.rotation_speed)
            self.camera.dir_y = old_dir_x * sin(self.rotation_speed) + self.camera.dir_y * cos(self.rotation_speed)

            old_plane_x = self.camera.plane_x
            self.camera.plane_x = self.camera.plane_x * cos(self.rotation_speed) - self.camera.plane_y * sin(self.rotation_speed)
            self.camera.plane_y = old_plane_x * sin(self.rotation_speed) + self.camera.plane_y * cos(self.rotation_speed)
        if self.key_right_pressed:
            old_dir_x = self.camera.dir_x
            self.camera.dir_x = self.camera.dir_x * cos(-self.rotation_speed) - self.camera.dir_y * sin(-self.rotation_speed)
            self.camera.dir_y = old_dir_x * sin(-self.rotation_speed) + self.camera.dir_y * cos(-self.rotation_speed)

            old_plane_x = self.camera.plane_x
            self.camera.plane_x = self.camera.plane_x * cos(-self.rotation_speed) - self.camera.plane_y * sin(-self.rotation_speed)
            self.camera.plane_y = old_plane_x * sin(-self.rotation_speed) + self.camera.plane_y * cos(-self.rotation_speed)

    def handle_message(self, message: Message):
        if message.message_type == "KB_PRESS_UP" or message.message_type == "KB_RELEASE_UP":
            self.key_up_pressed = not self.key_up_pressed
        if message.message_type == "KB_PRESS_DOWN" or message.message_type == "KB_RELEASE_DOWN":
            self.key_down_pressed = not self.key_down_pressed
        if message.message_type == "KB_PRESS_LEFT" or message.message_type == "KB_RELEASE_LEFT":
            self.key_left_pressed = not self.key_left_pressed
        if message.message_type == "KB_PRESS_RIGHT" or message.message_type == "KB_RELEASE_RIGHT":
            self.key_right_pressed = not self.key_right_pressed