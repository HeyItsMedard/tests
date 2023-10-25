from channel import Channel
from user import User
import pickle
from channel import Channel
from message import Message
from datetime import datetime

class App:
    """The main application class.

    Stores all the data and provides methods to manipulate them.
    """
    name = "Teamscord"

    def __init__(self) -> None:
        try: 
            with open('data.pickle', 'rb') as f:
                self.__dict__.update(pickle.load(f).__dict__)
        except Exception:
            print("Database File is missing.")
            self._users = dict[str: User]()
            self._channels = list[str: Channel]()
        # print(self._channels)
        self.current_user: User | None = None #?

    def save(self) -> None:
        """Save all data to file."""
        with open('data.pickle', 'wb') as p:
            pickle.dump(self, p) #self.__dict__, tuple???

    def login(self, username, password) -> None:
        """Log in as the given user.

        Raises:
            ValueError: If the username or password is incorrect.
        """
        user = self._users.get(username, None)
        if user and user.password ==password:
            self.current_user=user
        else:
        # if not self.user_exists(username) or self.users[username].password != password:
            raise ValueError
        # self.current_user = self.users[username]

    def logout(self) -> None:
        """Log out the current user."""
        self.current_user = None

    def user_exists(self, username) -> bool:
        """Check if a user with the given username exists."""
        # TODO
        return username in self._users

    def signup(self, username, password) -> None:
        """Sign up a new user.

        Raises:
            ValueError: If the username already exists.
        """
        # TODO
        if self.user_exists(username):
            raise ValueError
        self._users[username] = User(username, password)

    def create_channel(self, name) -> None:
        """Create a new channel with the given name.

        Raises:
            ValueError: If a channel with the given name already exists.
        """
        # TODO
        # Note: Loop through all channels and check if any of them has the same name
        # or define the __hash__ and __eq__ methods of Channel based on name
        if any(channel.name == name for channel in self._channels):
            raise ValueError("Channel already exists.")
        new_channel = Channel(name)
        self._channels.append(new_channel)

    def get_channels(self) -> list[Channel]:
        """Get a list of all channels."""
        return self._channels

    def get_subscribed_channels(self) -> list[Channel]:
        """Get a list of all channels the current user is subscribed to."""
        return [channel for channel in self._channels if self.current_user in channel.subscribers]

    def subscribe(self, channel: Channel) -> None:
        """Subscribe the current user to the given channel."""
        channel.subscribe(self.current_user)
        
    def unsubscribe(self, channel: Channel) -> None:
        """Unsubscribe the current user from the given channel."""
        channel.unsubscribe(self.current_user)

    def send_message(self, channel: Channel, content: str) -> None:
        """Send a message to the given channel."""
        message = Message(self.current_user.username, content)
        channel.add_message(message)

    def mark_as_read(self, channel: Channel) -> None:
        """Update last read time of the channel for the current user to current time."""
        channel.mark_as_read(self.current_user)