from messages.message import Message
from components.component import Component
from components.physics.transform import Transform

class PlayerMovement(Component):
    def start(self):
        self.player_transform : Transform = self.entity.get_component(Transform)

        self.speed = 500

        self.key_up_pressed = False
        self.key_down_pressed = False
        self.key_left_pressed = False
        self.key_right_pressed = False

    def update(self, dt: float):
        if self.key_up_pressed:
            self.player_transform.y -= self.speed * dt
        if self.key_down_pressed:
            self.player_transform.y += self.speed * dt
        if self.key_left_pressed:
            self.player_transform.x -= self.speed * dt
        if self.key_right_pressed:
            self.player_transform.x += self.speed * dt

    def handle_message(self, message: Message):
        if message.message_type == "KB_PRESS_UP" or message.message_type == "KB_RELEASE_UP":
            self.key_up_pressed = not self.key_up_pressed
        if message.message_type == "KB_PRESS_DOWN" or message.message_type == "KB_RELEASE_DOWN":
            self.key_down_pressed = not self.key_down_pressed
        if message.message_type == "KB_PRESS_LEFT" or message.message_type == "KB_RELEASE_LEFT":
            self.key_left_pressed = not self.key_left_pressed
        if message.message_type == "KB_PRESS_RIGHT" or message.message_type == "KB_RELEASE_RIGHT":
            self.key_right_pressed = not self.key_right_pressed