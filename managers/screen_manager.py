from config import SCREEN_HEIGHT, SCREEN_WIDTH
from managers.manager import Manager

class ScreenManager(Manager):
    def start(self):
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH), pygame.RESIZABLE)

    def update(self, dt: float, to_draw_entites = None):
        for entity in to_draw_entites:
            self.screen.blits(entity.surf, entity.rect)
        
        pygame.display.flip()