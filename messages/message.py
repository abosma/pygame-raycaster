import abc

class Message(metaclass=abc.ABCMeta):
    def __init__(self, message_type, message_content = None):
        self.message_type = message_type
        self.message_content = message_content

    def __str__(self):
        return f'Message Type: {self.message_type} | Message Content: {self.message_content}'