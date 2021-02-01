import logging
from managers.manager import Manager
from messages.message import Message

log = logging.getLogger()

class MessageBus():
    __instance = None

    @staticmethod
    def get_instance():
        if MessageBus.__instance == None:
            MessageBus()
        return MessageBus.__instance
    
    def __init__(self):
        if MessageBus.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MessageBus.__instance = self
            
        self.managers: list[Manager] = []
    
    def subscribe(self, manager: Manager):
        if not self.managers.__contains__(manager):
            self.managers.append(manager)

    def post_message(self, message: Message):
        if "DRAW" not in message.message_type:
            log.info(message)
        
        for manager in self.managers:
            manager.handle_message(message)