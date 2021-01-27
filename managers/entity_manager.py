from managers.manager import Manager
from entities.entity import Entity
from messages.message import Message

class EntityManager(Manager):
    def start(self):
        self.entity_list: list[Entity] = []
    
    def update(self, dt: float):
        for entity in self.entity_list:
            entity.update(dt)
            

    def add_entity(self, entity: Entity):
        if not self.entity_list.__contains__(entity):
            self.entity_list.append(entity)
            self.message_bus.post_message(Message("ADD_DRAWABLE_ENTITY", entity))

    def get_entities(self):
        return self.entity_list

    def handle_message(self, message: Message):
        for entity in self.entity_list:
            entity.handle_message(message)