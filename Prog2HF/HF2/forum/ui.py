from app import App


class UI:
    def __init__(self, app: App) -> None:
        self.app = app

    def start(self):
        print(f"Welcome to {self.app.name}!")
        self.main_menu()
        print("Goodbye!")

    def main_menu(self):
        while True:
            print("Main menu:")
            print("1: Login")
            print("2: Sign up")
            print("0: Exit")
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.login_menu()
                case "2":
                    self.signup_menu()
                case "0":
                    break
                case _:
                    print("Invalid choice!")

    def login_menu(self):
        print("Login:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            self.app.login(username, password)
            print("Login successful!")
        except Exception:
            print("Login failed!")
            return
        try:
            self.user_menu()
        except Exception:
            print("An error occurred!" + Exception) #CHANGES MADE!
        self.app.logout()

    def signup_menu(self):
        print("Sign up:")
        username = input("Enter your username: ")
        if self.app.user_exists(username):
            print("Username already exists!")
            return
        password = input("Enter your password: ")
        try:
            self.app.signup(username, password)
            print("Signup successful!")
        except Exception:
            print("Signup failed!")

    def user_menu(self):
        while True:
            print(f"Logged in as {self.app.current_user.username}. Choose an option:")
            print("0: Logout")
            print("1: Create new channel")
            print("2: Subscribe to a channel")
            channels = self.app.get_subscribed_channels()
            if channels:
                print("3: Unsubscribe from a channel")
                print("Enter a channel:") # ??
                for i, channel in enumerate(channels):
                    notification = ""
                    last_read = self.app.current_user.get_last_read(channel)
                    if last_read:
                        new_msgs = channel.get_messages_since(last_read)
                    else:
                        new_msgs = channel.get_messages()
                    if new_msgs:
                        notification = f" ({len(new_msgs)} new)"
                    print(f"{i + 4}: " + channel.name + notification)
            choice = input("Enter your choice: ")
            match choice:
                case "0":
                    break
                case "1":
                    self.create_channel_menu()
                case "2":
                    self.subscribe_menu()
                case "3":
                    if channels:
                        self.unsubscribe_menu()
                    else:
                        print("Invalid choice!")
                case _:
                    try:
                        channel = channels[int(choice) - 4]
                        self.channel_menu(channel)
                    except (ValueError, IndexError):
                        print("Invalid choice!")

    def create_channel_menu(self):
        print("Create channel:")
        name = input("Enter channel name: ")
        try:
            self.app.create_channel(name)
            print("Channel created!")
        except Exception:
            print("Channel creation failed!")

    def subscribe_menu(self):
        channels = set(self.app.get_channels())
        subscribed = set(self.app.get_subscribed_channels())
        channels = list(channels.difference(subscribed))
        while True:
            if not channels:
                print("No channels to subscribe to!")
                return
            print("Subscribe to a channel:")
            for i, channel in enumerate(channels):
                print(f"{i + 1}: " + channel.name)
            print("0: Cancel")
            try:
                index = int(input("Enter your choice: ")) - 1
                if index == -1:
                    return
                self.app.subscribe(channels[index])
                channels.pop(index)
                print("Subscribed!")
            except Exception:
                print("Invalid choice!")

    def unsubscribe_menu(self):
        channels = self.app.get_subscribed_channels()
        while True:
            if not channels:
                print("No channels to unsubscribe from!")
                return
            print("Unsubscribe from a channel:")
            for i, channel in enumerate(channels):
                print(f"{i + 1}: " + channel.name)
            print("0: Cancel")
            try:
                index = int(input("Enter your choice: ")) - 1
                if index == -1:
                    return
                self.app.unsubscribe(channels[index])
                channels.pop(index)
                print("Unsubscribed!")
            except Exception:
                print("Invalid choice!")

    def channel_menu(self, channel):
        print(f"Channel {channel.name}:")
        for message in channel.get_messages():
            print(message)
        while True:
            self.app.mark_as_read(channel)
            print("1: Send message")
            print("0: Back")
            choice = input("Enter your choice: ")
            match choice:
                case "0":
                    break
                case "1":
                    msg = input("Enter your message: ")
                    self.app.send_message(channel, msg)
                case _:
                    print("Invalid choice!")
