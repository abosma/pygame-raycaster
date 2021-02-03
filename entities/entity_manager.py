from managers.manager import Manager
from entities.entity import Entity
from messages.message import Message
from components.renderer.entity_renderer import EntityRenderer

class EntityManager(Manager):
    def start(self):
        self.entity_list: list[Entity] = []
    
    def update(self, dt: float):
        for entity in self.entity_list:
            entity.update(dt)

    def add_entity(self, entity: Entity):
        if not self.entity_list.__contains__(entity):
            self.entity_list.append(entity)

    def remove_entity(self, entity: Entity):
        if self.entity_list.__contains__(entity):
            self.entity_list.remove(entity)

    def get_entities(self):
        return self.entity_list

    def handle_message(self, message: Message):
        if message.message_type == "ADD_ENTITY":
            self.add_entity(message.message_content)
        else:
            for entity in self.entity_list:
                entity.handle_message(message)