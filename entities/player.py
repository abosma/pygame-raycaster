from entities.entity import Entity

class Player(Entity):
    def start(self):
        print("Player Start")

    def update(self, dt: float):
        print("Player Update")