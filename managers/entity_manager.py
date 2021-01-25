from managers.manager import Manager
from entities.entity import Entity

class EntityManager(Manager):
    def start(self):
        self.entity_list = []
    
    def update(self, dt: float):
        for entity in self.entity_list:
            entity.update(dt)

    def add_entity(self, entity: Entity):
        if not self.entity_list.__contains__(entity):
            self.entity_list.append(entity)

    def get_entities(self):
        return self.entity_list