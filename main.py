from game import Game
from messages.message_bus import MessageBus

if __name__ == "__main__":
    message_bus = MessageBus.get_instance()
    game = Game(message_bus)