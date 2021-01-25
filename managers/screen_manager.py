from managers.manager import Manager

class ScreenManager(Manager):
    def start(self):
        print("test start")

    def update(self, dt: float, to_draw_entites = None):
        return
        #print(f"test update {self}")