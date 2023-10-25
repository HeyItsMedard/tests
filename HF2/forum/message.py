from datetime import datetime


class Message:
    def __init__(self, author: str, content: str) -> None:
        self.author = author
        self.content = content
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        return (
            f"{self.author} at {self.timestamp.isoformat(' ', 'minutes')}:\n"
            + f"  {self.content}"
        ) 
