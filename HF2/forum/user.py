from channel import Channel

from datetime import datetime


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.channels = dict[Channel, datetime | None]()

    def get_last_read(self, channel: Channel) -> datetime | None:
        return self.channels.get(channel, None)
