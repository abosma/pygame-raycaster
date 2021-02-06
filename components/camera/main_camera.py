from pygame import Vector2
from pygame import Color
from pygame import draw
from messages.message import Message
from components.camera.line import Line
from components.component import Component
from components.physics.transform import Transform
from entities.entity import Entity

class MainCamera(Component):
    def __init__(self, entity, width: int = 0, height: int = 0):
        self.entity = entity
        self.message_bus = entity.message_bus
        self.width = width
        self.height = height
        
        self.dir_x = -1
        self.dir_y = 0
        self.plane_x = 0
        self.plane_y = 0.66

        self.map: list[list[int]] = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

        self.start()
    
    def start(self):
        self.entity_transform : Transform = self.entity.get_component(Transform)

    def calculate_and_draw_rays(self, screen):
        for x in range(self.width):
            self.hit = 0
            self.side = None

            self.camera_x = 2 * x / self.width - 1
            self.ray_dir_x = self.dir_x + self.plane_x * self.camera_x
            self.ray_dir_y = self.dir_y + self.plane_y * self.camera_x

            self.map_x = self.entity.get_transform().x
            self.map_y = self.entity.get_transform().y

            if self.ray_dir_y == 0:
                self.delta_dist_x = 0
            else:
                if self.ray_dir_x == 0:
                    self.delta_dist_x = 1
                else:
                    self.delta_dist_x = abs(1 / self.ray_dir_x)

            if self.ray_dir_x == 0:
                self.delta_dist_y = 0
            else:
                if self.ray_dir_y == 0:
                    self.delta_dist_y = 1
                else:
                    self.delta_dist_y = abs(1 / self.ray_dir_y)

            if self.ray_dir_x < 0:
                self.step_x = -1
                self.side_dist_x = (self.entity.get_transform().x - self.map_x) * self.delta_dist_x
            else:
                self.step_x = 1
                self.side_dist_x = (self.map_x + 1 - self.entity.get_transform().x) * self.delta_dist_x

            if self.ray_dir_y < 0:
                self.step_y = -1
                self.side_dist_y = (self.entity.get_transform().y - self.map_y) * self.delta_dist_y
            else:
                self.step_y = 1
                self.side_dist_y = (self.map_y + 1 - self.entity.get_transform().y) * self.delta_dist_y

            while self.hit == 0:
                if self.side_dist_x < self.side_dist_y:
                    self.side_dist_x += self.delta_dist_x
                    self.map_x += self.step_x
                    self.side = 0
                else:
                    self.side_dist_y += self.delta_dist_y
                    self.map_y += self.step_y
                    self.side = 1

                if self.map[int(self.map_x)][int(self.map_y)] > 0:
                    self.hit = 1
            
            if self.side == 0:
                self.perp_wall_dist = (self.map_x - self.entity.get_transform().x + (1 - self.step_x) / 2) / self.ray_dir_x
            else:
                self.perp_wall_dist = (self.map_y - self.entity.get_transform().y + (1 - self.step_y) / 2) / self.ray_dir_y

            try:
                self.line_height = self.height / self.perp_wall_dist
            except(ZeroDivisionError):
                self.line_height = self.height
            
            self.draw_start = -self.line_height / 2 + self.height / 2
            self.draw_end = self.line_height / 2 + self.height / 2
            
            self.line_colour = self.get_wall_color(self.map_x, self.map_y)

            if self.side == 1:
                new_r = int(self.line_colour.r / 2)
                new_g = int(self.line_colour.g / 2)
                new_b = int(self.line_colour.b / 2)
                self.line_colour = Color(new_r, new_g, new_b, 255)

            # Make sure the height is above 0 and below camera height
            if self.draw_start < 0:
                self.draw_start = 0
            if self.draw_end > self.height:
                self.draw_end = self.height - 1

            draw.line(screen, self.line_colour, Vector2(x, self.draw_start), Vector2(x, self.draw_end))

    def get_wall_color(self, map_x, map_y):
        if self.map[int(map_x)][int(map_y)] == 1:
            return Color(255,0,0)
        if self.map[int(map_x)][int(map_y)] == 2:
            return Color(0,255,0)
        if self.map[int(map_x)][int(map_y)] == 3:
            return Color(0,0,255)
        
        return Color(255, 255, 0)


    def translate_entity_to_screen(self, input_entity: Entity) -> Vector2:
        screen_position_x = input_entity.get_transform().x - self.entity.get_transform().x
        screen_position_y = input_entity.get_transform().y - self.entity.get_transform().y

        return Vector2(screen_position_x, screen_position_y)