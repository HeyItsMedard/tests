from message import Message

from datetime import datetime


# TODO
class Channel:
    MAX_MESSAGES = 100

    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = set()
        self.messages = list()
        self.last_read = dict()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Channel):
            return self.name == other.name
        return False

    def get_messages_since(self, start_time: datetime) -> list[Message]: # Write function
        messages_all = [message for message in self.messages if message.timestamp >= start_time]
        return messages_all

    def get_messages(self) -> list[Message]:
        return self.messages
    
    def subscribe(self, user):
        self.subscribers.add(user)

    def unsubscribe(self, user):
        self.subscribers.discard(user)

    def add_message(self, message):
        """Add a message to the channel.
        If MAX_MESSAGES is reached, remove the oldest message.
        """
        if len(self.messages) >= self.MAX_MESSAGES:
            self.messages.pop(0)
        self.messages.append(message)
    #elfelejtettem, hogy a változtatásokhoz törölni kéne a pickle fájlt...
        